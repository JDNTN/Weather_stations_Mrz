from configuration.ReadCofiguration import readJson as read
from Request.RequestController import RequestController as Request
from Response import ClientMQTT as response
import threading

Request(read.readJsonFile())

def recive():
    response.answer()

threadResponse = threading.Thread(target=recive())

if __name__ == '__main__':    
    threadResponse.start()
    while True:
        pass
    