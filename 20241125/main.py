def fat(n): #Função chama ela mesma até uma determinada condição
    if n==1: #Caso base
        return 1
    else: #Caso recursivo
        return n*fat(n-1) #Multiplica o número pelo seu antecessor.
    
def fatLaco(n):
    res = 1
    for i in range (1,n):
        res *=(i+1)
    return res

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    

def fibonacciLaco(n):
    inicial = 0
    final = 1
    for _ in range (n-1):
        inicial, final = final, inicial+final    
    return final

if __name__ == "__main__":

    #print(fat(5))
    #print(fatLaco(5))
    print(fibonacci(5))
    