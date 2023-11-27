import time
for i in range(100,200):
    print("Intentando con 192.168.0.{}".format(str(i)), end='\r')
    time.sleep(1)
