import numpy as np

def sin(a:float, f:float, t:float):
    return a * np.sin(2*np.pi*f*t)

def triangle(a:float, f:float, t:float):
    return 4*abs((f*t-np.floor(f*t+0.5))*a)-a

def square(a:float, f:float, t:float):
    return a * np.sign(np.sin(2*np.pi*f*t))

def saw(a:float, f:float, t:float):
    return a*2*(t%(1/f))*f-a