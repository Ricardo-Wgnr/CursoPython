#coding: utf-8
import math

def eq2Grau(a,b,c):
    delta = math.pow(b,2)-4*a*c
    x1 = None
    x2 = None
    if (delta > 0):
        #há duas raízes reais e distintas
        x1 = (-b-pow(delta, 0.5))/(2*a)
        x2 = (-b+pow(delta, 0.5))/(2*a)
    elif (delta == 0):
        print("Há uma raiz única, Delta =", delta)
        x1 = -b/(2*a)
        x2 = -b/(2*a)
    else:
        print("Raízes complexas, Delta =", delta)
    return x1,x2, delta

if __name__ == "__main__":
    x1, x2, delta = eq2Grau(1,4,4)
    print(f"As raízes são {x1} e {x2}, delta = {delta}")