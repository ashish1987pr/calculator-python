import tkinter as tk

ERROR = "Error!"

def string_to_double(s):
    try:
        val = float(s);
        return val;
    except ValueError:
        return None

def clear_if_error():
    s = display_str.get()
    if s == ERROR:
        display_str.set("0")

def double_to_string(v):
    s = str(v)
    if 'e' in s:
        return ERROR
    
    if '.' in s:
        while s[-1] == '0':
            s = s[0:-1]
            
    while len(s) > 10 and s[-1] != '.':
        s = s[0:-1]
        
    if s[-1] == '.':
        s = s[0:-1]
        
    if len(s) > 10:
        return ERROR
    return s

def do_clear():
    global accumulator, last_operation
    display_str.set("0")
    accumulator = 0.
    last_operation = ""


def do_digit_0():
    clear_if_error()
    s = display_str.get()
    if len(s) < 10 and s != "0":
        display_str.set(s + '0')


def do_digit_x(dig):
    clear_if_error()
    s = display_str.get()
    if len(s) < 10:
        if s == "0":
            display_str.set(dig)
        else:
            display_str.set(s + dig)


def do_dot():
    clear_if_error()
    s = display_str.get()
    if len(s) < 10 and "." not in s:
        display_str.set(s + ".")


def do_plus():
    global last_operation, accumulator
    clear_if_error()
    last_operation = "+"
    accumulator = string_to_double(display_str.get())
    display_str.set("0")


def do_minus():
    global last_operation, accumulator
    clear_if_error()
    last_operation = "-"
    accumulator = string_to_double(display_str.get())
    display_str.set("0")


def do_mult():
    global last_operation, accumulator
    clear_if_error()
    last_operation = "*"
    accumulator = string_to_double(display_str.get())
    display_str.set("0")


def do_divd():
    global last_operation, accumulator
    clear_if_error()
    last_operation = "/"
    accumulator = string_to_double(display_str.get())
    display_str.set("0")


def do_equal():
    global last_operation, accumulator
    clear_if_error()
    value = string_to_double(display_str.get())
    if last_operation == "+":
        accumulator += value
    elif last_operation == "-":
        accumulator -= value
    elif last_operation == "*":
        accumulator *= value
    elif last_operation == "/":
        if value != 0:
            accumulator /= value
        else:
            display_str.set(ERROR);
            return;
    display_str.set(double_to_string(accumulator))


def do_plusminus():
    clear_if_error()
    display_str.set(double_to_string(-string_to_double(display_str.get())))


window = tk.Tk()
window.title('Calc')
display_str = tk.StringVar()
display_str.set("0")
stick = tk.N + tk.S + tk.E + tk.W

display = tk.Entry(window, width=10, font=("Courier New", "15", "bold"), textvariable=display_str, justify=tk.RIGHT)
display.grid(row=0, columnspan=5, sticky=stick)

digit7 = tk.Button(window, text="7", command=lambda: do_digit_x("7"))
digit7.grid(row=1, column=0, sticky=stick)
digit8 = tk.Button(window, text="8", command=lambda: do_digit_x("8"))
digit8.grid(row=1, column=1, sticky=stick)
digit9 = tk.Button(window, text="9", command=lambda: do_digit_x("9"))
digit9.grid(row=1, column=2, sticky=stick)
plus = tk.Button(window, text="+", command=do_plus)
plus.grid(row=1, column=4, sticky=stick)

digit4 = tk.Button(window, text="4", command=lambda: do_digit_x("4"))
digit4.grid(row=2, column=0, sticky=stick)
digit5 = tk.Button(window, text="5", command=lambda: do_digit_x("5"))
digit5.grid(row=2, column=1, sticky=stick)
digit6 = tk.Button(window, text="6", command=lambda: do_digit_x("6"))
digit6.grid(row=2, column=2, sticky=stick)
minus = tk.Button(window, text="-", command=do_minus)
minus.grid(row=2, column=4, sticky=stick)

digit1 = tk.Button(window, text="1", command=lambda: do_digit_x("1"))
digit1.grid(row=3, column=0, sticky=stick)
digit2 = tk.Button(window, text="2", command=lambda: do_digit_x("2"))
digit2.grid(row=3, column=1, sticky=stick)
digit3 = tk.Button(window, text="3", command=lambda: do_digit_x("3"))
digit3.grid(row=3, column=2, sticky=stick)
equal = tk.Button(window, text=" = ", command=do_equal)
equal.grid(row=3, column=3, sticky=stick)
mult = tk.Button(window, text="*", command=do_mult)
mult.grid(row=3, column=4, sticky=stick)

digit0 = tk.Button(window, text="0", command=do_digit_0)
digit0.grid(row=4, column=0, sticky=stick)
dot = tk.Button(window, text=" . ", command=do_dot)
dot.grid(row=4, column=2, sticky=stick)
clear = tk.Button(window, text="C", command=do_clear)
clear.grid(row=4, column=1, sticky=stick)
plusminus = tk.Button(window, text="+/-", command=do_plusminus)
plusminus.grid(row=4, column=3, sticky=stick)

divd = tk.Button(window, text="/", command=do_divd)
divd.grid(row=4, column=4, sticky=stick)
accumulator = 0.
last_operation = ""
window.mainloop()
