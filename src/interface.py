from random_generator import Random_generator
import pyperclip


class Interface():
    rg: Random_generator
    def __init__(self):
        print("Welcome to Riddler. The Random password generator.")
        self.rg = Random_generator()

    def __del__(self):
        print("Stay secure! Bye!")

    def display_current_settings(self):
        pass

    def run_single(self):
        password = self.rg.create_random_str()
        print(password)
        choice = ''
        while ((choice is not 'y') and (choice is not 'n')):
            choice = input("Copy password to clipboard? <y, n>")
            if choice is 'y':
                pyperclip.copy(str(password))
                pyperclip.paste()
                
    def run_loop(self):
        self.display_current_settings()
        choice = input("Choose the options you want to enable/disable ")
        while(choice != "quit"):
            pass
