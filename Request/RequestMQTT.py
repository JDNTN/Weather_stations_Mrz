import paho.mqtt.publish as publish

class RequestMQTT:

    global contador, __Path
    contador = 0
    __Path = 'Sensor/data'

    @staticmethod
    def requestSensor():
        global contador, __Path        
        contador = contador + 1 
        publish.single(__Path, 'Pasame los datos :D '+str(contador), hostname='127.0.0.1')
