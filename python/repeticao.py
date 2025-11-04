import os

while True:
    #solicita dois números ao usuario
    os.system("cls")
    numero1 = float(input(" Digite o primeiro número: "))
    numero2 = float(input(" Digite o segundo número: "))
    
    #calcula a multiplicaçao
    resultado = numero1 * numero2
    
    #exibe o resultado
    print(f"\n O resultado da multiplicação de {numero1} * {numero2} é = {resultado}")
    
    #pergunta se o usuaario deseja continuar
    continuar = input(" deseja fazer outro cácalculo (s/n): ").strip().lower()
    
    #se o usuario digitar 'n', o prograna encerra
    if continuar != 's':
        print("\n Programa encerrado. até logo!.")
        break
    print("-" * 40 ) # separador visual