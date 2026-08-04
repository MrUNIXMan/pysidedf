from genericpath import exists
# Basic pytest for this GUI program to learn about UNIT testing
import pytest
from PySide6 import QtCore
import pydf
from numpy.ma.testutils import assert_equal
import os


@pytest.fixture
def app(qtbot):
    test_df_app = pydf.Window()
    qtbot.addWidget(test_df_app)
    print(app)
    return test_df_app

# Existance of Labels
def test_label(app):
    print()
    print("Testing Labels existance ...")
    assert 'lbl_info' in app.qlabels
    assert 'lbl_dev' in app.qlabels
    assert 'lbl_total' in app.qlabels
    assert 'lbl_used' in app.qlabels
    assert 'lbl_free' in app.qlabels
    assert 'lbl_fstype' in app.qlabels
    assert 'lbl_mountdir' in app.qlabels
    assert 'lbl_selectblksize' in app.qlabels
    assert 'lbl_showchart' in app.qlabels



    print("Checking Label Values ....")
    assert app.qlabels['lbl_info'].text() == "Displaying in 1k blocksize"
    assert app.qlabels['lbl_dev'].text() == "Filesystem Node"
    assert app.qlabels['lbl_total'].text() == "Total"
    assert app.qlabels['lbl_used'].text() == "Used"
    assert app.qlabels['lbl_free'].text() == "Free"
    assert app.qlabels['lbl_percent'].text() == "%Used"
    assert app.qlabels['lbl_fstype'].text() == "FS-Type"
    assert app.qlabels['lbl_mountdir'].text() == "Mounted on"
    assert app.qlabels['lbl_selectblksize'].text() == "Select Block Size:"
    assert app.qlabels['lbl_showchart'].text() == "Show Chart for mount directory:"

def test_no_of_labels(app):
    print("Testing Labels existance ...")
    assert_equal(len(app.qlabels), 11)

def test_textbox(app):
    print("Testing Textbox")
    assert 'dev_box' in app.widgets
    assert 'total_box' in app.widgets
    assert 'used_box' in app.widgets
    assert 'free_box' in app.widgets
    assert 'percent_box' in app.widgets
    assert 'fstype_box' in app.widgets
    assert 'mountdir_box' in app.widgets


    print("Checking if they are read only......")
    assert app.widgets['dev_box'].isReadOnly() == True
    assert app.widgets['total_box'].isReadOnly() == True
    assert app.widgets['used_box'].isReadOnly() == True
    assert app.widgets['free_box'].isReadOnly() == True
    assert app.widgets['percent_box'].isReadOnly() == True
    assert app.widgets['fstype_box'].isReadOnly() == True
    assert app.widgets['mountdir_box'].isReadOnly() == True

def test_no_of_textboxes(app):
    print("Testing how many textboxes are displayed ...")
    assert_equal(len(app.widgets), 7)

def test_comboboxes(app):
    print("Testing Comboboxes & Values....")
    assert app.combo['combo_blk_sizes'].isEditable() == False
    assert app.combo['combo_mount_dir_select'].isEditable() == False

def test_no_of_comboboxes(app):
    print("Testing how many comboboxes are displayed ...")
    assert_equal(len(app.combo), 2)


def test_buttons(app):
    print("Testing Buttons & Values....")
    assert app.buttons['btn_show_chart'].isEnabled() == True
    assert app.buttons['btn_about'].isEnabled() == True
    assert app.buttons['btn_quit'].isEnabled() == True

def test_no_of_buttons(app):
    print("Testing how many buttons are displayed ...")
    assert_equal(len(app.buttons),3)



def test_quitbutton_after_click(app, qtbot):
    print("Testing Quitbutton_after_click ...")
    qtbot.mouseClick(app.buttons['btn_quit'], QtCore.Qt.LeftButton)
    app.qlabels['lbl_info'].setText("Quit")
    assert app.qlabels['lbl_info'].text() == "Quit"


