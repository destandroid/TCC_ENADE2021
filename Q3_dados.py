import pandas as pd

nome_arquivo_entrada = "teste3.txt"
nome_arquivo_saida = "saida_teste3.txt"
colunas = ["NU_ANO", "CO_CURSO", "QE_I03"]

dados = pd.read_csv(nome_arquivo_entrada, sep=';', decimal='.', na_values='"', usecols=colunas)

dados["QE_I03"] = dados["QE_I03"].astype(str)

mapeamento_qe_i03 = {
    "A": "Brasileira",
    "B": "Brasileira naturalizada",
    "C": "Estrangeira"
}

dados["QE_I03"] = dados["QE_I03"].map(mapeamento_qe_i03)

contagem_qe_i03 = dados["QE_I03"].value_counts()

print("\nContagem dos itens em QE_I03:")
print(contagem_qe_i03)

dados.to_csv(nome_arquivo_saida, sep=';', index=False, decimal='.', na_rep='"')


