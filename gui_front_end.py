import tkinter as tk
import gui_utils as gutils
import menu_utils as mu

import grid_frame
import frame_layout
import frame_stacks


class ArchiverGUI:
    def __init__(self, backend):
        self.backend = backend
        self.gui = gutils.Gui(title='Secure Archive v001', width=800, height=300, bgcol='#9dd2c6', font='Helvetica')
        # self._default_key = '[copy and paste security key from here]'
        # self._default_arc_path = '[enter path to be archived here]'
        # self._default_arc_dest = '[enter archive destination path here]'


    def _master_frame(self):
        '''The highest level GUI parent.'''
        master_frame = self.gui.master_frame(self.gui.root_gen())
        return master_frame


    def _mode_title(self, parent):
        mode = self.gui.subframe(parent=parent, width=self.gui._width, height=20, bgcol=self.gui._bgcol)
        self.gui.frame_placer(mode, y=115, x=25)
        self.gui.label(parent=mode, text='ARCHIVE MODE', bgcol='#71a3ae')


    def _add_menu(self, stack):
        '''Dropdown menu two switch between archive and unarchive GUI.'''
        menu = mu.Menu(parent=self.gui._root)
        items = {'Archive': lambda: stack.show_archive(), 'Unarchive': lambda: stack.show_unarchive()}
        menu.make(name='Mode', items=items)


    def draw(self):
        mf = self._master_frame()
        stack = frame_stacks.FrameStack(parent=mf, gui=self.gui)
        self._add_menu(stack)
        self.gui.draw(master=mf)





'''
The base class holds the attributes that won't change between the sub classes, aka the constants.
'''

    # def _make_naked_grid(self, gui, parent):
    #     grid = gui_grid.Grid(gui=gui, parent=parent, layout_preview=False).create_grid()
    #     return grid




