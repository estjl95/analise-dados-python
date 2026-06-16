import pandas as pd
import matplotlib.pyplot as plt

# Carregar dataset
df = pd.read_csv("data.csv")

print("\nPrimeiras linhas do dataset:")
print(df.head())

print("\nEstatísticas descritivas:")
print(df.describe())

# Gráfico simples
plt.figure(figsize=(8, 5))
plt.plot(df.iloc[:, 0], df.iloc[:, 1], marker='o')
plt.title("Gráfico simples do dataset")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
