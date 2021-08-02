from Request.RequestMQTT import RequestMQTT as mqtt 
import time

class RequestController:

    def __init__(self, data):
        self.requestSensors(data)

    def requestSensors(self,data):
        while(True):
            for sensor in data['Sensors']:
                mqtt.requestSensor(sensor['path'])
            time.sleep(10)

    def contingency(dato):
        pass