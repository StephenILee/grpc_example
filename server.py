import grpc
from concurrent import futures
import chunk_pb2, chunk_pb2_grpc
import time


class ClassificationServer(chunk_pb2_grpc.ClassificationServerServicer):
    def __init__(self):
        class Servicer(chunk_pb2_grpc.ClassificationServerServicer):
            def inquire(self, chunks, context):
                buffer = b''
                for chunk in chunks:
                    buffer += chunk.buffer

                time.sleep(3)

                msg = 'S^PANTS^^^test.jpg'
                return chunk_pb2.Response(message=msg)

        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
        chunk_pb2_grpc.add_ClassificationServerServicer_to_server(Servicer(), self.server)

    def start(self, port):
        self.server.add_insecure_port(f'[::]:{port}')
        self.server.start()
        self.server.wait_for_termination()
