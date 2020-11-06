import tkinter as tk

class Gui():
	def __init__(self, title):
		self._title = title

	def make(self):
		root = tk.Tk()
		root.title(self._title)
		root.mainloop()


class ArchiveMenu():
	def __init__(self, frame, key_entry_message, main_colour, font, accent_1, accent_2, line_colour):
		self._frame = frame
		self._key_entry_message = key_entry_message
		self._main_colour = main_colour
		self._font = font
		self._white = 'white'
		self._accent_1 = accent_1
		self._accent_2 = accent_2
		self._line_colour = line_colour
		pass

	# layout_preview = 0

	# if layout_preview == 1:
	# 	interaction_colour = 'green'
	# 	line_colour = 'blue'
	# else:
	# 	interaction_colour = self._self._main_colour
	# 	line_colour = self._self._main_colour


	def make_archive(self):
		source = archive_entry.get()
		dest = dest_entry.get()
		if key_gen_var.get() == DEFAULT_MSG:
			print('No key generated')
			key = None
		else:
			key = key_gen_var.get()
		print(source, dest, key)

		backup = arc.Archive(source=source, dest=dest, format_='zip')
		# # No TOC yet!
		backup.publish(key=key, toc=False)


	def display_key(self):
		if encrypt_var.get() == 0:
			key_gen_var.set(DEFAULT_MSG)
			print('Secure key cleared from GUI')
			dest.text='George!'
		else:
			key = enc.fernet_key_gen()
			key_gen_var.set(key)
			print('New key diplayed in GUI')


	def reset_archive_values(self):
		dest_entry_var.set('')
		archive_entry_var.set('')
		key_gen_var.set(DEFAULT_MSG)
		encrypt_var.set(0)


	def draw_menu(self):
		lines = {}
		for i in range(6):
			line_key = 'l' + str(i)
			lines[line_key] = line_key
			lines[line_key] = tk.Canvas(self._frame, bg=self._line_colour, bd=0, highlightthickness=0)
			y = 0.15*i
			lines[line_key].place(height=20, width=670, relx=0, rely=y)


		src = tk.Label(lines['l1'], text='Path to be archived', bg=self._main_colour)
		src.place(x=1)

		src_entry_var = tk.StringVar()
		src_entry = tk.Entry(lines['l1'], bg=self._white, font=self._font, bd=0, highlightcolor=self._white, width=65,
			textvariable=src_entry_var)
		src_entry_var.set('/Users/georgeaugustustully/Documents/coding/projects/test_backup_proj')
		src_entry.place(x=145)

		dest = tk.Label(lines['l2'], text='Destination', bg=self._main_colour)
		dest.place(x=1)

		dest_entry_var = tk.StringVar()
		dest_entry = tk.Entry(lines['l2'], bd=0, bg=self._white, font=self._font,  highlightcolor=self._white, 
			textvariable=dest_entry_var, width=65)
		dest_entry_var.set('/Users/georgeaugustustully/Library/Mobile Documents/com~apple~CloudDocs/backup/')
		dest_entry.place(x=145)

		key_entry_var = tk.StringVar()
		key_entry = tk.Entry(lines['l3'], bd=0, bg=self._white, highlightcolor=self._white, textvariable=key_entry_var)
		key_entry_var.set(self._key_entry_message)
		key_entry.place(x=145, relheight=1, width=570)

		encrypt_var = tk.IntVar()
		encrypt_button = tk.Checkbutton(lines['l4'], text='Encrypt', variable=encrypt_var, 
			command=lambda :display_key(), onvalue=1, offvalue=0, bg=self._accent_1)
		encrypt_button.place(x=145, relheight=1, width=150)

		reset_button = tk.Button(lines['l4'], text='Reset', command=lambda :self.reset_archive_values())
		reset_button.place(x=530, relheight=1, width=150)

		archive_button = tk.Button(lines['l5'], text='Archive', command=lambda :self.make_archive())
		archive_button.place(x=530, relheight=1, width=150)

