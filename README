<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proxy Server & Web Server Project</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }

        h1, h2, h3 {
            color: #333;
        }

        code {
            background-color: #f4f4f4;
            padding: 5px;
            border-radius: 4px;
            font-family: monospace;
        }

        pre {
            background-color: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            font-size: 1.1em;
            white-space: pre-wrap;
            word-wrap: break-word;
        }

        ul {
            list-style: none;
        }

        li::before {
            content: "\2022";
            color: #ff6b6b;
            font-weight: bold;
            display: inline-block;
            width: 1em;
            margin-left: -1em;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
        }

        .highlight {
            background-color: #ff6b6b;
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
        }

    </style>
</head>
<body>

    <div class="container">
        <h1>Proxy Server & Web Server Project</h1>
        <p>This project consists of two main components: a Proxy Server (<code>proxyserver.py</code>) and a Web Server (<code>webserver.py</code>). Both programs utilize Python's standard library modules to provide basic functionalities of serving web pages and acting as a proxy.</p>
        <hr>

        <h2><b>External Libraries Used</b>:</h2>
        <p><span class="highlight">No external libraries are used.</span> Both servers rely solely on Python's standard library modules, such as:</p>
        <ul>
            <li><code>socket</code></li>
            <li><code>concurrent.futures</code></li>
            <li><code>hashlib</code></li>
            <li><code>time</code></li>
            <li><code>os</code></li>
        </ul>

        <hr>

        <h2><b>Instructions on How to Run the Programs:</b></h2>

        <h3>1. Proxy Server (<code>proxyserver.py</code>)</h3>
        <ol>
            <li>Open a terminal or command prompt.</li>
            <li>Navigate to the directory containing <code>proxyserver.py</code>.</li>
            <li>Run the proxy server with the following command:
                <pre><code>python proxyserver.py</code></pre>
            </li>
            <li>The proxy server will start listening on port <b>8888</b>. Webpages can be requested using:
                <pre><code>http://localhost:8888/www.google.com</code></pre>
                If it's running on another machine, replace <code>localhost</code> with the IP address of the computer where the server is running.
            </li>
        </ol>

        <h3>2. Web Server (<code>webserver.py</code>)</h3>
        <ol>
            <li>Place some HTML, text, JPEG, or PNG files in the same directory containing <code>webserver.py</code>.</li>
            <li>Open a terminal or command prompt.</li>
            <li>Navigate to the directory containing <code>webserver.py</code>.</li>
            <li>Run the HTTP server with the following command:
                <pre><code>python webserver.py</code></pre>
            </li>
            <li>The HTTP server will start listening on port <b>12000</b>. Files can be accessed by navigating to:
                <pre><code>http://localhost:12000/HelloWorld.html</code></pre>
                If it's running on another machine, replace <code>localhost</code> with the IP address of the computer.
            </li>
        </ol>

        <hr>

        <h2><b>Webpages Successfully Tested:</b></h2>
        <p>The proxy server and web server codes have been successfully tested with:</p>
        <ul>
            <li>Static HTML pages</li>
            <li>JPEG images</li>
            <li>Text files</li>
            <li>Pages given in the assignment</li>
        </ul>

        <p>Specific examples include serving a basic <code>HelloWorld.html</code> page and displaying JPEG and text files directly in the browser.</p>

        <p><b>Browser Tested:</b></p>
        <ul>
            <li>Safari</li>
        </ul>

        <hr>

        <h3>Example Commands for Running:</h3>
        <p>If you're running both servers on a single machine:</p>

        <h4><b>Start the Proxy Server:</b></h4>
        <pre><code>python proxyserver.py</code></pre>

        <h4><b>Start the Web Server:</b></h4>
        <pre><code>python webserver.py</code></pre>

        <h4><b>Request a Web Page Through the Proxy:</b></h4>
        <p>Open your browser and visit:</p>
        <pre><code>http://localhost:8888/www.google.com</code></pre>

        <hr>

        <h2>Usage Tips:</h2>
        <ul>
            <li>For debugging, open the terminal logs to see server requests in real time.</li>
            <li>You can modify the <code>proxyserver.py</code> to handle more advanced caching and request filtering if needed.</li>
        </ul>
    </div>

</body>
</html>
