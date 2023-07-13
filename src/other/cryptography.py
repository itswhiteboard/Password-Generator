import shutil

def start_prompt():
  
  start_input = input("Type E for Encryption | Type D for Decryption: ")
  
  while start_input.upper() != "E" and start_input.upper() != "D":
    start_input = input("Type E for Encryption | Type D for Decryption: ")

  if start_input.upper() == "E":
    encryption()
  elif start_input.upper() == "D":
    decryption()

def encryption():

  user_input = input("\nPassword: ")
  shift_input = input("\nShift: ")

  char_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "[", "}", "]", "|"]

  encrypt_output = ""
  
  for char in user_input:
    value = char_list.index(char) # Finds the corresponding number of the letter in the input
    shift_value = value + int(shift_input) # Adds the value of the corresponding number to the shift
    shifted_char = char_list[shift_value % len(char_list)] # Goes to char_list and finds the new letter
    encrypt_output += shifted_char # Adds the shifted character to the output

  print("\nOutput: " + encrypt_output)
  print("_" * terminal_width + "\n")

  start_prompt()
    
def decryption():
  
  user_input = input("\nPassword: ")
  shift_input = input("\nShift: ")

  char_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "[", "}", "]", "|"]

  encrypt_output = ""
  
  for char in user_input:
    value = char_list.index(char) # Finds the corresponding number of the letter in the input
    shift_value = value - int(shift_input) # Minuses the value of the corresponding number to the shift
    shifted_char = char_list[shift_value % len(char_list)] # Goes to char_list and finds the new letter
    encrypt_output += shifted_char # Adds the shifted character to the output

  print("\nOutput: " + encrypt_output)
  print("_" * terminal_width + "\n")

  start_prompt()

terminal_width = shutil.get_terminal_size().columns
print("Password Cryptography | Created by: itswhiteboard")
print("_" * terminal_width + "\n")

start_prompt()
