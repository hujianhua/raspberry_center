import numpy as np  
import matplotlib.pyplot as plt  
import serial
class ardunio_boy:
	def __init__(self, com_name = 'COM8', com_baud = 115200):
		self.ardunio_serial = serial.Serial(com_name, com_baud, timeout=1)
		print('ardunio_boy up!')
	def show_dht11(self):
		DH11_content = self.ardunio_serial.readline()
		print(DH11_content)
		
boy = ardunio_boy();
while 1:
	boy.show_dht11()
# x=np.linspace(-np.pi,np.pi,256,endpoint=True)  
# C,S=np.cos(x),np.sin(x)  
# plt.plot(x,C)  
# plt.plot(x,S) 
# plt.show() 
