import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig

from matplotlib.widgets import Slider

#Espectro de la señal continua
f  = np.linspace(-1,1,30)
Xf = np.cos((np.pi/2)*f)

#Crea la gráfica de la animación
fig, axs = plt.subplots(2,1)

#Función para graficar un frame
def draw(fs):
    axs[0].plot(f, Xf, 'b')
    axs[0].set(xlim=(-6, 6),ylim=(0,1.1))
    axs[0].set_title('Espectro de la señal continua original')
    axs[0].set_xticks([])
    axs[0].set_yticks([])
    axs[0].annotate('$-f_{max}$', xy=(-1,0.05))
    axs[0].annotate('$f_{max}$', xy=(1,0.05))
    kmax = int(1 + (6/fs))
    for k in range(-kmax,kmax):
        f0 = k*fs
        ff = f-f0
        axs[1].plot(ff, Xf, 'r')
        axs[1].annotate('%d$f_{s}$'%k, xy=(f0,0.05))
    axs[1].set(xlim=(-6, 6),ylim=(0,1.1))
    axs[1].set_title('Espectro de la señal muestreada')
    axs[1].set_xlabel('Frecuencia [x $f_{max}$]')
    axs[1].set_yticks([])

#Callback del Slider
def update(fs):
    axs[0].cla()
    axs[1].cla()
    draw(fs)

#Dibuja el primer frame   
draw(3)

#Ajusta el plot para hacer espacio para el slider
fig.subplots_adjust(bottom=0.25)

#Adiciona el Slider horizontal para controlar la frecuencia de muestreo
ax_fs = fig.add_axes([0.40, 0.1, 0.50, 0.03])
fs_slider = Slider(
    ax=ax_fs,
    label='Frecuencia de muestreo (x $f_{max}$)',
    valmin=0.4,
    valmax=4,
    valinit=3,
    valstep=.2
)

#Vincula la función update al Slider
fs_slider.on_changed(update)

plt.show()