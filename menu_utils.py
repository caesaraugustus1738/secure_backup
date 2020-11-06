import tkinter as tk

class Menu:

	def __init__(self, parent):
		self._parent = parent
		# Initialise menu (you just have to do this to make Tkinter work)
		self._menu = tk.Menu(self._parent)
		self._parent.config(menu=self._menu)
		

	def make(self, name, items):
		menu = tk.Menu(self._menu)
		self._menu.add_cascade(label=name, menu=menu)
		for item in items:
			menu.add_command(label=item, command=items[item])



# # Initialise a menu
# my_menu = tk.Menu(root)
# root.config(menu=my_menu)

	# # Add a menu items
# mode_menu = tk.Menu(my_menu)
# my_menu.add_cascade(label='Mode', menu=mode_menu)
# mode_menu.add_command(label='Archive', command=lambda :place_archive_frame())
# mode_menu.add_separator()
# mode_menu.add_command(label='Unarchive', command=lambda :place_unarchive_frame())