import numpy as np
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFormLayout, QMessageBox, QDoubleSpinBox
from PyQt5.QtCore import pyqtSignal, QObject

class FeatureFormWindow(QWidget):
    prediction_made = pyqtSignal(object)  # Signal to emit the prediction result

    def __init__(self, features, model, name):
        super().__init__()
        self.features = features
        self.model = model
        self.name = name
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Feature Form")
        self.layout = QVBoxLayout()

        # Form layout
        self.form_layout = QFormLayout()
        self.input_fields = {}

        for feature in self.features:
            label = QLabel(feature)
            line_edit = QDoubleSpinBox()
            line_edit.setSingleStep(0.1)
            line_edit.setMinimum(-10000)
            line_edit.setMaximum(10000)
            self.input_fields[feature] = line_edit
            self.form_layout.addRow(label, line_edit)

        self.layout.addLayout(self.form_layout)

        # Add predict button
        self.predict_button = QPushButton("Predict")
        self.predict_button.clicked.connect(self.predict)
        self.layout.addWidget(self.predict_button)

        self.setLayout(self.layout)

    def predict(self):
        print(self.name)
        try:
            if self.name == "Decision Tree" or self.name == "Random Forest":
                # Collect inputs
                inputs = []
                for feature in self.features:
                    value = float(self.input_fields[feature].text())  # Convert to float
                    inputs.append(value)

                # Make prediction
                feature_array = np.array(inputs).reshape(1, -1)
                prediction = self.model.predict(feature_array)[0]

                # Emit the prediction result
                self.prediction_made.emit(prediction)

                # Close the form
                self.close()
            else:
                inputs = []
                for feature in self.features:
                    value = float(self.input_fields[feature].text())  # Convert to float
                    inputs.append(value)

                # Convert inputs to a NumPy array
                feature_array = np.array(inputs)

                # Calculate distances between the new instance and each medoid
                distances = [
                    np.linalg.norm(feature_array - self.model['dataset'].drop(['Target', 'Clusters'], axis=1).iloc[medoid].values)
                    for medoid in self.model["best_medoids"]
                ]

                # Find the index of the closest medoid
                closest_medoid_index = np.argmin(distances)

                # Determine the cluster for the closest medoid
                x = self.model['dataset'].iloc[self.model["best_medoids"][closest_medoid_index]]
                input_cluster = list(x)[-1]

                # Predict using the mean 'Target' value of the identified cluster
                df = self.model['final_data']
                print(df.index)
                input_pred = df[df.index == input_cluster]['Target'].mean()
                input_lat_lon = (inputs[0],inputs[1])
                
                prediction =  (input_lat_lon, input_pred, input_cluster)
                self.prediction_made.emit(prediction)

                # Close the form
                self.close()
            
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Invalid input: {e}")
