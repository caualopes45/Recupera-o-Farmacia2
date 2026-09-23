import csv
import os

ARQUIVO_CSV = "medicamentos.csv"

CAMPOS = ["nome", "categoria", "quantidade"]
def carregar_medicamentos():
    medicamentos = []

    if not os.path.exists(ARQUIVO_CSV):
        return medicamentos

    with open(ARQUIVO_CSV, newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            linha["quantidade"] = int(linha["quantidade"])
            medicamentos.append(linha)

    return medicamentos
def salvar_medicamentos(medicamentos):
    with open(ARQUIVO_CSV, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(medicamentos)
def salvar_medicamentos(medicamentos):
    with open(ARQUIVO_CSV, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(medicamentos)
def buscar_medicamento(medicamentos, nome_buscado):
    for med in medicamentos:
        if med["nome"].lower() == nome_buscado.lower():
            return med

    return None
def exibir_medicamento(med):
    print(f"  Nome       : {med['nome']}")
    print(f"  Categoria  : {med['categoria']}")
    print(f"  Quantidade : {med['quantidade']}")
    print()


def listar_medicamentos(medicamentos):
    if not medicamentos:
        print("Nenhum medicamento cadastrado.\n")
        return

    for i, med in enumerate(medicamentos, start=1):
        print(f"[{i}]")
        exibir_medicamento(med)
def exibir_menu():
    print("=" * 40)
    print("   SISTEMA DE CADASTRO DE MEDICAMENTOS")
    print("=" * 40)
    print("1. Cadastrar medicamento")
    print("2. Listar medicamentos")
    print("3. Buscar medicamento")
    print("0. Sair")
    print("-" * 40)
def main():
    medicamentos = carregar_medicamentos()

    while True:
        exibir_menu()

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            print("\n--- Cadastrar Medicamento ---")

            nome = input("Nome      : ").strip()
            categoria = input("Categoria : ").strip()
            quantidade_str = input("Quantidade: ").strip()

            if not quantidade_str.isdigit():
                print("Quantidade invalida! Digite apenas numeros.\n")
                continue

            if nome and categoria:
                sucesso = cadastrar_medicamento(
                    medicamentos,
                    nome,
                    categoria,
                    int(quantidade_str)
                )

                if sucesso:
                    salvar_medicamentos(medicamentos)
                    print("Medicamento cadastrado com sucesso!\n")
                else:
                    print("Erro: ja existe um medicamento com esse nome.\n")

            else:
                print("Nome e categoria sao obrigatorios.\n")
        elif opcao == "2":
            print("\n--- Lista de Medicamentos ---")
            listar_medicamentos(medicamentos)

        elif opcao == "3":
            print("\n--- Buscar Medicamento ---")

            nome_buscado = input("Digite o nome do medicamento: ").strip()

            resultado = buscar_medicamento(medicamentos, nome_buscado)

            if resultado:
                print()
                exibir_medicamento(resultado)

            else:
                print("Medicamento nao encontrado.\n")

