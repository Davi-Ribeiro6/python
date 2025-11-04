import os
import math
import random


#função para calcular raiz quadrada
def raiz_quadrada():
    numero = float(input(" Digite um número para calcular a raiz quadrada: "))
    if numero < 0:
        print(f" Não é possivel calcular a raiz quadrada de número negativo!")
    else:
        resultado = math.sqrt(numero)
        print(f" A raiz quadrada de {numero} é {resultado}")
        input(" Pressione qualquer tecla para continar...")
        
        #função para calcular potência
def potencia_arg():
            base = float(input(" Digite a base: "))
            expoente = float(input(" Digite o expoente: "))
            resultado = math.pow(base, expoente)
            print(f" {base} elevado a {expoente} é igual a {resultado}")
            input(" Pressione qualquer tecla para continar...")
            
            # Função para gerar número randômico
def numero_aleatorio():
                inicio = int(input(" Digite o valor inicial do intervalo: "))
                fim = int(input(" Digite o valor final do intervalo: 3"))
                if inicio > fim:
                    print(f" O valor inicial deve ser menor que o valor final!")
                else:
                    numero = random.randint(inicio, fim)
                    print(F" Número aleatório gerado entre {inicio} e {fim}: {numero}")
                    input(" Pressione qualquer tecla para continar...")
                    
def equacao():
            num = float(input(" Digite o número escolhido: "))
            num2 = float(input(" Digite o segundo número escolhido: "))
            resul1 = num + num2
            resul2 = num - num2
            resul3 = num * num2 
            resul4 = num / num2
            resul5 = math.pow(num, num2)  
            print(F" Os resultados das equações são {resul1}, {resul2}, {resul3}, {resul4} e {resul5}")   
            input(" Pressione qualquer tecla para continar...")        
                    #programa principal com menu
def main():
                        
                        while True:
                            os.system("cls")
                            print("\n=== Menu DE OPERAÇÕES ===")
                            print(" 1 - Raiz quadrada")
                            print(" 2 - Potência")
                            print(" 3 - Número randômico")
                            print(" 4 - todas equações")
                            print(" 5 - Sair")
                            
                            opcao = input(" Escolha uma opção: ")
                            
                            if opcao == '1':
                                raiz_quadrada()
                            elif opcao == '2':
                                potencia_arg()                              
                            elif opcao == '3':
                                numero_aleatorio()
                            elif opcao == '4':
                                equacao()    
                            elif opcao == '5':
                                print(" Saindo do programa... até logo!")
                                break
                            else:
                                print(" Opção invalida tente novamente.")
                                
             #executa o programa

if __name__=="__main__":
                    main()
                                
                                
                            
                            
    