import pandas as pd
data = {
    "Name":["Shrishty","Agrim","Arsh",],
    "Age" :[17,17,17],
    "State":["Uttrakhand","Uttarpradesh","Bihar"]
}
df = pd.DataFrame(data)
print(df.head(3))
