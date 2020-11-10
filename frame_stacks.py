import frame_layout
import grid_frame
import mode_frame

class FrameStack:
    def __init__(self, parent, gui):
        self._parent = parent
        self._gui = gui
        self._layout = frame_layout.FrameLayout(parent=self._parent, gui=self._gui).make_layout()

        self._unarchive_interaction = grid_frame.UnarchiveFrame(parent=self._layout['interaction'], gui=self._gui).make_frame()
        self._archive_interaction = grid_frame.ArchiveFrame(parent=self._layout['interaction'], gui=self._gui).make_frame()
        
        self._unarchive_mode = mode_frame.UnarchiveMode(parent=self._layout['mode'], gui=self._gui).make_frame()
        self._archive_mode = mode_frame.ArchiveMode(parent=self._layout['mode'], gui=self._gui).make_frame()


    def show_archive(self):
        self._archive_mode.tkraise()
        self._archive_interaction.tkraise()
        print('Archive shown')


    def show_unarchive(self):
        self._unarchive_mode.tkraise()
        self._unarchive_interaction.tkraise()
        print('Unarchive shown')







        

