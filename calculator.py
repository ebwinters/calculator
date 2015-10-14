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

		self.build_grid()
		self.build_banner()
		self.build_all_buttons()

	def build_grid(self):
		self.mainframe.columnconfigure(0, weight=1)
		self.mainframe.rowconfigure(0, weight=0)
		self.mainframe.rowconfigure(1, weight=1)
		self.mainframe.rowconfigure(2, weight=1)
		self.mainframe.rowconfigure(3, weight=1)
		self.mainframe.rowconfigure(4, weight=1)
		self.mainframe.rowconfigure(5, weight=1)

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

		self.seven = tkinter.Button(
			buttons_frame,
			text='7'
			)
		self.eight = tkinter.Button(
			buttons_frame,
			text='8'
			)
		self.nine = tkinter.Button(
			buttons_frame,
			text='9'
			)
		self.plus = tkinter.Button(
			buttons_frame,
			text='+'
			)
		self.four = tkinter.Button(
			buttons_frame,
			text='4'
			)
		self.five = tkinter.Button(
			buttons_frame,
			text='5'
			)
		self.six = tkinter.Button(
			buttons_frame,
			text='6'
			)
		self.minus = tkinter.Button(
			buttons_frame,
			text='-'
			)
		self.one = tkinter.Button(
			buttons_frame,
			text='1'
			)
		self.two = tkinter.Button(
			buttons_frame,
			text='2'
			)
		self.three = tkinter.Button(
			buttons_frame,
			text='3'
			)
		self.slash = tkinter.Button(
			buttons_frame,
			text='/'
			)
		self.zero = tkinter.Button(
			buttons_frame,
			text='0'
			)
		self.equals = tkinter.Button(
			buttons_frame,
			text='='
			)
		self.star = tkinter.Button(
			buttons_frame,
			text='*'
			)
		self.blank = tkinter.Button(
			buttons_frame,
			text=''
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
		self.zero.grid(row=3, column=1, sticky='ew')
		self.equals.grid(row=3, column=2, sticky='ew')
		self.star.grid(row=3, column=3, sticky='ew')

if __name__ == '__main__':
	root = tkinter.Tk()
	Calculator(root)
	root.mainloop()
	