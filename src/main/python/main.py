#!/usr/bin/env python

#region licensing

#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
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

#ScribbleArea is a modified version of the Scribble example.
#The notice above is kept as a result.

#endregion licensing

#region imports
#i *would* convert these to asterisks but then pylint makes my document look like a bloodbath
#well the document is a bloodbath as is but i'll fix the camelcase vs snakecase later
#and everything else...

#https://stackoverflow.com/questions/3615125/should-wildcard-import-be-avoided
#perhaps this should be changed later
import sys
import webbrowser
import PyQt5
from PyQt5.QtCore import QDir, QPoint, QRect, QSize, Qt, pyqtSignal
from PyQt5.QtGui import QImage, QImageWriter, QPainter, QPen, qRgb, QPixmap, QCursor
from PyQt5.QtWidgets import (QColorDialog, QFileDialog,
                             QInputDialog, QMainWindow, QMessageBox, QWidget,
                             QTableWidgetItem, QVBoxLayout)
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from fbs_runtime.application_context.PyQt5 import ApplicationContext
#------
from rectmap import Ui_MainWindow
#------
appctxt = ApplicationContext()
#no need for this since we can load images now
#consider deleting rovercourse.png and associated references to below in the future
#imgpath = appctxt.get_resource('rovercourse.png')#gets relative/absolute path through fbs
#endregion imports

class ScribbleArea(QWidget):
    '''The primary canvas on which the user draws rectangles.
    
    Note that ScribbleArea is referred to as "the canvas" across (most) docstrings and comments.
    This class may change to "CanvasArea" in the future to match.'''
    #these are custom signals that will not work if placed in __init__
    #they must be class variables/attributes declared here
    dataChanged = pyqtSignal()
    posChanged = pyqtSignal(int, int)
    def __init__(self, parent=None):
        super(ScribbleArea, self).__init__(parent)

        #instance attributes...
        #self.setAttribute(Qt.WA_StaticContents)
        self.modified = False
        self.scribbling = False
        self.pen_width = 1
        self.pen_color = Qt.blue
        self.image = QImage()
        self.starting_point = QPoint()
        self.end_point = QPoint()
        #if colors will be implemented, then the structure will need to be modified
        #perhaps each element can be an array of [QRect, (r,g,b)]
        self.rects = []
        self.loaded_image = None

        #A QWidget normally only receives mouse move events (mouseMoveEvent) when a mouse button is being pressed.
        #This sets it to always receive mouse events, regardless.
        self.setMouseTracking(True)
        self.real_time_rects = True
        self.real_time_table = False
    def open_image(self, file_name):
        '''Open an external image and set it as the canvas background.
        This should also calculate any necessary canvas/image size changes.'''
        new_image = QImage()
        print(new_image.size())
        
        self.loaded_image = file_name
        self.draw_all_rects()
        '''
        loadedImage = QImage()
        if not loadedImage.load(file_name):
            return False

        #returns the maximum height and width given the two sizes
        new_size = loadedImage.size().expandedTo(self.size())
        #also see qsize.scale()
        self.resize_image(loadedImage, new_size)
        self.image = loadedImage
        self.modified = False
        self.update()
        return True
        '''

    def save_image(self, file_name, file_format):
        '''Save the image as the specified file name in the specified format.'''
        visible_image = self.image
        self.resize_image(visible_image, self.size())

        if visible_image.save(file_name, file_format):
            self.modified = False
            return True
        else:
            return False

    def clear_image(self):
        '''Clear the canvas.
        In the future, this might be changed such that the opened image is drawn here.'''
        self.image.fill(qRgb(255, 255, 255))
        self.modified = True
        self.update()

    def undo_last(self):
        '''Delete the most recent rectangle and redraw the canvas.'''
        self.clear_image()
        del self.rects[-1]
        self.draw_all_rects()
        #we also need to update the table here

    def mousePressEvent(self, event): # pylint: disable=invalid-name
        if event.button() == Qt.LeftButton:
            self.starting_point = event.pos()
            self.scribbling = True

    def mouseMoveEvent(self, event): # pylint: disable=invalid-name
        self.posChanged.emit(event.pos().x(), event.pos().y())
        if (event.buttons() & Qt.LeftButton) and self.scribbling:
            if self.real_time_rects:
                self.rects.append(QRect(self.starting_point, event.pos()))
                self.draw_all_rects()
                if self.real_time_table:
                    self.dataChanged.emit() #this is used for "real-time" table updates
                del self.rects[-1]

    def mouseReleaseEvent(self, event): # pylint: disable=invalid-name
        if event.button() == Qt.LeftButton and self.scribbling:
            self.end_point = event.pos()
            self.scribbling = False
            self.rects.append(QRect(self.starting_point, self.end_point))
            #here we should also add this data to the table and update it
            self.dataChanged.emit() #this says that the rectangle data has changed
            self.draw_all_rects()

    def paintEvent(self, event): # pylint: disable=invalid-name
        painter = QPainter(self)
        dirty_rect = event.rect()
        painter.drawImage(dirty_rect, self.image, dirty_rect)

    def resizeEvent(self, event): # pylint: disable=invalid-name
        if self.width() > self.image.width() or self.height() > self.image.height():
            new_width = max(self.width() + 128, self.image.width())
            new_height = max(self.height() + 128, self.image.height())
            self.resize_image(self.image, QSize(new_width, new_height))
            self.update()

        super(ScribbleArea, self).resizeEvent(event)

    def draw_all_rects(self):
        '''Redraw all rectangles, iterating over each rectangle object in self.rects.'''
        ####
        '''
        is very inefficient because we don't just update the thing - no, we redraw *everything*
        a better way of doing this (i believe) is to use QGraphicsView since we don't need to store (and redraw) elements - it's done for us

        that said, i wasn't able to implement a proper rectangle deletion function properly without using this "array -> draw everything method" w/ QPainter
        it's also a good deal easier to mesh with the table widget and export it into a format i understand

        so maybe one day i'll refactor this but for now this is good enough without absolutely shredding through resources
        '''
        self.clear_image()
        painter = QPainter(self.image)
        painter.setPen(QPen(self.pen_color, self.pen_width, Qt.SolidLine,
                            Qt.RoundCap, Qt.RoundJoin))
        #at this point we can redraw the image
        bg_img = QPixmap(self.loaded_image)
        #print(bg_img.height())
        # print(bg_img.width())
        #bg_img_width = bg_img.width()
        #bg_img_height = bg_img.height()
        if self.loaded_image:
            if bg_img.width() > self.frameGeometry().width(): #the image isn't drawing because you need to fix this
                final_height = (bg_img.height()*self.frameGeometry().width())/bg_img.width()
                print(final_height)
                final_width = self.frameGeometry().width()
                painter.drawPixmap(QRect(0, 0, final_width, final_height), bg_img)
            else:
                painter.drawPixmap(QRect(0, 0, bg_img.width(), bg_img.height()), bg_img)
            #add two override fields on the conversion tab to say "if your bottom-right handle is not located at the bottom-right of the image" on tooltip
        #painter.drawPixmap(QRect(0,0,self.frameGeometry().width(),self.frameGeometry().height()),QPixmap(imgpath))
        for rect in self.rects:
            painter.drawRect(rect)
        self.modified = True
        self.update()

    def resize_image(self, image, new_size):
        if image.size() == new_size:
            return

        new_image = QImage(new_size, QImage.Format_RGB32)
        new_image.fill(qRgb(255, 255, 255))
        painter = QPainter(new_image)
        painter.drawImage(QPoint(0, 0), image)
        self.image = new_image

    def print_(self):
        '''Handles canvas printing via QPrintDialog.'''
        printer = QPrinter(QPrinter.HighResolution)

        print_dialog = QPrintDialog(printer, self)
        if print_dialog.exec_() == QPrintDialog.Accepted:
            painter = QPainter(printer)
            rect = painter.viewport()
            size = self.image.size()
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.image.rect())
            painter.drawImage(0, 0, self.image)
            painter.end()

    #will probably just remove these later since we can just get drawing_area.pen_color and so on if we ever need these values...
    #but until then, to differentiate the method and the value, it stays camelcase
    def isModified(self): # pylint: disable=invalid-name
        '''Returns whether or not the canvas has been modified.
        Unnecessary - will be removed later.'''
        return self.modified

    def penColor(self): # pylint: disable=invalid-name
        '''Returns the default current pen color.'''
        return self.pen_color

    def penWidth(self):  # pylint: disable=invalid-name
        '''Returns the current default pen width.'''
        return self.pen_width

    #probably same with these
    def set_pen_color(self, new_color):
        '''Set a new default pen color for the canvas.'''
        self.pen_color = new_color

    def set_pen_width(self, new_width):
        '''Set a new default pen width for the canvas.'''
        self.pen_width = new_width

class ApplicationWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        PyQt5.QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("RectangleMappingTool")
        '''
        See https://stackoverflow.com/questions/35185113/configure-qwidget-to-fill-parent-via-layouts.
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
        self.drawing_area = ScribbleArea(self.scrollAreaWidgetContents)
        self.container_left.setWidgetResizable(True)
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.drawing_area)
        left_layout.setAlignment(Qt.AlignHCenter)
        self.scrollAreaWidgetContents.setLayout(left_layout)
        #we will need to set a signal later that resizes this widget based on a given background image
        #(or we just directly resize it after calling open())
        self.drawing_area.setFixedSize(400, 300) 
        self.drawing_area.setCursor(QCursor(Qt.CrossCursor)) #make this responsive to a setting

        self.drawing_area.dataChanged.connect(self.updatetable)
        self.drawing_area.posChanged.connect(self.update_coords)

        self.actionUndo.triggered.connect(self.undo)
        self.actionPen_Color.triggered.connect(self.change_pen_color)
        self.actionPen_Width.triggered.connect(self.change_pen_width)
        self.actionGitHub_Repository.triggered.connect(self.open_github)
        self.actionAbout.triggered.connect(self.about)
        self.actionOpen_image.triggered.connect(self.open)

        self.set_color_button.clicked.connect(self.change_pen_color)
        self.set_width_button.clicked.connect(self.change_pen_width)

        #im not sure if there's a better way to do this lol
        self.active_redraw_checkbox.toggled.connect(lambda: self.change_prefs("active_redraw", self.active_redraw_checkbox.isChecked()))
        self.active_table_checkbox.toggled.connect(lambda: self.change_prefs("active_table", self.active_table_checkbox.isChecked()))
        self.active_overlaps_checkbox.toggled.connect(lambda: self.change_prefs("active_overlaps", self.active_redraw_checkbox.isChecked()))
        self.check_overlaps_checkbox.toggled.connect(lambda: self.change_prefs("check_overlaps", self.active_redraw_checkbox.isChecked()))
        self.crop_image_checkbox.toggled.connect(lambda: self.change_prefs("crop_image", self.active_redraw_checkbox.isChecked()))
        self.stretch_image_checkbox.toggled.connect(lambda: self.change_prefs("stretch_image", self.active_redraw_checkbox.isChecked()))
        self.use_crosshair_checkbox.toggled.connect(lambda: self.change_prefs("use_crosshair", self.active_redraw_checkbox.isChecked()))
        self.show_color_checkbox.toggled.connect(lambda: self.change_prefs("show_color", self.active_redraw_checkbox.isChecked()))

        self.settings = {
            "active_redraw":True,
            "active_table":False,
            "active_overlaps":False,
            "check_overlaps":True,
            "crop_image":False,
            "stretch_image":False,
            "use_crosshair":True,
            "show_color":False
        }
        
        self.check_overlapping = False

        #this needs to be thrown into a function later
        if not self.check_overlapping:
            self.table_widget.setColumnCount(4)

        #self.resize(500, 500)
    def change_prefs(self, preference, value):
        '''Change <preference> to <value> and perform additional actions as necessary.
        
        Available preferences (all bool):
        active_redraw: (Re)draw the current rectangle during mousedown.
        active_table: Update the table during mousedown.
        active_overlaps: Calculate overlapping rectangles and update the table during mousedown.
        check_overlaps: Calculate overlapping rectangles after a rectangle has been drawn.
        crop_image: Crop loaded images to fit canvas (instead of upsizing the canvas to fit).
        stretch_image: Stretch the image to fit canvas (instead of downsizing the canvas).
        use_crosshair: Use a crosshair cursor instead of the standard pointer cursor.
        show_color: Enable per-rectangle colors and add a "color" column to the table.'''
        #https://stackoverflow.com/questions/8381735/how-to-toggle-a-value-in-python
        print(preference, value)
    def updatetable(self):
        '''Rebuild the entire table based on drawing_area.rects.'''
        #i hate this
        #but i want to finish other functionality before turning to efficiency changes so here we are

        #we rebuild the *entire* table on each call
        self.table_widget.setRowCount(0)

        for row_number in range(0, len(self.drawing_area.rects)):
            coords = self.drawing_area.rects[row_number].getCoords()
            #print("adding row %s" % str(int(row_number)+1))
            self.table_widget.setRowCount(row_number+1)
            self.table_widget.setItem(row_number, 0, QTableWidgetItem(str(coords[0])))
            self.table_widget.setItem(row_number, 1, QTableWidgetItem(str(coords[1])))
            self.table_widget.setItem(row_number, 2, QTableWidgetItem(str(coords[2])))
            self.table_widget.setItem(row_number, 3, QTableWidgetItem(str(coords[3]))) #row, column, QTableWidgetItem; zero-indexed
            self.table_widget.setItem(row_number, 4, QTableWidgetItem(""))
            self.table_widget.setItem(row_number, 5, QTableWidgetItem(""))#we can add the color property later

        #we can perform brute-force checking with QRect.intersects(<QRect2>)
        #the algorithm below checks each possible overlap, one-by-one (but does not check the same two rectangles for overlap twice)
        #add an "overlaps with" column if this is enabled
        if self.check_overlapping:
            rectangles = self.drawing_area.rects
            #we clear the entire column on each full overlap check
            #while implementing an array for each cell would be much better for various calculations and operations
            #maybe later
            for row_number in range(0, len(rectangles)):
                self.table_widget.setItem(row_number, 4, QTableWidgetItem(""))
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
                                                      QTableWidgetItem(str(rect2_index+1)))
                        else:
                            self.table_widget.setItem(rect1_index, 4,
                                                      QTableWidgetItem(current+","+str(rect2_index+1)))
                        if current2 == "":
                            self.table_widget.setItem(rect2_index, 4,
                                                      QTableWidgetItem(str(rect1_index+1)))
                        else:
                            self.table_widget.setItem(rect2_index, 4,
                                                      QTableWidgetItem(current+","+str(rect1_index+1)))
            #print("---")
    def remove_last(self):
        '''Remove the most recently added row.'''
        self.table_widget.removeRow(self.table_widget.rowCount()-1)
    def update_coords(self, x_pos, y_pos):
        '''Update the coordinate labels below the canvas.'''
        self.coord_label.setText("x:"+str(x_pos)+" y:"+str(y_pos))
    #region Actions
    def open(self):
        '''Handles opening an image.
        This includes the creation of a QFileDialog and determining if an image is valid.
        It will also ask the user if they want to clear the canvas on image load.'''
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File",
                                                   QDir.currentPath())
        if file_name:
            if not QImage().load(file_name):
                QMessageBox.critical(self, "Couldn't load image",
                                     "This image appears to be an unsupported filetype and could not be loaded.",
                                     QMessageBox.Ok)
                self.open()
            else:
                if self.drawing_area.rects:
                    response = QMessageBox.question(self, "Reset drawing area?",
                                                    'Do you want to clear drawn rectangles and start from scratch?',
                                                    QMessageBox.Yes | QMessageBox.No)
                    if response == QMessageBox.Yes:
                        self.drawing_area.rects = []
                        self.updatetable()
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
        new_color = QColorDialog.getColor(self.drawing_area.penColor())
        print(new_color.getRgb()) #returns a standard rgba tuple
        print(new_color.getRgb()[2])
        if new_color.isValid():
            self.drawing_area.set_pen_color(new_color)
    def change_pen_width(self):
        '''Open a dialog allowing the user to change the default rectangle width.'''
        new_width, response = QInputDialog.getInt(self, "Set New Pen Width",
                                                  "Select pen width:", 
                                                  self.drawing_area.penWidth(), 1, 50, 1)
        if response:
            self.drawing_area.set_pen_width(new_width)
    def about(self):
        '''Opens this program's about dialog.'''
        QMessageBox.about(self, "About RectangleMappingTool",
                '<p>RectangleMappingTool is a program designed for the'
                '<a href="https://github.com/aacttelemetry">AACT Telemetry project</a>,'
                'built with PyQt5 and packaged through fbs.</p>'
                '<p>Its primary purpose is to make creating rectangular bounding regions'
                'based on an image easier.</p>'
                '<p>You can view the source of this program and additional information'
                '<a href="https://github.com/aacttelemetry/RectangleMappingTool">here</a>.</p>')
    def open_github(self):
        '''Opens this program's repo in the user's default browser.'''
        webbrowser.open("https://github.com/aacttelemetry/RectangleMappingTool")
    #endregion
    def close_prompt(self):
        '''Warns the user if the canvas has been modified.
        This is determined by the presence of any rectangles.
        Returns True if the user wants to close the program anyways.
        Returns False otherwise.'''
        #because "saving" could mean anything from exporting the coords to saving the image
        #there is no handling of saving here
        #a modified drawing_area is one that has any rectangles whatsoever

        #if this ends up being just a pre-close prompt, change the language accordingly
        if self.drawing_area.rects:
            ret = QMessageBox.information(self, "RectangleMappingTool",
                                          'Ensure that you have exported or saved any data'
                                          'you were working with.\n'
                                          'Click "Close" to continue, or "Cancel" to return.',
                                          QMessageBox.Close | QMessageBox.Cancel)
            if ret == QMessageBox.Close:
                return True
            elif ret == QMessageBox.Cancel:
                return False
        else:
            return True
    def closeEvent(self, event): # pylint: disable=invalid-name
        if self.close_prompt():
            event.accept()
        else:
            event.ignore()
'''
    def saveFile(self, file_format):
        initialPath = QDir.currentPath() + '/untitled.' + file_format

        file_name, _ = QFileDialog.getSaveFileName(self, "Save As", initialPath,
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
