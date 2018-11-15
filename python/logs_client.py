"""The Python implementation of the GRPC logs.Logs client."""

from __future__ import print_function

import grpc

import logs_pb2
import logs_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = logs_pb2_grpc.LogsStub(channel)
        response = stub.Print(logs_pb2.GetRecentRequest(linesNo=b'10'))
    print("Logs client received: " + response.logs)


if __name__ == '__main__':
    run()

