import pandas as pd

# 1. Carregar os dados
df = pd.read_csv('churn.csv')

# 2. Visualizar as primeiras linhas e estrutura
print("--- Primeiras linhas ---")
print(df.head())

print("\n--- Informações do Dataset ---")
print(df.info())

# 3. Limpeza simples de dados
# Converter TotalCharges para numérico
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)

# 4. Perguntas de Negócio

# Pergunta 1: Qual a taxa geral de cancelamento (Churn)?
taxa_churn = df['Churn'].value_counts(normalize=True) * 100
print("\n--- Taxa Geral de Churn (%) ---")
print(taxa_churn.round(2))

# Pergunta 2: Cancelamento por tipo de contrato
churn_contrato = pd.crosstab(df['Contract'], df['Churn'], normalize='index') * 100
print("\n--- % de Churn por Tipo de Contrato ---")
print(churn_contrato.round(2))

# Pergunta 3: Qual o gasto médio de quem cancela vs quem continua?
gasto_medio = df.groupby('Churn')['MonthlyCharges'].mean()
print("\n--- Gasto Médio Mensal por Status ($) ---")
print(gasto_medio.round(2))
