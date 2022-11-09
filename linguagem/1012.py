A,B,C = input().split(" ")
A = float(A)
B = float(B)
C = float(C)
TRI = (A*C)/2 
CIR = ((C**2)*3.14159)
TRA = ((A+B)*C)/2
QUA = B**2
RET = A*B
print(f'TRIANGULO: {TRI:.3f}')
print(f'CIRCULO: {CIR:.3f}')
print(f'TRAPEZIO: {TRA:.3f}')
print(f'QUADRADO: {QUA:.3f}')
print(f'RETANGULO: {RET:.3f}')