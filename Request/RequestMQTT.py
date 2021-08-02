import paho.mqtt.publish as publish

class RequestMQTT:

    @staticmethod
    def requestSensor(path):
        publish.single(path, 'Funciona Chingadamadre' + path, hostname='127.0.0.1')