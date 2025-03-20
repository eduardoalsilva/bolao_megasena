"""
Sistema de Bolão da Mega-Sena

Este programa permite cadastrar apostadores, registrar apostas, realizar um sorteio e conferir os resultados.
Os dados são armazenados em um arquivo JSON para persistência.

Funcionalidades:
- Cadastrar apostadores
- Registrar apostas
- Realizar sorteios
- Conferir resultados
- Exibir vencedores

Autor: Eduardo Almeida da Silva
"""

import json

# Arquivo para armazenar os dados
FILENAME = "bolao.json"

# Função para carregar os dados do arquivo JSON
def carregar_dados():
    """Carrega os dados do arquivo JSON. Retorna um dicionário com os apostadores e suas apostas."""
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # Retorna um dicionário vazio se o arquivo não existir

# Função para salvar os dados no arquivo JSON
def salvar_dados(dados):
    """Salva os dados dos apostadores no arquivo JSON."""
    with open(FILENAME, "w") as file:
        json.dump(dados, file, indent=4)

# Função para cadastrar um novo apostador
def cadastrar_apostador(nome):
    """Cadastra um novo apostador se ele ainda não estiver registrado."""
    dados = carregar_dados()
    if nome not in dados:
        dados[nome] = []  # Inicializa uma lista vazia de apostas
        salvar_dados(dados)
        print(f"Apostador {nome} cadastrado com sucesso!")
    else:
        print("Apostador já cadastrado.")

# Função para registrar uma nova aposta para um apostador
def registrar_aposta(nome, numeros):
    """Registra uma aposta de 6 números entre 1 e 60 para um apostador cadastrado."""
    if len(numeros) != 6 or any(n < 1 or n > 60 for n in numeros):
        print("Aposta inválida. Escolha 6 números entre 1 e 60.")
        return
    dados = carregar_dados()
    if nome in dados:
        dados[nome].append(sorted(numeros))  # Armazena a aposta ordenada
        salvar_dados(dados)
        print("Aposta registrada com sucesso!")
    else:
        print("Apostador não encontrado.")

# Função para realizar o sorteio dos números da Mega-Sena
def realizar_sorteio():
    """Realiza um sorteio aleatório de 6 números entre 1 e 60."""
    return input('Digite o resultado do sorteio. Seis números separados por espaços.') # Gera 6 números únicos entre 1 e 60

# Função para conferir o resultado do sorteio e contar acertos de cada apostador
def conferir_resultado(resultado):
    """Verifica quantos números cada apostador acertou no sorteio."""
    dados = carregar_dados()
    vencedores = {}
    for apostador, apostas in dados.items():
        acertos = [len(set(aposta) & set(resultado)) for aposta in apostas]  # Conta os acertos por aposta
        vencedores[apostador] = acertos
    return vencedores

# Função para exibir os vencedores e o número de acertos
def exibir_vencedores(resultado):
    """Exibe os números sorteados e a maior quantidade de acertos de cada apostador."""
    vencedores = conferir_resultado(resultado)
    print(f"Números sorteados: {resultado}")
    for apostador, acertos in vencedores.items():
        print(f"{apostador}: {max(acertos)} acertos")  # Exibe o maior número de acertos de cada apostador

# Função principal para interagir com o usuário
def main():
    """
    Gerencia a interação do usuário para cadastrar apostadores e registrar apostas
    """
    print('==============MENU==============')
    print('====Digite a opção desejada:====')
    print('====1. Cadastrar apostador======')
    print('====2. Conferir sorteio=========')
    opcao = input('')
    if opcao == '1':
        while True:
            nome = input('Digite o nome do apostador (ou "sair" para encerrar: ')
            if nome.lower().rstrip() == 'sair':
                break
            cadastrar_apostador(nome)
            while True:
                aposta = input('Digite 6 números separados por espaços para apostar (ou "fim" para próximo apostador): ')
                if aposta.lower().rstrip() == "fim":
                    break
                try:
                    numeros = list(map(int, aposta.split()))
                    registrar_aposta(nome, numeros)
                except ValueError:
                    print('Entrada inválida. Digite 6 números válidos.')

    elif opcao == '2':
        resultado_sorteio = realizar_sorteio()
        exibir_vencedores(resultado_sorteio)

    else:
        print('Por favor digite uma das opções.')
        main()


# Exemplo de uso do sistema
if __name__ == "__main__":
    main()
