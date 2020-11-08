import tkinter as tk

class Gui:
	'''Tools to build visual elements of GUI.'''
	def __init__(self, title, bgcol, width, height, font):
		self._title = title
		self._bgcol = bgcol
		self._width = width
		self._height = height
		self._font = font
		

	def root_gen(self):
		'''All Tkinter GUI's begin with this object.'''
		self._root = tk.Tk()
		return self._root


	def master_frame(self, parent):
		'''Create the global GUI dimensions.

		Frames are like canvases for Tkinter.
		You place objects in frames, including other frames.'''
		master_frame = tk.Frame(master=parent, width=self._width, height=self._height, bg=self._bgcol)
		return master_frame


	def subframe(self, parent, name, width, height, bgcol):
		name = tk.Frame(parent, width=width, height=height, bg=bgcol)
		return name


	def frame_placer(self, name, x=0, y=0):
		'''Frames must be placed using this function.'''
		name.place(x=x, y=y)


	def rows(self, parent, height, num, vgap, colour):
		'''Create multiple canvases as rows.'''
		rows = {}
		for r in range(1, num+1):
			row_key = 'row' + str(r)
			rows[row_key] = row_key
			rows[row_key] = tk.Canvas(parent, height=height, highlightthickness=0, bg=colour)
			vg = r * vgap
			rows[row_key].place(y=vg-vgap, relwidth=1)

		return rows


	def cell_in_row(self, parent, start_point, width, colour):
		'''Create a cell in a row.'''
		cell = tk.Canvas(parent, bg=colour, highlightthickness=0)
		cell.place(x=start_point, width=width)
		return cell


	def label(self, parent, text, bgcol):
		label = tk.Label(parent, text=text, bg=bgcol)
		label.place(x=0)
		return label


	def text_entry(self, parent, text, bgcol, fill_parent=True):
		if fill_parent == False:
			fill_parent = None
		entry_var = tk.StringVar()
		entry = tk.Entry(parent, bg=bgcol, font=self._font, bd=0, highlightcolor='white', textvariable=entry_var)
		entry_var.set(text)
		entry.place(x=0, relwidth=fill_parent)
		return {'entry': entry, 'var': entry_var} 


	def tick_box(self, parent, label, bgcol, command=None):
		var = tk.IntVar()
		box = tk.Checkbutton(parent, text=label, variable=var, command=command, onvalue=1, offvalue=0, bg=bgcol)
		box.place(relwidth=1)
		return {'box': box,'var': var}


	def button(self, parent, label, command=None):
		'''Mac cannot change button colour.'''
		button = tk.Button(parent, text=label, command=command)
		button.place(relwidth=1)
		return button


	def draw(self, master):
		'''Draw the masterframe and all its contents.'''
		self._root.title(self._title)
		master.pack()
		self._root.mainloop()


