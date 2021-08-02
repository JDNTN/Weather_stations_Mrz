from configuration.ReadCofiguration import readJson as read
from Request.RequestController import RequestController as Request
from Response import ClientMQTT as response
from Response import ClientMQTT as response
import threading

def request():
    Request(read.readJsonFile())

def recive():
    response.answer()

threadResponse = threading.Thread(target=recive())
threadRequest = threading.Thread(target=request())

if __name__ == '__main__':
    threadResponse.start()
    threadRequest.start()