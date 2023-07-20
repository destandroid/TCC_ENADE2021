import pandas as pd

# nome do arquivo de entrada 
nome_arquivo_entrada = "teste1.txt"
#nome do arquivo de saída
nome_arquivo_saida = "saida.txt"

colunas = ["NU_ANO", "CO_CURSO", "QE_I01"]#coluna arquiv

dados = pd.read_csv(nome_arquivo_entrada, sep=';', decimal='.', na_values='"', usecols=colunas)#leitura do arquivo

mapeamento_qe_i01 = {
    "A": "Solteiro(a)",
    "B": "Casado(a)",
    "C": "Separado(a) judicialmente/divorciado(a)",
    "D": "Viúvo(a)",
    "E": "Outro"
}

dados["QE_I01"] = dados["QE_I01"].map(mapeamento_qe_i01)

contagem_qe_i01 = dados["QE_I01"].value_counts()

print("\nContagem dos itens em QE_I01:")
print(contagem_qe_i01)

dados.to_csv(nome_arquivo_saida, sep=';', index=False, decimal='.', na_rep='"')
