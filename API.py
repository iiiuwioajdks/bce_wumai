import time
import grpc
from concurrent import futures

import data_pb2
import data_pb2_grpc

ONE_DAY_IN_SECONDS = 60 * 60 * 24
IP = "192.168.154.1:8999"

class ServiceMain(data_pb2_grpc.DoFormatServicer):
    def get_Weather(self, request,context):
        global ip
        ip = request.IP
        return Data

def serve():
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=10))#最多同时服务4个客户端
    data_pb2_grpc.add_DoFormatServicer_to_server(ServiceMain(),grpcServer)#将服务类添加到
    grpcServer.add_insecure_port(IP)
    grpcServer.start()
    print("Server start success")
    try:
        while True:
            time.sleep(ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpcServer.stop(0)

if __name__ == "__main__":
    Data = []
    ip = "1"
    serve()

