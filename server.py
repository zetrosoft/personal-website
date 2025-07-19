#!/usr/bin/env python3
import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

# Change to the directory containing the website files
os.chdir(Path(__file__).parent)

PORT = 8181

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def log_message(self, format, *args):
        print(f"[{self.address_string()}] {format % args}")

if __name__ == "__main__":
    try:
        with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
            print(f"🚀 Personal Website Server started!")
            print(f"📱 Local URL: http://localhost:{PORT}")
            print(f"🌐 Network URL: http://127.0.0.1:{PORT}")
            print(f"📁 Serving files from: {os.getcwd()}")
            print(f"⏹️  Press Ctrl+C to stop the server")
            print("-" * 50)
            
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Port {PORT} is already in use. Trying port {PORT + 1}...")
            PORT += 1
            with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
                print(f"🚀 Personal Website Server started on port {PORT}!")
                print(f"📱 Local URL: http://localhost:{PORT}")
                httpd.serve_forever()
        else:
            print(f"❌ Error starting server: {e}")
