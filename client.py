import grpc
import chunk_pb2, chunk_pb2_grpc


class ClassificationClient:
    def __init__(self, address):
        # create credentials
        # credentials = grpc.ssl_channel_credentials()
        # create secure channel using credentials
        # self.channel = grpc.secure_channel(address, credentials)

        self.channel = grpc.insecure_channel(address)
        self.stub = chunk_pb2_grpc.ClassificationServerStub(self.channel)

    def inquire(self, request_iterator):
        response = self.stub.inquire(request_iterator)
        return response.message
