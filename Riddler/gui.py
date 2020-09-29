from gui_utils import create_tooltip, Entry_w_Placeholder
from random_generator import Random_generator

import os
import tkinter as tk
from tkinter import ttk
import pyperclip


class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        """
        Class constructor
        
        Parameters
        ----------
        *args:
            pass
        **kwargs:
            pass
        """
        super().__init__(*args, **kwargs)
        self.clrs = {'main': '#ADC4D6',
                     'button': '#A7B4D9'}
        self.__init_frames()
        self.bind('<Key-Escape>', self.exit_window)
        self.bind('<Control-Key-d>', self.exit_window)
        self.title('Riddler')
        #self.geometry('1000x1000')
        self.protocol("WM_DELETE_WINDOW", self.exit_window)        

    def show_frame(self, name):
        """
        Shows the frame with the given name.
        
        Parameters
        ----------
        name: str
            The name of the frame
        """
        self.frames[name].tkraise()

    def __init_frames(self):
        """
        Initialises the frames
        """
        container = ttk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1) # make the cell in grid cover the entire window
        container.grid_columnconfigure(0, weight=1) # make the cell in grid cover the entire window
        self.frames = {}

        for F in (MainPage, CalcPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(MainPage)

    def exit_window(self, event=None):
        """
        Event handler to exit the window. 
        Destroys the window when the Escape key is used.
        
        Parameters
        ----------
        event:
            The event to handle
        """
        self.destroy()
    
class MainPage(tk.Frame):
    """
    """
    def __init__(self, parent, controller):
        super().__init__(parent, bg=controller.clrs['main'])

        self.rnd_gen = Random_generator()

        self.init_frames(controller)
        self.init_message_widgets(controller)
        self.init_password_widgets(controller)
        self.init_psswd_diff_widgets(controller)

    def init_frames(self, controller):
        self.frame_password = tk.Frame(self, bg=controller.clrs['main'])
        self.frame_password.pack(side='top', fill='both')
        self.frame_diffic = tk.Frame(self, bg=controller.clrs['main'])
        self.frame_diffic.pack(side='top', fill='both')

    def init_message_widgets(self, controller):
        self.label_message =  tk.Label(self.frame_password, text='',
                                       bg=controller.clrs['main'])
        self.label_message.pack(side='top', padx=10)

    def init_password_widgets(self, controller):
        frame_left = tk.Frame(self.frame_password, bg=controller.clrs['main'])
        frame_right = tk.Frame(self.frame_password, bg=controller.clrs['main'])
        frame_left.pack(side='left', fill='both')
        frame_right.pack(side='right', fill='both')
        
        self.label_password = tk.Label(frame_left, text='Password',
                                       bg=controller.clrs['main'])
        self.label_password.pack(side='top', padx=10)

        self.result_password = tk.Entry(frame_left,
                                       bg=controller.clrs['main'])
        self.result_password.pack(side='top', padx=10)
        self.result_password.insert(0, ('*'*8))
        #self.result_password = tk.Label(frame_left, text='********',
        #                               bg=controller.clrs['main'])
        #self.result_password.pack(side='top', padx=10)
        create_tooltip(self.result_password,
                       text='The resulting password will be shown here if selected')

        self.hide_password = tk.IntVar()
        check_hide_password = tk.Checkbutton(frame_left, text='Hide password',
                                         variable=self.hide_password,
                                         onvalue=1, offvalue=0,
                                         bg=controller.clrs['main'])
        check_hide_password.pack(side='top', fill='both', padx=5)
        self.hide_password.set(1)
        create_tooltip(check_hide_password, text='Toggle the password to be hidden. Does not refresh unless a password is generated.')
        
        self.button_password = tk.Button(frame_left, text='Generate password',
                                         command= self.generate_password,
                                         bg=controller.clrs['button'])
        self.button_password.pack(side='top', fill='both', padx=10)
        create_tooltip(self.button_password, text='Generate a password')

        self.label_omit = tk.Label(frame_right, text='Characters to exclude:',
                                   bg=controller.clrs['main'])
        self.label_omit.pack(side='top', padx=10)
        self.entry_omit = tk.Entry(frame_right, bg=controller.clrs['main'])
        self.entry_omit.pack(side='top', padx=10)
        create_tooltip(self.entry_omit,
                       text='Type (or paste) any characters here to omit from a password')

        self.label_length = tk.Label(frame_right, text='Length of the password',
                                     bg=controller.clrs['main'])
        
        self.label_length.pack(side='top', padx=10)
        self.entry_length = tk.Entry(frame_right, bg=controller.clrs['main'])
        self.entry_length.insert(0, '8')
        self.entry_length.pack(side='top', padx=10)

        self.mem_password = tk.IntVar()
        check_mem_password = tk.Checkbutton(frame_right, text='Create memorable password',
                                            variable=self.mem_password,
                                            onvalue=1, offvalue=0,
                                            bg=controller.clrs['main'])
        check_mem_password.pack(side='top', fill='both', padx=5)
        self.mem_password.set(0)
        self.label_mem = tk.Label(frame_right, text='Memorable phrase:',
                                     bg=controller.clrs['main'])
        self.label_mem.pack(side='top', padx=10)
        self.entry_mem = tk.Entry(frame_right, bg=controller.clrs['main'])
        self.entry_mem.pack(side='top', padx=10)
        

    def init_psswd_diff_widgets(self, controller):
        frame_left = tk.Frame(self.frame_diffic, bg=controller.clrs['main'])
        frame_right = tk.Frame(self.frame_diffic, bg=controller.clrs['main'])
        frame_left.pack(side='left', fill='both')
        frame_right.pack(side='right', fill='both')
        
        self.label_entropy = tk.Label(frame_left, text='Nr bits required:',
                                      bg=controller.clrs['main'])
        self.label_entropy.pack(side='top', fill='both')

        self.label_guesses = tk.Label(frame_left, text='Maximum nr of guesses:',
                                      bg=controller.clrs['main'])
        self.label_guesses.pack(side='top', fill='both')

        self.label_entropy_res = tk.Label(frame_right, text='',
                                      bg=controller.clrs['main'])
        self.label_entropy_res.pack(side='top', fill='both')

        self.label_guesses_res = tk.Label(frame_right, text='',
                                      bg=controller.clrs['main'])
        self.label_guesses_res.pack(side='top', fill='both')

    def generate_password(self):
        if self.entry_length.get().isdigit():
            length = int(self.entry_length.get())
        else:
            length = 8

        omit = self.entry_omit.get() + ' '

        if self.mem_password.get() == 1:
            psswd = self.rnd_gen.create_memorable_string(pass_phrase=self.entry_mem.get(),
                                                         chars_to_omit=omit,
                                                         string_length=length)
        else:
            psswd = self.rnd_gen.create_random_str(chars_to_omit=omit,
                                                   string_length=length)
        
        self.result_password.delete(0, 'end')
        if self.hide_password.get() == 0:
            #self.result_password['text'] = psswd
            self.result_password.insert(0, psswd)
        else:
            #self.result_password['text'] = '*'*length
            self.result_password.insert(0, '*'*length)
            
        #self.result_password.update()
        self.copy_to_clipboard(psswd)
        self.update_message_timer('Password copied to clipboard')
        self.update_entropy(len(psswd))

    def update_entropy(self, psswd_length):
        entropy = self.rnd_gen.calculate_entropy(psswd_length)
        guesses = self.rnd_gen.calculate_max_guesses(entropy)

        self.label_entropy_res['text'] = entropy
        self.label_entropy_res.update()
        self.label_guesses_res['text'] = guesses
        self.label_guesses_res.update()
        
    def update_message(self, text):
        self.label_message['text'] = text
        self.label_message.update()
        
    def update_message_timer(self, text, time=5000):
        self.update_message('')
        self.update_message(text)
        #self.label_message.after(2000, self.update_message(''))

    def copy_to_clipboard(self, password):
        pyperclip.copy(password)
        pyperclip.paste()

class CalcPage(tk.Frame):
    """
    """
    def __init__(self, parent, controller):
        super().__init__(parent, bg=controller.clrs['main'])


    
if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
