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