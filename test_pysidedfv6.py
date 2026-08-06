from genericpath import exists
import pytest
from PySide6 import QtCore
import pysidedfv6
from numpy.ma.testutils import assert_equal
import os


@pytest.fixture
def app(qtbot):
    test_app = pysidedfv6.MainWindowGuis()
    qtbot.addWidget(test_app)
    return test_app

def test_labels(app):
    """ Test the window GUI """
    print("test_window")
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

def test_label_text(app):
    """Test Matching Labels text"""

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
    """Tests no of labels"""
    print("Testing Labels existance ...")
    assert_equal(len(app.qlabels), 11)


def test_textbox(app):
    """Tests textbox"""
    print("Testing Textbox")
    assert 'dev_box' in app.txtbox
    assert 'total_box' in app.txtbox
    assert 'used_box' in app.txtbox
    assert 'free_box' in app.txtbox
    assert 'percent_box' in app.txtbox
    assert 'fstype_box' in app.txtbox
    assert 'mountdir_box' in app.txtbox

def test_textbox_readonly(app):
    """Tests textbox readonly mode"""

    assert app.txtbox['dev_box'].isReadOnly() == True
    assert app.txtbox['total_box'].isReadOnly() == True
    assert app.txtbox['used_box'].isReadOnly() == True
    assert app.txtbox['free_box'].isReadOnly() == True
    assert app.txtbox['percent_box'].isReadOnly() == True
    assert app.txtbox['fstype_box'].isReadOnly() == True
    assert app.txtbox['mountdir_box'].isReadOnly() == True


def test_no_of_textboxes(app):
    """Tests no of textboxes"""
    print("Testing how many textboxes are displayed ...")
    assert_equal(len(app.txtbox), 7)


def test_comboboxes(app):
    """Tests comboboxes"""
    print("Testing Comboboxes & Values....")
    assert app.combo['combo_blk_sizes'].isEditable() == False
    assert app.combo['combo_mount_dir_select'].isEditable() == False

def test_no_of_comboboxes(app):
    """Tests no comboboxes"""
    print("Testing how many comboboxes are displayed ...")
    assert_equal(len(app.combo), 2)

def test_buttons(app):
    """Tests buttons"""
    print("Testing Buttons & Values....")
    assert app.buttons['btn_show_chart'].isEnabled() == True
    assert app.buttons['btn_about'].isEnabled() == True
    assert app.buttons['btn_quit'].isEnabled() == True

def test_no_of_buttons(app):
    """Tests no of buttons"""
    print("Testing how many buttons are displayed ...")
    assert_equal(len(app.buttons),3)
