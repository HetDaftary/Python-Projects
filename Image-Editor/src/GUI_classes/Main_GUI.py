from PyQt5 import QtCore, QtGui, QtWidgets
from Crop_GUI import CropGUI
import sys

# This class is designed with qt designer. 
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(729, 605)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 741, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.LabelLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.LabelLayout.setContentsMargins(0, 0, 0, 0)
        self.LabelLayout.setObjectName("LabelLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.LabelLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.LabelLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.LabelLayout.addItem(spacerItem1)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 320, 731, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.Buttons = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.Buttons.setContentsMargins(0, 0, 0, 0)
        self.Buttons.setObjectName("Buttons")
        self.ToCrop = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ToCrop.setObjectName("ToCrop")
        self.Buttons.addWidget(self.ToCrop, 0, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 100, 741, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.ImagePreview = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.ImagePreview.setContentsMargins(0, 0, 0, 0)
        self.ImagePreview.setObjectName("ImagePreview")
        self.ImageToShow = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        self.ImageToShow.setObjectName("ImageToShow")
        self.ImagePreview.addWidget(self.ImageToShow)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(-20, 510, 751, 91))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.OpenAndSave = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.OpenAndSave.setContentsMargins(0, 0, 0, 0)
        self.OpenAndSave.setObjectName("OpenAndSave")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.OpenAndSave.addItem(spacerItem2)
        self.ToOpenImage = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.ToOpenImage.setObjectName("ToOpenImage")
        self.OpenAndSave.addWidget(self.ToOpenImage)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.OpenAndSave.addItem(spacerItem3)
        self.ToSaveImage = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.ToSaveImage.setObjectName("ToSaveImage")
        self.OpenAndSave.addWidget(self.ToSaveImage)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.OpenAndSave.addItem(spacerItem4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Currently Opened: None"))
        self.ToCrop.setText(_translate("Dialog", "Crop"))
        self.ToOpenImage.setText(_translate("Dialog", "Open New Image"))
        self.ToSaveImage.setText(_translate("Dialog", "Save Image"))


class MainGUI:    
    def __init__(self):
        self.initUI()

    # Setting up the UI.
    def initUI(self):   
        self.app = QtWidgets.QApplication(sys.argv)
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()
        sys.exit(app.exec_())

    # Handling the events.
    # In all, we have three events of button press.
    def toCropImageOnPress(self):
        ans = CropGUI(self.img)
        return ans

    def toOpenImageOnPress(self):
        pass 

    def toSaveImageOnPress(self):
        pass