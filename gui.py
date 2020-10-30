import tkinter as tk

root = tk.Tk()
root.title('GT Secure Archives 1.0')

HEIGHT = 300
WIDTH = 700
PINK = '#ead0d6'

layout_preview = 0

if layout_preview is 1:
	interaction_colour = 'green'
	line_colour = 'blue'
else:
	interaction_colour = PINK
	line_colour = PINK

secure_colour = '#9bd2c6'

frame = tk.Frame(root, height=HEIGHT, width=WIDTH,\
	bg=PINK, bd=4)
frame.pack()

interaction = tk.Frame(frame, height=200, width=WIDTH, bg=interaction_colour, bd=4)
interaction.place(height=200, relwidth=1, relx=.005, y=100)

lines = {}
for i in range(6):
	lines['l' + str(i)] = 'l' + str(i)
	lines['l' + str(i)] = tk.Canvas(interaction, bg=line_colour, bd=0, highlightthickness=0)
	y = 0.15*i
	lines['l' + str(i)].place(height=20, width=670, relx=0, rely=y)

print(lines)

path_to_archive = tk.Label(lines['l1'], text='Path to be archived', bg=PINK)
path_to_archive.place(x=1)

archive_entry = tk.Entry(lines['l1'], bg='white',\
	font='helvetica',
	bd=0,
	highlightcolor='white',
	width=65
	)
archive_entry.place(x=145)

dest = tk.Label(lines['l2'], text='Destination', bg=PINK)
dest.place(x=1)


dest_entry = tk.Entry(lines['l2'], bg='white',\
	font='helvetica',
	bd=0,
	highlightcolor='white',
	width=65
	)

dest_entry.place(x=145)

# key_label = tk.Label(lines['l3'], text='Key',bg='#e2bec7')
# key_label.place(x=145, relheight=1, width=40)

key_gen_label = tk.Label(lines['l3'], text='[copy and paste the key from here]', bg='white')
key_gen_label.place(x=145, relheight=1, width=570)

secure_button = tk.Checkbutton(lines['l4'], text='Secure', variable=None, \
                 onvalue=1, offvalue=0, selectcolor='red', \
                 bg=secure_colour)
secure_button.place(x=145, relheight=1, width=150)



archive_button = tk.Button(lines['l5'], text='Archive',\
	activebackground='blue')
archive_button.place(x=530, relheight=1, width=150)

# dest = tk.Label(line2, text='Archive destination',\
# 	bg=PINK)
# dest.place(
# 	# height=20,
# 	# width=200,
# 	relx=0,
# 	rely=.5
# 	)

# dest_entry = tk.Entry(line2, bg='white',\
# 	font='helvetica',
# 	bd=0,
# 	highlightcolor='white',
# 	width=500
# 	)

# dest_entry.place(
# 	# height=20,
# 	# width=800,
# 	relx=.18,
# 	rely=.5
# 	)


# l2 = tk.Label(frame, text='Archive destination',\
# 	bg=PINK)
# l2.pack(side='left')

# dest_entry = tk.Entry(frame, bg='white',\
# 	font='helvetica',
# 	bd=0,
# 	highlightcolor='white',
# 	width=500
# 	)
# dest_entry.place(height=20,
# 	width=200,
# 	relx=0,
# 	rely=.05)


# Get value from button
# check_var = tk.IntVar()


# c1.place(relwidth=.8, relheight=.8, \
# 	relx=.1, rely=.1)

# canvas.place(relwidth=.8, relheight=.8, \
# 	relx=.1, rely=.1)


root.mainloop()