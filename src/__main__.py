## @file
from interface import Interface

def main():
    i = Interface()
    i.run_single()
"""rg = Random_generator()
    print("Welcome to Riddler. The Random password generator.")
    print("Default: " + rg.create_random_str())
    print("No letters: " + rg.create_random_str(include_asciilowercase=False,
                                                include_asciiuppercase=False))
    print("No lowercase: " + rg.create_random_str(include_asciilowercase=False))
    print("No uppercase: " + rg.create_random_str(include_asciiuppercase=False))
    print("No digits: " + rg.create_random_str(include_digits=False))
    print("No special chars: " + rg.create_random_str(include_spec_chars=False))
    print("Unique only: " + rg.create_random_str(unique_only=True))
    print("Length adjusted: " + rg.create_random_str(string_length=15))
    print("Omit chars: " + rg.create_random_str(chars_to_omit= ['1', '2', '3',
                                                                '4', '5', '6',
                                                                '7', '8', '9']))"""
    
if __name__ == "__main__":
    main()
