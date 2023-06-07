import random
import shutil 

terminal_width = shutil.get_terminal_size().columns

print("Password Generator | Created by: itswhiteboard")
print("_" * terminal_width)

def pass_gen():

  user_input = str(input("\nEnter # of characters: "))

  char_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "[", "}", "]", "|"]

  if user_input == "":
    pass_gen()
  elif not user_input.isdigit():
    pass_gen()
  
  user_input = int(user_input)
  
  if user_input < 1:
    pass_gen()

  pass_output = random.choices(char_list, k = user_input)
  
  print("\nPassword: ")
  print("".join(pass_output))
  print("_" * 50)

  pass_gen()

pass_gen()
