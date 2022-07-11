from Request.RequestMQTT import RequestMQTT as mqtt 
from threading import Thread
import time

class RequestController (Thread):

    global __time
    __time = 10 #Cambiar por 60
    _data = ''    

    def __init__(self, data):
        global _data        
        _data = data
        print(data) #Este linea se debe eliminar
        Thread.__init__(self)
        self.daemon = True
        self.start()
        
    def run(self):
        self.requestSensors()

    def requestSensors(self):
        global _data, __time
        print("entre")
        cont = 0
        while(True):
            cont = cont + 1 #Esta linea se debe eliminar          
            mqtt.requestSensor()
            print('Envie una peticion No: '+str(cont)) #Esta linea se debe de eliminar
            time.sleep(_data['Time']*__time)

    def contingency(dato):
        pass
