"""
calc_operations.py - Module containing the CalcOperations class for basic
calculator operations.

This module provides the CalcOperations class, which implements methods for
performing basic calculator operations such as addition, subtraction,
multiplication, division, percentage calculations, and more.

The CalcOperations class handles the internal logic of the calculator, including
parsing user input, performing calculations, handling errors, and updating
the calculator's display.

Author: Ashish Kumar
Contact: ashish.bmistry@gmail.com
"""
import tkinter as tk
from tkinter import messagebox


class CalcOperations:
    """
    A class to perform basic calculator operations.

    This class provides methods for various arithmetic operations such as addition,
    subtraction, multiplication, and division. It also includes methods for
    handling user input and error conditions.

    Attribute:
        - None

    Constants:
        - None

    Methods:
        string_to_double(self, str_value):
            Convert a string representation of a number to a float.

        double_to_string(self, num_value):
            Convert a float to a string representation with appropriate formatting.

        clear_if_error(self):
            Clear the display if an error message is currently being shown.

        disable_if_error(self):
            Disable operator buttons if an error message is currently being shown.

        do_clear(self, event=None):
            Reset the calculator's state to its initial state.

        do_clear_entry(self, event=None):
            Clear the current entry on the calculator display.

        do_digit_x(self, event=None):
            Handle input of digit characters (0-9) on the calculator display.

        do_dot(self, event=None):
            Handle input of the decimal point (.) on the calculator display.

        do_digit_0(self, event=None):
            Handle input of the digit 0 on the calculator display.

        do_plus(self, event=None):
            Perform addition operation.

        do_minus(self, event=None):
            Perform subtraction operation.

        do_multi(self, event=None):
            Perform multiplication operation.

        do_divd(self, event=None):
            Perform division operation.

        do_percent(self, event=None):
            Calculate the percentage of a number.

        do_equal(self, event=None, symbol='='):
            Perform the calculation when the equal button is pressed.

        do_plusminus(self, event=None):
            Toggle the sign of the current number.

        do_backspace(self, event=None):
            Remove the last character from the calculator display.

        under_maintenace(self):
            Show a message indicating that the scientific calculator is under maintenance.

        about_app(self):
            Show information about the developer and contact details.

        are_you_sure(self, event=None):
            Ask the user for confirmation before quitting the application.
        """

    def string_to_double(self, str_value):
        """
        Convert a string to a floating-point number.

        Parameters:
            str_value (str): The string value to convert.

        Local Variable:
            num_value (float): The converted float value.

        Returns:
            float or None: The converted floating-point number if successful, None otherwise.
        """
        try:
            num_value = float(str_value)

            return num_value
        except ValueError:
            return None

    def double_to_string(self, num_value):
        """
        Convert a floating-point number to a string.

        Parameters:
            num_value (float): The number to convert.

        Local Variable:
           str_value (str): The converted string value.

        Returns:
            str: The converted string representation of the number.
        """
        str_value = str(num_value)

        if '.' in str_value:
            while str_value[-1] == '0':
                str_value = str_value[0:-1]

        if str_value[-1] == '.':
            str_value = str_value[0:-1]

        if len(str_value) > 16:
            str_value = float(str_value)
            # Format the string to scientific notation if length is greater than 16 digits.
            str_value = "{:e}".format(str_value)

        return str_value

    def clear_if_error(self):
        """
        Clear the display if an error message is present in the display.

        Local Variable:
           str_value (str): The current sring stored into primary display.
        """
        str_value = self.primary_display_text.get()

        if str_value == self.Error:
            self.do_clear()

    def disable_if_error(self):
        """
        Disable certain calculator buttons if an error message is present in the display.

        Local Variable:
            btn_texts (list): A list to store text of the buttons that are to be disabled if error message is present in the display.

        Note:
            This method relies on the 'buttons_dict' attribute of the Calculator class to access the buttons.

        """
        btn_texts = ['%', '/', 'x', '-', '+', '+/-', '.', '=']

        # Modify state property of the buttons to disable them.
        for btn_text in btn_texts:
            self.buttons_dict[btn_text].config(state=tk.DISABLED,
                                               bg=self.btn_disabled_bg)

    def do_clear(self, event=None):
        """
        Clear the calculator display and reset internal state.

        This method clears the primary and secondary displays of the calculator,
        resetting them to '0'. Additionally, it resets the internal state of the
        calculator by initializing the 'last_operation' to an empty string, resetting
        the 'accumulator' to 0, and setting the 'flag' to 0.

        Parameters:
            event (optional): An event parameter that can be provided when the method is called as a callback for an event. Defaults to None.

        Notes:
            - This method affects the appearance and behavior of certain calculator
            buttons, such as resetting their state and background color to default values.
            - It relies on the 'buttons_dict', 'last_operation', 'accumulator', 'flag',
            'primary_display_text', and 'secondary_display_text' attributes of the
            Calculator class to perform its operation.

        """
        global last_operation, accumulator, flag
        self.last_operation = ""
        self.accumulator = 0.
        self.flag = 0
        self.primary_display_text.set('0')
        self.secondary_display_text.set('0')
        btn_texts = ['%', '/', 'x', '-', '+', '+/-', '.', '=']

        for btn_text in btn_texts:
            # This conditional check ensures that equal button get its original color when returning to its normal state.
            if btn_text != '=':
                self.buttons_dict[btn_text].config(state=tk.NORMAL,
                                                   bg=self.btn_operator_bg)
            else:
                self.buttons_dict[btn_text].config(state=tk.NORMAL,
                                                   bg=self.btn_equal_bg)

    def do_clear_entry(self, event=None):
        """
        Clear the current entry on the calculator display.
        """
        self.primary_display_text.set('0')

    def do_digit_x(self, event=None):
        """
        Handle digit inputs for the calculator.

        This method handles digit inputs for the calculator, updating the display accordingly.

        Parameters:
            event (tk.Event, optional): The event that triggered the digit input.

        Local Variables:
            str_value (str): The current value displayed on the calculator.

        Returns:
            None
        """
        global flag
        self.flag = 0
        self.clear_if_error()
        str_value = self.primary_display_text.get()

        if event.type == '4':   # If mouse click event is triggerred.
            digit = event.widget.cget('text')
        elif event.type == '2':    # If keyboard event is triggerred.
            digit = event.keysym

        # Set the input to the display.
        if len(str_value) < 16:
            if str_value == "0":
                self.primary_display_text.set(digit)
            else:
                self.primary_display_text.set(str_value + digit)

    def do_dot(self, event=None):
        """
        Handle decimal point input for the calculator.

        This method handles the input of a decimal point for the calculator,
        updating the display accordingly.

        Parameters:
            event (tk.Event, optional): The event that triggered the decimal point input. Defaults to None.

        Local Variables:
            str_value (str): The current value displayed on the calculator.

        Returns:
            None
        """
        global flag
        # flag (int): A variable that ensures that the code inside the operation
        # functions like 'do_plus' works only if there is input in the screen.
        self.flag = 0
        self.clear_if_error()
        str_value = self.primary_display_text.get()

        if len(str_value) < 16 and '.' not in str_value:
            self.primary_display_text.set(str_value + '.')

    def do_digit_0(self, event=None):
        """
        Handle zero digit input for the calculator.

        This method handles the input of zero digit ('0') for the calculator,
        updating the display accordingly.

        Parameters:
            event (tk.Event, optional): The event that triggered the zero digit input. Defaults to None.

        Local Variables:
            str_value (str): The current value displayed on the calculator.

        Returns:
            None
        """
        global flag
        self.flag = 0
        self.clear_if_error()
        str_value = self.primary_display_text.get()

        if len(str_value) < 16 and str_value != '0':
            self.primary_display_text.set(str_value + '0')

    def do_plus(self, event=None):
        """
        Handle addition operation for the calculator.

        This method handles the addition operation for the calculator, updating the display and internal state accordingly.

        Parameters:
            event (tk.Event, optional): The event that triggered the addition operation. Defaults to None.

        Returns:
            None
        """
        global last_operation, accumulator, flag
        self.clear_if_error()

        # Ensures that pressing plus button multiple times has no effect as flag is set
        # to 1 once the plus button is clicked.
        if self.flag == 0:
            if self.last_operation == '':
                self.accumulator = self.string_to_double(
                    self.primary_display_text.get())
                self.last_operation = '+'
                self.primary_display_text.set('0')
                self.secondary_display_text.set(self.double_to_string(
                    self.accumulator) + self.last_operation)
            else:
                self.do_equal(symbol='+')
                self.last_operation = '+'

        # This condition sets last_operation when user shift operations (eg. + to *) without entrying current value.
        if self.flag == 1:
            self.last_operation = '+'
            self.secondary_display_text.set(self.double_to_string(
                self.accumulator) + self.last_operation)

        self.flag = 1

    def do_minus(self, event=None):
        """
        Handle subtraction operation for the calculator.

        This method handles the subtraction operation for the calculator, updating the display and internal state accordingly.

        Parameters:
            event (tk.Event, optional): The event that triggered the subtraction operation. Defaults to None.

        Returns:
            None
        """
        global last_operation, accumulator, flag
        self.clear_if_error()

        # Ensures that pressing minus button multiple times has no effect as flag is set
        # to 1 once the minus button is clicked.
        if self.flag == 0:
            if self.last_operation == '':
                self.accumulator = self.string_to_double(
                    self.primary_display_text.get())
                self.last_operation = '-'
                self.primary_display_text.set('0')
                self.secondary_display_text.set(self.double_to_string(
                    self.accumulator) + self.last_operation)
            else:
                self.do_equal(symbol='-')
                self.last_operation = '-'

        # This condition sets last_operation when user shift operations (eg. - to *) without entrying current value.
        if self.flag == 1:
            self.last_operation = '-'
            self.secondary_display_text.set(self.double_to_string(
                self.accumulator) + self.last_operation)

        self.flag = 1

    def do_multi(self, event=None):
        """
        Handle multiplication operation for the calculator.

        This method handles the multiplication operation for the calculator, updating the display and internal state accordingly.

        Parameters:
            event (tk.Event, optional): The event that triggered the multiplication operation. Defaults to None.

        Returns:
            None
        """
        global last_operation, accumulator, flag
        self.clear_if_error()

        # Ensures that pressing multiply button multiple times has no effect as flag is set
        # to 1 once the multiply button is clicked.
        if self.flag == 0:
            if self.last_operation == '':
                self.accumulator = self.string_to_double(
                    self.primary_display_text.get())
                self.last_operation = '*'
                self.primary_display_text.set('0')
                self.secondary_display_text.set(self.double_to_string(
                    self.accumulator) + self.last_operation)
            else:
                self.do_equal(symbol='*')
                self.last_operation = '*'

        # This condition sets last_operation when user shift operations (eg. * to +) without entrying current value.
        if self.flag == 1:
            self.last_operation = '*'
            self.secondary_display_text.set(self.double_to_string(
                self.accumulator) + self.last_operation)

        self.flag = 1

    def do_divd(self, event=None):
        """
        Handle division operation for the calculator.

        This method handles the division operation for the calculator, updating the display and internal state accordingly.

        Parameters:
            event (tk.Event, optional): The event that triggered the division operation. Defaults to None.

        Returns:
            None
        """
        global last_operation, accumulator, flag
        self.clear_if_error()

        # Ensures that pressing division button multiple times has no effect as flag is set
        # to 1 once the division button is clicked.
        if self.flag == 0:
            if self.last_operation == '':
                self.accumulator = self.string_to_double(
                    self.primary_display_text.get())
                self.last_operation = '/'
                self.primary_display_text.set('0')
                self.secondary_display_text.set(self.double_to_string(
                    self.accumulator) + self.last_operation)
            else:
                self.do_equal(symbol='/')
                self.last_operation = '/'

        # This condition sets last_operation when user shift operations (eg. / to +) without entrying current value.
        if self.flag == 1:
            self.last_operation = '/'
            self.secondary_display_text.set(self.double_to_string(
                self.accumulator) + self.last_operation)

        self.flag = 1

    def do_percent(self, event=None):
        """
        Handle percentage calculation for the calculator.

        This method calculates the percentage of the current value displayed on the calculator. If no previous operation
        has been performed, it calculates the percentage of the current value relative to zero. It then updates the display
        and internal state accordingly.

        Parameters:
            event (tk.Event, optional): The event that triggered the percentage calculation. Defaults to None.

        Returns:
            None
        """
        global last_operation, accumulator, flag
        self.clear_if_error()

        if self.last_operation == '':
            self.accumulator = self.string_to_double(
                self.primary_display_text.get())
            self.do_equal(symbol='%')
            self.last_operation = ''
        else:
            self.do_equal(symbol='%')
            self.last_operation = ''

    def do_equal(self, event=None, symbol='='):
        """
        Handle the equal sign button press to perform arithmetic calculations.

        This method performs arithmetic calculations based on the last operation and the current value displayed
        on the calculator. It updates the secondary display with the operation and operand, performs the calculation,
        updates the primary display with the result, and resets the internal state accordingly.

        Parameters:
            event (tk.Event, optional): The event that triggered the equal sign button press. Defaults to None.
            symbol (str, optional): The symbol representing the operation. Defaults to '='.

        Attributes:
            last_operation (str): Represents the last operation performed.
            accumulator (float): Stores the intermediate result of calculations.
            flag (int): A variable that ensures that the code inside the operation functions works only if there is input on the screen.
            curr_value (float): Represents the current value displayed on the primary display.

        Returns:
            None
        """
        global last_operation, accumulator, flag
        # this ensures that nothing is done if = button is pressed before any operation that +, -, etc.
        if self.last_operation == '' and symbol != '%':
            # this also allow below code to be executed if last_operation is '' but symbol is %.
            return None

        self.curr_value = self.string_to_double(
            self.primary_display_text.get())

        self.flag = 0
        self.clear_if_error()

        # Sets secondary display
        if symbol == '=':
            self.secondary_display_text.set(self.double_to_string(self.accumulator)
                                            + self.last_operation
                                            + self.double_to_string(self.curr_value)
                                            + '=')
        elif self.last_operation == '' and symbol == '%':
            self.secondary_display_text.set(self.double_to_string(self.accumulator)
                                            + symbol)
        elif self.last_operation != '' and symbol == '%':
            self.secondary_display_text.set(self.double_to_string(self.accumulator)
                                            + self.last_operation
                                            + self.double_to_string(self.curr_value)
                                            + symbol
                                            + '=')

        # These code perform calculations based on last_operatin & symbols.
        if self.last_operation == '*' and symbol != '%':
            self.accumulator *= self.curr_value
        elif self.last_operation == "-" and symbol != '%':
            self.accumulator -= self.curr_value
        elif self.last_operation == "+" and symbol != '%':
            self.accumulator += self.curr_value
        elif self.last_operation == "/" and symbol != '%':

            # Handle ZeroDivsionError that may occur during division operation.
            try:
                self.accumulator /= self.curr_value
            except ZeroDivisionError:
                self.primary_display_text.set(self.Error)
                self.disable_if_error()
                return None

        elif self.last_operation == '' and symbol == '%':
            self.accumulator /= 100
        elif self.last_operation == '*' and symbol == '%':
            self.accumulator = self.accumulator * (self.curr_value/100)
        elif self.last_operation == '/' and symbol == '%':

            # Handle ZeroDivsionError that may occur during percentage operation.
            try:
                self.accumulator = self.accumulator / (self.curr_value/100)
            except ZeroDivisionError:
                self.primary_display_text.set(self.Error)
                self.disable_if_error()
                return None

        elif self.last_operation == '+' and symbol == '%':
            self.accumulator += (self.accumulator * (self.curr_value/100))
        elif self.last_operation == '-' and symbol == '%':
            self.accumulator -= (self.accumulator * (self.curr_value/100))

        # Sets primary display.
        if symbol == '=':  # Excecuted when uses presses = button.
            self.primary_display_text.set(
                self.double_to_string(self.accumulator))
            self.last_operation = ''
        elif symbol == '%':  # Set primary display when symbol is %.
            self.primary_display_text.set(
                self.double_to_string(self.accumulator))
        # Executed when user want to calculated series of more than two like 10 + 20 + 30 etc.
        else:
            self.primary_display_text.set('0')
            self.secondary_display_text.set(
                self.double_to_string(self.accumulator)+symbol)

    def do_plusminus(self, event=None):
        """
        Toggle the sign of the number displayed on the calculator.

        This method changes the sign of the number displayed on the calculator's primary display.
        If the number is positive, it becomes negative, and vice versa.

        Parameters:
            event (tk.Event, optional): The event that triggered the plus/minus button press. Defaults to None.

        Returns:
            None
        """
        self.clear_if_error()
        self.primary_display_text.set(
            self.double_to_string(-self.string_to_double(self.primary_display_text.get())))

    def do_backspace(self, event=None):
        """
        Perform backspace operation on the calculator display.

        This method removes the last character from the number displayed on the calculator's primary display.
        If the displayed number has only one digit after backspacing, it sets the display to '0'.

        Parameters:
            event (tk.Event, optional): The event that triggered the backspace operation. Defaults to None.

        Returns:
            None
        """
        self.clear_if_error()
        str_value = self.primary_display_text.get()
        if str_value != '0':
            self.primary_display_text.set(str_value[0:-1])
            if len(str_value) == 1:
                self.primary_display_text.set('0')

    def under_maintenace(self):
        """
        Show a message indicating that the scientific calculator is under maintenance.

        This method displays an informational message box informing the user that the scientific calculator
        functionality is currently under maintenance.

        Parameters:
            None

        Returns:
            None
        """
        messagebox.showinfo('Under Maintenance',
                            'Scientific calculator\nis under maintenance.')

    def about_app(self):
        """
        Display information about the application.

        This method displays information about the developer, including their name, email, and contact number.

        Parameters:
            None

        Returns:
            None
        """
        messagebox.showinfo(
            'About us', 'Developed by Ashish Kumar\nEmail: ashish.bmistry@gmail.com\nContact: +91 8502025686')

    def are_you_sure(self, event=None):
        """
        Prompt the user to confirm quitting the application.

        This method displays a message box asking the user if they are sure they want to quit the application. 
        If the user confirms, the application window is destroyed.

        Parameters:
            event (optional): The event that triggered the quit action.

        Returns:
            None
        """
        reply = messagebox.askyesno(
            title='Quit?', message='Are you sure you want to quit?')
        if reply:
            self.window.destroy()
