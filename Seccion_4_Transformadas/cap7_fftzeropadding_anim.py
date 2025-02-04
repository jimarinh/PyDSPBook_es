import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig
from scipy.fft import fft

from matplotlib.widgets import Slider

#Muestras de la señal de entrada
x = [0.5, 1, 0.7, 0.3]

#Espectro de la señal discreta (DTFT)
w, Xw = sig.freqz(x,1)

#Crea la gráfica de la animación
fig, axs = plt.subplots(2,2)

#Función para graficar un frame
def draw(N):
    axs[0,0].stem(x)
    axs[0,0].set_title('Señales en el tiempo')
    axs[0,0].set_ylabel('x[n] original')
    axs[0,0].set_xlabel('Tiempo [n]')

    axs[0,1].plot(w/np.pi, np.abs(Xw), 'r')
    axs[0,1].set_title('Espectros')
    axs[0,1].set_ylabel(r'DTFT - $X(\Omega)$')
    axs[0,1].set_xlabel(r'Frecuencia [$\Omega \times \pi$]')
    axs[0,1].set(xlim=(0, 1))

    #FFT calculada insertando ceros a la señal
    xz = np.zeros(N)
    xz[0:4] = x

    Xk = fft(xz, N)
    k = np.arange(0,N)

    axs[1,0].stem(xz)
    axs[1,0].set_ylabel('x[n] con ceros')
    axs[1,0].set_xlabel('Tiempo [n]')

    axs[1,1].plot((N/2)*w/np.pi, np.abs(Xw), 'r:')
    axs[1,1].stem(k, np.abs(Xk))
    axs[1,1].set_ylabel('FFT - X[k]')
    axs[1,1].set_xlabel('Muestra de frecuencia [k]')
    axs[1,1].set(xlim=(0, N/2))

#Callback del Slider
def update(N):
    axs[0,0].cla()
    axs[0,1].cla()
    axs[1,0].cla()
    axs[1,1].cla()
    draw(N)

#Dibuja el primer frame   
draw(4)

#Ajusta el plot para hacer espacio para el slider
fig.subplots_adjust(bottom=0.25)

#Adiciona el Slider horizontal para controlar la frecuencia de muestreo
ax_N = fig.add_axes([0.40, 0.1, 0.50, 0.03])
N_slider = Slider(
    ax=ax_N,
    label='Tamaño de la FFT (N)',
    valmin=4,
    valmax=128,
    valinit=4,
    valstep=1
)

#Vincula la función update al Slider
N_slider.on_changed(update)

plt.show()