import pandas as pd

# list of name, degree, score
# nme = ["aparna", "pankaj", "sudhir", "Geeku"]
nme=["my name is rajnish","my name is kaka","whats uyour name","k ff dfdf"]

deg = ["MBA", "BCA", "M.Tech", "MBA"]
scr = [90, 40, 80, 98]

# dictionary of lists
dict = {'name': nme, 'degree': deg, 'score': scr}

df = pd.DataFrame(dict)
df1=df

# df['q']=df['name'].apply(lambda row:len(row.split(" ")))
# df['q'] = df['name'].map(lambda x: len(x.split(" ")))
# df['q'] = [(lambda x: len(x.split(" "))) (n) for n in df['name']]


print(df)
