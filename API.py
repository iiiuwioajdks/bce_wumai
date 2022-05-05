import time
import grpc
from concurrent import futures


ONE_DAY_IN_SECONDS = 60 * 60 * 24
IP = "192.168.154.1:8999"

class ServiceMain(data_pb2_grpc.DoFormatServicer):
    def add(self, request, context):
        '''
        :param request: 书籍对象，包括书名，作者，ID
        :return:添加是否成功
        添加书籍\n
        如果ID已经存在，返回false\n
        如果ID不存在，添加书籍对象并返回true
        '''
        book = {}
        book['shuming'] = request.shuming
        book['zuozhe'] = request.zuozhe
        book['ID'] = request.ID
        for libbook in Library:
            if (libbook['ID'] == book['ID']):
                print("Add failure!")
                print(Library)
                return data_pb2.Success(success=False);
        Library.append(book)
        print("Add success!")
        print(Library)
        return data_pb2.Success(success=True);
    def queryByID(self,request,context):
        '''
        :param request: 待查询书籍的ID
        :return: 查询到的书籍对象
        通过ID查询书籍\n
        查找失败，返回：shuming='NULL',zuozhe='NULL',ID=-1
        '''
        for book in Library:
            if (book['ID'] == request.ID):
                print("Find it!")
                print(book)
                return data_pb2.Book(shuming=book['shuming'],zuozhe=book['zuozhe'],ID=book['ID']);
        print("Don't find it!")
        return data_pb2.Book(shuming='NULL',zuozhe='NULL',ID=-1);
    def queryByName(self,request,context):
        '''
        :param request:待查询书籍名称（部分）
        :return: 所有包含该名称的书籍
        通过名称模糊查询书籍
        '''
        partName = (str(request.shuming)).lower()
        findbook = []
        for book in Library:
            if partName in book['shuming'].lower():
                findbook.append(data_pb2.Book(shuming=book['shuming'],zuozhe=book['zuozhe'],ID=book['ID']))
        return data_pb2.BookList(book=findbook);
    def delete(self,request,context):
        '''
        :param request: 待删除书籍的ID
        :return: 删除是否成功
        通过ID删除书籍\n
        若ID存在，则返回true\n
        若ID不存在，则返回false
        '''
        for book in Library:
            if (book['ID'] == request.ID):
                print("Success delete :" , book , " !")
                Library.remove(book)
                return data_pb2.Success(success=True);
        print("Delete failure!")
        return data_pb2.Success(success=False);
def serve():
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=4))#最多同时服务4个客户端
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
    Library = []
    serve()