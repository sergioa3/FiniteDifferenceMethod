import numpy as np
import matplotlib.pyplot as plt

IntervTiempo = 12000
IntervLongitud = 40
k = 1.71
L = 100
T = 300
dx = L/IntervLongitud
dt = T/IntervTiempo

def darCalor():
    Calores = []
    for t in range(IntervTiempo):
        U = []
        if t == 0:
            for x in range(IntervLongitud+1):
                U.append(funcionCalor(L,t,x,[],dx,dt))
        else:
           for x in range(IntervLongitud+1):
                U.append(funcionCalor(L,t,x,Calores[t-1],dx,dt)) 
        Calores.append(U)
    return Calores


def funcionCalor(L, t, x, TiempAnterior, dx, dt):
    if t == 0:
        return CondicionesIniciales(x*dx)
    elif x == 0:
        return 0
    elif x == IntervLongitud:
        return 0
    else:
        r = k*dt/(dx*dx)
        return (1-2*r)*TiempAnterior[x]+r*(TiempAnterior[x-1]+TiempAnterior[x+1])
    

def CondicionesIniciales(x):
    return np.sin(2*np.pi/L*x)


Calores = darCalor()
def graficar():
    fig, ax = plt.subplots(figsize=(10,5))

    x = np.linspace(0,L,IntervLongitud+1)

    colores = ['blue','red','green','purple','pink']
    for i in range(0, 5):
        I = i*T/5
        plt.plot(x,Calores[int(I//dt)],color=colores[i],linestyle="-",label=str(I)+'s')
    
    plt.plot(x,Calores[-1],color="black",linestyle="-",label=str(T)+'s')
    plt.legend()
    plt.xlabel('Longitud (cm)')
    plt.ylabel('Temperatura (C°)')
    plt.grid(b=True, which='major', color='gray', linestyle='--')
    y  = np.linspace(0,T,IntervTiempo)
    X, Y = np.meshgrid(x,y)
    Z = np.asarray(Calores)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(Y, X, Z, cmap='viridis')
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Longitud')
    ax.set_zlabel('Temperatura')
    ax.view_init(30, 250)
    plt.show()

graficar()

