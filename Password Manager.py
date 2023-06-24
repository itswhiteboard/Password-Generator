import random
import tkinter as tk

global root
global entry

root = tk.Tk()
root.geometry("800x600")
root.title("OpenPM | Main Page")
root.resizable(width=True, height=True)

#def pass_man()

def pass_gen():

    def get_input():

        user_input = user_entry.get()

        char_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "[", "}", "]", "|"]

        if user_input == "":
            get_input()
        elif not user_input.isdigit():
            get_input()
  
        user_input = int(user_input)
  
        if user_input < 1 or user_input > 50:
            get_input()

        pass_output = random.choices(char_list, k = user_input)
        pass_output = "".join(pass_output)

        generated_pass = tk.Label(text=pass_output, font=("Arial", 15))
        generated_pass.pack()

    root.title("OpenPM | Password Generator")

    title_header.pack_forget()
    desc_text.pack_forget()
    passman_button.pack_forget()
    passgen_button.pack_forget()
    encrypt_button.pack_forget()
    decrypt_button.pack_forget()

    title_header2 = tk.Label(root, text="Password Generator", font=("Arial", 30))
    instruction = tk.Label(root, text="Enter # of characters:")
    user_entry = tk.Entry(root)
    generate_pass = tk.Button(root, text="Generate Password", font=("Arial", 12))
    pass_output = tk.Label(root, text="Password: ", font=("Arial", 15))

    title_header2.pack(padx=20, pady=20)
    instruction.pack()
    user_entry.pack()
    generate_pass.pack(pady=10)
    pass_output.pack(pady=20)

    generate_pass.config(command=get_input)

def encrypt_pass():

    root.title("OpenPM | Password Encryptor")
    
    # Forgets the main_page contents
    title_header.pack_forget()
    desc_text.pack_forget()
    passman_button.pack_forget()
    passgen_button.pack_forget()
    encrypt_button.pack_forget()
    decrypt_button.pack_forget()

    title_header3 = tk.Label(root, text="Password Encryptor", font=("Arial", 30))

    title_header3.pack(padx=20, pady=20)

def main_page():

    global title_header, desc_text, passman_button, passgen_button, encrypt_button, decrypt_button

    title_header = tk.Label(root, text="OpenPM", font=("Arial", 30))

    desc_text = tk.Label(root, text="OpenPM, the open source password manager written entirely in Python!", font=("Arial", 15)) 

    passman_button = tk.Button(root, text="Password Manager", font=("Arial", 20))
    passgen_button = tk.Button(root, text="Password Generator", font=("Arial", 20), command=pass_gen)
    encrypt_button = tk.Button(root, text="Password Encryption", font=("Arial", 20), command=encrypt_pass)
    decrypt_button = tk.Button(root, text="Password Decryption", font=("Arial", 20))

    title_header.pack(padx=20, pady=20)
    desc_text.pack(pady=10)
    passman_button.pack(pady=15)
    passgen_button.pack(pady=15)
    encrypt_button.pack(pady=15)
    decrypt_button.pack(pady=15)

    root.mainloop()

main_page()