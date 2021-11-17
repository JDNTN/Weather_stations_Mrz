import paho.mqtt.publish as publish

class RequestMQTT:

    global contador
    contador = 0

    @staticmethod
    def requestSensor(path):
        global contador
        contador = contador + 1 
        publish.single(path, 'Funciona Chingadamadre' + path + "   "+str(contador), hostname='127.0.0.1')
