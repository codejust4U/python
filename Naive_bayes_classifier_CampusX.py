import numpy as np
import pandas as pd


url = 'https://raw.githubusercontent.com/codejust4U/dataset/main/play_tennis.csv'
dataset = pd.read_csv(url)


dataset.head()
dataset.drop(columns=['day'],inplace=True)
print(dataset)

print("\n\n",dataset['play'].value_counts())

py = 9/14
pn = 5/14
print("\n\n",py,'\n',pn)

print("\n\n",pd.crosstab(dataset['outlook'],dataset['play']))

PovercastN = 0
PrainN = 2/5
PsunnyN = 3/5

PovercastY = 4/9
PrainY = 3/9
PsunnyY = 2/9

print("\n\n",pd.crosstab(dataset['temp'],dataset['play']))

PcoolN = 1/5
PhotN = 2/5
PmildN = 2/5

PcoolY = 3/9
PhotY = 2/9
PmildY = 4/9

print("\n\n",pd.crosstab(dataset['humidity'],dataset['play']))

PhighN = 4/5
PnormalN = 1/5

PhighY = 3/9
Pnormaly = 6/9

print("\n\n",pd.crosstab(dataset['wind'],dataset['play']))

PstrongN = 3/5
PweakN = 2/5

PstrongY = 3/9
PweakY = 6/9

Pyes = py*PsunnyY*PhotY*PhighY*PweakY
print("\n\n",Pyes)

Pno = pn*PsunnyN*PhotN*PhighN*PweakN
print("\n\n",Pno)


print("Outlook = sunny, temp = hot, humidity = high, wind = weak")
if Pyes>Pno:
    print("\n\n","Play = Yes")
else:
    print("\n\n","Play =  No")