from http.server import HTTPServer, SimpleHTTPRequestHandler

class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # These headers aren’t strictly needed for compat mode,
        # but won’t hurt if you later switch to full build.
        self.send_header("Cross-Origin-Opener-Policy",  "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy","require-corp")
        super().end_headers()

if __name__ == '__main__':
    HTTPServer(('localhost', 8000), Handler).serve_forever()
