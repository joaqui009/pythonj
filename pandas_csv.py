import pandas as pd
import matplotlib.pyplot as plt
 #criar dadis para o dataframe

dados = {
    "nome": ["Arthur", "Maria", "Matheus", "Carlos", "Bruna"],
    "idade": [28, 22, 18, 35, 20],
    "cidade": ["Cotia", "Carapicuiba","Cotia","Osasco", "Cotia"],
 }
df = pd.DataFrame(dados)
 #exibir o dataframe
print(df)

#salvar dataframe no csv
df.to_csv("pandas_dados.csv", index=False)
#visualizar em datafrane o csv
df_csv = pd.read_csv("pandas_dados.csv")

df_filtrado = df[df["idade"] > 25]
print(df_filtrado)#todas as pessoas com menos de 25 anos não aparecem

df_ordenado = df.sort_values(by="idade", ascending=False) 
print(df_ordenado)

#exibir estatisticas
print(df.describe())

media_cidade = df.groupby("cidade")["idade"].mean()
print(media_cidade)

# df.plot(kind="bar", x="nome", y="idade", color="blue")
# plt.title("idade das Pessoas")
# plt.xlabel("nome")
# plt.ylabel("idade")
# plt.show()

df.boxplot(column="idade", by="cidade", grid=False)
plt.title("Distribuição de idades por cidade")
plt.xlabel("cidade")
plt.ylabel("idade")

plt.show()

