External Libraries Used:
-----------------------------------------
No external libraries are used. Both servers program rely solely on Python's standard library modules, such as socket, concurrent.futures, hashlib, time and os.
------------------------------------------
Instructions on How to Run the Programs:

<b>proxyserver.py</b>
1. Open a terminal or command prompt.
2. Navigate to the directory containing proxy_server.py.
3. Run the proxy server with the following command:
  ```
    python proxyserver.py
```
5. The proxy server will start listening on port 8888. Webpages can be requested using http://localhost:8888/www.google.com if it's from the same machine, or replace localhost with the IP address of the computer if it's running on another machine.

<b>webserver.py</b>
1. Place some HTML, text, JPEG, or PNG files in the same directory containing webserver.py.
2. Open a terminal or command prompt.
3. Navigate to the directory containing webserver.py.
4. Run the HTTP server with the following command:
   ```     
        python webserver.py
   ```
6. The HTTP server will start listening on port 12000. Files can be accessed by navigating to http://localhost:12000/HelloWorld.html in a browser if it's from the same machine, or replace localhost with the IP address of the computer if it's running on another machine.
---------------------------------------------------------

The proxy server and web server codes have been successfully tested with static HTML pages, JPEG images, text files and the pages that has been given in assignment part. Specific examples for webserver code include serving a basic HelloWorld.html page and displaying JPEG and text files directly in the browser. These tests were conducted using the Safari browser.


