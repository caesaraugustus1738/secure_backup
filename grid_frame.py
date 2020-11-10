import grid

class GridFrame:
    '''Add buttons/labels/entry fields to a grid frame.'''
    def __init__(self, gui, parent):
        self.gui = gui
        self.label_1 = 'label_1'
        self.entry_1 = 'arc_path'
        self.label_2 = 'label_2'
        self.entry_2 = 'arc_dest'
        self.entry_3 = 'key'
        self.label_2_text = 'Destination'
        self.button_1 = 'reset'
        self.bgcol = '#9dd2c6'
        self.grid = grid.Grid(gui=self.gui, parent=parent).create_grid()


    def _make_entries(self, grid):
        '''Populate naked grid with text/entry fields.'''
        fields = {
        self.label_1: self.gui.label(grid['row1_col1'], text=self._label_1_text, bgcol=self.bgcol),
        self.entry_1: self.gui.text_entry(grid['row1_col2'], text=self._entry_1_text, bgcol='white', fill_parent=True),
        self.label_2: self.gui.label(grid['row2_col1'], text=self.label_2_text, bgcol=self.bgcol),
        self.entry_2: self.gui.text_entry(grid['row2_col2'], text=self._entry_2_text, bgcol='white', fill_parent=True),
        self.entry_3: self.gui.text_entry(grid['row3_col1'], text=self._entry_3_text, bgcol='white', fill_parent=True)
        }

        return fields


    def _make_buttons(self, grid):
        '''Populate naked grid with command buttons.'''
        unarchive = self._unarchive
        buttons = {
        self.button_1: self.gui.button(grid['row5_col1'], label=self.button_1.capitalize()),
        self._button_2: self.gui.button(grid['row6_col1'], label=self._button_2_label)
        }

        if unarchive:
            pass
        else:
            buttons[self._tickbox_1] = self.gui.tick_box(grid['row4_col1'], label=self._tickbox_1_label, bgcol='grey')

        return buttons


    def make_frame(self):
        self._make_entries(self.grid['grid'])
        self._make_buttons(self.grid['grid'])
        return self.grid['frame']


class ArchiveFrame(GridFrame):
    '''Subclass for archive menu set.'''
    def __init__(self, gui, parent):
        super().__init__(gui, parent)
        self._label_1_text = 'Path to be archived'
        self._entry_1_text = '[enter path to be archived here]'
        self._entry_2_text = '[enter archive destination path here]'
        self._entry_3_text = '[copy and paste security key from here]'
        self._tickbox_1 = 'encrypt'
        self._tickbox_1_label = 'Encrypt'
        self._button_2 = 'archive'
        self._button_2_label = 'Archive'
        self._unarchive = False


class UnarchiveFrame(GridFrame):
    '''Subclass for unarchive menu set.'''
    def __init__(self, gui, parent):
        super().__init__(gui, parent)
        self._label_1_text = 'Path to be unarchived'
        self._entry_1_text = '[enter path to be unarchived here]'
        self._entry_2_text = '[enter unarchive destination path here]'
        self._entry_3_text = '[add path to key.txt or paste security key here]'
        self._button_2 = 'unarchive'
        self._button_2_label = 'Unarchive'
        self._unarchive = True
