#!/usr/bin/env python3
import random
import string
import secrets
import numpy as np

class Random_generator():

    def __init__(self):
        self.library_size = 0

    def __del__(self):
        pass

    def create_random_str(self,
                          chars_to_omit: list= [' '],
                          include_asciilowercase: bool = True,
                          include_asciiuppercase: bool = True,
                          include_digits: bool =True,
                          include_spec_chars: bool =True,
                          unique_only: bool = False,
                          string_length: int = 8):
        """
        Creates a string of random characters.

        Characters can be omitted, lowercase can be omitted, uppercase can be omitted, 
        digits can be omitted, special characters can be omitted, all characters can be set to 
        be unique and the string length can be set.
        """
        if string_length <= 0:
            return ''
        
        library = ''
        random_string: list = ['']

        # Set the library of characters
        if(include_asciilowercase == True):
            library = library + string.ascii_lowercase
        if(include_asciiuppercase == True):
            library = library + string.ascii_uppercase
        if(include_digits == True):
            library = library + string.digits
        if(include_spec_chars == True):
            library = library + string.punctuation

        temp_library = ''
        for i in range(len(library)):
            if not(library[i] in chars_to_omit):
                temp_library += library[i]
        library = temp_library
            
        self.library_size = len(library)

        # Create a string of unique characters
        if(unique_only == True):
            random_string = ''.join(random.SystemRandom().sample(library, string_length))
            random_string = list(random_string)
            for i in range(len(chars_to_omit)):
                for j in range(len(random_string)):
                    while(chars_to_omit[i] == random_string[j]):
                        random_string[j] = random.SystemRandom().sample(library, 1)
        # Create a string of random characters (Recommended)
        else:
            random_string = ''.join(secrets.choice(library) for i in range(string_length))
            random_string = list(random_string)
            for i in range(len(chars_to_omit)):
                for j in range(len(random_string)):
                    while(chars_to_omit[i] == random_string[j]):
                        random_string[j] = secrets.choice(library)
                    
        return ''.join(random_string)

    def create_memorable_string(self, pass_phrase: str,
                                chars_to_omit: list= [' '],
                                include_asciilowercase: bool = True,
                                include_asciiuppercase: bool = True,
                                include_digits: bool =True,
                                include_spec_chars: bool =True,
                                unique_only: bool = False,
                                string_length: int = 8):
        """
        Creates a string of characters, based on a given pass phrase. The first letter of all 
        words in the phrase are taken to add to the string, followed by random characters, 
        until the string is of the desired length.

        This creates less strong
        passwords than 'create_random_str()', since the characters are based on a given phrase 
        and therefore not completely random. This is improved by making the string_length longer 
        and allowing the function to supplement the string with some random characters.
        """
        pass_phrase = pass_phrase.split(' ')
        memorable_string = []

        for part in pass_phrase:
            memorable_string.append(part[0])

        rnd_str = self.create_random_str(chars_to_omit,
                                         include_asciilowercase,
                                         include_asciiuppercase,
                                         include_digits,
                                         include_spec_chars,
                                         unique_only,
                                         string_length-len(memorable_string))

        return ''.join(memorable_string) + rnd_str

    def calculate_entropy(self, nr_chars, library_size=None):
        if library_size == None:
            library_size = self.library_size
        entropy = np.ceil(nr_chars*(np.log(library_size)/np.log(2)))
        return int(entropy)

    def calculate_max_guesses(self, entropy):
        guesses = 2**(entropy-1)
        return int(guesses)

        

if __name__ == '__main__':

    rangen = Random_generator()

    p1 = rangen.create_random_str(string_length=12)
    print(p1)

    p2 = rangen.create_memorable_string(pass_phrase = 'python3 can be cool',
                                        string_length=12)
    print(p2)
