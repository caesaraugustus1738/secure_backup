class FrameLayout:
    '''Create a layout for the masterframe.

    Divide the masterframe into sections, into which 
    we place frames.'''
    def __init__(self, gui, parent):
        self._parent = parent
        self._gui = gui


    def _place_frame(self):
        frame = self._gui.subframe(parent=self._parent, width=self._gui._width, height=self._height, bgcol=self._bgcol)
        self._gui.frame_placer(frame=frame, x=self._x, y=self._y)
        return frame


    def make_layout(self):
        frames = {
        'interaction': Interaction(gui=self._gui, parent=self._parent)._place_frame(),
        'mode': Mode(gui=self._gui, parent=self._parent)._place_frame()
        }
        return frames


class Interaction(FrameLayout):
    def __init__(self, gui, parent):
        super().__init__(gui, parent)
        self._height = 190
        self._bgcol = 'yellow'
        self._y = 140
        self._x = 0


class Mode(FrameLayout):
    def __init__(self, gui, parent):
        super().__init__(gui, parent)
        self._height = 20
        self._bgcol = 'red'
        self._y = 115
        self._x = 25



