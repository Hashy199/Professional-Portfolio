import pandas as pd
data = pd.read_csv('morse codes.csv')
if data.isna:
    data.dropna()

user_str = input("Please enter the string you want to convert : \n").upper().strip()
morse_code = ""

for char in user_str:
    morse_code += data.loc[data['char'] == char].code.values[0]
    morse_code += " "


print(f"The morse code is : {morse_code}")
