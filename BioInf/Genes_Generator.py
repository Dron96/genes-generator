import pandas as pd
import random
from tqdm import tqdm
import time

def Type(sr):
    for i in range(len(sr)):
        if type(sr[i]) == float:
            sr[i] = str(sr[i])

def generator(s, n):
    d = []
    i = 0
    while i < n:
        p = random.randint(0, s)
        if p not in d:
            d.append(p)
            i +=1
    return d


print("Введите путь к входному файлу:")
s = str(input())
print("Введите количество генов:")
n = int(input())
print("Введите название выходного файла:")
name = str(input())

df = pd.read_excel(s)
num = [i for i in range(1,len(df['Entry'])+1)]

df.insert(0, '№', num)

g = generator(len(df['Gene names']), n)
g.sort()


columns = df.columns
f = pd.DataFrame(columns=columns)

i = 0
for j in tqdm(g):
    time.sleep(0.1)
    f.loc[i] = df.loc[j]
    i += 1

f.to_excel(name)
print('Выбор генов завершен. Нажмите Enter')
input()
