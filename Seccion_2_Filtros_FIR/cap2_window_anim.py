import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig

from matplotlib.widgets import Slider

#Respuesta al impulso de un filtro pasa-bajo ideal
Omegac = 0.3*np.pi
n = np.arange(-50,51,1)
hIdeal = (Omegac/np.pi)*np.sinc(n*(Omegac/np.pi))

#Crea la gráfica de la animación
fig, axs = plt.subplots(nrows=3, ncols=3)
axs[0,0].stem(n,hIdeal) #Respuesta al impulso ideal
axs[0,0].set(xlim=(-50,50))
axs[0,0].set_ylabel(r'Filtro Ideal $h_{D}[n]$')
axs[0,0].set_xlabel('n')
axs[0,1].plot([0,0.3,0.3001,1],[1,1,0,0])  #Respuesta en frecuencia ideal
axs[0,1].set_ylabel(r'$|H_{D}(\Omega)|$')
axs[0,1].set_xlabel(r'$\Omega$ (x $\pi$)')

#Función para graficar el n-ésimo frame
def draw(Nh):
    #Calcula la respuesta al impulso del filtro pasa-bajo (implícita ventana rectangular)
    n = np.arange(-(Nh-1)/2,((Nh-1)/2)+1,1)
    hw = (Omegac/np.pi)*np.sinc(n*(Omegac/np.pi))
    win = np.ones(Nh)
    #Calcula la respuesta en frecuencia y DTFT de la ventana
    w, Hw = sig.freqz(hw)
    w, Ww = sig.freqz(win)

    #Graficas
    axs[1,0].stem(n,win) #Ventana
    axs[1,0].set(xlim=(-50,50))
    axs[1,0].set_ylabel(r'Ventana $w[n]$')
    axs[1,0].set_xlabel('n')
    axs[1,1].plot(w/np.pi, np.abs(Ww)) #Espectro ventana
    axs[1,1].set_ylabel(r'$|W(\Omega)|$')
    axs[1,1].set_xlabel(r'$\Omega$ (x $\pi$)')
    axs[1,1].grid()
    axs[1,2].plot(w/np.pi, 20*np.log10(np.abs(Ww))) #Espectro ventana en decibeles
    axs[1,2].set_ylabel(r'$|W(\Omega)|_{dB}$')
    axs[1,2].set_xlabel(r'$\Omega$ (x $\pi$)')
    axs[1,2].grid()
    
    axs[2,0].stem(n,hw) #Respuesta al impulso enventanada
    axs[2,0].set(xlim=(-50,50))
    axs[2,0].set_ylabel(r'Filtro Real $h_{w}[n]$')
    axs[2,0].set_xlabel('n')
    axs[2,1].plot(w/np.pi, np.abs(Hw)) #Respuesta en frecuencia filtro real
    axs[2,1].set_ylabel(r'$|H_{w}(\Omega)|$')
    axs[2,1].set_xlabel(r'$\Omega$ (x $\pi$)')
    axs[2,1].grid()
    axs[2,2].plot(w/np.pi, 20*np.log10(np.abs(Hw))) #Respuesta en frecuencia en decibeles
    axs[2,2].set_ylabel(r'$|H_{w}(\Omega)|_{dB}$')
    axs[2,2].set_xlabel(r'$\Omega$ (x $\pi$)')
    axs[2,2].grid()

#Callback del Slider
def update(Nh):
    axs[1,0].cla()
    axs[1,1].cla()
    axs[1,2].cla()
    axs[2,0].cla()
    axs[2,1].cla()
    axs[2,2].cla()
    draw(Nh)

#Dibuja el primer frame   
draw(21)

#Ajusta el plot para hacer espacio para el slider
fig.subplots_adjust(bottom=0.25)

#Adiciona el Slider horizontal para controlar la posición de n
ax_n = fig.add_axes([0.25, 0.1, 0.65, 0.03])
n_slider = Slider(
    ax=ax_n,
    label='Longitud Nh',
    valmin=11,
    valmax=81,
    valinit=11,
    valstep=2
)

#Vincula la función update al Slider
n_slider.on_changed(update)

plt.show()