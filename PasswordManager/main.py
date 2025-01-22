# to create GUI
import tkinter as tk
from tkinter import messagebox, scrolledtext
# to encrypt
from cryptography.fernet import Fernet # type: ignore
# simple DB
import sqlite3
# to interact with OS
import os


class Encryption:
    # __init__ is the constructor method that is called when an object is created from the class
    def __init__(self, key_file="key.key"):
        # Initializing attributes
        # This is the file where the encryption key is or will be stored
        self.key_file = key_file
        # The key is loaded from the file or generated
        self.key = self.load_or_generate_key()
        # Encryption method that uses the key to encrypt/decrypt data
        self.cipher = Fernet(self.key)

    # If the key file exists, the method loads the key and returns it.
    # If the key file does not exist, it generates a new key, saves it to the file, and returns the new key.
    # This ensures that the key is persistent between program runs, allowing the same key to be reused for encryption and decryption operations.
    def load_or_generate_key(self):
        # Check if the key file exists at the path specified by self.key_file
        if os.path.exists(self.key_file):
            # If the key file exists, open the file in binary read mode ('rb')
            with open(self.key_file, "rb") as key_file:
                # Read the key from the file and return it
                return key_file.read()
        else:
            # If the key file doesn't exist, generate a new key using Fernet
            key = Fernet.generate_key()
            # Open the key file in binary write mode ('wb') to save the generated key
            with open(self.key_file, "wb") as key_file:
                # Write the newly generated key to the file
                key_file.write(key)
            # Return the key
            return key

    # data - text to be encrypted
    def encrypt(self, data):
        # Returns the encrypted data (in bytes)
        return self.cipher.encrypt(data.encode())
    
    # data - text to be decrypted
    def decrypt(self, data):
        # Returns the decrypted data as a string
        return self.cipher.decrypt(data).decode()


class PasswordManager:
    # __init__ is the constructor
    def __init__(self, db_file="passwords.db"): 
        # Initializing attributes
        # Creates an instance of the 'Encryption' class and assigns it to the 'self.encryption' attribute
        # This instance will be used for encryption and decryption operations
        self.encryption = Encryption()
        # This file will be used for storing the data in a SQLite database
        self.db_file = db_file
        # This file will be used for storing the data in a SQLite database
        self.connection = self.create_database()

    def create_database(self):
        # Establish a connection to the SQLite database specified by self.db_file
        connection = sqlite3.connect(self.db_file)
        # Create a cursor object that allows interaction with the database
        cursor = connection.cursor()
        # Execute the SQL command to create a table called 'passwords'
        # The table will have three columns: service, username, and password
        # The service and username column is the PRIMARY KEY, meaning each service name will be unique
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS passwords (
                service TEXT,
                username TEXT,
                password TEXT,
                PRIMARY KEY (service, username)
            )"""
        )
        # Save (commit) the changes to the database
        connection.commit()
        # Return the connection object to allow further database operations
        return connection

    def add_password(self, service, username, password):
        # Encrypt stored password. This ensures that passwords are stored securely in the database
        encrypted_password = self.encryption.encrypt(password)
        
        # Create a cursor object to interact with the database
        cursor = self.connection.cursor()

        cursor.execute(
            "SELECT * FROM passwords WHERE service = ? AND username = ?",
            (service, username)
        )
        if cursor.fetchone():
            return False  # This service and username combination already exists

        try:
            
            # Execute an SQL INSERT statement to add a new record to the 'passwords' table
             # '?' placeholders are used to prevent SQL injection, and actual values are provided as a tuple
            cursor.execute(
                "INSERT INTO passwords (service, username, password) VALUES (?, ?, ?)",
                (service, username, encrypted_password),
            )
            # Commit the transaction to save the changes to the database
            self.connection.commit()
            return True
        #If a SQLite IntegrityError occurs (e.g., duplicate service key), return False.
        except sqlite3.IntegrityError:
            return False

    def retrieve_password(self, service, username):
        # Create a cursor object to interact with the database
        cursor = self.connection.cursor()
        # Execute an SQL SELECT query to fetch the username and encrypted password for the given service
        cursor.execute("SELECT username, password FROM passwords WHERE service = ? AND username = ?", (service, username))
        # Fetch the first result from the query
        result = cursor.fetchone()
        if result:
            # If a matching record is found, unpack the result into 'username' and 'encrypted_password'
            username, encrypted_password = result
            # Decrypt the encrypted password using the 'decrypt' method of the Encryption object
            decrypted_password = self.encryption.decrypt(encrypted_password)
            # Return the username and the decrypted password
            return username, decrypted_password
        else:
            return None
    
    #Get a list of all saved records
    def get_all_passwords(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT service, username, password FROM passwords")
        records = cursor.fetchall()
        return records


class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")

        # Create an instance of PasswordManager
        self.manager = PasswordManager()

        # Configure the grid to be responsive
        root.columnconfigure(0, weight=1)  # Allow column 0 to grow
        root.columnconfigure(1, weight=2)  # Allow column 1 to grow more than column 0
        root.rowconfigure(0, weight=1)  # Allow row 0 to grow (optional for rows)
        root.rowconfigure(1, weight=1)  # Allow row 1 to grow (optional for rows)

        # Service name input
        self.service_label = tk.Label(root, text="Service:")
        self.service_label.grid(row=0, column=0, padx=10, pady=10)
        self.service_entry = tk.Entry(root)
        self.service_entry.grid(row=0, column=1, padx=10, pady=10)

        # Username input
        self.username_label = tk.Label(root, text="Username:")
        self.username_label.grid(row=1, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(root)
        self.username_entry.grid(row=1, column=1, padx=10, pady=10)

        # Password input
        self.password_label = tk.Label(root, text="Password:")
        self.password_label.grid(row=2, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)

        # Add Password Button
        self.add_button = tk.Button(root, text="Add Password", command=self.add_password)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Retrieve Password Button
        self.retrieve_button = tk.Button(root, text="Retrieve Password", command=self.retrieve_password)
        self.retrieve_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Show all passwords button
        self.show_all_button = tk.Button(root, text="Show All Passwords", command=self.show_all_passwords)
        self.show_all_button.grid(row=5, column=0, columnspan=2, pady=10)

    # Add new record
    def add_password(self):
        service = self.service_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Validate input
        if not service or not username or not password:
            messagebox.showerror("Error", "All fields must be filled.")
            return

        success = self.manager.add_password(service, username, password)

        if success:
            messagebox.showinfo("Success", f"Password for '{service}' and username '{username}' added successfully.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", f"Service '{service}' and/or username '{username}' already exists.")

    # Get a record
    def retrieve_password(self):
        service = self.service_entry.get()
        username = self.username_entry.get()
        
        # Validate input
        if not service or not username:
            messagebox.showerror("Error", "Please enter both service and username.")
            return

        result = self.manager.retrieve_password(service, username)

        if result:
            username, password = result
            messagebox.showinfo("Password", f"Service: {service}\nUsername: {username}\nPassword: {password}")
        else:
            messagebox.showerror("Error", f"No entry found for service '{service}' and username '{username}'.")

    # Show all saved records
    def show_all_passwords(self):
        records = self.manager.get_all_passwords()
        
        # Message if DB empty
        if not records:
            messagebox.showinfo("No Records", "No records found.")
            return
        
        records_window = tk.Toplevel(self.root)
        records_window.title("All Saved Passwords")
        
        text_widget = scrolledtext.ScrolledText(records_window, width=50, height=20)
        text_widget.pack(padx=10, pady=10)

        # List to hold the encrypted passwords for later toggling visibility
        decrypted_passwords = {}

        for record in records:
            service, username, encrypted_password = record
            decrypted_password = self.manager.encryption.decrypt(encrypted_password)
            decrypted_passwords[(service, username)] = decrypted_password

            # Initially display masked password
            masked_password = "****"  

            text_widget.insert(tk.END, f"Service: {service}, Username: {username}, Password: {masked_password}\n")
       
        # Password visibility state (Initially, passwords are hidden)
        passwords_visible = False

        # Function to toggle the password visibility
        def toggle_password_visibility():
            
            nonlocal passwords_visible
            # Visibility state false
            passwords_visible = not passwords_visible

            # Toggle between showing and hiding passwords
            text_widget.config(state=tk.NORMAL)  # Enable editing to change text
            text_widget.delete(1.0, tk.END)  # Clear existing text
            
            # Rebuild the list with the current visibility (masked or decrypted passwords)
            for record in records:
                service, username, encrypted_password = record
                if passwords_visible:
                    decrypted_password = decrypted_passwords.get((service, username), "****")
                else:
                    # Hide the password again if not visible
                    decrypted_password = "****"  
                
                text_widget.insert(tk.END, f"Service: {service}, Username: {username}, Password: {decrypted_password}\n")
            
            # Disable editing to prevent further changes
            text_widget.config(state=tk.DISABLED)

        # Add the eye toggle button
        show_button = tk.Button(records_window, text="👁️ Show/Hide", command=toggle_password_visibility)
        show_button.pack(pady=10)
        
        # Disable editing initially
        text_widget.config(state=tk.DISABLED)  



    def clear_entries(self):
        self.service_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()

    # Create and run the application
    app = PasswordManagerApp(root)

    # Start the Tkinter event loop
    root.mainloop()
