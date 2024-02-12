from tkinter import Tk, StringVar, END
from tkinter.ttk import *

import pyautogui

screenWidth, screenHeight = pyautogui.size()
main = Tk()
main.title("Unit conversion")
main.minsize(320, 200)
main.geometry("{}x{}+{}+{}".format(320, 200, (screenWidth - 320) // 2, (screenHeight - 200) // 2))
Label(main, text="Select the original unit", foreground="blue").pack(side="top")
frame = Frame(main)
frame.pack(side="top")


def only_numbers(chars):
    return all(char.isdigit() or char == '.' for char in chars)


validation = main.register(only_numbers)
userInput = Entry(frame, width=10, validate="key", validatecommand=(validation, "%P"))
userInput.pack(side="left")
originalUnit = StringVar()
dropdown0 = OptionMenu(frame, originalUnit, "Minutes", "Yocto-seconds", "Zepto-seconds", "Atto-seconds", "Femto-seconds",
                       "Picoseconds", "Nanoseconds", "Microseconds", "Milliseconds", "Seconds", "Minutes", "Hours",
                       "Days", "Weeks", "Months", "Years", "Decades", "Centuries", "Millennia")
dropdown0.pack(side="left")
Label(main, text="Select the modified unit", foreground="blue").pack(side="top")
modifiedUnit = StringVar()
dropdown1 = OptionMenu(main, modifiedUnit, "Seconds", "Yocto-seconds", "Zepto-seconds", "Atto-seconds", "Femto-seconds",
                       "Picoseconds", "Nanoseconds", "Microseconds", "Milliseconds", "Seconds", "Minutes", "Hours",
                       "Days", "Weeks", "Months", "Years", "Decades", "Centuries", "Millennia")
dropdown1.pack(side="top")


# noinspection PyGlobalUndefined
def convert():
    global operator, x, y
    if all(char == '.' for char in userInput.get()):
        userInput.delete(0, END)
        userInput.insert(0, "0")
    times = ["Yocto-seconds", "Zepto-seconds", "Atto-seconds", "Femto-seconds", "Picoseconds", "Nanoseconds",
             "Microseconds", "Milliseconds", "Seconds", "Minutes", "Hours", "Days", "Weeks", "Months", "Years",
             "Decades", "Centuries", "Millennia"]
    firstValue = times.index(originalUnit.get())
    secondValue = times.index(modifiedUnit.get())

    if firstValue == secondValue:
        result = userInput.get()
    else:
        if firstValue > secondValue:
            x = firstValue
            y = secondValue
            operator = "*"
        elif secondValue > firstValue:
            x = secondValue
            y = firstValue
            operator = "/"
        result = float(userInput.get())
        while True:
            x -= 1
            if x <= 7:
                if operator == "*":
                    result *= 1000
                if operator == "/":
                    result /= 1000
            elif x == 8 or x == 9:
                if operator == "*":
                    result *= 60
                if operator == "/":
                    result /= 60
            elif x == 10:
                if operator == "*":
                    result *= 24
                if operator == "/":
                    result /= 24
            elif x == 11:
                if operator == "*":
                    result *= 7
                if operator == "/":
                    result /= 7
            elif x == 12:
                if operator == "*":
                    result *= 4
                if operator == "/":
                    result /= 4
            elif x == 13:
                if operator == "*":
                    result *= 12
                if operator == "/":
                    result /= 12
            elif x >= 14:
                if operator == "*":
                    result *= 10
                if operator == "/":
                    result /= 10
            if x <= y:
                break

    userInput.delete(0, END)
    userInput.insert(0, "{}".format(result))
    storedValue = originalUnit.get()
    originalUnit.set(modifiedUnit.get())
    modifiedUnit.set(storedValue)


Button(main, text="Convert to modified unit", command=convert).pack(side="top")
main.mainloop()
