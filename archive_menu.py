import tkinter as tk

class ArchiveMenu():
	def __init__(self):
		pass

	def draw_menu():
		lines = {}
		for i in range(6):
			lines['l' + str(i)] = 'l' + str(i)
			lines['l' + str(i)] = tk.Canvas(archive_frame, bg=line_colour, bd=0, highlightthickness=0)
			y = 0.15*i
			lines['l' + str(i)].place(height=20, width=670, relx=0, rely=y)


		path_to_archive = tk.Label(lines['l1'], text='Path to be archived', bg=MAIN_COLOUR)
		path_to_archive.place(x=1)

		archive_entry_var = tk.StringVar()
		archive_entry = tk.Entry(lines['l1'], bg=WHITE, font=FONT, bd=0, highlightcolor=WHITE, width=65,
			textvariable=archive_entry_var)
		archive_entry_var.set('/Users/georgeaugustustully/Documents/coding/projects/test_backup_proj')
		archive_entry.place(x=145)


		dest = tk.Label(lines['l2'], text='Destination', bg=MAIN_COLOUR)
		dest.place(x=1)

		dest_entry_var = tk.StringVar()
		dest_entry = tk.Entry(lines['l2'], bg='white', font=FONT, bd=0, highlightcolor=WHITE, width=65,
			textvariable=dest_entry_var)
		dest_entry_var.set('/Users/georgeaugustustully/Library/Mobile Documents/com~apple~CloudDocs/backup/')
		dest_entry.place(x=145)


		key_gen_var = tk.StringVar()
		key_gen = tk.Entry(lines['l3'], textvariable=key_gen_var, bg='white', highlightcolor=WHITE, bd=0)
		key_gen_var.set(DEFAULT_MSG)
		key_gen.place(x=145, relheight=1, width=570)


		encrypt_var = tk.IntVar()
		encrypt_button = tk.Checkbutton(lines['l4'], text='Encrypt', variable=encrypt_var, command=lambda :display_key(),\
		                 onvalue=1, offvalue=0, bg=ACCENT_1)
		encrypt_button.place(x=145, relheight=1, width=150)

		reset_button = tk.Button(lines['l4'], text='Reset', command=lambda :reset_archive_values())
		reset_button.place(x=530, relheight=1, width=150)

		archive_button = tk.Button(lines['l5'], text='Archive', command=lambda :make_archive())
		archive_button.place(x=530, relheight=1, width=150)