import pandas as pd
import random

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


df = pd.read_excel('./Genes.xlsx')
num = [i for i in range(1,len(df['Entry'])+1)]
# df['№']=num
# df['№'].index
# Type(df["Gene names"])
# sorted(df['Gene names'])
# df.sort_values(['Gene names'])

df.insert(0, '№', num)
print(df)


#print(list(df['Gene names']))
# pr = random.sample(list(df['Gene names']),24000)
# print(pr)
# print(len(pr))
# pr = Type(pr)
# print(sorted(pr))

g = generator(len(df['Gene names']), 240)
g.sort()
print(g)
# print(sorted(g))
print(len(g))
print(df.iloc[4])


columns = df.columns
f = pd.DataFrame(columns=columns)
print(f)

i = 0
for j in g:
    f.loc[i] = df.loc[j]
    i += 1
    print(f)

# print(f.iloc[200])
# print(df.iloc[13035])

f.to_excel('gene.xlsx')