name = input("variable name: ")
print("self.{} = tkinter.Button(buttons_frame, text={}, command=self.press_{})".format(name, name, name))