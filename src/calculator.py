"""
calculator module

This module contains the implementation of a simple calculator GUI
application using tkinter. It provides classes and methods to create
a calculator window with basic arithmetic operations.

Classes:
    Calculator: A class that represent a general calculator such as standard
        or scientific calculator.
    StandardCalc: A class representing a standard calculator that performs
        basic arithmetic operations.
    ScientificCalc: A class representing a scientific calculator that performs
        scientific operations.

Imports:
    tkinter: For creating the GUI components for the calculator application.
    tkinter.messagebox: For creating messagebox model dialog window.
    calc_operations: A custom module providing additional methods for
        arithmetic operations for the calculator.

Author:
    Ashish Kumar (ashish.bmistry@gmail.com)

Example:
    >>> from calculator import Calculator
    >>> calc = Calculator()
    >>> calc.window.mainloop()
"""

# Importing required modules
import tkinter as tk
from tkinter import messagebox

from calc_operations import CalcOperations


class Calculator(CalcOperations):
    """
    A class that represent a general calculator such as a standard or
    scientific calculator, a sublclass of CalOperations of calc_operations
    module.

    It implements common functionality that both standard and scientific
    calculator has such as creating main window, creating and placing display,
    menu, info label and buttons widget.

    Attributes:
        app_name (str): Application name.
        app_ver (str): Calculator application version information.
        app_copyright (str): Copyright information.
        app_developer (str): Developer information.
        window (tk.Tk): The main window of the calculator.
        frame (tk.Frame): The frame widget which is master widget of
            developer_label and button widgets.
        win_title_st_calc (str): Title of the standard calculator window.
        win_title_sci_calc (str): Title of scientific calculator window.
        win_padx (int): Horizontal padding of the calculator window.
        win_pady (int): Vertical padding of the calculator window.
        win_bg_color (str): Background color of the calculator
        display_bg (str): Background color of the display area.
        pri_display_font (tuple): Font for primary display.
        sec_display_font (tuple): Font for secondary display.
        btn_bg (str): Background color of buttons.
        btn_active_bg (str): Background color of active buttons.
        btn_padx (tuple): Horizontal padding of buttons.
        btn_pady (tuple): Vertical padding of buttons.
        btn_back_pady (tuple): Padding for the 'Back' button.
        btn_borderwidth (int): Border width of buttons.
        btn_height (int): Height of buttons.
        btn_width (int): Width of buttons.
        btn_digit_font (tuple): Font for digit buttons.
        btn_operator_font (tuple): Font for operator buttons.
        stick (str): Sticky parameter for grid layout.
        calc_type (StandardCalc | ScientificCalc): Stores instance of
            either StandardCalc or ScientificCalc class.

    Note:
        - Calculator class inherits attributes and methods from its parent
          class CalcOperations responsible for various arithmetic operations.
          This class extends CalcOperations class's behaviour.
        - Calculator class is also composed of either StandardCalc or
          ScientificCalc instances. It enables Calculator class to equip
          itself with additional attributes and methods of component class.
    """

    def __init__(self, calc_type):
        """
        Initialize the Calculator class.

        Initialize the Calculator class along with necessary method calls
        to create the calculator.

        Args:
            calc_types (StandardCalc | ScientificCalc): An instance of either
                StandardCalc or ScientificCalc class.

        Returns:
            None
        """
        self.app_name = 'Calculator'
        self.app_ver = 1.0
        self.app_copyright = 'Copyright 2024 © Ashish Kumar'
        self.app_developer = 'Ashish Kumar\nashish.bmistry@gmail.com'

        self.win_title_st_calc = 'Standard Calculator'
        self.win_title_sci_calc = 'Scientific Calculator'
        self.win_padx = 20
        self.win_pady = 20
        self.win_bg_color = '#ECEFFB'

        # Calling create_main_window create the main window.
        self.create_main_window()
        # Calling create_menu create the menu.
        self.create_menu()

        # Calling CalcOperations's __init__() to inherit its properties.
        super().__init__()

        self.display_bg = '#FFFFFF'
        self.pri_display_font = ('Courier New', '28', 'bold')
        self.sec_display_font = ('Courier New', '13', 'bold')
        self.btn_bg = '#FCFDFF'
        self.btn_active_bg = '#EAEEFC'
        self.btn_padx = (1, 1)
        self.btn_pady = (1, 1)
        self.btn_back_pady = (10, 1)
        self.btn_borderwidth = 0
        self.btn_height = 2
        self.btn_width = 7
        self.btn_digit_font = ('', '14', 'bold')
        self.btn_operator_font = ('', '14', '')
        self.stick = tk.N + tk.S + tk.E + tk.W

        # Calling create_display create the calculator display.
        self.create_display()
        # Calling create_frame to create a frame for developer_label and
        # buttons placement.
        self.create_frame()
        # Calling create_developer_label create the developer_label.
        self.create_developer_label()

        # calc_type stores object of either StandardCalc or ScientificCalc
        # class. By default, it stores StandardCalc class object as it is
        # the default calculator when the application start. If user selects
        # Scientific Calculator option from File menu, value of calc_type
        # will be replaced by ScientificCalc class object.
        self.calc_type = calc_type()
        # Calling create_button create calculator buttons.
        self.create_buttons()
        # Both standard and scientific calculator has differnt types of buttons
        # and buttons layout, so button placement is done by place_buttons
        # method of respective class. Note: self (reference to Calculator
        # instance) argument passed into place_buttons() definition is to
        # access its attributes inside place_buttons() method of eight
        # StandardCalc or ScientificCalc class.
        self.calc_type.place_buttons(self)

    def create_main_window(self):
        """
        Create the main window of the calculator.

        This method initializes the main window of the calculator with
        specified attributes.

        Returns:
            None
        """
        self.window = tk.Tk()
        self.window.title(self.win_title_st_calc)
        # Make the window stiff.
        self.window.resizable(width=False, height=False)
        self.window.config(padx=self.win_padx,
                           pady=self.win_padx,
                           bg=self.win_bg_color)
        # Set non-default icon to the window.
        self.window.tk.call('wm', 'iconphoto', self.window._w,
                            tk.PhotoImage(file='.\\static\\calc_fevicon.png'))

    def create_menu(self):
        """
        Create the menu for the calculator.

        This method adds menu options to the main menu bar of the calculator
        window.

        Note:
            - This method utilizes the following locally declared variables:
                - main_menu (tk.Menu): The main menu bar of the calculator
                  window.
                - sub_menu_file (tk.Menu): The submenu under the 'File' menu.
            - These variables are used internally within the method and are
              not exposed to the method's caller.

        Note:
            - This method implements callback binding for the following
              callbacks:
                - calc_type_switch(self, symbol):
                    Callback function to switch between Standard and Scientific
                    calculator.
                - are_you_sure(self, event=None):
                    Callback function for the 'Quit' menu option.
                - about_app(self):
                    Callback function for the 'About' menu option.

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
        sub_menu_file.add_command(
            label='Standard calculator',
            command=lambda: self.calc_type_switch("stand_calc"))
        sub_menu_file.add_command(
            label='Scientific calculator',
            command=lambda: self.calc_type_switch("sci_calc"))
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
        Create the primary and secondary display for the calculator.

        This method creates labels for primary and secondary displays.

        Note:
            - This method utilizes the following locally declared variables:
                - primary_display (tk.Label): The primary display of the
                  calculator.
                - secondary_display (tk.Label): The secondary display of the
                  calculator.
            - These variables are used internally within the method and are
              not exposed to the method's caller.

        Returns:
            None
        """
        secondary_display = tk.Label(master=self.window,
                                     width=self.sec_display_width,
                                     font=self.sec_display_font,
                                     textvariable=self.sec_display_text,
                                     anchor='e',
                                     bg=self.display_bg,
                                     padx=4)
        primary_display = tk.Label(master=self.window,
                                   width=self.pri_display_width,
                                   font=self.pri_display_font,
                                   textvariable=self.pri_display_text,
                                   anchor='e',
                                   bg=self.display_bg)

        secondary_display.grid(row=0, columnspan=1, sticky=self.stick)
        primary_display.grid(row=1, columnspan=1, sticky=self.stick)

    def create_frame(self):
        """
        Create frame widget for developer_label and button widgets placement.

        Returns:
            None
        """
        self.frame = tk.Frame(master=self.window,
                              bg=self.win_bg_color)
        self.frame.grid(row=2,
                        column=0,
                        columnspan=1,
                        sticky=self.stick)

    def create_developer_label(self):
        """
        Create the developer label for the calculator.

        Creates a label at the bottom of the display for additional
        information to be shown about developer.

        Note:
            - This method utilizes the following locally declared variables:
                - developer_label (tk.Label): The label displaying information
                  about developer.
            - These variables are used internally within the method and are
              not exposed to the method's caller.

        Returns:
            None
        """
        developer_label = tk.Label(master=self.frame,
                                   text=f'Developer: {self.app_developer}',
                                   font=('Arial', '8', ''),
                                   bg=self.win_bg_color,
                                   anchor='sw',
                                   justify=tk.LEFT)

        developer_label.grid(row=0, column=0, columnspan=3,
                             sticky=self.stick, pady=(29, 5))

    def create_buttons(self):
        """
        Create button widgets for the calculator.

        This method creates buttons for digits and operators, and binds them
        to respective callback functions.

        Each button is created with specific attributes and configured with
        appropriate commands and bindings. After creating each button, it is
        added to the `buttons_dict` dictionary to access them later.

        Note:
            - This method utilizes the following locally declared variables:
                - btn_bg_color (str): background color for buttons.
                - btn_font (tuple): Font for buttons.
                - btn (tk.Button): Button widget object.
                - btn_text (str): A string representing button's text accessed
                  from btn_callbacks dictionary inherited from CalcOperations
                  class of calc_operations module.
                - callback (str): Name reference to the callback function for
                  each button respectively. It is accessed from btn_callbacks
                  dictionary inherited from CalcOperations class of
                  calc_operations module.
            - These variables are used internally within the method and are
              not exposed to the method's caller.

        Note:
            - This method implements callback binding for the following
              callbacks implemented in CalcOperations class of module
              calc_operations:
                - do_backspace(self, event=None): Handle Backspace button
                  press event.
                - do_clear(self, event=None): Handle Clear (C) button press
                  event.
                - do_clear_entry(self, event=None): Handle Clear Entry (CE)
                  button press event.
                - do_percent(self, event=None): Handle Percentage (%) button
                  press event.
                - do_divd(self, event=None): Handle Division (/) button press
                  event.
                - do_multi(self, event=None): Handle Multiplication (x) button
                  press event.
                - do_minus(self, event=None): Handle the Subtraction (-)
                  button press event.
                - do_plus(self, event=None): Handle Addition (+) button press
                  event.
                - do_equal(self, event=None, curr_operation='='): Handle Equal
                  (=) button press event.
                - do_dot(self, event=None): Handle Dot (.) button press event.
                - do_digit_0(self, event=None): Handle Digit 0 (0) button
                  press event.
                - do_plusminus(self, event=None): Handle Plus/Minus (+/-)
                  button press event.
                - do_digit_x(self, event=None): Handle Digit buttons (1-9)
                  press event.

        Returns:
            None
        """
        # Each time create_buttons() is called to create buttons for standard
        # or scientific calculator, it set buttons_dict to empty dictionary.
        self.buttons_dict = {}

        # Creating button objects with specified properties.
        for btn_text, callback in self.btn_callbacks.items():
            if btn_text in ['1', '2', '3', '4', '5',
                            '6', '7', '8', '9', '0']:
                btn_bg_color = self.btn_bg
                btn_font = self.btn_digit_font
            elif btn_text == '.':
                btn_bg_color = self.btn_operator_bg
                btn_font = self.btn_digit_font
            else:
                btn_bg_color = self.btn_operator_bg
                btn_font = self.btn_operator_font

            btn = tk.Button(master=self.frame,
                            text=btn_text,
                            height=self.btn_height,
                            width=self.btn_width,
                            bg=btn_bg_color,
                            activebackground=self.btn_active_bg,
                            font=btn_font,
                            borderwidth=self.btn_borderwidth)
            # Bind callback to mouse left click event.
            btn.bind('<Button-1>', callback)
            # Bind callback to keyboard event.
            self.window.bind(self.btn_key_events[btn_text], callback)

            if btn_text == '=':
                btn.config(bg=self.btn_equal_bg,
                           fg=self.btn_equal_fg)
                # Bind callback for Enter key additionally which is already
                # assigned for <KeyPress-equal> event.
                self.window.bind('<Return>', self.do_equal)

            # Store each button object to the dictionary to access them later.
            self.buttons_dict.update([(btn_text, btn)])

        # If type of calculator is Scientific, then create additional buttons
        # by calling create_buttons() of ScientificCalc class.
        if isinstance(self.calc_type, ScientificCalc):
            self.calc_type.create_buttons(self)

    def calc_type_switch(self, symbol):
        """
        A callback designed to switch between Standard and Scientific
        calculator.

        Args:
            symbol (str): A string representing type of calculator. The strings
                that represent type of calculator are either 'stand_calc' or
                'sci_calc'.

        Note:
            - This method performs following functionality.
                - Set title of the main window depending on selected type of
                  calculator from the menu options.
                - Depending on type of instance stored inside calc_type
                  attribute, it resets the calculator's state to its initial
                  state.
                - It destroys the frame widget which is master widget for
                  developer_label and button widgets, then create a new frame
                  widget object. By destroying frame, it also recursively
                  destroys all the button and developer_label widget, which
                  ensures that resources are freed up with the help python
                  garbadge collector.
                - Create new developer_label for the calculator.
                - Set calc_type to the instance of either StandardCalc or
                  ScientificCalc class depending on the selected calculator
                  type.
                - Create new buttons for the specific type calculator.
                - Places the developer_label and button widgets to the frame
                  widget.

        Returns:
            None
        """
        if not isinstance(self.calc_type,
                          StandardCalc) and symbol == 'stand_calc':
            self.window.title(self.win_title_st_calc)
            self.do_clear()
            self.frame.destroy()
            self.create_frame()
            self.create_developer_label()
            self.calc_type = StandardCalc()
            self.create_buttons()
            self.calc_type.place_buttons(self)
        elif not isinstance(self.calc_type,
                            ScientificCalc) and symbol == 'sci_calc':
            self.window.title(self.win_title_sci_calc)
            self.do_clear()
            self.frame.destroy()
            self.create_frame()
            self.create_developer_label()
            self.calc_type = ScientificCalc()
            self.create_buttons()
            self.calc_type.place_buttons(self)

    def about_app(self):
        """
        Display information about the application.

        It displays information about the application such as name, version,
        copyright and developer.

        Returns:
            None
        """
        messagebox.showinfo('About',
                            f'{self.app_name}\n'
                            + f'Version: {self.app_ver}\n\n'
                            + f'{self.app_copyright}\n\n'
                            + f'Developer: {self.app_developer}')

    def are_you_sure(self, event=None):
        """
        Prompt the user to confirm quitting the application.

        It displays a message box asking the user if they are sure they want
        to quit the application. If the user confirms, the application window
        is destroyed.

        Args:
            event (tk.Event, optional): An event parameter that can be provided
                when the method is called as a callback for quit event.
                Defaults to None.

        Returns:
            None
        """
        reply = messagebox.askyesno(title='Quit?',
                                    message='Are you sure you want to quit?')
        if reply:
            self.window.destroy()


class StandardCalc():
    """
    A class representing a standard calculator that performs basic arithmetic
    operations.

    This class defines additional methods required execlusively for Standard
    calculator not defined in Calculator class.

    Attributes:
        rows (int): Represent row counter for button placement.
        cols (int): Represent column counter for button placement.
    """

    def __init__(self):
        """
        Initialize the StandardCalc class along with necessary method calls
        to creating calculator.

        Returns:
            None
        """
        self.rows = 3    # Row counter for button placement initialization.
        self.cols = 3    # Column counter for button placement initialization.

    def place_buttons(self, calc):
        """
        Places buttons into frame widget of main window.

        It utilizes button_dict of Calculator class to access button widget
        object and grid geomatry to place buttons into frame widget of main
        window.

        Args:
            calc (Calcualator): An instance of Calculator class.

        Note:
            - This method utilizes the following locally declared variables:
                - btn_text (str): A string representing button's text from
                  buttons_dict dictionary of Calculator class.
                - btn (tk.Button): Button widget object.
            - These variables are used internally within the method and are
              not exposed to the method's caller.

        Returns:
            None
        """
        # buttons_dict attribute of Calculator class is used to place buttons
        # inside the main window using grid geomatry manager.
        for btn_text, btn in calc.buttons_dict.items():
            # Placing the buttons into the main window.
            btn.grid(row=(self.rows//4),
                     column=self.cols % 4,
                     sticky=calc.stick,
                     pady=calc.btn_back_pady if btn_text == 'Back' else calc.btn_pady,
                     padx=calc.btn_padx)
            self.rows += 1
            self.cols += 1


class ScientificCalc():
    """
    A class representing a scientific calculator that performs scientific
    operations.

    This class defines additional methods required execlusively for Scientific
    calculator not defined in Calculator class.

    Attributes:
        rows (int): Represent row counter for button placement.
        cols (int): Represent column counter for button placement.

    Todo:
        - Implemention of functionality for Scientific calculator.

    Note:
        - ScientificCalc class is under development.
    """

    def __init__(self):
        """
        Initialize the ScientificCalc class.

        Initialize the ScientificCalc class along with necessary method calls
        to creating calculator.

        Returns:
            None
        """
        self.rows = 3    # Row counter for button placement.
        self.cols = 3    # Column counter for button placement.

    def create_buttons(self, calc):
        """
        Create additional buttons for scientific calculator which are not part
        of the standard calculator.

        It use calc (instance of Calculator class) to access Calculator class's
        attributes to create additional buttons.

        Args:
            calc (Calculator): An instance of Calculator class.

        Returns:
            None
        """

    def place_buttons(self, calc):
        """
        Places buttons into frame widget of main window.

        It utilizes button_dict of Calculator class to access button widget
        object and grid geomatry to place buttons into frame widget of main
        window.

        Args:
            calc (Calculator): An instance of Calculator class.

        Note:
            - This method utilizes the following locally declared temporary
              variables:
                - under_develop (tk.Label): Temporary tk.Label widget
                  representing text that 'Scientific calculator is under
                  development'. It is placed inside the frame widget of
                  Calculator class.
            - These variables are used internally within the method and are
              not exposed to the method's caller.

        Note:
            - "As the ScientificCalc class is under development, a temporary
              message 'Scientific calculator is under development' is
              displayed on the screen when the user selects the Scientific
              calculator option from the menu."

        Returns:
            None
        """
        under_develop = tk.Label(master=calc.frame,
                                 text='Scientific calculator\n'
                                 + 'is under development.',
                                 bg=calc.win_bg_color,
                                 font=calc.btn_digit_font,
                                 width=29, height=13)
        under_develop.grid(row=1, column=2, padx=(4, 3), pady=(2, 1))


calc = Calculator(StandardCalc)
calc.window.mainloop()
