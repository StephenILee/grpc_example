import client
import sys
import chunk_pb2, chunk_pb2_grpc

CHUNK_SIZE = 1024 * 1024


def get_image_chunks(path):
    with open(path, 'rb') as f:
        while True:
            b = f.read(CHUNK_SIZE)
            if len(b) == 0:
                break
            yield chunk_pb2.Image(buffer=b)


if __name__ == '__main__':
    host = sys.argv[1]
    port = sys.argv[2]
    file_path = sys.argv[3]
    client = client.ClassificationClient(f'{host}:{port}')
    chunk_generator = get_image_chunks(file_path)
    message = client.inquire(chunk_generator)
    print(message)

