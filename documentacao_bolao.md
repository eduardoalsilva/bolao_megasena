# Documentação do Sistema de Bolão da Mega-Sena

## Introdução
Este sistema permite a gestão de um bolão da Mega-Sena, possibilitando o cadastro de apostadores, o registro de apostas, a realização de sorteios e a verificação dos resultados. Todos os dados são armazenados em um arquivo JSON para garantir a persistência das informações.

## Funcionalidades
- Cadastrar apostadores
- Registrar apostas
- Realizar sorteios
- Conferir resultados
- Exibir vencedores

## Estrutura do Arquivo JSON
O sistema armazena os dados dos apostadores em um arquivo JSON no seguinte formato:
```json
{
    "Nome do Apostador": [
        [10, 15, 23, 34, 45, 50],
        [5, 18, 26, 30, 42, 59]
    ]
}
```
Cada apostador possui uma lista de apostas associada a seu nome.

## Funções do Sistema

### `carregar_dados()`
**Objetivo:** Carregar os dados do arquivo JSON.
**Retorno:** Um dicionário contendo os apostadores e suas apostas.

### `salvar_dados(dados)`
**Objetivo:** Salvar os dados dos apostadores no arquivo JSON.
**Parâmetros:**
- `dados` (dict): Dicionário contendo os apostadores e suas apostas.

### `cadastrar_apostador(nome)`
**Objetivo:** Cadastrar um novo apostador.
**Parâmetros:**
- `nome` (str): Nome do apostador.

Se o apostador já estiver cadastrado, o sistema emite um aviso.

### `registrar_aposta(nome, numeros)`
**Objetivo:** Registrar uma aposta de 6 números para um apostador já cadastrado.
**Parâmetros:**
- `nome` (str): Nome do apostador.
- `numeros` (list[int]): Lista contendo 6 números entre 1 e 60.

Se a aposta for inválida (quantidade diferente de 6 ou números fora do intervalo), o sistema exibe uma mensagem de erro.

### `realizar_sorteio()`
**Objetivo:** Obter os números do sorteio da Mega-Sena.
**Retorno:** Lista de 6 números informados pelo usuário.

### `conferir_resultado(resultado)`
**Objetivo:** Verificar quantos números cada apostador acertou no sorteio.
**Parâmetros:**
- `resultado` (list[int]): Lista contendo os números sorteados.
**Retorno:** Dicionário com os apostadores e suas respectivas quantidades de acertos.

### `exibir_vencedores(resultado)`
**Objetivo:** Exibir os vencedores e a quantidade de acertos de cada apostador.
**Parâmetros:**
- `resultado` (list[int]): Lista contendo os números sorteados.

### `main()`
**Objetivo:** Gerenciar a interação do usuário com o sistema.

Menu inicial:
1. Cadastrar apostadores e registrar apostas.
2. Conferir o resultado do sorteio.

Se a opção for inválida, o menu é reapresentado.

## Execução
O programa é iniciado pelo bloco principal:
```python
if __name__ == "__main__":
    main()
```
Isso garante que o código só será executado quando o script for rodado diretamente, e não quando importado como módulo.

## Melhorias Futuras
- Implementação de sorteio automático ao invés de entrada manual.
- Melhor validação da entrada do usuário.
- Interface gráfica para facilitar a interação.
- Armazenamento em banco de dados ao invés de arquivo JSON.