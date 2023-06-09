import os
import random
import sqlite3
import tkinter as tk

root = tk.Tk()
root.geometry("800x600")
root.resizable(width=True, height=True)

def forget_main_page():
    title_header.pack_forget()
    desc_text.pack_forget()
    passman_button.pack_forget()
    passgen_button.pack_forget()
    encrypt_button.pack_forget()
    decrypt_button.pack_forget()
    passlookup_button.pack_forget()

def pass_lookup():

    global pass_list

    pass_list = []

    def forget_pass_lookup():
        back_button.pack_forget()
        title_header.pack_forget()
        instruction.pack_forget()
        password.pack_forget()
        lookup_button.pack_forget()

    def back_button():
        forget_pass_lookup()
        delete_passwords()
        main_page()

    def delete_passwords():
        for response in pass_list:
            response.destroy()
            pass_list.remove(response)

    def search_passwords():

        delete_passwords()

        passw = password.get()

        with open("breach.txt", "r") as file:
            data = file.read()
            if passw in data:
                response = tk.Label(root, text="Password leaked in data breach!", font=("Arial", 15))
                response.pack(pady=10)
                pass_list.append(response)
            else:
                response = tk.Label(root, text="Password not in any known data breach.", font=("Arial", 15))
                response.pack(pady=10)
                pass_list.append(response)

    root.title("OpenPM | Password Lookup")

    forget_main_page()

    back_button = tk.Button(root, text="<--", font=("Arial", 10), command=back_button)

    title_header = tk.Label(root, text="Password Lookup", font=("Arial", 20))
    instruction = tk.Label(root, text="Enter a password:", font=("Arial", 15))
    password = tk.Entry(root)
    lookup_button = tk.Button(root, text="Lookup", command=search_passwords)

    back_button.pack(pady=5)

    title_header.pack(pady=10)
    instruction.pack(pady=10)
    password.pack(pady=10)
    lookup_button.pack(pady=10)

def pass_man():

    password_list = []

    def forget_pass_man():
        back_button.pack_forget()
        title_header5.pack_forget()
        disclaimer.pack_forget()
        instruction6.pack_forget()
        vault_name.pack_forget()
        instruction7.pack_forget()
        vault_pass.pack_forget()
        create_vault_button.pack_forget()
        enter_vault_button.pack_forget()

    # Later add every module to a list and then pack forget them like you did the passwords 

    def back_button():
        forget_pass_man()
        main_page()

    def create_vault():

        user_input = vault_name.get()
        user_input2 = vault_pass.get()

        user_input = user_input.replace(" ", "-")

        db = sqlite3.connect(f'{user_input}.sql')
        cursor = db.cursor()

        create_table_query = '''
        CREATE TABLE IF NOT EXISTS vault (
            vault_name TEXT,
            vault_pass TEXT
        );
        '''

        insert_query = "INSERT INTO vault (vault_name, vault_pass) VALUES (?, ?)"
        values = (f"{user_input}", f"{user_input2}",)

        cursor.execute(create_table_query)
        cursor.execute(insert_query, values)

        db.commit()

        cursor.close()
        db.close()

        vault_name.delete(0, tk.END)
        vault_pass.delete(0, tk.END)

    def enter_vault():

        global website, password

        def forget_enter_vault():
            back_button2.pack_forget()
            title_header6.pack_forget()
            instruction8.pack_forget()
            user_entry6.pack_forget()
            instruction9.pack_forget()
            user_entry7.pack_forget()
            submit_password.pack_forget()

        def back_button():
            delete_passwords()
            forget_enter_vault()
            pass_man()

        def delete_passwords():
            for passwords in password_list: # For every password in password list
                passwords.destroy() # Destroy that password
            password_list.clear() # Then clear the password list

        def add_password():

            user_input = vault_name.get()

            website = user_entry6.get()
            password = user_entry7.get()

            user_input = user_input.replace(" ", "-")
            user_entry6_value = user_entry6.get().replace(".", "_")

            db = sqlite3.connect(f'{user_input}.sql')
            cursor = db.cursor()

            create_table_query = f'''
            CREATE TABLE IF NOT EXISTS {user_entry6_value} (
                website TEXT,
                password TEXT
            );
            '''

            insert_query = f"INSERT INTO {user_entry6_value} (website, password) VALUES (?, ?)"
            values = (f"{website}", f"{password}")

            cursor.execute(create_table_query)
            cursor.execute(insert_query, values)

            db.commit()

            vault_name.delete(0, tk.END)
            vault_pass.delete(0, tk.END)

            cursor.close()
            db.close()

        user_input = vault_name.get()
        user_input2 = vault_pass.get()

        user_input = user_input.replace(" ", "-")

        directory = os.path.dirname(os.path.realpath(__file__)) # Gets the directory of the current python file

        os.chdir(directory) # Changes the current directory to the directory of the current python file

        if os.path.isfile(f'{user_input}.sql') == True: # If SQL file is a file (not a directory)
            pass # Continue
        elif os.path.exists(f'{user_input}.sql') == False: # If SQL file doesn't exist
            print(f"{user_input} doesn't exist, please try again.")
            return 1
        elif os.path.exists(f'{user_input}.sql') == True: 
            print(f"{user_input} already exists, please try again.")
            return 1
        else:
            pass

        db = sqlite3.connect(f'{user_input}.sql')

        cursor = db.cursor()

        select_query = "SELECT * FROM vault WHERE vault_name = ? AND vault_pass = ?"

        cursor.execute(select_query, (user_input, user_input2))
        result = cursor.fetchone()

        if result == (user_input, user_input2):
            pass
        else:
            return 1
        
        cursor.close()
        db.close()

        forget_pass_man()

        back_button2 = tk.Button(root, text="<--", font=("Arial", 10), command=back_button)

        title_header6 = tk.Label(root, text="Password Manager", font=("Arial", 30))
        instruction8 = tk.Label(root, text="Enter Website", font=("Arial", 12))
        user_entry6 = tk.Entry(root)
        instruction9 = tk.Label(root, text="Enter Password", font=("Arial", 12))
        user_entry7 = tk.Entry(root)
        submit_password = tk.Button(root, text="Submit Password", font=("Arial", 15), command=add_password)

        back_button2.pack()

        title_header6.pack()
        instruction8.pack()
        user_entry6.pack()
        instruction9.pack()
        user_entry7.pack()
        submit_password.pack(pady=10)

        db = sqlite3.connect(f'{user_input}.sql')

        cursor = db.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        
        tables = cursor.fetchall()

        for table in tables:
            table_name = table[0]

            cursor.execute(f"SELECT * FROM {table_name}")

            results = cursor.fetchall()

            if "vault" in table_name:
                continue

            passwords = tk.Label(root, text=f"{results}", font=("Arial", 10))

            for row in results: # For every row in results
                passwords.pack() # Print password to screen
                password_list.append(passwords) # Append password to password_list
                
        cursor.close()
        db.close()

    root.title("OpenPM | Password Manager")

    forget_main_page()

    back_button = tk.Button(root, text="<--", font=("Arial", 10), command=back_button)

    title_header5 = tk.Label(root, text="Password Manager", font=("Arial", 30))
    disclaimer = tk.Label(root, text="DISCLAIMER: Passwords are stored locally in your computer's filesystem. Note this before using!", font=("Arial", 12), bg="red")
    instruction6 = tk.Label(root, text="Vault Name", font=("Arial", 20))
    vault_name = tk.Entry(root)
    instruction7 = tk.Label(root, text="Vault Password", font=("Arial", 20))
    vault_pass = tk.Entry(root)
    create_vault_button = tk.Button(root, text="Create Vault", font=("Arial", 12), command=create_vault)
    enter_vault_button = tk.Button(root, text="Enter Vault", font=("Arial", 12), command=enter_vault)

    back_button.pack(pady=5)

    title_header5.pack(padx=20, pady=20)
    disclaimer.pack()
    instruction6.pack(pady=10)
    vault_name.pack()
    instruction7.pack(pady=10)
    vault_pass.pack()
    create_vault_button.pack(pady=10)
    enter_vault_button.pack(pady=10)

def pass_gen():

    global generated_pass_list

    generated_pass_list = []

    def back_button():
        back_button.pack_forget()
        title_header2.pack_forget()
        instruction.pack_forget()
        user_entry.pack_forget()
        generate_pass.pack_forget()
        pass_output.pack_forget()
        delete_pass()
        main_page()

    def delete_pass():
        for generated_pass in generated_pass_list:
            generated_pass.destroy()
            generated_pass_list.remove(generated_pass)
            
    def get_input():

        global generated_pass

        delete_pass()

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

        generated_pass_list.append(generated_pass)

    root.title("OpenPM | Password Generator")

    forget_main_page()

    back_button = tk.Button(root, text="<--", font=("Arial", 10), command=back_button)

    title_header2 = tk.Label(root, text="Password Generator", font=("Arial", 30))
    instruction = tk.Label(root, text="Enter # of characters:")
    user_entry = tk.Entry(root)
    generate_pass = tk.Button(root, text="Generate Password", font=("Arial", 12), command=get_input)
    pass_output = tk.Label(root, text="Password: ", font=("Arial", 15))

    back_button.pack(pady=5)

    title_header2.pack(padx=20, pady=20)
    instruction.pack()
    user_entry.pack()
    generate_pass.pack(pady=10)
    pass_output.pack(pady=20)

def encrypt_pass():

    global encrypted_pass_list

    encrypted_pass_list = []

    def back_button():
        back_button.pack_forget()
        title_header3.pack_forget()
        instruction2.pack_forget()
        user_entry2.pack_forget()
        instruction3.pack_forget()
        user_entry3.pack_forget()
        encrypt_pass.pack_forget()
        pass_output2.pack_forget()
        delete_pass()
        main_page()

    def delete_pass():
        for encrypted_pass in encrypted_pass_list:
            encrypted_pass.destroy()
            encrypted_pass_list.remove(encrypted_pass)

    def get_input():

        global encrypted_pass

        delete_pass()

        user_input = user_entry2.get()
        shift_input = user_entry3.get()

        char_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "[", "}", "]", "|"]

        encrypt_output = ""
  
        for char in user_input:
            value = char_list.index(char) # Finds the corresponding number of the letter in the input
            shift_value = value + int(shift_input) # Adds the value of the corresponding number to the shift
            shifted_char = char_list[shift_value % len(char_list)] # Goes to char_list and finds the new letter
            encrypt_output += shifted_char # Adds the shifted character to the output

        encrypted_pass = tk.Label(root, text=encrypt_output, font=("Arial", 15))
        encrypted_pass.pack()

        encrypted_pass_list.append(encrypted_pass)
            
    root.title("OpenPM | Password Encryptor")

    forget_main_page()

    back_button = tk.Button(root, text="<--", command=back_button)

    title_header3 = tk.Label(root, text="Password Encryptor", font=("Arial", 30))
    instruction2 = tk.Label(root, text="Enter a password to encrypt:", font=("Arial", 12))
    user_entry2 = tk.Entry(root)
    instruction3 = tk.Label(root, text="Enter a shift value:", font=("Arial", 12))
    user_entry3 = tk.Entry(root)
    encrypt_pass = tk.Button(root, text="Encrypt Password", font=("Arial", 12), command=get_input)
    pass_output2 = tk.Label(root, text="Password: ", font=("Arial", 15))

    back_button.pack()

    title_header3.pack(padx=20, pady=20)
    instruction2.pack()
    user_entry2.pack()
    instruction3.pack()
    user_entry3.pack()
    encrypt_pass.pack(pady=10)
    pass_output2.pack(pady=20)

def decrypt_pass():

    global decrypted_pass_list

    decrypted_pass_list = []

    def back_button():
        back_button.pack_forget()
        title_header4.pack_forget()
        instruction4.pack_forget()
        user_entry4.pack_forget()
        instruction5.pack_forget()
        user_entry5.pack_forget()
        decrypt_pass.pack_forget()
        pass_output3.pack_forget()
        delete_pass()
        main_page()

    def delete_pass():
        for decrypted_pass in decrypted_pass_list:
            decrypted_pass.destroy()
            decrypted_pass_list.remove(decrypted_pass)

    def get_input():

        global decrypted_pass

        delete_pass()

        user_input = user_entry4.get()
        shift_input = user_entry5.get()

        char_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "[", "}", "]", "|"]

        decrypt_output = ""
  
        for char in user_input:
            value = char_list.index(char) # Finds the corresponding number of the letter in the input
            shift_value = value - int(shift_input) # Adds the value of the corresponding number to the shift
            shifted_char = char_list[shift_value % len(char_list)] # Goes to char_list and finds the new letter
            decrypt_output += shifted_char # Adds the shifted character to the output

        decrypted_pass = tk.Label(text=decrypt_output, font=("Arial", 15))
        decrypted_pass.pack()

        decrypted_pass_list.append(decrypted_pass)

    root.title("OpenPM | Password Decryptor")
    
    forget_main_page()

    back_button = tk.Button(root, text="<--", font=("Arial", 10), command=back_button)

    title_header4 = tk.Label(root, text="Password Decryptor", font=("Arial", 30))
    instruction4 = tk.Label(root, text="Enter a password to decrypt:", font=("Arial", 12))
    user_entry4 = tk.Entry(root)
    instruction5 = tk.Label(root, text="Enter a shift value:", font=("Arial", 12))
    user_entry5 = tk.Entry(root)
    decrypt_pass = tk.Button(root, text="Decrypt Password", font=("Arial", 12), command=get_input)
    pass_output3 = tk.Label(root, text="Password: ", font=("Arial", 15))

    back_button.pack(pady=5)

    title_header4.pack(padx=20, pady=20)
    instruction4.pack()
    user_entry4.pack()
    instruction5.pack()
    user_entry5.pack()
    decrypt_pass.pack(pady=10)
    pass_output3.pack(pady=20)

def main_page():

    global title_header, desc_text, passlookup_button, passman_button, passgen_button, encrypt_button, decrypt_button

    root.title("OpenPM | Main Page")

    title_header = tk.Label(root, text="OpenPM", font=("Arial", 30))

    desc_text = tk.Label(root, text="OpenPM, the open source password manager written entirely in Python!", font=("Arial", 15)) 

    passlookup_button = tk.Button(root, text="Password Lookup", font=("Arial", 20), command=pass_lookup)
    passman_button = tk.Button(root, text="Password Manager", font=("Arial", 20), command=pass_man)
    passgen_button = tk.Button(root, text="Password Generator", font=("Arial", 20), command=pass_gen)
    encrypt_button = tk.Button(root, text="Password Encryption", font=("Arial", 20), command=encrypt_pass)
    decrypt_button = tk.Button(root, text="Password Decryption", font=("Arial", 20), command=decrypt_pass)

    title_header.pack(padx=20, pady=20)
    desc_text.pack(pady=10)
    passlookup_button.pack(pady=15)
    passman_button.pack(pady=15)
    passgen_button.pack(pady=15)
    encrypt_button.pack(pady=15)
    decrypt_button.pack(pady=15)

    root.mainloop()

main_page()