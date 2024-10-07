#coding: utf-8
import math

def eq2Grau(a,b,c):
    delta = math.pow(b,2)-4*a*c
    if (delta > 0):
        #há duas raízes reais e distintas
        x1 = (-b-pow(delta, 0.5))/(2*a)
        x2 = (-b+pow(delta, 0.5))/(2*a)
        return x1,x2
    elif (delta == 0):
        #há uma raiz
        pass
    else:
        #raízes complexas
        pass

if __name__ == "__main__":
    x1, x2 = eq2Grau(1,4,3)
    print(f"As raízes são {x1} e {x2}")