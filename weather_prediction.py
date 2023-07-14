"""import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB

url = 'https://raw.githubusercontent.com/codejust4U/dataset/main/play_tennis.csv'
dataset = pd.read_csv(url)

numerics = LabelEncoder()

inputs = dataset.drop('play',axis='columns')
target = dataset['play']

inputs['outlook_n']=numerics.fit_transform(inputs['outlook'])
inputs['temp_n']=numerics.fit_transform(inputs['temp'])
inputs['humidity_n']=numerics.fit_transform(inputs['humidity'])
inputs['windy_n']=numerics.fit_transform(inputs['wind'])

clf = GaussianNB()

clf.fit(inputs,target)"""

"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB

url = 'https://raw.githubusercontent.com/codejust4U/dataset/main/play_tennis.csv'
dataset = pd.read_csv(url)

numerics = LabelEncoder()

inputs = dataset.drop('play', axis='columns')
target = dataset['play']

inputs['outlook_n']=numerics.fit_transform(inputs['outlook'])
inputs['temp_n']=numerics.fit_transform(inputs['temp'])
inputs['humidity_n']=numerics.fit_transform(inputs['humidity'])
inputs['windy_n']=numerics.fit_transform(inputs['wind'])

inputs_encoded = pd.get_dummies(inputs)  # Perform one-hot encoding

clf = GaussianNB()

clf.fit(inputs_encoded, target)


clf.predict([[1,1,0,0]])"""


import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB

url = 'https://raw.githubusercontent.com/codejust4U/dataset/main/play_tennis.csv'
dataset = pd.read_csv(url)

numerics = LabelEncoder()

inputs = dataset.drop('play', axis='columns')
target = dataset['play']

inputs['outlook_n'] = numerics.fit_transform(inputs['outlook'])
inputs['temp_n'] = numerics.fit_transform(inputs['temp'])
inputs['humidity_n'] = numerics.fit_transform(inputs['humidity'])
inputs['windy_n'] = numerics.fit_transform(inputs['wind'])

inputs_encoded = pd.get_dummies(inputs)  # Perform one-hot encoding

clf = GaussianNB()

clf.fit(inputs_encoded, target)

# Create a sample input for prediction
sample_input = {
    'outlook_n': [1],
    'temp_n': [1],
    'humidity_n': [0],
    'windy_n': [0],
    'outlook_sunny': [0],
    'outlook_overcast': [1],
    'outlook_rainy': [0],
    'temp_hot': [0],
    'temp_mild': [1],
    'temp_cool': [0],
    'humidity_high': [0],
    'humidity_normal': [1],
    'windy_false': [1],
    'windy_true': [0]
}

sample_input_df = pd.DataFrame(sample_input)

prediction = clf.predict(sample_input_df)
print(prediction)
