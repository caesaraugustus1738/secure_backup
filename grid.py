class Grid:
    '''Create a frame containing a grid. 

    Buttons/labels/entry fields can be placed on top of this grid.'''
    def __init__(self, gui, parent):
        self.gui = gui
        self._parent = parent


    def _naked_grid(self, parent):
            '''Design grid for a frame.

            To preview layout, change rowcol/cellcol.'''
            rowcol=self.gui._bgcol
            cellcol=self.gui._bgcol

            rows = self.gui.rows(parent=parent, height=20, num=6, vgap=26, colour=rowcol)

            col1_x=25
            col2_x=180
            col3_x=630

            grid = {
            'row1_col1': self.gui.cell_in_row(parent=rows['row1'], start_point=col1_x, width=150, colour=cellcol),
            'row1_col2': self.gui.cell_in_row(parent=rows['row1'], start_point=col2_x, width=600, colour=cellcol),
            'row2_col1': self.gui.cell_in_row(parent=rows['row2'], start_point=col1_x, width=150, colour=cellcol),
            'row2_col2': self.gui.cell_in_row(parent=rows['row2'], start_point=col2_x, width=600, colour=cellcol),
            'row3_col1': self.gui.cell_in_row(parent=rows['row3'], start_point=col2_x, width=600, colour=cellcol),
            'row4_col1': self.gui.cell_in_row(parent=rows['row4'], start_point=col2_x, width=150, colour=cellcol),
            'row5_col1': self.gui.cell_in_row(parent=rows['row5'], start_point=col3_x, width=150, colour=cellcol),
            'row6_col1': self.gui.cell_in_row(parent=rows['row6'], start_point=col3_x, width=150, colour=cellcol)
            }
            return grid


    def _grid_frame(self, parent, bgcol):
        '''Make a frame for the grid.'''
        return self.gui.subframe(parent=parent, width=800, height=190, bgcol=bgcol)


    def create_grid(self):
        '''Create and place a frame. Draw naked grid within frame.'''
        frame = self._grid_frame(parent=self._parent, bgcol=self.gui._bgcol)
        self.gui.frame_placer(frame=frame)
        grid = self._naked_grid(parent=frame)
        return {'grid': grid, 'frame': frame}


















