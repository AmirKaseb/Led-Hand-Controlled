import pyfirmata

comport='COM3'

board=pyfirmata.Arduino(comport)

led_1=board.get_pin('d:13:o')
led_2=board.get_pin('d:12:o')
led_3=board.get_pin('d:11:o')
led_4=board.get_pin('d:10:o')
led_5=board.get_pin('d:9:o')

def led(total):
    if total==0:
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif total==1:
        led_1.write(1)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif total==2:
        led_1.write(1)
        led_2.write(1)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif total==3:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(0)
        led_5.write(0)
    elif total==4:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(0)
    elif total==5:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)
