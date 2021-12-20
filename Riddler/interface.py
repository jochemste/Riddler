from random_generator import Random_generator
import pyperclip
import sys
import getopt

class CLI_Interface():
    rg: Random_generator
    def __init__(self):
        print("Welcome to Riddler. The Random password generator.")
        self.rg = Random_generator()
        self.argv = sys.argv[1:]
        self.opts, self.args = getopt.getopt(self.argv, '-l:-o:')
        self.strlength=16
        self.omit=[' ']
        
        for opt in self.opts:
            if opt[0] == '-l':
                self.strlength=int(opt[1])
            elif opt[0] == '-o':
                self.omit = str(opt[1])+' '

    def __del__(self):
        print("Stay secure! Bye!")

    def run_single(self):
            
        password = self.rg.create_random_str(string_length=self.strlength,
                                             chars_to_omit=self.omit)
        if 'print' in self.args:
            print("    " + password)
        else:
            print('*'*self.strlength)
        choice = ''
        while (not(choice == 'y') and not(choice == 'n')):
            choice = input("Copy password to clipboard? <y, n>")
            if choice == 'y':
                self.__copy_to_clipboard(password)

    def __copy_to_clipboard(self, password):
        pyperclip.copy(password)
        pyperclip.paste()
        print("Password copied to clipboard.")
        #print("Paste it to wherever you need it and press enter, when ready.")
        #print("Your clipboard will be cleared, once the program ends.")
        #input("Ready? <Enter>\n")
