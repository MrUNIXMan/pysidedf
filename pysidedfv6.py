#!/usr/bin/env python3

"""
Formatted GUI Disk Free For UNIX Like systems Copyright 2026  (C) Vince


This is UNIX Only and Support for Windows is dropped.
This should work on Linux, BSD and the Mac

Rewrote on: 6 Aug 2026
Version: 0.6

------------------------------------------------------------------------------
This program requires psutil, pySide6, qt6-charts and python3
"""

# Normal Imports & PyQT6 stuff
import os
import sys
import psutil
from psutil._common import bytes2human
from PySide6.QtCore import Qt
from PySide6.QtGui import (
    QPixmap,
    QPainter,
    QPen,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QLabel,
    QMainWindow,
    QPushButton,
    QTextEdit,
    QDialog,
    QVBoxLayout,
    QWidget,
)

from PySide6.QtCharts import (
    QChart,
    QChartView,
    QPieSeries,
    QPieSlice,
)

# This file is protected by the GNU General Public License v3.
LICENSE_TEXT = """
Copyright (C) 2026 Vince

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.
"""
#---------------------------------------------------------------------------------
"""
 Default Disk UNIT index that can be used with DISK_UNIT =

  0 = 1024 blocks
  1 = Megabytes
  2 = Gigabytes
  3 = Human Readable
  4 = Bytes
  5 = 512 blocks 

 These are required for blocksize calculations
"""

# Global Params goes here

DISK_UNIT = 0

class DlgCopyRight(QDialog):
    """ Copyright  Dialog"""
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('About....')
        self.setFixedSize(400, 400)
        layout = QVBoxLayout()
        self.lbltitle = QLabel("Formatted Disk free for UNIX like systems")
        self.lblcopyright = QLabel("Copyright 2026 by MrUNIXMan")
        self.diskpic = QLabel("Disk")
        self.diskpic.setPixmap(QPixmap("disk.png"))
        self.edit = QTextEdit(LICENSE_TEXT.strip())
        self.edit.setReadOnly(True)
        self.button = QPushButton('OK')
        layout.addWidget(self.diskpic)
        layout.addWidget(self.lbltitle)
        layout.addWidget(self.lblcopyright)
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.button.clicked.connect(self.closewindow)

    def closewindow(self):
        """ Close dialog """
        return self.close()



class DlgPieChart(QDialog):
    """ PieChart Dialog"""
    def __init__(self, mnt_point, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        self.setWindowTitle('Pie Chart for Disk Usage')
        self.setFixedSize(600, 600)
        disk = psutil.disk_usage(mnt_point)

        #  Set up the Chart

        series = QPieSeries()
        series.setLabelsVisible(True)
        series.append("Total", disk.total)
        series.append("Used", disk.used)
        series.append("Free", disk.free)
        for pslice in series.slices():
            percent = pslice.percentage() * 100
            pslice.setLabel(f"{pslice.label()}: {percent:.1f}%")

        # Adding Slice
        pslice = QPieSlice()
        pslice = series.slices()[0]
        pslice.setBrush(Qt.GlobalColor.darkMagenta)
        pslice = series.slices()[1]
        pslice.setBrush(Qt.red)
        pslice = series.slices()[2]
        pslice.setBrush(Qt.green)
        pslice.setExploded(True)
        pslice.setPen(QPen(Qt.darkGreen, 2))

        # Chart
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Pie Chart for Disk Usage")
        chart.setTitle(mnt_point)
        chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)

        # Create the chart view

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)


        layout.addWidget(chart_view)

        # --------------- End of Pie Charts
        self.btn = QPushButton('OK')
        layout.addWidget(self.btn)
        self.setLayout(layout)
        self.btn.clicked.connect(self.closechart)

    def closechart(self):
        """ Close chart dialog """
        return self.close()



#-----------------------------------------------------------------------

class UiMainWindow:
    """ Sets up UI class """
    def __init__(self):
        self.qlabels = None
        self.txtbox = None
        self.buttons = None
        self.combo = None
    def setup_ui(self, MainWindowGui):
        """ Sets up UI items"""
        super().__init__()

        MainWindowGui.setObjectName("MainWindowGui")

        # Labels

        self.qlabels = {
            'lbl_dev': QLabel(self),  # Device
            'lbl_total': QLabel(self),  # Total
            'lbl_used': QLabel(self),  # Used
            'lbl_free': QLabel(self),  # Free
            'lbl_percent': QLabel(self),  # % Usage
            'lbl_fstype': QLabel(self),  # Filesystem Type
            'lbl_mountdir': QLabel(self),  # Mounted on
            'lbl_info': QLabel(self),  # Information
            'lbl_blksize': QLabel(self),  # Block Size info
            'lbl_showchart': QLabel(self),  # Show Chart
            'lbl_selectblksize': QLabel(self),  # Select Block Size
        }

        # Set the sizes of the labels
        self.qlabels['lbl_dev'].setGeometry(10, 5, 350, 70)
        self.qlabels['lbl_total'].setGeometry(427, 5, 350, 70)
        self.qlabels['lbl_used'].setGeometry(582, 5, 350, 70)
        self.qlabels['lbl_free'].setGeometry(737, 5, 350, 70)
        self.qlabels['lbl_percent'].setGeometry(892, 5, 350, 70)
        self.qlabels['lbl_fstype'].setGeometry(972, 5, 350, 70)
        self.qlabels['lbl_mountdir'].setGeometry(1074, 5, 350, 70)
        self.qlabels['lbl_info'].setGeometry(5, 570, 350, 70)
        self.qlabels['lbl_blksize'].setGeometry(452, 600, 350, 70)
        self.qlabels['lbl_showchart'].setGeometry(240, 680, 190, 35)
        self.qlabels['lbl_selectblksize'].setGeometry(240, 640, 190, 35)

        self.qlabels['lbl_dev'].setText("Filesystem Node")
        self.qlabels['lbl_total'].setText("Total")
        self.qlabels['lbl_used'].setText("Used")
        self.qlabels['lbl_free'].setText("Free")
        self.qlabels['lbl_percent'].setText("%Used")
        self.qlabels['lbl_fstype'].setText("FS-Type")
        self.qlabels['lbl_mountdir'].setText("Mounted on")

        # Labels for Combo box
        self.qlabels['lbl_selectblksize'].setText("Select Block Size:")
        self.qlabels['lbl_showchart'].setText("Show Chart for mount directory:")

        #------------- Text Boxes

        self.txtbox = {
            'dev_box': QTextEdit(self),  # Devices
            'total_box': QTextEdit(self),  # Total
            'used_box': QTextEdit(self),  # Used
            'free_box': QTextEdit(self),  # Free
            'percent_box': QTextEdit(self),  # Percent
            'fstype_box': QTextEdit(self),  # Fstype
            'mountdir_box': QTextEdit(self),  # Mount Dir
        }

        self.txtbox['dev_box'].setGeometry(5, 60, 420, 530)
        self.txtbox['total_box'].setGeometry(425, 60, 155, 530)
        self.txtbox['used_box'].setGeometry(580, 60, 155, 530)
        self.txtbox['free_box'].setGeometry(735, 60, 155, 530)
        self.txtbox['percent_box'].setGeometry(890, 60, 80, 530)
        self.txtbox['fstype_box'].setGeometry(970, 60, 100, 530)
        self.txtbox['mountdir_box'].setGeometry(1070, 60, 375, 530)

        # Make the boxes Read Only
        self.txtbox['dev_box'].setReadOnly(True)
        self.txtbox['total_box'].setReadOnly(True)
        self.txtbox['used_box'].setReadOnly(True)
        self.txtbox['free_box'].setReadOnly(True)
        self.txtbox['percent_box'].setReadOnly(True)
        self.txtbox['fstype_box'].setReadOnly(True)
        self.txtbox['mountdir_box'].setReadOnly(True)

        self.buttons = {
            'btn_about': QPushButton("About", self),  # Copyright/About Button
            'btn_quit': QPushButton("Quit", self),  # Quit
            'btn_show_chart': QPushButton("Show Chart", self),  # Show Chart
        }

        # Three Buttons

        self.buttons['btn_about'].setGeometry(780, 650, 180, 30)
        self.buttons['btn_quit'].setGeometry(980, 650, 180, 30)
        self.buttons['btn_show_chart'].setGeometry(780, 680, 180, 30)


        # Combo Box
        self.combo = {
            'combo_blk_sizes': QComboBox(self),  # Select Block Sizes
            'combo_mount_dir_select': QComboBox(self),  # Select Mount dir
        }

        # Combo Box - Block sizes and Select Mount dir

        self.combo['combo_blk_sizes'].setGeometry(450, 650, 300, 30)
        self.combo['combo_mount_dir_select'].setGeometry(450, 680, 300, 30)

        # Blocksize Combo Box Add Items
        self.combo['combo_blk_sizes'].addItems(
            [
                "1024 Blocksize",
                "Megabytes",
                "Gigabytes",
                "Human Format",
                "Bytes",
                "512 Blocksize",
            ]
        )


#---------------------------------------------------------------
class Disks(QWidget):
    """Get Disks Usage Class"""
    def __init__(self, main_window, diskunit=0):
        super().__init__()
        self.main_window = main_window
        self.diskunit = diskunit

        self.spaces_dict = {
            'total':'total',
            'used':'used',
            'free':'free'
        }

        main_window.txtbox['dev_box'].clear()
        main_window.txtbox['percent_box'].clear()
        main_window.txtbox['fstype_box'].clear()
        main_window.txtbox['mountdir_box'].clear()
        main_window.txtbox['total_box'].clear()
        main_window.txtbox['used_box'].clear()
        main_window.txtbox['free_box'].clear()

        #-------------------------------------------------------------
        for partition in psutil.disk_partitions(all=False):

            if "squashfs" in partition.fstype:
                continue
            if "devfs" in partition.fstype:
                continue

            # Add mount point to combo box
            main_window.combo['combo_mount_dir_select'].addItem(partition.mountpoint)

            #PS Utils equiv to statvfs
            usage = psutil.disk_usage(partition.mountpoint)

            # Box that don't require calculation

            main_window.txtbox['dev_box'].append(partition.device)
            main_window.txtbox['percent_box'].append(str(usage.percent))
            main_window.txtbox['fstype_box'].append(partition.fstype)
            main_window.txtbox['mountdir_box'].append(partition.mountpoint)





            match diskunit:
                case 0:
                    # 1024 Blocksize
                    self.spaces_dict['total'] = usage.total / 1024
                    self.spaces_dict['used'] = usage.used / 1024
                    self.spaces_dict['free'] = usage.free / 1024

                    # Insert a thousand seperator on every 3 numbers
                    main_window.txtbox['total_box'].append(f"{int(self.spaces_dict['total']):,}")
                    main_window.txtbox['used_box'].append(f"{int(self.spaces_dict['used']):,}")
                    main_window.txtbox['free_box'].append(f"{int(self.spaces_dict['free']):,}")

                    # Final Label
                    main_window.qlabels['lbl_info'].setText("Displaying in 1k blocksize")
               #-----------------------------------------------------------------------------------
                case 1:
                    # Megabytes
                    self.spaces_dict['total'] = usage.total / 1024 / 1024
                    self.spaces_dict['used'] = usage.used / 1024 / 1024
                    self.spaces_dict['free'] = usage.free / 1024 / 1024

                    # Insert a thousand seperator on every 3 numbers
                    main_window.txtbox['total_box'].append(f"{int(self.spaces_dict['total']):,}")
                    main_window.txtbox['used_box'].append(f"{int(self.spaces_dict['used']):,}")
                    main_window.txtbox['free_box'].append(f"{int(self.spaces_dict['free']):,}")

                    # Final Label
                    main_window.qlabels['lbl_info'].setText("Displaying in Megabytes")
                #-------------------------------------------------------------
                case 2:
                    #Gigabytes

                    self.spaces_dict['total'] = usage.total / 1024 / 1024 / 1024
                    self.spaces_dict['used'] = usage.used / 1024 / 1024 / 1024
                    self.spaces_dict['free'] = usage.free / 1024 / 1024 / 1024

                    # Insert a thousand seperator on every 3 numbers
                    main_window.txtbox['total_box'].append(f"{int(self.spaces_dict['total']):,}")
                    main_window.txtbox['used_box'].append(f"{int(self.spaces_dict['used']):,}")
                    main_window.txtbox['free_box'].append(f"{int(self.spaces_dict['free']):,}")

                    # Final Label
                    main_window.qlabels['lbl_info'].setText("Displaying in gigabytes")
                # ------------------------------------------------------------------------------
                case 3:
                    #Human Readable format
                    main_window.txtbox['total_box'].append(bytes2human(usage.total))
                    main_window.txtbox['used_box'].append(bytes2human(usage.used))
                    main_window.txtbox['free_box'].append(bytes2human(usage.free))
                    main_window.qlabels['lbl_info'].setText("Displaying in Human readable format")
                #-----------------------------------------------------------------------------------
                case 4:
                    main_window.txtbox['total_box'].append(f"{usage.total:,}")
                    main_window.txtbox['used_box'].append(f"{usage.used:,}")
                    main_window.txtbox['free_box'].append(f"{usage.free:,}")
                    # Final Label
                    main_window.qlabels['lbl_info'].setText("Displaying in bytes")



                case 5:
                    self.spaces_dict['total'] = usage.total / 512
                    self.spaces_dict['used'] = usage.used / 512
                    self.spaces_dict['free'] = usage.free / 512

                    # Insert a thousand seperator on every 3 numbers
                    main_window.txtbox['total_box'].append(f"{int(self.spaces_dict['total']):,}")
                    main_window.txtbox['used_box'].append(f"{int(self.spaces_dict['used']):,}")
                    main_window.txtbox['free_box'].append(f"{int(self.spaces_dict['free']):,}")
                    # Final Label
                    main_window.qlabels['lbl_info'].setText("Displaying in 512k blocksize")
                    # ------------------------------------------------------

#--------------------------------------------------------------
class MainWindowGuis(QMainWindow, UiMainWindow):
    """ Main window class"""
    def __init__(self):
        """ init function"""
        super().__init__()

        self.dlg_copyright = None
        self.piechartsdlg = None
        self.updatedisks = None


        self.ui = UiMainWindow()
        self.setup_ui(self)
        self.setFixedSize(1450, 760)
        self.update_disk(DISK_UNIT)

        #Button Function
        self.buttons['btn_quit'].clicked.connect(self.close_window)
        self.buttons['btn_show_chart'].clicked.connect(self.show_chart)
        self.buttons['btn_about'].clicked.connect(self.show_about)

        self.combo['combo_blk_sizes'].currentIndexChanged.connect(self.update_disk)

    def show_chart(self):
        """Show chart page"""
        mount_directory = self.combo['combo_mount_dir_select'].currentText()
        self.piechartsdlg = DlgPieChart(mount_directory)
        result = self.piechartsdlg.exec()
        print("result: ", result)

    def show_about(self):
        """About page"""
        self.dlg_copyright = DlgCopyRight()
        result = self.dlg_copyright.exec()
        print("result: ", result)


    def update_disk(self, idx):
        """Update disk"""
        self.updatedisks = Disks(self, idx)

    def close_window(self):
        """Close window"""
        self.close()





#---------------------------------------------------------------------------------
# Test if the OS is UNIX Based

if os.name == 'nt':
    print("This program is not supported in Windows")
    sys.exit()
else:
    print("A Unix-like system is detected.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindowGuis()
    window.show()
    sys.exit(app.exec())
