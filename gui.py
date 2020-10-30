import tkinter as tk
import encryption as enc
import archive as arc


HEIGHT = 300
WIDTH = 700
FONT = 'helvetica'
MAIN_COLOUR = '#9dd2c6'
WHITE = 'white'
ACCENT_1 = '#999795'
ACCENT_2 = '#dbf4cc'
ENTRY_TEXT_BG = WHITE
DEFAULT_KEY = '[copy and paste secure key from here]'

layout_preview = 0

if layout_preview == 1:
	interaction_colour = 'green'
	line_colour = 'blue'
else:
	interaction_colour = MAIN_COLOUR
	line_colour = MAIN_COLOUR


def make_archive():
	source = archive_entry.get()
	dest = dest_entry.get()
	if key_gen_var.get() == DEFAULT_KEY:
		print('No key generated')
		key = None
	else:
		key = key_gen_var.get()
	print(source, dest, key)

	backup = arc.Archive(source=source, dest=dest, format_='zip')
	# # No TOC yet!
	backup.publish(key=key, toc=False)


def display_key():
	if encrypt_var.get() == 0:
		key_gen_var.set(DEFAULT_KEY)
		print('Secure key cleared from GUI')
		dest.text='George!'
	else:
		key = enc.fernet_key_gen()
		key_gen_var.set(key)
		print('New key diplayed in GUI')


root = tk.Tk()
root.title('GT Secure Archiver 1.0')


frame = tk.Frame(root, width=WIDTH, height=HEIGHT, bg=MAIN_COLOUR, bd=4)
frame.pack()


interaction = tk.Frame(frame, width=WIDTH, height=200, bg=interaction_colour, bd=4)
interaction.place(height=200, relwidth=1, relx=.005, y=100)


lines = {}
for i in range(6):
	lines['l' + str(i)] = 'l' + str(i)
	lines['l' + str(i)] = tk.Canvas(interaction, bg=line_colour, bd=0, highlightthickness=0)
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
key_gen_var.set(DEFAULT_KEY)
key_gen.place(x=145, relheight=1, width=570)


encrypt_var = tk.IntVar()
encrypt_button = tk.Checkbutton(lines['l4'], text='Encrypt', variable=encrypt_var, command=lambda :display_key(),\
                 onvalue=1, offvalue=0, bg=ACCENT_1)
encrypt_button.place(x=145, relheight=1, width=150)


archive_button = tk.Button(lines['l5'], text='Archive', command=lambda :make_archive())
archive_button.place(x=530, relheight=1, width=150)


root.mainloop()

