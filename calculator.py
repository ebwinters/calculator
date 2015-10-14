try:
    import Tkinter  
except ImportError:
    import tkinter

class Calculator:
	def __init__(self, master):
		master.minsize(width=500, height=500)
		master.maxsize(width=500, height=500)
		self.master = master
		self.mainframe = tkinter.Frame(self.master, bg='white')
		self.mainframe.pack(fill=tkinter.BOTH, expand=True)

		self.display = tkinter.StringVar()
		self.display.trace('w', self.build_box)
		self.output = tkinter.IntVar()
		self.num1 = tkinter.IntVar()
		self.num2 = tkinter.IntVar()
		self.add = False
		self.sub = False
		self.div = False
		self.mult = False


		self.build_grid()
		self.build_banner()
		self.build_all_buttons()
		self.build_box()


	def build_grid(self):
		self.mainframe.columnconfigure(0, weight=1)
		self.mainframe.rowconfigure(0, weight=0)
		self.mainframe.rowconfigure(1, weight=1)
		self.mainframe.rowconfigure(2, weight=1)
		self.mainframe.rowconfigure(3, weight=1)
		self.mainframe.rowconfigure(4, weight=1)
		self.mainframe.rowconfigure(5, weight=1)
		self.mainframe.rowconfigure(6, weight=1)

	def build_banner(self):
		banner = tkinter.Label(
			self.mainframe,
			background='black',
			text='Calculator',
			fg='blue',
			font=('Courier', 22)
			)
		banner.grid(
			row=0, column=0,
			sticky='ew'
			)

	def build_all_buttons(self):
		buttons_frame = tkinter.Frame(self.mainframe)
		buttons_frame.grid(row=2, column=0, sticky='nsew')
		#configure columns
		buttons_frame.columnconfigure(0, weight=1)
		buttons_frame.columnconfigure(1, weight=1)
		buttons_frame.columnconfigure(2, weight=1)
		buttons_frame.columnconfigure(3, weight=1)
		#configure rows
		buttons_frame.rowconfigure(0, weight=1)
		buttons_frame.rowconfigure(1, weight=1)
		buttons_frame.rowconfigure(2, weight=1)
		buttons_frame.rowconfigure(3, weight=1)
		buttons_frame.rowconfigure(4, weight=1)

		self.seven = tkinter.Button(
			buttons_frame,
			text='7',
			command=self.press_seven
			)
		self.eight = tkinter.Button(
			buttons_frame,
			text='8',
			command=self.press_eight
			)
		self.nine = tkinter.Button(
			buttons_frame,
			text='9',
			command=self.press_nine
			)
		self.plus = tkinter.Button(
			buttons_frame,
			text='+',
			command=self.press_plus
			)
		self.four = tkinter.Button(
			buttons_frame,
			text='4',
			command=self.press_four
			)
		self.five = tkinter.Button(
			buttons_frame,
			text='5',
			command=self.press_five
			)
		self.six = tkinter.Button(
			buttons_frame,
			text='6',
			command=self.press_six
			)
		self.minus = tkinter.Button(
			buttons_frame,
			text='-',
			command=self.press_minus
			)
		self.one = tkinter.Button(
			buttons_frame,
			text='1',
			command=self.press_one
			)
		self.two = tkinter.Button(
			buttons_frame,
			text='2',
			command=self.press_two
			)
		self.three = tkinter.Button(
			buttons_frame,
			text='3',
			command=self.press_three
			)
		self.slash = tkinter.Button(
			buttons_frame,
			text='/',
			command=self.press_slash
			)
		self.zero = tkinter.Button(
			buttons_frame,
			text='0',
			command=self.press_zero
			)
		self.equals = tkinter.Button(
			buttons_frame,
			text='=',
			command=self.press_equals
			)
		self.star = tkinter.Button(
			buttons_frame,
			text='*',
			command=self.press_star
			)
		self.clr = tkinter.Button(
			buttons_frame,
			text='clr',
			command=self.press_clr
			)
		#enter buttons into grid
		self.seven.grid(row=0, column=0, sticky='ew')
		self.eight.grid(row=0, column=1, sticky='ew')
		self.nine.grid(row=0, column=2, sticky='ew')
		self.plus.grid(row=0, column=3, sticky='ew')
		self.four.grid(row=1, column=0, sticky='ew')
		self.five.grid(row=1, column=1, sticky='ew')
		self.six.grid(row=1, column=2, sticky='ew')
		self.minus.grid(row=1, column=3, sticky='ew')
		self.one.grid(row=2, column=0, sticky='ew')
		self.two.grid(row=2, column=1, sticky='ew')
		self.three.grid(row=2, column=2, sticky='ew')
		self.slash.grid(row=2, column=3, sticky='ew')
		self.clr.grid(row=3, column=0, sticky='ew')
		self.zero.grid(row=3, column=1, sticky='ew')
		self.equals.grid(row=3, column=2, sticky='ew')
		self.star.grid(row=3, column=3, sticky='ew')

	def build_box(self, *args):
		box = tkinter.Label(
			self.mainframe,
			text=self.display.get(),
			font=('Courier', 22)
			)
		box.grid(row=1, column=0, sticky='ew')

	def press_seven(self):
		self.num1 = 7
		self.display.set('7')
		print(self.num1)
	def press_eight(self):
		self.num1 = 8
		self.display.set('8')
		print(self.num1)
	def press_nine(self):
		self.num1 = 9
		self.display.set('9')
		print(self.num1)
	def press_plus(self):
		pass
	def press_four(self):
		self.num1 = 4
		self.display.set('4')
		print(self.num1)
	def press_five(self):
		self.num1 = 5
		self.display.set('5')
		print(self.num1)
	def press_six(self):
		self.num1 = 6
		self.display.set('6')
		print(self.num1)
	def press_minus(self):
		pass
	def press_one(self):
		self.num1 = 1
		self.display.set('1')
		print(self.num1)
	def press_two(self):
		self.num1 = 2
		self.display.set('2')
		print(self.num1)
	def press_three(self):
		self.num1 = 3
		self.display.set('3')
		print(self.num1)	
	def press_slash(self):
		pass
	def press_zero(self):
		self.num1 = 0
		self.display.set('0')
		print(self.num1)	
	def press_equals(self):
		pass
	def press_clr(self):
		pass
	def press_star(self):
		pass


if __name__ == '__main__':
	root = tkinter.Tk()
	Calculator(root)
	root.mainloop()
	