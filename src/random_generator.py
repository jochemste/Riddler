import random
import string
import secrets

class Random_generator():

    def __init__(self):
        pass

    def __del__(self):
        pass

    def create_random_str(self, chars_to_omit: list= [' '],
                          include_asciilowercase: bool = True,
                          include_asciiuppercase: bool = True,
                          include_digits: bool =True,
                          include_spec_chars: bool =True,
                          unique_only: bool = False,
                          string_length: int = 8):
        if string_length <= 0:
            return ''
        
        library = ''
        random_string: list = ['']
        
        if(include_asciilowercase == True):
            library = library + string.ascii_lowercase
        if(include_asciiuppercase == True):
            library = library + string.ascii_uppercase
        if(include_digits == True):
            library = library + string.digits
        if(include_spec_chars == True):
            library = library + string.punctuation

        if(unique_only == True):
            random_string = ''.join(random.SystemRandom().sample(library, string_length))
            random_string = list(random_string)
            for i in range(len(chars_to_omit)):
                for c in range(len(random_string)):
                    while(chars_to_omit[i] == random_string[c]):
                        random_string[c] = random.SystemRandom().sample(library, 1)
        else:
            random_string = ''.join(secrets.choice(library) for i in range(string_length))
            random_string = list(random_string)
            for i in range(len(chars_to_omit)):
                for c in range(len(random_string)):
                    while(chars_to_omit[i] == random_string[c]):
                        random_string[c] = secrets.choice(library)
                    
        return ''.join(random_string)

    def create_memorable_string(self, pass_phrase: str,
                                chars_to_omit: list= [' '],
                                include_asciilowercase: bool = True,
                                include_asciiuppercase: bool = True,
                                include_digits: bool =True,
                                include_spec_chars: bool =True,
                                unique_only: bool = False,
                                string_length: int = 8):
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
        
