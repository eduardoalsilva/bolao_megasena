# Sistema de Bolão da Mega-Sena

## Descrição
Este sistema permite gerenciar um bolão da Mega-Sena, oferecendo funcionalidades como cadastro de apostadores, registro de apostas, realização de sorteios e conferência dos resultados. Os dados são armazenados em um arquivo JSON para persistência.

## Funcionalidades
- Cadastrar apostadores
- Registrar apostas
- Realizar sorteios
- Conferir resultados
- Exibir vencedores

## Requisitos
- Python 3.x

## Instalação e Execução
1. Clone este repositório ou baixe os arquivos do projeto.
2. Certifique-se de ter o Python instalado.
3. Execute o script principal:
   ```sh
   python bolao.py

## Menu Principal
Ao iniciar, o programa apresenta o seguinte menu:

```diff
==============MENU==============
====Digite a opção desejada:====
====1. Cadastrar apostador======
====2. Conferir sorteio=========
```

- Opção 1: Permite cadastrar um novo apostador e registrar suas apostas.
- Opção 2: Solicita os números sorteados e exibe os apostadores com mais acertos. 

## Exemplo de Estrutura do JSON
O sistema salva o dados no formato:

```json
{
    "João": [[10, 15, 23, 34, 45, 50], [5, 18, 26, 30, 42, 59]],
    "Maria": [[3, 12, 25, 36, 41, 58]]
}
```

## Melhorias Futuras
- Sorteio automático (atualmente o usuário digita o sorteio manualmente).
- Validação apromorada das apostas.
- Inferface gráfica para facilitar o uso.
- Armazenamento em banco de dados.

## Autor
Eduardo Almeida da Silva

```vbnet
Esse README agora resume bem o projeto, servindo como um guia rápido. Caso precise de mais alguma informação ou ajuste, me avise! 😊
```