import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import sounddevice as sd

t = np. linspace(0,3,3*1024)

third_octave = [130.81,146.83,220,174.61,164.81,246.93,196]
forth_octave = [293.66,392,130.81,261.83,392,0,349.23]
Start = [0,0.6,1,1.5,1.8,2.1,2.6]
End = [0.5,1,1.5,1.8,2.1,2.4,3]

x_t = 0

for i in range(0,7,1):
   u1 = np.where(t>=Start[i],1,0)
   u2 = np.where(t>=End[i],1,0)
   u = u1-u2
   temp = (np.sin(2*np.pi*third_octave[i]*t) + np.sin(2*np.pi*forth_octave[i]*t)) * u
   x_t += temp

#sd.play(x_t,3*1024) 


#start of milestone 2

N = 3*1024 
f = np.linspace(0, 512, int(N/2))

x_f = fft(x_t) #max value is 0.3
x_f = 2/N * np.abs( x_f[0:np.int(N/2)] )

fn = np.random.randint(0,512,2)

x_noiseT = x_t + ( np.sin(2*np.pi*fn[0]*t) + np.sin(2*np.pi*fn[1]*t) )

x_noiseF = fft(x_noiseT)
x_noiseF = 2/N * np.abs( x_noiseF[0:np.int(N/2)] )

x_filteredT = x_noiseT 


foundF = []
for i in range(0, np.size(x_noiseF), 1):
    if ((x_noiseF[i] > 0.5) and   (  (np.int(f[i]))  in foundF)==False ) :
        foundF.append(np.int(f[i]))
        x_filteredT =  x_filteredT - np.sin(2*np.pi*np.int(f[i])*t)
  
x_filteredF = fft(x_filteredT) 
x_filteredF = 2/N * np.abs( x_filteredF[0:np.int(N/2)] )   


sd.play(x_filteredT,3*1024) 

plt.subplot(3,2,1)
plt.title('Time Domain')
plt.plot(t,x_t)
plt.ylabel('before noise')

plt.subplot(3,2,2)
plt.title('Frequency Domain')
plt.plot(f,x_f)

plt.subplot(3,2,3)
plt.plot(t,x_noiseT)
plt.ylabel('noise')

plt.subplot(3,2,4)
plt.plot(f,x_noiseF)

plt.subplot(3,2,5)
plt.plot(t,x_filteredT)
plt.ylabel('after filteration')
plt.xlabel('Time')

plt.subplot(3,2,6)
plt.plot(f,x_filteredF)
plt.xlabel('Frequency')

plt.show()



















