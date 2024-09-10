
def ler_vetor(tamanho):
    vetor = []
    for i in range(tamanho):
        while True:
            try:
                numero = int(input(f"Digite o número {i + 1}: "))

                vetor.append(numero)

                break
            except ValueError:
                print("Por favor, insira um número inteiro válido.")
                
    return vetor

def soma_dos_quadrados(vetor):
    soma = sum(x**2 for x in vetor)
    return soma


def main():
    tamanho = 10
    vetor = ler_vetor(tamanho)
    resultado = soma_dos_quadrados(vetor)
    print(f"A soma dos quadrados dos elementos do vetor é: {resultado}")

if __name__ == "__main__":
    main()
