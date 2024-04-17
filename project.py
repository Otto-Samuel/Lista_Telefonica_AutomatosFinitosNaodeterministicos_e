import re
import os

def validar_telefone(telefone):

    regex = r'^\(?[1-9]{2}\)?[-. ]?[2-9][0-9]{3,4}[-. ]?[0-9]{4}$'

    if re.match(regex, telefone):
        return True
    else:
        return False

def extrair_telefones(texto):
    regex = r'\(?\b[1-9]{2}\)?[-. ]?[2-9][0-9]{3,4}[-. ]?[0-9]{4}\b'
    
    telefones = re.findall(regex, texto)
    
    return telefones

def validar_numero():
    telefone = input("Insira um número de telefone para validar (formato: xx xxxx-xxxx): ")
    if validar_telefone(telefone):
        print("\n [ O número de telefone é válido. ]")
    else:
        print("\n [ O número de telefone é inválido. ]")

def extrair_numeros():
    texto = input("Insira um texto contendo números de telefone para extrair: ")
    telefones_encontrados = extrair_telefones(texto)
    if telefones_encontrados:
        print("\nNúmeros de telefone encontrados no texto:")
        for telefone in telefones_encontrados:
            print(telefone)
    else:
        print("\nNenhum número de telefone encontrado no texto.")

def menu():
    while True:
        
        print("\n### Menu ###")
        print("1. Validar número de telefone")
        print("2. Extrair números de telefone de um texto")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            validar_numero()
        elif escolha == "2":
            extrair_numeros()
        elif escolha == "3":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def main():
    os.system('cls')
    print("Bem-vindo ao Validador de Telefones!")
    menu()

if __name__ == "__main__":
    main()
