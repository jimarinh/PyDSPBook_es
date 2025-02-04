import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig

from matplotlib.widgets import Slider

x  = [1, 1/2, -1/2, 1/4]       #Señal de entrada Nx=4
h = [1/2, -1/2, 0, 1/4, 3/4]   #Señal de salida Nh=5
y = sig.convolve(x, h)  #Cálculo de la convolución

Nx = len(x)
Nh = len(h)
Ny = len(y)

#Crea la gráfica de la animación
fig, axs = plt.subplots(2,1)

#Función para graficar el n-ésimo frame
def draw(n):
    n_x = np.arange(0,Nx,1)
    n_h = np.arange(n-(Nh-1), n+1, 1)
    axs[0].stem(n_x, x, 'b', label='x[k]')
    axs[0].set(xlim=(-4, 8), ylim=(-0.8,1.5))
    axs[0].stem(n_h, np.flip(h), 'r', label='h[n-k]') 
    axs[0].arrow(x=n, y=1.2, dx=0, dy=-0.2, width=.08, facecolor='red')
    axs[0].annotate('n', xy=(n,1.3))
    axs[0].legend(bbox_to_anchor=(1,1),loc='upper right')    
    axs[1].stem(y[0:(n+1)], 'b', label='y[n]')
    axs[1].set(xlim=(-4, 8), ylim=(-0.8,1.5)) 
    axs[1].legend(bbox_to_anchor=(1,1),loc='upper right')

#Callback del Slider
def update(n):
    axs[0].cla()
    axs[1].cla()
    draw(n)

#Dibuja el primer frame   
draw(0)

#Ajusta el plot para hacer espacio para el slider
fig.subplots_adjust(bottom=0.25)

#Adiciona el Slider horizontal para controlar la posición de n
ax_n = fig.add_axes([0.25, 0.1, 0.65, 0.03])
n_slider = Slider(
    ax=ax_n,
    label='Instante n',
    valmin=0,
    valmax=Ny,
    valinit=0,
    valstep=1
)

#Vincula la función update al Slider
n_slider.on_changed(update)

plt.show()