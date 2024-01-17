# Welcome the user
'''welcome = [
"He"
]

question = [
  
]
You are working for a food delivery app, and you need to create a chatbot that will help customers when their food hasn’t arrived.

options = [
  "Buy a product"
]
 # Collect the user’s name and age
 # Ask the user how it can help them
# Allow the user to choose from a menu/list of options on how they can continue the conversation
#-Include one menu option for exiting the conversation. This option should display a goodbye message and end your program.'''
class user:
  def __init__(self):
    self.name = ''
    self.age = ''
    self.choice = ''
  def biogrhapicalinfo(self):
    self.name = input("What is your name? ")
    self.age = input ("How old are you? ")
  def menu(self):
    print(f"Welcome to my online store, I can see that you are named {self.name} and you are {self.age} years old.")
    print("How can I help you today? ")
  def choices(self):

  
    print(" 1. Buy a product.\n 2.Return a Product. \n 3. Speak to a representative. \n 4. Exit Store.")
    self.choice = int(input("Pick the number of the option you want to choose."))
    if self.choice < 4 or choice > 1:
      if self.choice == 1:
        print("Placeholder")
      elif self.choice == 2:
        print("Placeholder")
      elif self.choice == 3:
        print("Placeholder")
      else:
        print("Goodbye!")
    else:
      print("Please enter a valid number.")
      self.choice = int(input("Pick the number of the option you want to choose."))
user1 = user()    
user1.biogrhapicalinfo()  
user1.menu()
user1.choices()