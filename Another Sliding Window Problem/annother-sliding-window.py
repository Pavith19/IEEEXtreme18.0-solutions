"""
Author: Pavith Bambaravanage
URL: https://github.com/Pavith19
"""
def costo_optimo(A, l, r):
    if r - l == 0:
        return A[r]
    
    if (r - l + 1) % 2 == 0:
        suma_maxima = 0
        i, j = l, r
        while i < j:
            suma_maxima = max(suma_maxima, A[i] + A[j])
            i += 1
            j -= 1
        return suma_maxima
    
    suma_maxima = A[l + (r - l) // 2]
    i, j = l, r
    while i < j and i < l + (r - l) // 2:
        suma_maxima = max(suma_maxima, A[i] + A[j])
        i += 1
        j -= 1
    return suma_maxima

def resolver(A, N, Q):
    resultado = []
    for _ in range(Q):
        x = int(input())
        suma_diferencia = 0
        
        for izquierda in range(N):
            derecha = izquierda
            while derecha < N:
                costo = costo_optimo(A, izquierda, derecha)
                if costo <= x:
                    suma_diferencia += A[derecha] - A[izquierda]
                    derecha += 1
                else:
                    break
        resultado.append(suma_diferencia)
    
    return resultado

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    
    resultado = resolver(A, N, Q)
    for r in resultado:
        print(r)

if __name__ == "__main__":
    main()
