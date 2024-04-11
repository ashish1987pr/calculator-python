"""
calc_operations.py - Module containing the CalcOperations class for basic
calculator operations.

This module provides the CalcOperations class, which implements methods for
performing basic calculator operations such as addition, subtraction,
multiplication, division, percentage calculations, and more.

The CalcOperations class handle internal logic of the calculator, including
parsing user input, performing calculations, handling errors, and updating
the calculator's display.

Classes:
    - CalcOperations: A class containing methods for basic calculator
      operations.

Functions:
    - None

Constants:
    - None

Modules Required:
    - tkinter: For creating the GUI components of the calculator.
    - decimal: This module provides functionality for precise arithmetic
      operations using the Decimal data type from the decimal module.

Author: Ashish Kumar
Contact: ashish.bmistry@gmail.com
"""

# Importing required modules
import tkinter as tk
from decimal import Decimal


class CalcOperations:
    """
    A class to perform basic & scientific calculator operations.

    This class provides methods for various arithmetic operations such as
    addition, subtraction, multiplication, and division. It also include
    methods for handling user input and error conditions. In future
    development, it will also have methods for scientific calculation
    operations.

    Attribute:
        pri_display_text (tk.StringVar): String var for primary display.
        sec_display_text (tk.StringVar): String var for secondary display.
        pri_display_width (int): Width of primary display.
        sec_display_width (int): Width of secondary display.
        btn_disabled_bg (str): Background color of disabled buttons.
        btn_operator_bg (str): Background color of operator buttons.
        btn_equal_bg (str): Background color of equal button.
        btn_equal_fg (str): Foreground color of equal button.
        buttons_dict (dict): A dictionary to store button objects with their
            respective text as keys.
        btn_key_events (dict): A dictionary representing button's text and
            their respective keyboard event name.
        btn_callbacks (dict): A dictionary representing button's text and
            reference to their respective callback.
        disabled_btn_texts (list): A list of text of buttons which are to be
            disabled when error message is present in the display.
        btn_state (str: tk.DISABLED | tk.NORMAL = tk.NORMAL): Represents
            certain button widgets state which changes when error message is
            present in the display.
        last_operation (str): String to store the last operation performed.
        accumulator (float): Accumulator to store temporary results.
        switch (boolean): A switch variable to track the state of operator
            buttons. By default, the switch is set to False. When a user
            presses an operator button (e.g., +, -, *, /), the switch
            transitions to True. Once in the True state, subsequent presses
            of operator buttons merely switch the operator sign without
            executing additional code associated with the operation (e.g., the
            do_plus method). This design ensures seamless handling of
            consecutive operator inputs while maintaining the expected
            functionality of the calculator. Defaults to False.
        last_oper_eq_state (boolean): A boolean variable to track whether the
            last operation performed was the equals (=) operation. This is
            used to control the behavior of the calculator after the equals
            operation, ensuring that subsequent numerical inputs after
            pressing equals don't append to the previous result. Defaults to
            False.
        curr_value (float): Represent the current value displayed on the
            primary display.

    Constants:
        ERROR (str): Error message for division by zero.

    Methods:
        __init__(self):
            Initialize the CalcOperations class.
        str_to_float(self, str_value):
            Convert a string representation of a number to a float.
        float_to_str(self, num_value):
            Convert a float to a string representation with appropriate
            formatting.
        clear_if_error(self):
            Reset the calculator state if an error message is present in the
            dipslay.
        clear_if_last_oper_equal(self):
            Reset the calculator state if the last operation performed was the
            equals (=) operation and subsequent numerical key pressed.
        disable_if_error(self):
            Disable operator buttons if an error message is currently being
            shown.
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
        do_operation(self, curr_operation):
            Handle addition, subtraction, multiplication and division
            operation for the calculator.
        do_plus(self, event=None):
            Handle addition operation.
        do_minus(self, event=None):
            Handle subtraction operation.
        do_multi(self, event=None):
            Handle multiplication operation.
        do_divd(self, event=None):
            Handle division operation.
        do_percent(self, event=None):
            Handle the percentage operation.
        do_equal(self, event=None, curr_operation='='):
            Handle calculation operations based on the last_operation and
            curr_operation.
        do_plusminus(self, event=None):
            Toggle the sign of the current number.
        do_backspace(self, event=None):
            Remove the last character from the calculator display.
        """

    def __init__(self):
        """
        Initialize the CalcOperations class.

        Returns:
            None
        """
        self.pri_display_text = tk.StringVar()
        self.pri_display_text.set('0')
        self.sec_display_text = tk.StringVar()
        self.sec_display_text.set('0')
        self.pri_display_width = 16
        self.sec_display_width = 34
        self.btn_disabled_bg = '#F1F1F1'
        self.btn_operator_bg = '#F3FAFE'
        self.btn_equal_bg = '#7DB8FF'
        self.btn_equal_fg = '#FFFFFF'
        # Empty dictionary to store buttons object.
        self.buttons_dict = {}
        # A dictionary containing all button's text and their respective
        # keyboard event name. Order of items in the dictionary decides the
        # way buttons are placed inside the window.
        self.btn_key_events = {'Back': '<BackSpace>',
                               'C': '<Escape>',
                               'CE': '<Delete>',
                               '%': '<KeyPress-percent>',
                               '/': '<KeyPress-/>',
                               '7': '<KeyPress-7>',
                               '8': '<KeyPress-8>',
                               '9': '<KeyPress-9>',
                               'x': '<KeyPress-asterisk>',
                               '4': '<KeyPress-4>',
                               '5': '<KeyPress-5>',
                               '6': '<KeyPress-6>',
                               '-': '<KeyPress-minus>',
                               '1': '<KeyPress-1>',
                               '2': '<KeyPress-2>',
                               '3': '<KeyPress-3>',
                               '+': '<KeyPress-plus>',
                               '+/-': '<F9>',
                               '0': '<KeyPress-0>',
                               '.': '<KeyPress-period>',
                               '=': '<KeyPress-equal>'}
        # A dictionary containing all button's text and reference to their
        # respective callback. Order of items in the dictionary decides the
        # way buttons are bound to the callbacks.
        self.btn_callbacks = {'Back': self.do_backspace,
                              'C': self.do_clear,
                              'CE': self.do_clear_entry,
                              '%': self.do_percent,
                              '/': self.do_divd,
                              '7': self.do_digit_x,
                              '8': self.do_digit_x,
                              '9': self.do_digit_x,
                              'x': self.do_multi,
                              '4': self.do_digit_x,
                              '5': self.do_digit_x,
                              '6': self.do_digit_x,
                              '-': self.do_minus,
                              '1': self.do_digit_x,
                              '2': self.do_digit_x,
                              '3': self.do_digit_x,
                              '+': self.do_plus,
                              '+/-': self.do_plusminus,
                              '0': self.do_digit_0,
                              '.': self.do_dot,
                              '=': self.do_equal}
        # A list containing text of buttons that are to be disabled when error
        # message is present in the display.
        self.disabled_btn_texts = ['%', '/', 'x', '-', '+', '+/-', '.', '=']
        self.btn_state = tk.NORMAL

        self.last_operation = ''
        self.accumulator = 0.
        self.switch = False
        self.last_oper_eq_state = False
        self.curr_value = 0.0

        self.ERROR = 'Div. by 0 Error!'

    def str_to_float(self, str_value):
        """
        Convert a string to a floating-point number.

        Args:
            str_value (str): The string value to convert.

        Local Variable:
            num_value (float): Stores the converted float value.

        Raises:
            ValueError: If the input parameters are not valid.

        Returns:
            float or None: The converted floating-point number if successful,
            None otherwise.
        """
        try:
            num_value = Decimal(str_value)

            return num_value
        except ValueError:
            return None

    def float_to_str(self, num_value):
        """
        Convert a floating-point number to a string.

        Depending on length of the num_value and presence of '.', it convert
        the floating-point number to a string. Depending on the context, It
        also converts the floating-point number to a string representing
        scientific notation.

        Args:
            num_value (float): The number to convert.

        Local Variable:
            str_value (str): The converted string value.
            sci_notation_len (int): The desired length of the scientific
                notation string representation. The resulting string length
                may vary depending on whether the number is negative or
                positive, as the representation includes a sign for negative
                numbers.
            int_part (str): String representing integer part of the str_value
                when lenght of the str_value is greater than primary display
                width and '.' is present.
            n_digits (int): Remaining number of digits after duducting (lenght
                of int_part + 1 for dot) from primary display width.

        Returns:
            str: The converted string representation of the number.
        """
        str_value = str(num_value)

        # Sometimes, in the % operations, when digits after decimal point
        # are more than 6 in the accumulator, python converts it to the
        # scientific notation (like 0.00000008 becomes 8E-8), but since we
        # want to convert only when length of the whole value becomes more
        # than primary display width, so we check the presence of 'E' in the
        # num_value and format it to the regular decimal number. After
        # converting it back to the regular decimal number, if length of the
        # value becomes greater than the primary display size, futher
        # operations are performed below.
        if 'E' in str(num_value):
            str_value = f'{num_value:f}'

        # Remove all trailing zero when '.' is present in the string str_value.
        if '.' in str_value:
            while str_value[-1] == '0':
                str_value = str_value[0:-1]

        # Remove '.' from the string str_value when it is not followed by any
        # digit.
        if str_value[-1] == '.':
            str_value = str_value[0:-1]

        # If length of str_value is greater than primary display width.
        if len(str_value) > self.pri_display_width:
            sci_notation_len = 9 if '-' in str_value else 10

            # If '.' is present in the str_value, split the str_value into
            # integer and decimal part.
            if '.' in str_value:
                # Split the string into two part and storing integer part
                # into int_part variable.
                int_part = str_value.split('.')[0]
                str_value = Decimal(str_value)

                # If integer part is equal to the zero then convert the
                # str_value to the scientific notation.
                if int_part == '0':
                    str_value = f"{str_value:.{sci_notation_len}E}"
                # If lenght of integer part is greater than primary display
                # width, convert the str_value into scientific notation.
                elif len(int_part) > self.pri_display_width:
                    str_value = f"{str_value:.{sci_notation_len}E}"
                else:
                    # If length of integer parts is less than or equal to
                    # primary display width, round off the str_value upto
                    # n_digits.
                    # Subtract 1 for the dicimal point in n_digits expresssion.
                    n_digits = self.pri_display_width - len(int_part) - 1
                    str_value = f"{str_value:.{max(0, n_digits)}f}"

                    # If rounded off str_value become longer than primary
                    # display width (eg. 9999999999999999.8 becomes
                    # 10000000000000000), which may not fit into primary
                    # display, so convert it into scientific notation.
                    if len(str_value) > self.pri_display_width:
                        str_value = f"{Decimal(str_value):.{sci_notation_len}E}"
            else:
                str_value = Decimal(str_value)
                # When lenght of str_value is greater than primary display
                # width and '.' is not present into str_value then directly
                # convert it into scientific notation.
                str_value = f"{str_value:.{sci_notation_len}E}"

        return str_value

    def clear_if_error(self):
        """
        Clear the display if an error message is present in the display.

        Local Variable:
           str_value (str): The current string stored into primary display.

        Returns:
            None
        """
        str_value = self.pri_display_text.get()

        if str_value == self.ERROR:
            self.do_clear()
            return True

    def clear_if_last_oper_equal(self):
        """
        Reset the calculator state if the last operation performed was the
        equals (=) operation and subsequent numerical key is pressed.

        This method checks if the last operation performed was the equals
        operation (=) (Note: last_operation is always equal when = button is
        pressed or % operation is performed). It is used to control the
        behavior of the calculator after the equals operation, ensuring that
        subsequent numerical inputs after pressing equals don't append to the
        previous result.

        Returns:
            None
        """
        if self.last_operation == '' and self.last_oper_eq_state is True:
            self.do_clear()
            self.last_oper_eq_state = False
            return True

    def disable_if_error(self):
        """
        Disable certain calculator buttons(operator buttons) if an error
        message is present in the display.

        Local Variable:
            btn_texts(str): A string representing button text from
                disabled_btn_texts list.

        Note:
            This method relies on the 'buttons_dict' attribute of the
            CalcOperations class to access the buttons.

        Returns:
            None
        """
        # Set certain buttons state to DISABLED and unbind the callback
        # assigned for mouse and keyboard event for DISABLED button.
        for btn_text in self.disabled_btn_texts:
            self.buttons_dict[btn_text].config(state=tk.DISABLED,
                                               bg=self.btn_disabled_bg)
            self.buttons_dict[btn_text].unbind('<Button-1>')
            self.window.unbind(self.btn_key_events[btn_text])

        # Unbind the callback (self.do_equal()) assigned for Enter key.
        self.window.unbind('<Return>')

        # btn_state changes when certain buttons are set to disabled due to
        # error message present in the display.
        self.btn_state = tk.DISABLED

    def do_clear(self, event=None):
        """
        Clear the calculator display and reset internal state.

        This method clears primary and secondary displays of the calculator,
        resetting them to '0'. Additionally, it resets the internal state of
        the calculator by initializing the 'last_operation' to an empty string,
        resetting the 'accumulator' to 0, and setting the 'switch' and
        'last_oper_eq_state' to False.

        Args:
            event(tk.Event, optional): An event parameter that can be provided
                when the method is called as a callback for a clear display
                event. Defaults to None.

       Local Variable:
            btn_texts (str): A string representing button text from
                disabled_btn_texts list.

        Notes:
            - This method affects the appearance and behavior of certain
              calculator buttons, such as resetting their state and background
              color to default values.
            - It relies on the 'buttons_dict', 'last_operation', 'accumulator',
              'switch', 'pri_display_text', and 'sec_display_text' attributes
              of the CalcOperations class to perform its operation.

        Returns:
            None
        """
        self.last_operation = ""
        self.accumulator = 0.
        self.switch = False
        self.last_oper_eq_state = False
        self.pri_display_text.set('0')
        self.sec_display_text.set('0')

        if self.btn_state == tk.DISABLED:
            for btn_text in self.disabled_btn_texts:
                # Below conditional check ensures that equal button get its
                # original color when returning to its normal state.
                if btn_text != '=':
                    self.buttons_dict[btn_text].config(state=tk.NORMAL,
                                                       bg=self.btn_operator_bg)
                else:
                    self.buttons_dict[btn_text].config(state=tk.NORMAL,
                                                       bg=self.btn_equal_bg)

                # Bind callback to mouse left click event.
                self.buttons_dict[btn_text].bind('<Button-1>',
                                                 self.btn_callbacks[btn_text])

                # Bind callback to keyboard event.
                self.window.bind(self.btn_key_events[btn_text],
                                 self.btn_callbacks[btn_text])

            # Bind callback for Enter key additionally which is already
            # assigned for <KeyPress-equal> event.
            self.window.bind('<Return>', self.do_equal)

            # Set btn_state to tk.NORMAL once disabled buttons' state are set
            # to tk.NORMAL.
            self.btn_state = tk.NORMAL

    def do_clear_entry(self, event=None):
        """
        Clear the current entry on the calculator display.

        It clears the current entry on the display if no error message is
        present in the dipslay otherwise reset the calculator's internal state
        to initial state.

        Note: It also reset the calculator state if error is present in the
        primary display or the last_operation is = (equal) (last_operation is
        always equal when =  button is pressed or % operation is performed).

        Args:
            event (tk.Event, optional): An event parameter that can be provided
                when the method is called as a callback for a clear entry
                event. Defaults to None.

        Returns:
            None
        """
        # If here is an error in the display or last performed operation was
        # equal (=), reset the caculator's state and do nothing.
        if self.clear_if_error() or self.clear_if_last_oper_equal():
            return None

        self.pri_display_text.set('0')

    def do_digit_x(self, event=None):
        """
        Handle digit inputs for the calculator.

        This method handles digit inputs for the calculator, updating the
        display accordingly.

        Args:
            event (tk.Event, optional): An event parameter that can be provided
                when the method is called as a callback for digit input event.
                Defaults to None.

        Local Variables:
            str_value (str): The current value displayed on the calculator.
            digit (str): The pressed (by mouse or keyboard) numerical buttons'
                text (0 to 9).

        Returns:
            None
        """
        self.switch = False

        self.clear_if_error()
        self.clear_if_last_oper_equal()

        str_value = self.pri_display_text.get()

        if event.type == '4':   # If mouse click event is triggerred.
            digit = event.widget.cget('text')
        elif event.type == '2':    # If keyboard event is triggerred.
            digit = event.keysym

        # Set the input value to the display.
        if len(str_value) < self.pri_display_width:
            if str_value == "0":
                self.pri_display_text.set(digit)
            else:
                self.pri_display_text.set(str_value + digit)

    def do_dot(self, event=None):
        """
        Handle decimal point input for the calculator.

        This method handles the input of a decimal point for the calculator,
        updating the display accordingly.

        Args:
            event (tk.Event, optional): An event parameter that can be provided
                when the method is called as a callback for dot event. Defaults
                to None.

        Local Variables:
            str_value (str): The current value displayed on the calculator.

        Returns:
            None
        """
        # switch (boolean): A variable that ensures that code inside the
        # operation functions like 'do_plus' works only if there is input in
        # the screen.
        self.switch = False

        self.clear_if_error()
        self.clear_if_last_oper_equal()

        str_value = self.pri_display_text.get()

        if len(str_value) < self.pri_display_width and '.' not in str_value:
            self.pri_display_text.set(str_value + '.')

    def do_digit_0(self, event=None):
        """
        Handle zero digit input for the calculator.

        This method handles the input of zero digit ('0') for the calculator,
        updating the display accordingly.

        Args:
            event (tk.Event, optional): An event parameter that can be provided
                when the method is called as a callback for an zero digit input
                event. Defaults to None.

        Local Variables:
            str_value (str): The current value displayed on the calculator.

        Returns:
            None
        """
        self.switch = False

        self.clear_if_error()
        self.clear_if_last_oper_equal()

        str_value = self.pri_display_text.get()

        if len(str_value) < self.pri_display_width and str_value != '0':
            self.pri_display_text.set(str_value + '0')

    def do_operation(self, curr_operation):
        """
        Handle addition, subtraction, multiplication and division operation
        for the calculator.

        This method handles the addition, subtraction, multiplication and
        division operation for the calculator, updating the display and
        internal state accordingly.

        Args:
            curr_operation (str): A string representing current operation.

        Returns:
            None
        """
        # If here is an error in the display, reset the calculator state and do
        # nothing.
        if self.clear_if_error():
            return None

        # Ensures that pressing + or - or x or / button subsequently has no
        # effect as switch is set to True once any of the above mentioned
        # button is clicked. It only helps to replace current operation to be
        # performed.
        if self.switch is False:
            if self.last_operation == '':
                self.accumulator = self.str_to_float(
                    self.pri_display_text.get())
                # Current operation becomes the last operation for any
                # subsequent operation.
                self.last_operation = curr_operation
                self.pri_display_text.set('0')
                self.sec_display_text.set(self.float_to_str(
                    self.accumulator) + self.last_operation)
            else:
                self.do_equal(curr_operation=curr_operation)
                # Current operation becomes the last operation for any
                # subsequent operation.
                self.last_operation = curr_operation

        # This condition sets last_operation when user switch operations
        # (eg. from + to *, etc) without any current value as input.
        if self.switch is True:
            self.last_operation = curr_operation
            self.sec_display_text.set(self.float_to_str(
                self.accumulator) + self.last_operation)

        self.switch = True

    def do_plus(self, event=None):
        """
        Handle addition operation for the calculator.

        Args:
            event (tk.Event, optional): An event parameter that can be provided
                when the method is called as a callback for an addition event.
                Defaults to None.

        Returns:
            None
        """
        self.do_operation(curr_operation='+')

    def do_minus(self, event=None):
        """
        Handle subtraction operation for the calculator.

        Args:
            event (tk.Event, optional): An event parameter that can be provided
                when the method is called as a callback for substraction event.
                Defaults to None.

        Returns:
            None
        """
        self.do_operation(curr_operation='-')

    def do_multi(self, event=None):
        """
        Handle multiplication operation for the calculator.

        Args:
            event (tk.Event, optional): An event parameter that can be provided
                when the method is called as a callback for multiplication
                event. Defaults to None.

        Returns:
            None
        """
        self.do_operation(curr_operation='*')

    def do_divd(self, event=None):
        """
        Handle division operation for the calculator.

        Args:
            event (tk.Event, optional): An event parameter that can be provided
                when the method is called as a callback for division event.
                Defaults to None.

        Returns:
            None
        """
        self.do_operation(curr_operation='/')

    def do_percent(self, event=None):
        """
        Handle percentage calculation for the calculator.

        This method calculates the percentage of the current value displayed
        on the calculator. If no previous operation has been performed, it
        calculates the percentage of the current value relative to zero. It
        then updates the display and internal state accordingly.

        Args:
            event (tk.Event, optional): An event parameter that can be provided
                when the method is called as a callback for percentage event.
                Defaults to None.

        Returns:
            None
        """
        # If here is an error in the display, reset the calculator state and do
        # nothing.
        if self.clear_if_error():
            return None

        if self.last_operation == '':
            self.accumulator = self.str_to_float(
                self.pri_display_text.get())

        self.do_equal(curr_operation='%')
        self.last_operation = ''

    def do_equal(self, event=None, curr_operation='='):
        """
        Handle the equal sign button press to perform arithmetic calculations.

        This method performs arithmetic calculations based on the last
        operation and the current value displayed on the calculator. It
        updates the secondary display with the operation and operand, performs
        the calculation, updates the primary display with the result, and
        resets the internal state accordingly.

        Args:
            event (tk.Event, optional): An event parameter that can be provided
                when the method is called as a callback for equal event.
                Defaults to None.
            curr_operation (str, optional): A string representing the
                curr_operation. Defaults to '='.

        Raises:
            ZeroDivisionError: If division by zero occur during division and
                percentage operation.

        Returns:
            None
        """
        # If here is an error in the display, reset the calculator state and do
        # nothing.
        if self.clear_if_error():
            return None

        # If last_operaton is set to '' and curr_operation is not set to '%',
        # then do nothing. It also works when there is an error in the display
        # which is reset by clear_if_error() as the same has been called above.
        if self.last_operation == '' and curr_operation != '%':
            return None

        self.curr_value = self.str_to_float(
            self.pri_display_text.get())

        self.switch = False

        # Set secondary display for three different conditions i.e. 5+8=, 5%,
        # and 100*5% or 100/5% or 100-5% or 100+5%.

        # Set the last_oper_eq_state to True if the last operation performed
        # was the equals operation(=) (last_operation is always equal when =
        # button is pressed or % operation is performed). It is used to
        # control the behavior of the calculator after the equals operation,
        # ensuring that subsequent numerical inputs after pressing equals don't
        # append to the previous result.
        if curr_operation == '=':
            self.sec_display_text.set(self.float_to_str(self.accumulator)
                                      + self.last_operation
                                      + self.float_to_str(self.curr_value)
                                      + '=')
            self.last_oper_eq_state = True
        elif self.last_operation == '' and curr_operation == '%':
            self.sec_display_text.set(self.float_to_str(self.accumulator)
                                      + curr_operation)
            self.last_oper_eq_state = True
        elif self.last_operation != '' and curr_operation == '%':
            self.sec_display_text.set(self.float_to_str(self.accumulator)
                                      + self.last_operation
                                      + self.float_to_str(self.curr_value)
                                      + curr_operation
                                      + '=')
            self.last_oper_eq_state = True

        # Below code perform calculation based on last_operation &
        # curr_operation.
        if self.last_operation == '*' and curr_operation != '%':
            self.accumulator *= self.curr_value
        elif self.last_operation == "-" and curr_operation != '%':
            self.accumulator -= self.curr_value
        elif self.last_operation == "+" and curr_operation != '%':
            self.accumulator += self.curr_value
        elif self.last_operation == "/" and curr_operation != '%':

            # Handle ZeroDivsionError that may occur during division operation.
            try:
                self.accumulator /= self.curr_value
            except ZeroDivisionError:
                self.pri_display_text.set(self.ERROR)
                # Set secondary display in case of ZeroDivisionError occurred
                # during series of operations like (5+8)/0+.
                if curr_operation != '=':
                    self.sec_display_text.set(self.float_to_str(self.accumulator)
                                              + self.last_operation
                                              + self.float_to_str(self.curr_value)
                                              + '=')
                self.disable_if_error()
                return None

        elif self.last_operation == '' and curr_operation == '%':
            self.accumulator /= 100
        elif self.last_operation == '*' and curr_operation == '%':
            self.accumulator = self.accumulator * (self.curr_value/100)
        elif self.last_operation == '/' and curr_operation == '%':

            # Handle ZeroDivsionError that may occur during percentage
            # operation.
            try:
                self.accumulator = self.accumulator / self.curr_value * 100
            except ZeroDivisionError:
                self.pri_display_text.set(self.ERROR)
                self.disable_if_error()
                return None

        elif self.last_operation == '+' and curr_operation == '%':
            self.accumulator += (self.accumulator * (self.curr_value/100))
        elif self.last_operation == '-' and curr_operation == '%':
            self.accumulator -= (self.accumulator * (self.curr_value/100))

        # Set primary display.
        # Excecuted when user presses equal (=) button.
        if curr_operation == '=':
            self.pri_display_text.set(
                self.float_to_str(self.accumulator))
            self.last_operation = ''
        # Set primary display when curr_operation is %.
        elif curr_operation == '%':
            self.pri_display_text.set(
                self.float_to_str(self.accumulator))
        else:
            # Executed when user want to calculated series of operations such
            # as 10 + 20 + 30 - 23 * 4 etc.
            self.pri_display_text.set('0')
            self.sec_display_text.set(
                self.float_to_str(self.accumulator)+curr_operation)

    def do_plusminus(self, event=None):
        """
        Toggle the sign of the number displayed on the calculator.

        It changes the sign of the number displayed on the calculator's
        primary display. If the number is positive, it becomes negative, and
        vice versa.

        Args:
            event (tk.Event, optional): An event parameter that can be provided
                when the method is called as a callback for plusminus (+/-)
                event. Defaults to None.

        Returns:
            None
        """
        # If here is an error in the display we need to clear the error and do
        # nothing.
        if self.clear_if_error():
            return None

        self.pri_display_text.set(
            self.float_to_str(-self.str_to_float(self.pri_display_text.get())))

    def do_backspace(self, event=None):
        """
        Perform backspace operation on the calculator display.

        This method removes the last character from the number displayed on
        the calculator's primary display. If the displayed number has only one
        digit after backspacing, it sets the display to '0'.

        Note: It also reset the calculator state if error is present in the
        primary display or the last_operation is = (equal) (last_operation is
        always equal when =  button is pressed or % operation is performed).

        Args:
            event (tk.Event, optional): An event parameter that can be provided
                when the method is called as a callback for backspace event.
                Defaults to None.

        Local Variable:
            str_value (str): A string variable to store primary display value.

        Returns:
            None
        """
        # If here is an error in the display or last performed operation was
        # equal (=), reset the caculator's state and do nothing.
        if self.clear_if_error() or self.clear_if_last_oper_equal():
            return None

        self.clear_if_last_oper_equal()

        str_value = self.pri_display_text.get()

        if str_value != '0':
            self.pri_display_text.set(str_value[0:-1])
            if len(str_value) == 1:
                self.pri_display_text.set('0')
