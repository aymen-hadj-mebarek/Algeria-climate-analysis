from PyQt5 import QtWidgets, QtCore

class LoadingDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Loading...")
        self.setFixedSize(300, 100)  # Set size for the loading dialog

        # Add a simple loading text or a progress bar
        self.label = QtWidgets.QLabel("Training the model, please wait...", self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setGeometry(50, 30, 200, 40)  # Adjust position and size of label
