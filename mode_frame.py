class ModeFrame:
    '''A frame to display program mode.

    The mode can either be Archive or Unarchive.'''
    def __init__(self, gui, parent):
        self._gui = gui
        self._parent = parent
        self._bgcol = '#71a3ae'
        self._mode_frame = self._gui.subframe(parent=self._parent, width=self._gui._width, height=20, bgcol=self._gui._bgcol)
        self._gui.frame_placer(self._mode_frame)


    def _make_label(self):
        return self._gui.label(parent=self._mode_frame, text=self._mode_name, bgcol=self._bgcol)


    def make_frame(self):
        self._make_label()
        return self._mode_frame


class ArchiveMode(ModeFrame):
    def __init__(self, gui, parent):
        super().__init__(gui, parent)
        self._mode_name = 'ARCHIVE'
        


class UnarchiveMode(ModeFrame):
    def __init__(self, gui, parent):
        super().__init__(gui, parent)
        self._mode_name = 'UNARCHIVE'
