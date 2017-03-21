import SimpleHTTPServer
import SocketServer

PORT = 9090


def main():
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    httpd = SocketServer.TCPServer(("", PORT), Handler)

    print("serving at port", PORT)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
