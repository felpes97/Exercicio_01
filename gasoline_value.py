import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Importando o dado
vl_gas = pd.read_csv("preço gasolina.csv", sep=",")

#Criando o grafico
with sns.axes_style("whitegrid"):
    grafico = sns.lineplot(data=vl_gas, x="dia", y="venda")
grafico.set(
      title="Preço da gasolina no mês de Agosto - 10 dias",
      xlabel="Dia",
      ylabel="Preço"
  )

#Salvando o gráfico na pasta
plt.savefig("Preço da gasilina.jpg", dpi=300, bbox_inches='tight')


