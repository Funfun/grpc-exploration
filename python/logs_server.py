
"""The Python implementation of the GRPC logs.Greeter server."""

from concurrent import futures
import time

import grpc

import logs_pb2
import logs_pb2_grpc


class Logs(logs_pb2_grpc.LogsServicer):

    def Print(self, request, context):
        logfile = open("trace.log", "r")
        return logs_pb2.GetRecentResponse(logs = logfile.read())


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    logs_pb2_grpc.add_LogsServicer_to_server(Logs(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
