
from machine import Pin
from utime import sleep

#Dentro do Pin, o número é o número do GPIO e OUT pois liberamos sinais (nesse caso, ligamos e desligamos o led)
verde = Pin(15, Pin.OUT)
amarelo = Pin(2, Pin.OUT)
vermelho = Pin(0, Pin.OUT)

while True:
    verde.on()
    print ("Sinal liberado")
    sleep(20)
    verde.off()

    sleep(0.5)

    amarelo.on()
    print ("Atenção")
    sleep(10)
    amarelo.off()

    sleep(0.5)

    vermelho.on()
    print ("Sinal fechado")
    sleep(7)
    vermelho.off()

    sleep(0.5)

