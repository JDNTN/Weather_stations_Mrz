from Request.RequestMQTT import RequestMQTT as mqtt 
from threading import Thread
import time

class RequestController (Thread):

    _data = ''

    def __init__(self, data):
        global _data 
        _data = data
        print(data)
        Thread.__init__(self)
        self.daemon = True
        self.start()
        
    def run(self):
        self.requestSensors()

    def requestSensors(self):
        global _data
        print("entre")
        while(True):
            for sensor in _data['Sensors']:
                mqtt.requestSensor(sensor['path'])
                print('Envie al path: '+ sensor['path'])
            time.sleep(10)

    def contingency(dato):
        pass
