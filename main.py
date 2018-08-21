# John Moffitt 2018

# simple cross platform app that allows user to create a maze with a checkbox grid
# solves fastest path from bottom left to top right, without diagonals
# checked boxes are walls, which can be broken in 7 steps
# walking onto an unchecked path or broken wall takes 1 step
# path taken is shown by which checkboxes are enabled after it's done solving
# number of steps taken is shown next to the button

# runs on python 3.6 and requires pipenv
# run 'pipenv install' and then 'pipenv run python main.py' to run it
# or to run it without pipenv, install wxpython and run main.py directly

# main.py is main script that creates GUI
# solver.py is background thread that solves the fastest path
# wxgui.py is automatically generated code from wxFormBuilder (RAD GUI tool for wxWidgets), which contains all GUI elements
# solving is done in a background thread to prevent blocking the GUI which would make everything freeze

import wx
import wx.lib.pubsub

import wxgui
import solverthread

# class for the frame of the GUI


class GUIFrame(wxgui.MainFrame):
    def __init__(self):
        super(GUIFrame, self).__init__(None)
        # solver_thread is the background thread if it's running or None if not
        self.solver_thread = None
        # subscribe to the solved event so background solver thread can notify main GUI thread through wx's pub/sub message system
        wx.lib.pubsub.pub.subscribe(self.solver_done, 'solved')

    # event when solve button is clicked
    def solve_click(self, event):
        # disable solve button to avoid clicking it multiple times
        self.button_solve.Disable()
        if not self.solver_thread:
            # check the label on the button to see if we should reset the checkboxes or start the solver
            if self.button_solve.GetLabel() == 'Solve':
                self.static_text_status.SetLabel('Solving...')
                # grid_list will be the final list of lists representing the array of walls/paths
                grid_list = []
                # inner_grid_list is a single row
                inner_grid_list = []
                grid_width = 5
                checkbox_count = 0
                # iterate over all the checkboxes in the GUI panel
                for panel_child in self.panel_main.GetChildren():
                    if isinstance(panel_child, wx.CheckBox):
                        # disable the checkbox
                        panel_child.Disable()
                        checkbox_count += 1
                        # see if we've reached the end of the current row
                        if checkbox_count > grid_width:
                            # start the next row by appending the current row the grid list and then creating a new inner list with the value of the current checkbox
                            checkbox_count = 1
                            grid_list.append(inner_grid_list)
                            inner_grid_list = [panel_child.IsChecked()]
                        else:
                            # otherwise we're in the middle of populating a row, just append the checked value
                            inner_grid_list.append(panel_child.IsChecked())
                # append the last row because it won't be done inside the loop
                grid_list.append(inner_grid_list)
                # initialize the background thread, passing the grid of bools
                self.solver_thread = solverthread.SolverThread(grid_list)
                # start the thread
                self.solver_thread.start()
            elif self.button_solve.GetLabel() == 'Reset':
                # iterate on checkboxes to enable them all, except start and end checkboxes which are always disabled
                for panel_child in self.panel_main.GetChildren():
                    if isinstance(panel_child, wx.CheckBox) and panel_child not in (self.check_box_end, self.check_box_start):
                        panel_child.Enable()
                # reset the rest of the GUI elements as well
                self.static_text_status.SetLabel('Ready')
                self.button_solve.SetLabel('Solve')
                self.button_solve.Enable()
        event.Skip()

    # event when solver is finished, passes the path taken and number of steps
    def solver_done(self, path, steps):
        # block until thread is stopped before removing the reference to it, because I'm afraid of zombies
        self.solver_thread.join()
        self.solver_thread = None
        # show number of steps taken in label next to button
        self.static_text_status.SetLabel('Steps: {}'.format(steps))
        # enable the checkboxes on path to indicate the path taken
        checkbox_x_index = 0
        checkbox_y_index = 0
        grid_width = 5
        for panel_child in self.panel_main.GetChildren():
            if isinstance(panel_child, wx.CheckBox):
                # check if we're beyond the current row of checkboxes
                if checkbox_x_index >= grid_width:
                    # reset x index and add 1 to y index to go to next row
                    checkbox_x_index = 0
                    checkbox_y_index += 1
                # check if this checkboxes location is in the solution set
                if (checkbox_y_index, checkbox_x_index) in path:
                    # make sure it's not the start or end which are always disabled
                    if panel_child not in (self.check_box_end, self.check_box_start):
                        panel_child.Enable()
                checkbox_x_index += 1
        self.button_solve.SetLabel('Reset')
        self.button_solve.Enable()

    # event when app is closing (x pressed), kill solver thread early if it's running
    def app_close(self, event):
        if self.solver_thread:
            # disable GUI and turn on busy cursor if mouse is over it in case background thread is slow to stop
            wx.BeginBusyCursor()
            self.solver_thread.cancel()
            # blocks until it stops
            self.solver_thread.join()
            self.solver_thread = None
        # allows event to propagate to higher level handlers which actually close the app and stop the event loop
        event.Skip()


def main():
    # create app and frame
    app = wx.App()
    frm = GUIFrame()
    app.SetTopWindow(frm)
    frm.Show()
    # run blocking GUI event loop
    app.MainLoop()


if __name__ == '__main__':
    main()
