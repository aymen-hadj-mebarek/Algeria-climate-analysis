from PyQt5 import QtWidgets, QtCore

class LabelSelectionWindow(QtWidgets.QDialog):
    def __init__(self, features, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select the Target")

        # Create the main layout for the dialog
        self.layout = QtWidgets.QVBoxLayout(self)

        # Create a scroll area widget
        self.scroll_area = QtWidgets.QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)

        # Create a widget to hold the checkboxes
        self.scroll_widget = QtWidgets.QWidget(self)
        self.scroll_layout = QtWidgets.QGridLayout(self.scroll_widget)

        # Add checkboxes to the grid layout
        self.feature_checkboxes = {}
        row, col = 0, 0  # Start at the top-left corner of the grid layout

        for i, feature in enumerate(features):
            checkbox = QtWidgets.QRadioButton(feature, self)
            self.feature_checkboxes[feature] = checkbox
            self.scroll_layout.addWidget(checkbox, row, col)

            # Move to the next column
            col += 1
            if col == 3:
                col = 0
                row += 1

        # Set the scroll area widget
        self.scroll_area.setWidget(self.scroll_widget)

        # Add the scroll area to the main layout
        self.layout.addWidget(self.scroll_area)

        # Add the "OK" button to confirm selection
        self.ok_button = QtWidgets.QPushButton("OK", self)
        self.ok_button.clicked.connect(self.accept)
        self.layout.addWidget(self.ok_button)

        self.setLayout(self.layout)

    def get_selected_features(self):
        # Return the selected features
        return [feature for feature, checkbox in self.feature_checkboxes.items() if checkbox.isChecked()]
