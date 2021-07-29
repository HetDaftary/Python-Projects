from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import QApplication
from qt_material import apply_stylesheet

# Global constants
darkTheme, lightTheme = 'dark_blue.xml', 'light_blue.xml'

def toggle_stylesheet(app, path):
    '''
    Toggle the stylesheet to use the desired path in the Qt resource
    system (prefixed by `:/`) or generically (a path to a file on
    system).

    :path:      A full path to a resource or file on system
    '''

    # get the QApplication instance,  or crash if not set
    if app is None:
        raise RuntimeError("No Qt Application found.")

    apply_stylesheet(app, path)