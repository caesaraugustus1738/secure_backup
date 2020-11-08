import tkinter as tk
import gui_utils as gutils
import menu_utils as mu
from encryption import fernet_key_gen
import gui_grid


class ArchiverGUI:
    def __init__(self, backend):
        self.backend = backend
        self.gui = gutils.Gui(title='Secure Archive v001', width=800, height=300, bgcol='#9dd2c6', font='Helvetica')
        self._default_key = '[copy and paste security key from here]'
        self._default_arc_path = '[enter path to be archived here]'
        self._default_arc_dest = '[enter archive destination path here]'
        # self._archive_mode = 
        # self._master_frame = self.gui.master_frame()
        # self._root = self.gui._root


    def _master_frame(self):
        '''The highest level GUI parent.'''
        master_frame = self.gui.master_frame(self.gui.root_gen())
        return master_frame


    def _mode_title(self, parent):
        mode = self.gui.subframe(parent=parent, name='mode_title', width=self.gui._width, height=20, bgcol=self.gui._bgcol)
        self.gui.frame_placer(mode, y=115, x=25)
        self.gui.label(parent=mode, text='ARCHIVE MODE', bgcol='#71a3ae')


    def _make_naked_grid(self, gui, parent):
        grid = gui_grid.Grid(gui=gui, parent=parent, layout_preview=False).create_grid()
        return grid


    def _archive_skin(self, grid):
        '''Populate naked grid with text/entry fields.'''
        skin = {
        'label_1': self.gui.label(grid['row1_col1'], text='Path to be archived', bgcol='#9dd2c6'),
        'arc_path': self.gui.text_entry(grid['row1_col2'], text=self._default_arc_path, bgcol='white', fill_parent=True),
        'label_2': self.gui.label(grid['row2_col1'], text='Destination', bgcol='#9dd2c6'),
        'arc_dest': self.gui.text_entry(grid['row2_col2'], text=self._default_arc_dest, bgcol='white', fill_parent=True),
        'key': self.gui.text_entry(grid['row3_col1'], text=self._default_key, bgcol='white', fill_parent=True)
        }
        return skin


    def _archive_buttons(self, grid):
        '''Populate naked grid with command buttons.'''
        buttons = {
        'encrypt': self.gui.tick_box(grid['row4_col1'], label='Encrypt', bgcol='grey'),
        'reset': self.gui.button(grid['row5_col1'], label='Reset'),
        'archive': self.gui.button(grid['row6_col1'], label='Archive')
        }
        return buttons


    def _button_commands(self, buttons, skin):
        buttons['encrypt']['box'].config(command=lambda: self._key_gen(skin=skin, buttons=buttons))
        buttons['reset'].config(command=lambda: self._reset_inputs(skin=skin, buttons=buttons))
        buttons['archive'].config(command=lambda: self._archive(skin))


    def _add_menu(self):
        '''Dropdown menu two switch between archive and unarchive GUI.'''
        menu = mu.Menu(parent=self.gui._root)
        items = {'Archive': False, 'Unarchive': False}
        menu.make(name='Mode', items=items)


    def _get_inputs(self, skin):
        '''Get values from input fields.'''
        inputs = {
        'arc_path': skin['arc_path']['entry'].get(),
        'arc_dest': skin['arc_dest']['entry'].get(),
        'key': skin['key']['entry'].get()
        }
        return inputs


    def _archive(self, skin):
        self.backend.archive(self._get_inputs(skin))


    def _reset_inputs(self, skin, buttons):
        skin['arc_path']['var'].set(self._default_arc_path)
        skin['arc_dest']['var'].set(self._default_arc_dest)
        buttons['encrypt']['var'].set(0)
        self._key_gen(skin, buttons)


    def _key_gen(self, skin, buttons):
        if not buttons['encrypt']['var'].get():
            skin['key']['var'].set(self._default_key)
        else:
            key = fernet_key_gen()
            skin['key']['var'].set(key)


    def draw(self):
        mf = self._master_frame()
        self._add_menu()
        self._mode_title(parent=mf)
        a_grid = self._make_naked_grid(gui=self.gui, parent=mf)
        skin = self._archive_skin(a_grid)
        buttons = self._archive_buttons(a_grid)
        self._button_commands(buttons=buttons, skin=skin)
        self.gui.draw(master=mf)


# class GUIView:
#     def __init__(self, master_frame):
#         self._grid = ArchiverGUI._make_naked_grid(master_frame)


#     def _archive_skin(self, grid):
#         '''Populate naked grid with text/entry fields.'''
#         skin = {
#         'label_1': self.gui.label(grid['row1_col1'], text='Path to be archived', bgcol='#9dd2c6'),
#         'arc_path': self.gui.text_entry(grid['row1_col2'], text=self._default_arc_path, bgcol='white', fill_parent=True),
#         'label_2': self.gui.label(grid['row2_col1'], text='Destination', bgcol='#9dd2c6'),
#         'arc_dest': self.gui.text_entry(grid['row2_col2'], text=self._default_arc_dest, bgcol='white', fill_parent=True),
#         'key': self.gui.text_entry(grid['row3_col1'], text=self._default_key, bgcol='white', fill_parent=True)
#         }
#         return skin


# class ArchiveGUIView(GUIView):
#     def __init__(self):
#         self._skin = ArchiverGUI._archive_skin(self._grid)
#         self._buttons = ArchiverGUI._archive_buttons()


