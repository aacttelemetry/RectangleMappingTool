#!/usr/bin/env python

#region licensing

#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of Qt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
##     permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
#############################################################################

#This program is a modified version of the Scribble example.
#The notice above is kept as a result.

#endregion licensing

#region imports

#https://stackoverflow.com/questions/3615125/should-wildcard-import-be-avoided
#will change to qualified imports later
import sys
import webbrowser
import json
#QImageWriter is currently unused but it's used for saving images
#specifically, determining savable formats
from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
from fbs_runtime.application_context.PyQt5 import ApplicationContext
#------
from rectmap import Ui_MainWindow
#------
appctxt = ApplicationContext()
prefpath = appctxt.get_resource('preferences.json')
default_prefpath = appctxt.get_resource('default.json')
#endregion imports

'''todo (vaguely in this order):
        full settings implementation (logic)
        clear field button
        disable live overlap calculation in table if live table is disabled
        forced resize option (define custom canvas area, preload)
        resize on image load (includes settings logic: crop if big, stretch if small, default otherwise)
        resize logic post image load
        conversion table
        csv export
        custom ordering of csv with qlistwidget
        fstring export
        edit table values and update accordingly
        custom fields
        disable "change color" button if disabled
        warn that custom colors will be discarded if colors are enabled and then disabled
        update coordinate table upper-left labels on draw finish
        highlight row on draw finish
        click row (or row element) to show rectangle info
        click row (or row element) to highlight associated rectangle in some way
        right-click custom context menu
        toolbar (if needed)
        make undo work to not just delete rectangles, but undo other actions (or drop entirely)
        docstring standards conformity
        other pylint stuff
        qualify pyqt5 calls (not "from pyqt5.a import b, c, d" but "from pyqt5 import a, b, c, d" and use "a.aa" calls)
        unbreak the overlap system (which doesn't even work correctly in its current state)
        unbreak the draw system
'''

def get_prefs(source="user"):
    '''Get `data` from either preferences.json or default.json.
    `source` is a `str`, either `"user"` or `"default"`. The default is `"user"`.\n
    Using `"user"` returns the local preferences from preferences.json.
    Using `"default"` returns the default preferences from default.json.\n
    Returns a standard Python dict.'''
    if source == "user":
        pref_file = open(prefpath)
        data = json.load(pref_file)
        pref_file.close()
        return data
    elif source == "default":
        pref_file = open(default_prefpath)
        data = json.load(pref_file)
        pref_file.close()
        return data

def write_prefs(data):
    '''Write `data` to preferences.json with 4-space indents.
    `data` is a standard Python dict, likely the result of get_prefs().'''
    pref_file = open(prefpath, "w+") #write and truncate
    pref_file.write(json.dumps(data, indent=4))
    pref_file.close()

class ScribbleArea(QtWidgets.QWidget):
    '''The primary canvas on which the user draws rectangles.
    
    Note that ScribbleArea is referred to as "the canvas" across (most) docstrings and comments.
    This class may change to "CanvasArea" in the future to match.'''
    #these are custom signals that will not work if placed in __init__
    #they must be class variables/attributes declared here
    dataChanged = QtCore.pyqtSignal()
    posChanged = QtCore.pyqtSignal(int, int)
    sizeChanged = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        super(ScribbleArea, self).__init__(parent)

        #instance attributes...
        #self.setAttribute(QtCore.Qt.WA_StaticContents)
        self.scribbling = False
        self.image = QtGui.QImage()
        self.starting_point = QtCore.QPoint()
        self.end_point = QtCore.QPoint()
        #if colors will be implemented, then the structure will need to be modified
        #perhaps each element can be an array of [QtCore.QRect, (r,g,b)]
        self.rects = []
        self.loaded_image_path = None
        self.loaded_image_size = None

        #A QtWidgets.QWidget normally only receives mouse move events (mouseMoveEvent) when a mouse button is being pressed.
        #This sets it to always receive mouse events, regardless.
        self.setMouseTracking(True)

        self.settings = {
            "real_time_rects": True,
            "real_time_table": False,
            "crop_large_images": False,
            "stretch_small_images": False,
            "default_pen_width": 1,
            "default_pen_color": QtGui.QColor(0, 0, 255, 255)
        }
    def open_image(self, file_name):
        '''Sets the image at `file_name` to be the canvas background.
        It will then resize the canvas as needed and redraw rectangles.'''        
        self.loaded_image_path = file_name
        self.calculate_sizes()
        self.draw_all_rects()
        '''
        loadedImage = QtGui.QImage()
        if not loadedImage.load(file_name):
            return False

        #returns the maximum height and width given the two sizes
        new_size = loadedImage.size().expandedTo(self.size())
        #also see qsize.scale()
        self.resize_image(loadedImage, new_size)
        self.image = loadedImage
        self.update()
        return True
        '''

    def calculate_sizes(self):
        '''Determine what size the image should be, and if needed, resize the canvas.'''
        image = QtGui.QImage()
        image.load(self.loaded_image_path)

        image_size = image.size()
        canvas_size = self.size()

        if self.settings['crop_large_images'] and (image_size.width() > canvas_size.width() or image_size.height() > canvas_size.height()):
            self.loaded_image_size = image_size
        elif self.settings['stretch_small_images'] and (image_size.width() < canvas_size.width() or image_size.height() < canvas_size.height()):
            self.loaded_image_size = canvas_size
        else:
            #if there aren't any special settings, just set the canvas to be the size of the loaded image
            self.setFixedSize(image_size)
            self.sizeChanged.emit()
            self.loaded_image_size = image_size

    def save_image(self, file_name, file_format):
        '''Save the image as the specified file name in the specified format.'''
        visible_image = self.image
        self.resize_image(visible_image, self.size())

        if visible_image.save(file_name, file_format):
            return True
        else:
            return False

    def clear_image(self):
        '''Clear the canvas.
        In the future, this might be changed such that the opened image is drawn here.'''
        self.image.fill(QtGui.qRgb(255, 255, 255))
        self.update()

    def undo_last(self):
        '''Delete the most recent rectangle and redraw the canvas.'''
        self.clear_image()
        del self.rects[-1]
        self.draw_all_rects()
        #we also need to update the table here

    def mousePressEvent(self, event): # pylint: disable=invalid-name
        if event.button() == QtCore.Qt.LeftButton:
            self.starting_point = event.pos()
            self.scribbling = True

    def mouseMoveEvent(self, event): # pylint: disable=invalid-name
        self.posChanged.emit(event.pos().x(), event.pos().y())
        if (event.buttons() & QtCore.Qt.LeftButton) and self.scribbling:
            if self.settings['real_time_rects']:
                self.rects.append(QtCore.QRect(self.starting_point, event.pos()))
                self.draw_all_rects()
                if self.settings['real_time_table']:
                    self.dataChanged.emit() #this is used for "real-time" table updates
                del self.rects[-1]

    def mouseReleaseEvent(self, event): # pylint: disable=invalid-name
        if event.button() == QtCore.Qt.LeftButton and self.scribbling:
            self.end_point = event.pos()
            self.scribbling = False
            self.rects.append(QtCore.QRect(self.starting_point, self.end_point))
            #here we should also add this data to the table and update it
            self.dataChanged.emit() #this says that the rectangle data has changed
            self.draw_all_rects()

    def paintEvent(self, event): # pylint: disable=invalid-name
        painter = QtGui.QPainter(self)
        dirty_rect = event.rect()
        painter.drawImage(dirty_rect, self.image, dirty_rect)

    def resizeEvent(self, event): # pylint: disable=invalid-name
        if self.width() > self.image.width() or self.height() > self.image.height():
            new_width = max(self.width() + 128, self.image.width())
            new_height = max(self.height() + 128, self.image.height())
            self.resize_image(self.image, QtCore.QSize(new_width, new_height))
            self.update()

        super(ScribbleArea, self).resizeEvent(event)

    def draw_all_rects(self):
        '''Redraw all rectangles, iterating over each rectangle object in self.rects.'''
        ####
        '''
        is very inefficient because we don't just update the thing - no, we redraw *everything*
        a better way of doing this (i believe) is to use QGraphicsView since we don't need to store (and redraw) elements - it's done for us

        that said, i wasn't able to implement a proper rectangle deletion function properly without using this "array -> draw everything method" w/ QtGui.QPainter
        it's also a good deal easier to mesh with the table widget and export it into a format i understand

        so maybe one day i'll refactor this but for now this is good enough without absolutely shredding through resources
        '''
        self.clear_image()
        painter = QtGui.QPainter(self.image)
        painter.setPen(QtGui.QPen(self.settings['default_pen_color'], self.settings['default_pen_width'], QtCore.Qt.SolidLine,
                            QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
        #at this point we can redraw the image
        if self.loaded_image_path:
            bg_img = QtGui.QPixmap(self.loaded_image_path)
            #because of the way this is set up right now - to use a qrect of x size and place an image in it
            #we don't directly change the size of the image
            #so the instance attribute "loaded_image_size" is used instead
            painter.drawPixmap(QtCore.QRect(0, 0, self.loaded_image_size.width(), self.loaded_image_size.height()), bg_img)
        #drawing area has no border so use of frameGeometry should not be necessary?
        #painter.drawPixmap(QtCore.QRect(0,0,self.frameGeometry().width(),self.frameGeometry().height()),bg_img)
        for rect in self.rects:
            painter.drawRect(rect)
        self.update()

    def resize_image(self, image, new_size):
        if image.size() == new_size:
            return

        new_image = QtGui.QImage(new_size, QtGui.QImage.Format_RGB32)
        new_image.fill(QtGui.qRgb(255, 255, 255))
        painter = QtGui.QPainter(new_image)
        painter.drawImage(QtCore.QPoint(0, 0), image)
        self.image = new_image

    def print_(self):
        '''Handles canvas printing via QtPrintSupport.QPrintDialog.'''
        printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)

        print_dialog = QtPrintSupport.QPrintDialog(printer, self)
        if print_dialog.exec_() == QtPrintSupport.QPrintDialog.Accepted:
            painter = QtGui.QPainter(printer)
            rect = painter.viewport()
            size = self.image.size()
            size.scale(rect.size(), QtCore.Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.image.rect())
            painter.drawImage(0, 0, self.image)
            painter.end()

    #will probably just remove these later since we can just get drawing_area.settings['default_pen_color'] and so on if we ever need these values...
    #but until then, to differentiate the method and the value, it stays camelcase
    #might just keep them for clarity

    def penColor(self): # pylint: disable=invalid-name
        '''Returns the default current pen color.'''
        return self.settings['default_pen_color']

    def penWidth(self):  # pylint: disable=invalid-name
        '''Returns the current default pen width.'''
        return self.settings['default_pen_width']

    #probably same with these
    def set_pen_color(self, new_color):
        '''Set a new default pen color for the canvas.'''
        self.settings['default_pen_color'] = new_color

    def set_pen_width(self, new_width):
        '''Set a new default pen width for the canvas.'''
        self.settings['default_pen_width'] = new_width

class ApplicationWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    '''The main window. Instantiated once.'''
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("RectangleMappingTool")
        '''
        See https://stackoverflow.com/questions/35185113/configure-qtwidgets.qwidget-to-fill-parent-via-layouts.
        this appears to be the same issue in which this new widget is initialized to a 100px by 25px area
        so we create a new grid layout and place drawing_area into it
        this also affords us some flexibility if we ever want to hide drawing_area and place something different in container_left
        ---
        in order for a qscrollarea to work, the child (here self.scrollAreaWidgetContents) must have its own layout
        however, obviously a layout will auto-resize elements inside it
        so in order to account for this, we will manually set the minimum size of the newly-created drawing area 
        thus forcing it to be that size and give us the scroll bars
        the above is what i understood from a bunch of qt forum and stackoverflow posts
        although the docs say that a standard resize() will be respected
        i could not get it to do that
        '''
        #region Canvas initialization
        self.drawing_area = ScribbleArea(self.scrollAreaWidgetContents)
        self.container_left.setWidgetResizable(True)
        left_layout = QtWidgets.QVBoxLayout()
        left_layout.addWidget(self.drawing_area)
        left_layout.setAlignment(QtCore.Qt.AlignHCenter)
        self.scrollAreaWidgetContents.setLayout(left_layout)
        #we will need to set a signal later that resizes this widget based on a given background image
        #(or we just directly resize it after calling open())
        self.drawing_area.setFixedSize(400, 300)
        self.drawing_area.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor)) #make this responsive to a setting

        self.drawing_area.dataChanged.connect(self.update_table)
        self.drawing_area.posChanged.connect(self.update_coords)
        self.drawing_area.sizeChanged.connect(self.update_size_labels)
        #endregion

        #region Action signals and slots
        self.actionUndo.triggered.connect(self.undo)
        self.actionPen_Color.triggered.connect(self.change_pen_color)
        self.actionPen_Width.triggered.connect(self.change_pen_width)
        self.actionGitHub_Repository.triggered.connect(self.open_github)
        self.actionAbout.triggered.connect(self.about)
        self.actionOpen_image.triggered.connect(self.open)
        #endregion

        #region Tab 1: Coordinate Table

        #endregion

        #region Tab 2: Conversion

        #endregion

        #region Tab 3: Export Data

        #endregion

        #region Tab 4: Settings
        self.set_color_button.clicked.connect(self.change_pen_color)
        self.set_width_button.clicked.connect(self.change_pen_width)
        self.reset_settings_button.clicked.connect(self.reset_prefs)

        #im not sure if there's a better way to do this lol
        #pylint is fuming but my screen is wide enough so ill change it later
        self.active_redraw_checkbox.toggled.connect(lambda: self.change_preference("active_redraw", self.active_redraw_checkbox.isChecked()))
        self.active_table_checkbox.toggled.connect(lambda: self.change_preference("active_table", self.active_table_checkbox.isChecked()))
        self.active_overlaps_checkbox.toggled.connect(lambda: self.change_preference("active_overlaps", self.active_overlaps_checkbox.isChecked()))
        self.check_overlaps_checkbox.toggled.connect(lambda: self.change_preference("check_overlaps", self.check_overlaps_checkbox.isChecked()))
        self.crop_image_checkbox.toggled.connect(lambda: self.change_preference("crop_image", self.crop_image_checkbox.isChecked()))
        self.stretch_image_checkbox.toggled.connect(lambda: self.change_preference("stretch_image", self.stretch_image_checkbox.isChecked()))
        self.use_crosshair_checkbox.toggled.connect(lambda: self.change_preference("use_crosshair", self.use_crosshair_checkbox.isChecked()))
        self.show_color_checkbox.toggled.connect(lambda: self.change_preference("show_color", self.show_color_checkbox.isChecked()))

        self.set_canvas_size_button.clicked.connect(self.change_canvas_size)
        #endregion

        #region Default settings
        #Technically some of these don't need to be here and can instead be in drawing_area
        #but I found it easier to refer to these values here rather than doing it across classes
        self.settings = {
            "active_redraw":True,
            "active_table":False,
            "active_overlaps":False, #this setting is broken and needs to be fixed along with the overlap stuff
            "check_overlaps":True,
            "crop_image":False,
            "stretch_image":False,
            "use_crosshair":True,
            "show_color":False,
            "default_color":[0, 0, 255, 255],
            "default_width":1
        }
        #endregion

        #region All other initialization
        self.load_from_prefs()

        #this needs to be thrown into a function later, especially if color is a thing
        if not self.settings['check_overlaps']:
            self.table_widget.setColumnCount(4)
        #endregion
    def change_preference(self, preference, value):
        '''Change `preference` to `value` and perform additional actions as necessary.
        This includes updating preferences.json.\n
        Available preferences (all `bool`, except the last two):\n
        `active_redraw`: (Re)draw the current rectangle during mousedown.\n
        `active_table`: Update the table during mousedown.\n
        `active_overlaps`: Calculate overlapping rectangles and update the table during mousedown.\n
        `check_overlaps`: Calculate overlapping rectangles after a rectangle has been drawn.\n
        `crop_image`: Crop loaded images to fit canvas (instead of upsizing the canvas to fit).\n
        `stretch_image`: Stretch the image to fit canvas (instead of downsizing the canvas).\n
        `use_crosshair`: Use a crosshair cursor instead of the standard pointer cursor.\n
        `show_color`: Enable per-rectangle colors and add a "color" column to the table.\n
        `default_color (list)`: The default color used for drawing rectangles, represented by an rgba array.\n
        `default_width (int)`: The default width of rectangles in pixels.'''
        #https://stackoverflow.com/questions/8381735/how-to-toggle-a-value-in-python
        self.settings[preference] = value

        #rewrite as dict later?
        if preference == "active_redraw":
            self.drawing_area.settings['real_time_rects'] = value
        if preference == "active_table":
            self.drawing_area.settings['real_time_table'] = value
        if preference == "use_crosshair":
            if value:
                self.drawing_area.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
            else:
                self.drawing_area.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        if preference == "active_table" or preference == "check_overlaps":
            if self.settings['active_table'] and self.settings['check_overlaps']:
                self.active_overlaps_checkbox.setEnabled(True)
            else:
                self.active_overlaps_checkbox.setEnabled(False)
                self.active_overlaps_checkbox.setChecked(False)
                self.settings['active_overlaps'] = False
        if preference == "crop_image":
            self.drawing_area.settings['crop_large_images'] = value
        if preference == "stretch_image":
            self.drawing_area.settings['stretch_small_images'] = value

        write_prefs(self.settings)
    def load_from_prefs(self):
        '''Update self.settings based on values read from preferences.json.
        Remove if the __init__ call becomes the only call.
        Also updates UI elements as needed to reflect these.'''
        self.settings = get_prefs()

        #to unpack a list and expand it for arguments, place an asterisk before the list
        #see https://stackoverflow.com/questions/3941517/converting-list-to-args-when-calling-function
        self.drawing_area.settings['default_pen_color'] = QtGui.QColor(*self.settings['default_color'])
        self.drawing_area.settings['default_pen_width'] = self.settings['default_width']

        #table logic
        #make sure we don't destroy the user's custom fields if we do this
        if self.settings['check_overlaps'] and self.settings['show_color']:
            pass
        elif self.settings['check_overlaps']:
            pass
        elif self.settings['show_overlaps']:
            pass
        else:
            #maybe default column should be set to 3 in __init__?
            #or the first condition should just do nothing...
            pass

        #update checkboxes and stuff to match...
        self.active_redraw_checkbox.setChecked(self.settings['active_redraw'])
        self.active_table_checkbox.setChecked(self.settings['active_table'])
        self.active_overlaps_checkbox.setChecked(self.settings['active_overlaps'])
        self.check_overlaps_checkbox.setChecked(self.settings['check_overlaps'])
        self.crop_image_checkbox.setChecked(self.settings['crop_image'])
        self.stretch_image_checkbox.setChecked(self.settings['stretch_image'])
        self.use_crosshair_checkbox.setChecked(self.settings['use_crosshair'])
        self.show_color_checkbox.setChecked(self.settings['show_color'])

        #and finally update the canvas and table(s) as required
        self.update_all()
    def reset_prefs(self):
        '''Set the user preference file (preferences.json) to the defaults.
        This is achieved by getting the contents of defaults.json and writing it to the user's preference file.
        It will also call `load_from_prefs()` to deal with necessary post-processing.
        Also calls `reset_prompt()` to warn the user of a potentially destructive action.'''
        if self.reset_prompt():
            default_prefs = get_prefs("default")
            write_prefs(default_prefs)
            self.load_from_prefs()
    def update_table(self):
        '''Rebuild the entire table based on drawing_area.rects.'''
        #i hate this
        #but i want to finish other functionality before turning to efficiency changes so here we are

        #we rebuild the *entire* table on each call
        self.table_widget.setRowCount(0)

        for row_number in range(0, len(self.drawing_area.rects)):
            coords = self.drawing_area.rects[row_number].getCoords()
            #print("adding row %s" % str(int(row_number)+1))
            self.table_widget.setRowCount(row_number+1)
            self.table_widget.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(coords[0])))
            self.table_widget.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(coords[1])))
            self.table_widget.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str(coords[2])))
            self.table_widget.setItem(row_number, 3, QtWidgets.QTableWidgetItem(str(coords[3]))) #row, column, QtWidgets.QTableWidgetItem; zero-indexed
            self.table_widget.setItem(row_number, 4, QtWidgets.QTableWidgetItem(""))
            self.table_widget.setItem(row_number, 5, QtWidgets.QTableWidgetItem(""))#we can add the color property later

        #we can perform brute-force checking with QtCore.QRect.intersects(<QtCore.QRect2>)
        #the algorithm below checks each possible overlap, one-by-one (but does not check the same two rectangles for overlap twice)
        #add an "overlaps with" column if this is enabled
        if self.settings['check_overlaps']:
            rectangles = self.drawing_area.rects
            #we clear the entire column on each full overlap check
            #while implementing an array for each cell would be much better for various calculations and operations
            #maybe later
            for row_number in range(0, len(rectangles)):
                self.table_widget.setItem(row_number, 4, QtWidgets.QTableWidgetItem(""))
            for rect1_index in range(0, len(rectangles)):
                for rect2_index in range(rect1_index+1, len(rectangles)):
                    intersects = rectangles[rect1_index].intersects(rectangles[rect2_index])
                    #print(rectangles[rect1_index].intersects(rectangles[rect2_index]))
                    #print(f"Rectangle {rect1_index} overlaps with {rect2_index}?"+str(intersects))
                    current = self.table_widget.item(rect1_index, 4).text()
                    current2 = self.table_widget.item(rect2_index, 4).text()
                    if intersects:
                        if current == "":
                            self.table_widget.setItem(rect1_index, 4,
                                                      QtWidgets.QTableWidgetItem(str(rect2_index+1)))
                        else:
                            self.table_widget.setItem(rect1_index, 4,
                                                      QtWidgets.QTableWidgetItem(current+","+str(rect2_index+1)))
                        if current2 == "":
                            self.table_widget.setItem(rect2_index, 4,
                                                      QtWidgets.QTableWidgetItem(str(rect1_index+1)))
                        else:
                            self.table_widget.setItem(rect2_index, 4,
                                                      QtWidgets.QTableWidgetItem(current+","+str(rect1_index+1)))
            #print("---")
    def update_all(self):
        '''Shorthand call to redraw all rectangles and reprocess the coordinate table.\n
        Might need to be updated with the conversion table in the future.
        Since the color field is planned to say "Default" when using to the default pen color\n
        (as opposed to explicitly defining the rgba value), these "default-colored" rectangles
        should immediately reflect changes to the default pen color.'''
        self.drawing_area.draw_all_rects()
        self.update_table()
    def change_canvas_size(self):
        '''Change the size of the canvas to that specified in `canvas_width_edit` and
        `canvas_height_edit`. This is influenced by the `crop_image` and `stretch_image` settings.
        Note that the image and canvas maniuplation are not actually done here - they are done
        in ScribbleArea itself.'''
        new_width = int(self.canvas_width_edit.text())
        new_height = int(self.canvas_height_edit.text())
        new_size = QtCore.QSize(new_width, new_height)
        self.drawing_area.setFixedSize(new_size)
    def update_size_labels(self):
        self.canvas_width_edit.setText(str(self.drawing_area.size().width()))
        self.canvas_height_edit.setText(str(self.drawing_area.size().height()))
    def remove_last(self):
        '''Remove the most recently added row.'''
        self.table_widget.removeRow(self.table_widget.rowCount()-1)
    def update_coords(self, x_pos, y_pos):
        '''Update the coordinate labels below the canvas.'''
        self.coord_label.setText("x:"+str(x_pos)+" y:"+str(y_pos))
    #region Actions
    def open(self):
        '''Handles opening an image.
        This includes the creation of a QtWidgets.QFileDialog and determining if an image is valid.
        It will also ask the user if they want to clear the canvas on image load.'''
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File",
                                                   QtCore.QDir.currentPath())
        if file_name:
            if not QtGui.QImage().load(file_name):
                QtWidgets.QMessageBox.critical(self, "Couldn't load image",
                                     "This image appears to be an unsupported filetype and could not be loaded.",
                                     QtWidgets.QMessageBox.Ok)
                self.open()
            else:
                if self.drawing_area.rects:
                    response = QtWidgets.QMessageBox.question(self, "Reset drawing area?",
                                                    'Do you want to clear drawn rectangles and start from scratch?',
                                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                    if response == QtWidgets.QMessageBox.Yes:
                        self.drawing_area.rects = []
                        self.update_table()
                self.drawing_area.open_image(file_name)
                #at this point, we should execute the resize logic
    def undo(self):
        '''Tell the canvas to remove the most recent rectangle.
        Also updates the coordinate table.'''
        self.drawing_area.undo_last()
        #delete most recent table entry on undo
        self.table_widget.removeRow(self.table_widget.rowCount()-1)
    def change_pen_color(self):
        '''Open a dialog allowing the user to change the default rectangle color.'''
        new_color = QtWidgets.QColorDialog.getColor(self.drawing_area.penColor())
        if new_color.isValid():
            self.drawing_area.set_pen_color(new_color)
            self.change_preference('default_color', list(new_color.getRgb()))
            self.update_all()
    def change_pen_width(self):
        '''Open a dialog allowing the user to change the default rectangle width.'''
        new_width, response = QtWidgets.QInputDialog.getInt(self, "Set New Pen Width",
                                                  "Select pen width:",
                                                  self.drawing_area.penWidth(), 1, 50, 1)
        if response:
            self.drawing_area.set_pen_width(new_width)
            self.change_preference('default_width', new_width)
            self.update_all()
    def about(self):
        '''Opens this program's about dialog.'''
        QtWidgets.QMessageBox.about(self, "About RectangleMappingTool",
                '<p>RectangleMappingTool is a program designed for the '
                '<a href="https://github.com/aacttelemetry">AACT Telemetry project</a>, '
                'built with PyQt5 and packaged through fbs.</p>'
                '<p>Its primary purpose is to make creating rectangular bounding regions '
                'based on an image easier.</p>'
                '<p>You can view the source of this program and additional information '
                '<a href="https://github.com/aacttelemetry/RectangleMappingTool">here</a>.</p>')
    def open_github(self):
        '''Opens this program's repo in the user's default browser.'''
        webbrowser.open("https://github.com/aacttelemetry/RectangleMappingTool")
    #endregion
    def reset_prompt(self):
        '''Warns the user that they are about to reset the program's settings to their defaults.
        Returns `True` if "Reset" is selected.
        Returns `False` otherwise.'''
        ret = QtWidgets.QMessageBox.warning(self, "Reset preferences?",
                                          'Are you sure you want to reset your preferences to the default preferences?',
                                          QtWidgets.QMessageBox.Reset | QtWidgets.QMessageBox.Cancel)
        if ret == QtWidgets.QMessageBox.Reset:
            return True
        elif ret == QtWidgets.QMessageBox.Cancel:
            return False
    def close_prompt(self):
        '''Warns the user if the canvas has been modified.
        This is determined by the presence of any rectangles.
        Returns True if the user wants to close the program anyways or no rectangles have been drawn.
        Returns False otherwise.'''
        #because "saving" could mean anything from exporting the coords to saving the image
        #there is no handling of saving here
        #a modified drawing_area is one that has any rectangles whatsoever

        #if this ends up being just a pre-close prompt, change the language accordingly
        if self.drawing_area.rects:
            ret = QtWidgets.QMessageBox.information(self, "Close?",
                                          'Ensure that you have exported or saved any data '
                                          'you were working with.\n'
                                          'Click "Close" to continue, or "Cancel" to return.',
                                          QtWidgets.QMessageBox.Close | QtWidgets.QMessageBox.Cancel)
            if ret == QtWidgets.QMessageBox.Close:
                return True
            elif ret == QtWidgets.QMessageBox.Cancel:
                return False
        else:
            return True
    def closeEvent(self, event): # pylint: disable=invalid-name
        '''Reimplementation of the close event to warn the user on program close.
        See close_prompt().'''
        if self.close_prompt():
            event.accept()
        else:
            event.ignore()
'''
    def saveFile(self, file_format):
        initialPath = QtCore.QDir.currentPath() + '/untitled.' + file_format

        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save As", initialPath,
                "%s Files (*.%s);;All Files (*)" % (file_format.upper(), file_format))
        if file_name:
            return self.scribbleArea.save_image(file_name, file_format)

        return False
    '''

class AppContext(ApplicationContext):
    '''fbs requires that one instance of ApplicationContext be instantiated.
    This represents the app window.'''
    def run(self):
        application_window = ApplicationWindow()
        application_window.show()
        return self.app.exec_()

if __name__ == '__main__':
    appctxt = AppContext()
    exit_code = appctxt.run()
    sys.exit(exit_code)
