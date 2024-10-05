import socket
from concurrent.futures import ThreadPoolExecutor
import hashlib
import time

cache={}
CACHE_TIMEOUT=300

def get_cache_key(request):
    """Generate a cache key based on the request URL."""
    return hashlib.sha256(request).hexdigest()

def is_cache_valid(timestamp):
    """Check if the cache entry is still valid based on its timestamp."""
    return  (time.time() - timestamp) < CACHE_TIMEOUT

def handle_client_request(client_socket):
    request = client_socket.recv(1024)
    
    host, port, path = extract_host_port_and_path_from_request(request)  
    cache_key = get_cache_key(request)
    
    if cache_key in cache and is_cache_valid(cache[cache_key]['timestamp']):
        client_socket.sendall(cache[cache_key]['data'])
    else:
        modified_request = modify_request_for_forwarding(request, host, path)
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as destination_socket:
            try:
                destination_socket.connect((host, port))
                destination_socket.sendall(modified_request)  
                response = b''
                while True:
                    data = destination_socket.recv(4096)
                    if not data:
                        break
                    response += data
                    client_socket.sendall(data)
                cache[cache_key] = {'timestamp': time.time(), 'data': response}
            except socket.error as e:
                print(f"Error communicating with destination server: {e}")
    destination_socket.close()
    client_socket.close()

def extract_host_port_and_path_from_request(request):
    lines = request.split(b'\r\n')
    first_line = lines[0].decode('utf-8')  
    parts = first_line.split(' ')
    
    if len(parts) > 1:
        path = parts[1] 
        url = path[1:]  
        
        if url.startswith('www.'):
            host = url
            port = 80
            path = '/'
        else:
            protocol, rest = url.split('://')
            host_port, path = rest.split('/', 1)
            path = '/' + path 
            if ':' in host_port:
                host, port = host_port.split(':')
                port = int(port)
            else:
                host = host_port
                port = 80 if protocol == 'http' else 443
    else:
        raise ValueError("Malformed request line")
    
    return host, port, path
def modify_request_for_forwarding(request, host, path):
    lines = request.split(b'\r\n')
    lines[0] = lines[0].split(b' ')[0] + b' ' + path.encode('utf-8') + b' HTTP/1.1'
    host_header_found = False
    for i, line in enumerate(lines):
        if line.startswith(b'Host:'):
            lines[i] = b'Host: ' + host.encode('utf-8')
            host_header_found = True
            break
    if not host_header_found:
        lines.insert(1, b'Host: ' + host.encode('utf-8'))
    
    return b'\r\n'.join(lines)


def start_proxy_server(port=8888, max_workers=50):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(('0.0.0.0', port))
        server.listen(10)
        print(f"Proxy server listening on port {port}...")

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            while True:
                client_socket, addr = server.accept()
                print(f"Accepted connection from {addr}")
                executor.submit(handle_client_request, client_socket)


if __name__ == "__main__":
    start_proxy_server()