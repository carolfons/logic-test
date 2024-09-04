def is_fibonacci(n):
    #função interna para calcular a sequência de Fibonacci até um número N
    def fibonacci_sequence(aux):
        fib_sequence = [0,1] #começa com a sequência com os dois primeiros números conhecidos da sequência de Fibonacci
        while fib_sequence[-1]<aux: #compara se o ultimo valor da lista é menor que numero informado
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2]) #adiciona o próximo numero da sequencia
        return fib_sequence
    
    #gera a sequencia até o numero informado
    fib_sequence = fibonacci_sequence(n)

    #se o num está na lista então retorna que ele pertence a sequencia
    if n in fib_sequence:
        return f"O número {n} pertence à sequencia de Fibonacci"
    else:
        return f"O número {n} não pertence à sequencia de Fibonacci"
    
#Exemplo de uso

numero_informado = int(input("Informe um número: ")) #solicita ao usuário a entrada de um dado

resultado = is_fibonacci(numero_informado) # chama a função is_fibonacci passando o número informado

print(resultado) #exibe o resultado
