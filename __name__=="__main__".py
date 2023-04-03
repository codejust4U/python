#pk.py file
def welcome():
  response = str(input("How are you dude? "))
  print("I\'m ", response)


print(__name__)

#like it get the output as twice coz once the welcome function is already been executed at pk.py and 
#again executed at pk.py so it runs two times in order to avoid that we use __name__, it helps to get the output only one times

if __name__ == "__main__":
  welcome()

#at the output level if user runs the python main.py, it runs from pk.py and if the user runs python pk.py, it runs from __main__



--------------------------------------------------------------------------------------------------------------------------------------------------------

#main.py

import pk

pk.welcome()
