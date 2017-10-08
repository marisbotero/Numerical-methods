import numpy as np 
import matplotlib.pyplot as plt #libreria para hacer caluclos avanzados

x= np.linspace(-5,5, 100)    #graficar la funcion
plt.plot(x, np.exp(x) -x)
plt.show()


def f(x):             #definir la funcion
  return np.exp(x) -x
  
  
def Df(x):           #derivar la funcion
  return 1
  
x0=1
for interacion in range(1,6):   #ciclo para recorrer el metodo de Newton R y encontrar valores aproximados a la solucion
    x1= x0 -f(x0)/Df(x0)
    x0=x1
    print(x0)