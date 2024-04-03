"""
Calculator Module

This module contains the implementation of a simple calculator GUI application using tkinter.
It provides classes and functions to create a calculator window with basic arithmetic operations.

Classes:
    - Calculator: A class to create a calculator that performs basic arithmetic operations.

Functions:
    - None

Constants:
    - None

Modules Required:
    - tkinter: For creating the GUI components of the calculator.
    - calc_operations: A custom module providing additional arithmetic operations for the calculator.

Example:
    >>> from calculator import Calculator
    >>> calc = Calculator()
    >>> calc.window.mainloop()
"""

# Importing required modules
import tkinter as tk

from calc_operations import CalcOperations


class Calculator(CalcOperations):
    """
    A class to create a calculator that performs basic calculation operations.

    Attributes:
    ----------
        window_title: (str): The title of the calculator window.
        window_padx (int): Horizontal padding of the calculator window.
        window_pady (int): Vertical padding of the calculator window.
        window_bg_color (str): Background color of the calculator window.
        primary_display_text (tk.StringVar): String variable for primary display.
        secondary_display_text (tk.StringVar): String variable for secondary display.
        display_bg (str): Background color of the display area.
        primary_display_font (tuple): Font for primary display.
        secondary_display_font (tuple): Font for secondary display.
        btn_bg (str): Background color of buttons.
        btn_operator_bg (str): Background color of operator buttons.
        btn_equal_bg (str): Background color of equal button.
        btn_active_bg (str): Background color of active buttons.
        btn_disabled_bg (str): Background color of disabled buttons.
        btn_padx (tuple): Horizontal padding of buttons.
        btn_pady (tuple): Vertical padding of buttons.
        btn_back_pady (tuple): Padding for the 'Back' button.
        btn_borderwidth (int): Border width of buttons.
        btn_height (int): Height of buttons.
        btn_width (int): Width of buttons.
        btn_digit_font (tuple): Font for digit buttons.
        btn_operator_font (tuple): Font for operator buttons.
        stick (str): Sticky parameter for grid layout.
        last_operation (str): String to store the last operation performed.
        accumulator (float): Accumulator to store temporary results.
        flag (int): A variable that ensures that the code inside the operation functions like 'do_plus' works only if there is input in the screen.
        Error (str): Error message for division by zero.

    Methods:
        __init__(): Initialize the Calculator class.
        create_main_window(): Create the main window of the calculator.
        create_menu(): Create the menu for the calculator.
        create_display(): Create the display area for the calculator.
        create_info_label(): Create the information label for the calculator.
        create_button(): Create buttons for the calculator.
    """

    def __init__(self):
        """
        Initialize the Calculator class.

        Initialize the Calculator class along with necessary method calls
        to create the calculator.

        Attributes:
            window_title (str): The title of the calculator window.
            window_padx (int): Horizontal padding of the calculator window.
            window_pady (int): Vertical padding of the calculator window.
            window_bg_color (str): Background color of the calculator window.
            primary_display_text (tk.StringVar): String variable for primary display.
            secondary_display_text (tk.StringVar): String variable for secondary display.
            display_bg (str): Background color of the display area.
            primary_display_font (tuple): Font for primary display.
            secondary_display_font (tuple): Font for secondary display.
            btn_bg (str): Background color of buttons.
            btn_operator_bg (str): Background color of operator buttons.
            btn_equal_bg (str): Background color of equal button.
            btn_active_bg (str): Background color of active buttons.
            btn_disabled_bg (str): Background color of disabled buttons.
            btn_padx (tuple): Horizontal padding of buttons.
            btn_pady (tuple): Vertical padding of buttons.
            btn_back_pady (tuple): Padding for the 'Back' button.
            btn_borderwidth (int): Border width of buttons.
            btn_height (int): Height of buttons.
            btn_width (int): Width of buttons.
            btn_digit_font (tuple): Font for digit buttons.
            btn_operator_font (tuple): Font for operator buttons.
            stick (str): Sticky parameter for grid layout.
            last_operation (str): String to store the last operation performed.
            accumulator (float): Accumulator to store temporary results.
            flag (int): Flag variable.
            Error (str): Error message for division by zero.

        Returns:
            None
        """
        self.window_title = 'Calculator'
        self.window_padx = 20
        self.window_pady = 20
        self.window_bg_color = '#ECEFFB'

        # Calling create_main_window create the main window.
        self.create_main_window()
        # Calling create_menu create the menu.
        self.create_menu()

        self.primary_display_text = tk.StringVar()
        self.primary_display_text.set('0')
        self.secondary_display_text = tk.StringVar()
        self.secondary_display_text.set('0')
        self.display_bg = '#FFFFFF'
        self.primary_display_font = ('Courier New', '28', 'bold')
        self.secondary_display_font = ('Courier New', '16', 'bold')

        self.btn_bg = '#FCFDFF'
        self.btn_operator_bg = '#F8FAFE'
        self.btn_equal_bg = '#A0D3E7'
        self.btn_active_bg = '#EAEEFC'
        self.btn_disabled_bg = '#F5F5F5'
        self.btn_padx = (1, 1)
        self.btn_pady = (1, 1)
        self.btn_back_pady = (10, 1)
        self.btn_borderwidth = 0
        self.btn_height = 2
        self.btn_width = 2
        self.btn_digit_font = ('', '14', 'bold')
        self.btn_operator_font = ('', '14', '')
        self.stick = tk.N + tk.S + tk.E + tk.W

        self.last_operation = ''
        self.accumulator = 0.
        self.flag = 0
        self.Error = 'Div. by 0 Error!'

        # Calling create_display create the calculator display.
        self.create_display()
        # Calling create_info_label create the infomation label.
        self.create_info_label()
        # Calling create_button create calculator buttons.
        self.create_button()

    def create_main_window(self):
        """
        Create the main window of the calculator.

        This method initializes the main window of the calculator with specific attributes.

        Attributes:
            self.window (tk.Tk): The main window of the calculator.
            self.window_title (str): The title of the calculator window.
            self.window_padx (int): Horizontal padding of the calculator window.
            self.window_pady (int): Vertical padding of the calculator window.
            self.window_bg_color (str): Background color of the calculator window.

        Returns:
            None
        """
        self.window = tk.Tk()
        self.window.title(self.window_title)
        # Make the window stiff.
        self.window.resizable(width=False, height=False)
        self.window.config(padx=self.window_padx,
                           pady=self.window_padx,
                           bg=self.window_bg_color)
        self.window.tk.call('wm', 'iconphoto', self.window._w,
                            tk.PhotoImage(file='calc_fevicon.png'))     # Set the non-default icon to the window.

    def create_menu(self):
        """
        Create the menu for the calculator.

        This method adds menu options to the main menu bar of the calculator window.

        Attributes:
            self.window (tk.Tk): The main window of the calculator.
            self.under_maintenace (function): Callback function for the 'Scientific calculator' menu option.
            self.are_you_sure (function): Callback function for the 'Quit' menu option.
            self.about_app (function): Callback function for the 'About' menu option.

        Local Variables:
            main_menu (tk.Menu): The main menu bar of the calculator window.
            sub_menu_file (tk.Menu): The submenu under the 'File' menu.

        Returns:
            None
        """
        # Adding main menu to the main self.window.
        main_menu = tk.Menu(self.window)
        self.window.config(menu=main_menu)

        # Adding options to the main menu bar with empty sub_menu.
        sub_menu_file = tk.Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label='File', menu=sub_menu_file, underline=0)
        # Adding items to the file menu.
        sub_menu_file.add_command(label='Standard calculator')
        sub_menu_file.add_command(
            label='Scientific calculator', command=self.under_maintenace)
        sub_menu_file.add_separator()    # Add line separator.
        sub_menu_file.add_command(label='Quit',
                                  command=self.are_you_sure,
                                  underline=0,
                                  accelerator='Ctrl-Q')
        # Bind Ctr-Q and Ctr-q event to the specified callback.
        self.window.bind('<Control-Q>', self.are_you_sure)
        self.window.bind('<Control-q>', self.are_you_sure)

        # Adding options to the main menu bar with callback.
        main_menu.add_command(label='About',
                              command=self.about_app,
                              underline=0)

    def create_display(self):
        """
        Create the display area for the calculator.

        This method creates labels for primary and secondary displays.

        Attributes:
            self.window (tk.Tk): The main window of the calculator.
            self.under_maintenace (function): Callback function for the 'Scientific calculator' menu option.
            self.are_you_sure (function): Callback function for the 'Quit' menu option.
            self.about_app (function): Callback function for the 'About' menu option.

        Local Variables:
            primary_display (tk.Label): The primary display of the menu.
            secondary_display (tk.Label): The secondary display of the menu.

        Returns:
            None
        """
        secondary_display = tk.Label(master=self.window,
                                     width=16,
                                     font=self.secondary_display_font,
                                     textvariable=self.secondary_display_text,
                                     anchor='e',
                                     bg=self.display_bg)
        primary_display = tk.Label(master=self.window,
                                   width=16,
                                   font=self.primary_display_font,
                                   textvariable=self.primary_display_text,
                                   anchor='e',
                                   bg=self.display_bg)

        secondary_display.grid(row=0, columnspan=4, sticky=self.stick)
        primary_display.grid(row=1, columnspan=4, sticky=self.stick)

    def create_info_label(self):
        """
        Create the information label for the calculator.

        This method creates a label at the bottom of the calculator for additional information
        such as developer's email.

        Attributes:
            self.window (tk.Tk): The main window of the calculator.
            self.window_bg_color (str): Background color of the calculator window.

        Local Variables:
            company_label (tk.Label): The label widget displaying developer's email.

        Returns:
            None
        """
        company_label = tk.Label(master=self.window,
                                 text='Developer Email:\nashish.bmistry@gmail.com',
                                 font=('Arial', '8', ''),
                                 bg=self.window_bg_color,
                                 anchor='sw',
                                 justify=tk.LEFT)

        company_label.grid(row=2, column=0, columnspan=3,
                           sticky=self.stick, pady=(0, 5))

    def create_button(self):
        """
        Create buttons for the calculator.

        This method creates buttons for digits and various operations, places them inside the grid, 
        and binds them to respective callback functions.

        Attributes:
            buttons_dict (dict): A dictionary to store button objects with their respective text as keys.

        Local Variables:
            btn_texts (list): A list of strings representing the text for each button.
            rows (int): An integer representing the row counter for button placement initialization.
            cols (int): An integer representing the column counter for button placement initialization.

        Each button is created with specific attributes and configured with appropriate commands and bindings.
        After creating each button, it is added to the `buttons_dict` dictionary for later access.
        The buttons are placed inside the main window using the grid layout manager.

        Callbacks (Handler functions):
            - do_backspace: Handles the Backspace button press event.
            - do_clear: Handles the Clear (C) button press event.
            - do_clear_entry: Handles the Clear Entry (CE) button press event.
            - do_percent: Handles the Percentage (%) button press event.
            - do_divd: Handles the Division (/) button press event.
            - do_multi: Handles the Multiplication (x) button press event.
            - do_minus: Handles the Subtraction (-) button press event.
            - do_plus: Handles the Addition (+) button press event.
            - do_equal: Handles the Equal (=) button press event.
            - do_dot: Handles the Dot (.) button press event.
            - do_digit_0: Handles the Digit 0 (0) button press event.
            - do_plusminus: Handles the Plus/Minus (+/-) button press event.
            - do_digit_x: Handles the Digit buttons (1-9) press event.
        """
        # Empty dictionary to store buttons object.
        self.buttons_dict = {}
        # List to stores all button's text. Order of the element in the list
        # decides the way buttons are placed inside the window.
        btn_texts = ['Back', 'C', 'CE', '%', '/', '7', '8', '9', 'x', '4',
                     '5', '6', '-', '1', '2', '3', '+', '+/-', '0', '.', '=']
        rows = 3    # Row counter initialization.
        cols = 3    # Column counter initialization.

        # Creating button objects with specified properties.
        for btn_text in btn_texts:
            btn = tk.Button(master=self.window,
                            text=btn_text,
                            height=self.btn_height,
                            width=self.btn_width,
                            bg=self.btn_operator_bg,
                            activebackground=self.btn_active_bg,
                            font=self.btn_operator_font,
                            borderwidth=self.btn_borderwidth)

            if btn_text == 'Back':
                btn.config(command=self.do_backspace)
                self.window.bind('<BackSpace>', self.do_backspace)
            elif btn_text == 'C':
                btn.config(command=self.do_clear)
                self.window.bind('<Escape>', self.do_clear)
            elif btn_text == 'CE':
                btn.config(command=self.do_clear_entry)
                self.window.bind('<Delete>', self.do_clear_entry)
            elif btn_text == '%':
                btn.config(command=self.do_percent)
                self.window.bind('%', self.do_percent)
            elif btn_text == '/':
                btn.config(command=self.do_divd)
                self.window.bind('/', self.do_divd)
            elif btn_text == 'x':
                btn.config(command=self.do_multi)
                self.window.bind('*', self.do_multi)
            elif btn_text == '-':
                btn.config(command=self.do_minus)
                self.window.bind('-', self.do_minus)
            elif btn_text == '+':
                btn.config(command=self.do_plus)
                self.window.bind('+', self.do_plus)
            elif btn_text == '=':
                btn.config(command=self.do_equal,
                           bg=self.btn_equal_bg)
                self.window.bind('=', self.do_equal)
                self.window.bind('<Return>', self.do_equal)
            elif btn_text == '.':
                btn.config(command=self.do_dot,
                           font=self.btn_digit_font)
                self.window.bind('.', self.do_dot)
            elif btn_text == '0':
                btn.config(command=self.do_digit_0,
                           font=self.btn_digit_font,
                           bg=self.btn_bg)
                self.window.bind('0', self.do_digit_0)
            elif btn_text == '+/-':
                btn.config(command=self.do_plusminus)
                self.window.bind('<F9>', self.do_plusminus)
            elif btn_text in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                btn.config(font=self.btn_digit_font,
                           bg=self.btn_bg)
                btn.bind('<Button-1>', self.do_digit_x)
                self.window.bind(btn_text, self.do_digit_x)

            # Storing each button object to the dictionary to access them later.
            self.buttons_dict.update([(btn_text, btn)])

            # Placing the buttons into the main window.
            btn.grid(row=(rows//4) + 2, column=cols % 4, sticky=self.stick,
                     pady=self.btn_back_pady if btn_text == 'Back' else self.btn_pady,
                     padx=self.btn_padx)
            rows += 1
            cols += 1


calc = Calculator()
calc.window.mainloop()
