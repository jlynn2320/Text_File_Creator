name = input("What's your name? \n")
color = input("what's your favorite color? \n")
with open('example.txt', 'w') as file:
    file.write(f"{name} created this file")
    file.write(f"\n{color} favorite color")
          
