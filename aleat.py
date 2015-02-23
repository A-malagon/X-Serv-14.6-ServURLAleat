import webapp
import socket
import random


class otroServidor(webapp.webApp):
    def process(self, parsedRequest):
        numeroAleatorio = random.randint(0, 500000000)
        return("HTTP/1.1 200 OK", "<html>"
               "<html><body><h1>Hola</h1>" +
               "<body link='green'>" +
               "<body text='red'>" +
               "<body bgcolor='#87CEFA'>"
               "\r\n" +
               "<a href='" + str(numeroAleatorio) + "'>Dame otra</a>"
               "</body></html>" +
               "\r\n")
if __name__ == "__main__":
    servidor = otroServidor(socket.gethostname(), 1234)
