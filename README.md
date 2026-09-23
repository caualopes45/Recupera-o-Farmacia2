# Sistema de Cadastro de Medicamentos

## Sobre o projeto

Esse projeto foi feito em Python para simular um sistema simples de cadastro de medicamentos de uma farmácia.

O sistema permite cadastrar medicamentos, visualizar os medicamentos cadastrados e pesquisar um medicamento pelo nome. Os dados ficam salvos em um arquivo CSV, então não são perdidos quando o programa é fechado.

## Funcionalidades

* Cadastrar medicamento
* Listar medicamentos cadastrados
* Buscar medicamento pelo nome
* Verificar se o medicamento já está cadastrado
* Conferir se a quantidade informada é válida
* Salvar os dados no arquivo CSV
* Carregar os dados quando o programa é iniciado

## Como executar

Para executar o programa, é necessário ter o Python instalado.

No terminal, dentro da pasta do projeto, execute:

```bash
python main.py
```

Depois é só escolher uma das opções mostradas no menu.

Os medicamentos cadastrados ficam salvos no arquivo `medicamentos.csv`.

## Requisitos usados no projeto

### Menu e decisões

Usei `if`, `elif` e `else` para controlar as opções do menu e decidir o que o programa deve fazer de acordo com a escolha do usuário.

Isso está na função `main()`.

### Repetição

Usei um `while` para manter o menu aparecendo até o usuário escolher a opção de sair.

Isso também está na função `main()`.

### Funções

Separei o programa em várias funções para deixar o código mais organizado e facilitar a realização de cada tarefa.

Algumas delas são:

* `cadastrar_medicamento()`
* `buscar_medicamento()`
* `listar_medicamentos()`
* `carregar_medicamentos()`
* `salvar_medicamentos()`

### Lista e dicionários

Os medicamentos ficam guardados em uma lista. Cada medicamento é representado por um dicionário com seu nome, categoria e quantidade.

### Arquivo

Usei um arquivo `medicamentos.csv` para salvar os medicamentos cadastrados.

Quando o programa começa, ele carrega os dados desse arquivo. Quando um novo medicamento é cadastrado, os dados são salvos novamente.

### Bibliotecas

Usei somente bibliotecas que já vêm com o Python, como `csv` e `os`. Não foi necessário instalar nenhum pacote externo.

## Arquivos

* `main.py` — código principal do programa
* `medicamentos.csv` — onde os medicamentos ficam salvos
* `README.md` — explicação do projeto

## Git

Usei o Git para acompanhar as mudanças feitas no projeto durante o desenvolvimento. Os commits foram usados para registrar as principais alterações e correções do sistema.
