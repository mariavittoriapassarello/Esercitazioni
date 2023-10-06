import pandas as pd 
graduates = ({'name': ["Maria Vittoria", "Greta", "Andrea"], 'age': [24,25,23]})
dataframe = pd.DataFrame(graduates)
print("Graduates:")
print(dataframe)

print("In ordine crescente di età:")
print(dataframe.sort_values('age'))