import numpy as np
import matplotlib.pyplot as plt

IntervTiempo = 1200
IntervLongitud = 40
k = 1.8
L = 50
T = 500
dx = L/IntervLongitud
dt = T/IntervTiempo

def darOnda():
    Calores = []
    for t in range(IntervTiempo):
        U = []
        if t == 0:
            for x in range(IntervLongitud+1):
                U.append(funcionOnda(L,t,x,[],[],dx,dt))
        else:
           for x in range(IntervLongitud+1):
                U.append(funcionOnda(L,t,x,Calores[t-1],Calores[t-2],dx,dt)) 
        Calores.append(U)
    return Calores


def funcionOnda(L, t, x, TiempAnterior1,TiempAnterior2, dx, dt):
    if t == 0:
        return CondicionesIniciales(x)
    elif x == 0:
        return 0
    elif x == IntervLongitud:
        return 0
    else:
        c = k*dt/dx
        return -TiempAnterior2[x]+TiempAnterior1[x]+c*c*(
            TiempAnterior1[x+1]-2*TiempAnterior1[x]+TiempAnterior1[x-1])
    

def CondicionesIniciales(x):
    return 5
    return np.sin(x)



Calores = darOnda()
def graficar():
    fig, ax = plt.subplots(figsize=(10,5))
    plt.axis([0,L,0,11])
    x = np.linspace(0,L,IntervLongitud+1)
    colores=['blue', 'red', 'green', 'purple', 'pink','black']
    for i in range(5):
        mano = i*T/5
        plt.plot(x,Calores[int(mano//dt)],color=colores[i],linestyle="-",label='t={}'.format(mano))
    plt.plot(x,Calores[-1],color=colores[-1],linestyle="-",label='t={}'.format(T))
    plt.legend()
    plt.xlabel('Longitud (cm)')
    plt.ylabel('Altitud (cm)')
    plt.grid(b=True, which='major', color='gray', linestyle='--')
    plt.show()
    y  = np.linspace(0,T,IntervTiempo)
    X, Y = np.meshgrid(x,y)
    Z = np.asarray(Calores)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(Y, X, Z, cmap='viridis')
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Longitud')
    ax.set_zlabel('Altitud')
    ax.view_init(30, 250)
    plt.show()

graficar()