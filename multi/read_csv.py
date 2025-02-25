import pandas as pd
# Esse programa serviu apenas para teste de como manipular arquivos .csv, além de permitir a formatação da base de dados
# definida após os testes com a Spotter da Sofar Ocean. Ele não está ligado diretamente com os outros programas.

df = pd.read_csv("acc.csv", header=[0])

df = df.drop(columns=["Mean_Height"])
df = df.drop(columns=["Mean_Period"])
df = df.drop(columns=["Mean_Period2"])
df = df.drop(columns=["Maximum_Height"])

df.to_csv('acc.csv', index=False)