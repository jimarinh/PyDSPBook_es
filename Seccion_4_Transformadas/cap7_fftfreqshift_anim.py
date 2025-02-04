import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig
from scipy.fft import fft

from matplotlib.widgets import Slider

#Muestras del espectro de frecuencia
#Xk = [0.5, 1, 0.7, 0.3, 0, 0, 0, 0, 0, 0, 0, 0.3, 0.7, 1]
#x0 = ifft(Xk)

x0 = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]


N = len(x0)
n = np.arange(0,N)
k = np.arange(0,N)

#Crea la gráfica de la animación
fig, axs = plt.subplots(2,1)

#Función para graficar un frame
def draw(k0):
    #Aplica desplazamiento en frecuencia multiplicando por la exponencial compleja en el tiempo
    x = x0*np.exp(1j*2*np.pi*k0*n/N)
    #Calcula FFT de la nueva señal
    Xk = fft(x)
    #Grafica señal y espectro
    axs[0].stem(x)
    axs[0].set_ylabel(r'$x[n]*exp(j 2\pi k0 n/N)$')
    axs[0].set_xlabel('Tiempo [n]')
    axs[0].set(ylim=(-2,2))
    axs[1].stem(k, np.abs(Xk))
    axs[1].set_ylabel('Espectro X[k]')
    axs[1].set_xlabel('Frecuencia [k]')
    axs[1].set(xlim=(0, N))

#Callback del Slider
def update(k0):
    axs[0].cla()
    axs[1].cla()
    draw(k0)

#Dibuja el primer frame   
draw(0)

#Ajusta el plot para hacer espacio para el slider
fig.subplots_adjust(bottom=0.25)

#Adiciona el Slider horizontal para controlar la frecuencia de muestreo
ax_k0 = fig.add_axes([0.40, 0.1, 0.50, 0.03])
k0_slider = Slider(
    ax=ax_k0,
    label='Desplazamiento en frecuencia (k0)',
    valmin=0,
    valmax=2*N,
    valinit=0,
    valstep=1
)

#Vincula la función update al Slider
k0_slider.on_changed(update)

plt.show()