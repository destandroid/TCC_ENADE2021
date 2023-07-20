import pandas as pd

nome_arquivo_entrada = "teste2.txt"
nome_arquivo_saida = "saida_teste2.txt"
colunas = ["NU_ANO", "CO_CURSO", "QE_I02"]

dados = pd.read_csv(nome_arquivo_entrada, sep=';', decimal='.', na_values='"', usecols=colunas)

mapeamento_qe_i02 = {
    "A": "Branca",
    "B": "Preta",
    "C": "Amarela",
    "D": "Parda",
    "E": "Indígena",
    "F": "Não quero declarar"
}

dados["QE_I02"] = dados["QE_I02"].map(mapeamento_qe_i02)


contagem_qe_i02 = dados["QE_I02"].value_counts()

print("\nContagem dos itens em QE_I02:")
print(contagem_qe_i02)

dados.to_csv(nome_arquivo_saida, sep=';', index=False, decimal='.', na_rep='"')
