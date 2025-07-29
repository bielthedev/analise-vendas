import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("vendas.csv")
print(df.groupby("Produto")["Valor"].sum())

df.groupby("Produto")["Valor"].sum().plot(kind="bar", title="Vendas por Produto")
plt.xlabel("Produto")
plt.ylabel("Total em R$")
plt.tight_layout()
plt.savefig("grafico_vendas.png")
plt.show()