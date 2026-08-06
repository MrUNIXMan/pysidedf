# pysidedfv6.py
Little df like program in a window showing a formatted output allowing changing of block sizes and showing a pie chart of a mount dir.
Although it is called pydf.py but it is called pysidedf.


This program requires:
1. PySide6
2. qt6-charts
3. psutil
----------------------
UI - Contains
## Boxes
1. Filesystem for device nodes
2. Total
3. Used
4. Free
5. Used %
6. FS-Type
7. Mounted On

## Other parts
1. Combo box for selecting block size - this will refresh the disk list
2. Combo box for selecting mount dir - to use with show chart button.
3. Show chart button - shows a dialog with a pie chart for a selected mount point.
4. About button - About dialog
5. Quit button - exits
----------------------------------------------------
# test_pysidedfv6.py - pysidedfv6.py unit tester

This program requires:
1. pytest-qt

This is a 1st Unit test program to learn how to write one but there is not
enough documentation on GUIs using pytest.
Future changes to occur for this program.

I would use this inside a venv environment and pip install each of the requirements.
