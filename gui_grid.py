class Grid:
    def __init__(self, gui, parent, layout_preview=False):
        self.gui = gui
        self._parent = parent
        self._layout_preview = layout_preview
    # def __init__(self, gui, parent, rowcol, cellcol, frame_name, layout_preview=False):
        # self._rowcol = rowcol
        # self._cellcol = cellcol
        # self._frame_name = frame_name
        # self._layout_preview = layout_preview


    def _design_naked_grid(self, parent, rowcol, cellcol):
            '''Design layout.'''
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


    def _naked_grid_placement(self, parent, layout_preview):
        '''Place a subframe in the GUI and place design grid in subframe.'''
        if layout_preview:
            col1 = 'green'
            col2 = 'red'
            col3 = 'blue'
        else:
            col1 = self.gui._bgcol
            col2 = self.gui._bgcol
            col3 = self.gui._bgcol

        grid_frame = self.gui.subframe(parent=parent, name='archive', width=800, height=190, bgcol=col1)
        self.gui.frame_placer(name=grid_frame, y=140)
        grid = self._design_naked_grid(parent=grid_frame, rowcol=col2, cellcol=col3)
        return grid


    def create_grid(self):
        naked_grid = self._naked_grid_placement(parent=self._parent, layout_preview=self._layout_preview)
        return naked_grid