
class EchoParser(object):
    def recognize(self, message):
        return True
    
    def process(self, message):
        return message.getBody()