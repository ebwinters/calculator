try:
    import Tkinter  
except ImportError:
    import tkinter

class Calculator:
	def __init__(self, master):
		self.master = master
		self.mainframe = tkinter.Frame(self.master, bg='white')
		self.mainframe.pack(fill=tkinter.BOTH, expand=True)

		self.build_grid()
		self.build_banner()


	def build_grid(self):
		self.mainframe.columnconfigure(0, weight=1)
		self.mainframe.rowconfigure(0, weight=0)
		self.mainframe.rowconfigure(1, weight=1)
		self.mainframe.rowconfigure(2, weight=0)

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

if __name__ == '__main__':
	root = tkinter.Tk()
	Calculator(root)
	root.mainloop()
	