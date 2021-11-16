import server
import sys

if __name__ == '__main__':
    port = sys.argv[1]
    server.ClassificationServer().start(port)
