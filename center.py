import numpy as np  
import matplotlib.pyplot as plt  
import serial
ardunio_serial = serial.Serial('COM8', 115200, timeout=1)
while 1:
	DH11_content = ardunio_serial.readline()
	print(DH11_content)
# x=np.linspace(-np.pi,np.pi,256,endpoint=True)  
# C,S=np.cos(x),np.sin(x)  
# plt.plot(x,C)  
# plt.plot(x,S) 
# plt.show() 