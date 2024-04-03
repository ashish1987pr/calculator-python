import tkinter as tk
from tkinter import messagebox
from decimal import Decimal


def string_to_double(s):
    try:
        value = float(s)
        return value
    except ValueError:
        return None


def double_to_string(val):
    s = str(val)
    if '.' in s:
        while s[-1] == '0':
            s = s[0:-1]
    if s[-1] == '.':
        s = s[0:-1]
    if len(s) > 16:
        s = float(s)
        s = "{:e}".format(s)
    return s


def clear_if_error():
    s = display_str_main.get()
    if s == Error:
        do_clear()


def disable_if_error():
    divd.config(state=tk.DISABLED, bg='#f5f5f5')
    multi.config(state=tk.DISABLED, bg='#f5f5f5')
    minus.config(state=tk.DISABLED, bg='#f5f5f5')
    plus.config(state=tk.DISABLED, bg='#f5f5f5')
    percent.config(state=tk.DISABLED, bg='#f5f5f5')
    plusminus.config(state=tk.DISABLED, bg='#f5f5f5')
    dot.config(state=tk.DISABLED, bg='#f5f5f5')
    equal.config(state=tk.DISABLED, bg='#f5f5f5')


def do_clear():
    global last_operation, accumulator, flag
    last_operation = ""
    accumulator = 0.
    flag = 0
    display_str_main.set('0')
    display_str_secondary.set('0')
    divd.config(state=tk.NORMAL, bg=btn_bg_color,
                activebackground=btn_active_color,)
    multi.config(state=tk.NORMAL, bg=btn_bg_color,
                 activebackground=btn_active_color,)
    minus.config(state=tk.NORMAL, bg=btn_bg_color,
                 activebackground=btn_active_color,)
    plus.config(state=tk.NORMAL, bg=btn_bg_color,
                activebackground=btn_active_color,)
    percent.config(state=tk.NORMAL, bg=btn_bg_color,
                   activebackground=btn_active_color,)
    plusminus.config(state=tk.NORMAL, bg=btn_bg_color,
                     activebackground=btn_active_color,)
    dot.config(state=tk.NORMAL, bg=btn_bg_color,
               activebackground=btn_active_color,)
    equal.config(state=tk.NORMAL, bg=btn_bg_color,
                 activebackground=btn_active_color,)


def do_clear_entry():
    display_str_main.set('0')


def do_digit_x(dig):
    global flag
    # flag is variable that ensures that if there is input in the screen then only code inside the operation function like do_plus works, otherwise will not work. this is becuase sometime we may press +, - etc buttons multiple times at the same time.
    flag = 0
    clear_if_error()
    s = display_str_main.get()
    if len(s) < 16:
        if s == "0":
            display_str_main.set(dig)
        else:
            display_str_main.set(s+dig)


def do_dot():
    global flag
    # flag is variable that ensures that if there is input in the screen then only code inside the operation function like do_plus works, otherwise will not work. this is becuase sometime we may press +, - etc buttons multiple times at the same time.
    flag = 0
    clear_if_error()
    s = display_str_main.get()
    if len(s) < 16 and '.' not in s:
        display_str_main.set(s+'.')


def do_digit_0():
    global flag
    # flag is variable that ensures that if there is input in the screen then only code inside the operation function like do_plus works, otherwise will not work. this is becuase sometime we may press +, - etc buttons multiple times at the same time.
    flag = 0
    clear_if_error()
    s = display_str_main.get()

    if len(s) < 16 and s != '0':
        display_str_main.set(s+'0')


def do_plus():
    global last_operation, accumulator, flag
    clear_if_error()
    if flag == 0:  # this ensures that pressing plus button multiple times has no effect as flag is set to 1 below.
        if last_operation == '':
            accumulator = string_to_double(display_str_main.get())
            last_operation = '+'
            display_str_main.set('0')
            display_str_secondary.set(
                double_to_string(accumulator)+last_operation)
        else:
            do_equal('+')
            last_operation = '+'

    # This condition sets last_operation when user changes operation from one to another(eg. + to *) at the same time without entrying current value.
    if flag == 1:
        last_operation = '+'
        display_str_secondary.set(double_to_string(accumulator)+last_operation)

    flag = 1


def do_minus(event=None):
    global last_operation, accumulator, flag
    clear_if_error()
    if flag == 0:  # this ensures that pressing minus button multiple times has no effect as flag is set to 1 below.
        if last_operation == '':
            accumulator = string_to_double(display_str_main.get())
            last_operation = '-'
            display_str_main.set('0')
            display_str_secondary.set(
                double_to_string(accumulator)+last_operation)
        else:
            do_equal('-')
            last_operation = '-'
    if flag == 1:
        last_operation = '-'
        display_str_secondary.set(double_to_string(accumulator)+last_operation)
    flag = 1


def do_multi():
    global last_operation, accumulator, flag
    clear_if_error()
    if flag == 0:  # this ensures that pressing multi button multiple times has no effect as flag is set to 1 below.
        if last_operation == '':
            accumulator = string_to_double(display_str_main.get())
            last_operation = '*'
            display_str_main.set('0')
            display_str_secondary.set(
                double_to_string(accumulator)+last_operation)
        else:
            do_equal('*')
            last_operation = '*'
    if flag == 1:
        last_operation = '*'
        display_str_secondary.set(double_to_string(accumulator)+last_operation)
    flag = 1


def do_divd():
    global last_operation, accumulator, flag
    clear_if_error()
    if flag == 0:
        if last_operation == '':
            accumulator = string_to_double(display_str_main.get())
            last_operation = '/'
            display_str_main.set('0')
            display_str_secondary.set(
                double_to_string(accumulator)+last_operation)
        else:
            do_equal('/')
            last_operation = '/'
    if flag == 1:
        last_operation = '/'
        display_str_secondary.set(double_to_string(accumulator)+last_operation)
    flag = 1


def do_percent():
    global last_operation, accumulator, flag
    clear_if_error()
    if last_operation == '':
        accumulator = string_to_double(display_str_main.get())
        do_equal('%')
        last_operation = ''
    else:
        do_equal('%')
        last_operation = ''


def do_equal(symbol='='):
    global last_operation, accumulator, flag
    # this ensures that nothing is done if = button is pressed before any operation that +, -, etc.
    if last_operation == '' and symbol != '%':
        # this also allow below code to be executed if last_operation is '' but symbol is %.
        return None

    curr_value = string_to_double(display_str_main.get())

    flag = 0
    clear_if_error()

    # these code sets secondary display
    if symbol == '=':
        display_str_secondary.set(double_to_string(
            accumulator)+last_operation+double_to_string(curr_value)+'=')
    elif last_operation == '' and symbol == '%':
        display_str_secondary.set(double_to_string(accumulator)+symbol)
    elif last_operation != '' and symbol == '%':
        display_str_secondary.set(double_to_string(
            accumulator)+last_operation+double_to_string(curr_value)+symbol+'=')

    # thsese code perform calculations
    if last_operation == '*' and symbol != '%':
        accumulator *= curr_value
    elif last_operation == "-" and symbol != '%':
        accumulator -= curr_value
    elif last_operation == "+" and symbol != '%':
        accumulator += curr_value
    elif last_operation == "/" and symbol != '%':
        if curr_value != 0:
            accumulator /= curr_value
        else:
            display_str_main.set(Error)
            disable_if_error()
            return None
    elif last_operation == '' and symbol == '%':
        accumulator /= 100
    elif last_operation == '*' and symbol == '%':
        accumulator = accumulator * (curr_value/100)
    elif last_operation == '/' and symbol == '%':
        accumulator = accumulator / (curr_value/100)
    elif last_operation == '+' and symbol == '%':
        accumulator += (accumulator * (curr_value/100))
    elif last_operation == '-' and symbol == '%':
        accumulator -= (accumulator * (curr_value/100))

    # these code sets main display.
    if symbol == '=':  # this is excecuted when uses presses = button.
        display_str_main.set(double_to_string(accumulator))
        last_operation = ''
    elif symbol == '%':  # this sets main display value when symbol is %.
        display_str_main.set(double_to_string(accumulator))
    # this is executed when user want to calculated series of more than two like 10 + 20 + 30 etc.
    else:
        display_str_main.set('0')
        display_str_secondary.set(double_to_string(accumulator)+symbol)


def do_plusminus():
    clear_if_error()
    display_str_main.set(
        double_to_string(-string_to_double(display_str_main.get())))


def do_backspace():
    clear_if_error()
    s = display_str_main.get()
    if s != '0':
        display_str_main.set(s[0:-1])
        if len(s) == 1:
            display_str_main.set('0')


# Callback definition for main menu option named About.
def about_app():
    messagebox.showinfo('About us', 'Developed by Ashish B. Mistry')


# Callback definition for sub file menu option named Quit.
def are_you_sure(event=None):
    reply = messagebox.askyesno(
        title='Quit?', message='Are you sure you want to quit the app?')
    if reply:
        window.destroy()


window = tk.Tk()
window.title("Calculator")
window.resizable(width=False, height=False)
window.config(padx=10, pady=10, bg='#F0F3FF')

# Adding main menu to the main window.
main_menu = tk.Menu(window)
window.config(menu=main_menu)

# Adding options to the main menu bar with empty sub_menu.
sub_menu_file = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='File', menu=sub_menu_file, underline=0)

sub_menu_file.add_command(label='Regular calculator')
sub_menu_file.add_command(label='Scientific calculator')
sub_menu_file.add_separator()
sub_menu_file.add_command(
    label='Quit', command=are_you_sure, underline=0, accelerator='Ctrl-Q')
window.bind('<Control-Q>', are_you_sure)
window.bind('<Control-q>', are_you_sure)

main_menu.add_command(label='About', command=about_app, underline=0)


display_str_main = tk.StringVar()
display_str_secondary = tk.StringVar()
display_str_main.set("0")
display_str_secondary.set("0")

display_bg_color = '#FFFFFF'
btn_bg_color = "#FCFDFF"
btn_active_color = "#EAEEFC"
borderwidth = 0
btn_pady = (1, 1)
btn_padx = (1, 1)
stick = tk.N + tk.S + tk.E + tk.W

display_secondary = tk.Label(master=window, width=16, font=(
    "Courier New", "16", "bold"), textvariable=display_str_secondary, anchor='e', bg=display_bg_color)
display_secondary.grid(row=0, columnspan=4, sticky=stick)
display_main = tk.Label(master=window, width=16, font=(
    "Courier New", "28", "bold"), textvariable=display_str_main, anchor='e', bg=display_bg_color)
display_main.grid(row=1, columnspan=4, sticky=stick)

company_label = tk.Label(master=window, text='Developed By Ashish B. Mistry\nE-Mail: enquiry@ruchiez.in\nMob: +91 8502025686',
                         font=("Arial", "8", ""), bg='#F0F3FF', anchor='sw', justify=tk.LEFT)
company_label.grid(row=2, column=0, columnspan=3, sticky=stick, pady=(0, 5))
backspace = tk.Button(master=window, text="Back", command=do_backspace, height=2, width=2,
                      bg=btn_bg_color, activebackground=btn_active_color, font=('', '14', ''), borderwidth=0)
backspace.grid(row=2, column=3, sticky=stick, pady=(10, 1), padx=btn_padx)

clear = tk.Button(window, text="C", command=do_clear, height=2, width=2, bg=btn_bg_color,
                  activebackground=btn_active_color, font=('', '14', ''), borderwidth=0)
clear.grid(row=3, column=0, sticky=stick, pady=btn_pady, padx=btn_padx)
clear_entry = tk.Button(window, text="CE", command=do_clear_entry, height=2, width=2,
                        bg=btn_bg_color, activebackground=btn_active_color, font=('', '14', ''), borderwidth=0)
clear_entry.grid(row=3, column=1, sticky=stick, pady=btn_pady, padx=btn_padx)
percent = tk.Button(master=window, text='%', command=do_percent, height=2, bg=btn_bg_color,
                    activebackground=btn_active_color, font=('', '14', ''), borderwidth=0)
percent.grid(row=3, column=2, sticky=stick, pady=btn_pady, padx=btn_padx)
divd = tk.Button(master=window, text="/", command=do_divd, height=2, bg=btn_bg_color,
                 activebackground=btn_active_color, font=('', '14', ''), borderwidth=0)
divd.grid(row=3, column=3, sticky=stick, pady=btn_pady, padx=btn_padx)

digit7 = tk.Button(master=window, text='7', command=lambda: do_digit_x("7"), height=2, width=2, bg=btn_bg_color, activebackground=btn_active_color, font=(
    '', '14', 'bold'), borderwidth=0)  # By this ways of using lambda, we can send arguments to the callback function.
digit7.grid(row=4, column=0, sticky=stick, pady=btn_pady, padx=btn_padx)
digit8 = tk.Button(master=window, text='8', command=lambda: do_digit_x("8"), height=2,
                   bg=btn_bg_color, activebackground=btn_active_color, font=('', '14', 'bold'), borderwidth=0)
digit8.grid(row=4, column=1, sticky=stick, pady=btn_pady, padx=btn_padx)
digit9 = tk.Button(master=window, text='9', command=lambda: do_digit_x("9"), height=2,
                   bg=btn_bg_color, activebackground=btn_active_color, font=('', '14', 'bold'), borderwidth=0)
digit9.grid(row=4, column=2, sticky=stick, pady=btn_pady, padx=btn_padx)
multi = tk.Button(master=window, text="x", command=do_multi, height=2, bg=btn_bg_color,
                  activebackground=btn_active_color, font=('', '14', ''), borderwidth=0)
multi.grid(row=4, column=3, sticky=stick, pady=btn_pady, padx=btn_padx)

digit4 = tk.Button(master=window, text='4', command=lambda: do_digit_x("4"), height=2, width=2, bg=btn_bg_color, activebackground=btn_active_color, font=(
    '', '14', 'bold'), borderwidth=0)  # By this ways of using lambda, we can send arguments to the callback function.
digit4.grid(row=5, column=0, sticky=stick, pady=btn_pady, padx=btn_padx)
digit5 = tk.Button(master=window, text='5', command=lambda: do_digit_x("5"), height=2,
                   bg=btn_bg_color, activebackground=btn_active_color, font=('', '14', 'bold'), borderwidth=0)
digit5.grid(row=5, column=1, sticky=stick, pady=btn_pady, padx=btn_padx)
digit6 = tk.Button(master=window, text='6', command=lambda: do_digit_x("6"), height=2,
                   bg=btn_bg_color, activebackground=btn_active_color, font=('', '14', 'bold'), borderwidth=0)
digit6.grid(row=5, column=2, sticky=stick, pady=btn_pady, padx=btn_padx)
minus = tk.Button(master=window, text="-", command=do_minus, height=2, bg=btn_bg_color,
                  activebackground=btn_active_color, font=('', '14', ''), borderwidth=0)
minus.grid(row=5, column=3, sticky=stick, pady=btn_pady, padx=btn_padx)

digit1 = tk.Button(master=window, text='1', command=lambda: do_digit_x("1"), height=2, width=2, bg=btn_bg_color, activebackground=btn_active_color, font=(
    '', '14', 'bold'), borderwidth=0)  # By this ways of using lambda, we can send arguments to the callback function.
digit1.grid(row=6, column=0, sticky=stick, pady=btn_pady, padx=btn_padx)
digit2 = tk.Button(master=window, text='2', command=lambda: do_digit_x("2"), height=2,
                   bg=btn_bg_color, activebackground=btn_active_color, font=('', '14', 'bold'), borderwidth=0)
digit2.grid(row=6, column=1, sticky=stick, pady=btn_pady, padx=btn_padx)
digit3 = tk.Button(master=window, text='3', command=lambda: do_digit_x("3"), height=2,
                   bg=btn_bg_color, activebackground=btn_active_color, font=('', '14', 'bold'), borderwidth=0)
digit3.grid(row=6, column=2, sticky=stick, pady=btn_pady, padx=btn_padx)
plus = tk.Button(master=window, text="+", command=do_plus, height=2, bg=btn_bg_color,
                 activebackground=btn_active_color, font=('', '14', ''), borderwidth=0)
plus.grid(row=6, column=3, sticky=stick, pady=btn_pady, padx=btn_padx)

digit0 = tk.Button(master=window, text='0', command=do_digit_0, height=2, width=2,
                   bg=btn_bg_color, activebackground=btn_active_color, font=('', '14', 'bold'), borderwidth=0)
digit0.grid(row=7, column=1, sticky=stick, pady=btn_pady, padx=btn_padx)
dot = tk.Button(master=window, text=" . ", command=do_dot, height=2, bg=btn_bg_color,
                activebackground=btn_active_color, font=('', '14', 'bold'), borderwidth=0)
dot.grid(row=7, column=2, sticky=stick, pady=btn_pady, padx=btn_padx)
plusminus = tk.Button(master=window, text='+/-', command=do_plusminus, height=2,
                      bg=btn_bg_color, activebackground=btn_active_color, font=('', '14', ''), borderwidth=0)
plusminus.grid(row=7, column=0, sticky=stick, pady=btn_pady, padx=btn_padx)
equal = tk.Button(master=window, text="=", command=do_equal, height=2, bg=btn_bg_color,
                  activebackground=btn_active_color, font=('', '14', ''), borderwidth=0)
equal.grid(row=7, column=3, sticky=stick, pady=btn_pady, padx=btn_padx)

last_operation = ""
accumulator = 0.
flag = 0
Error = "Div. by 0 Error!"
window.mainloop()
