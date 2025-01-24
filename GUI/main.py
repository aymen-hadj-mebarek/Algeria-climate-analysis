from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import pandas as pd
import numpy as np
from PredictForm import FeatureFormWindow
from train import Ui_Train
from loading import LoadingDialog
from ModelTraining import ModelTrainingWorker
from Features_window import FeatureSelectionWindow
from Labels_window import LabelSelectionWindow
from sklearn.model_selection import train_test_split
from Decision_Tree import DecisionTree
from Random_Forest import RandomForest
import pickle
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.metrics import davies_bouldin_score, calinski_harabasz_score, silhouette_score
import matplotlib.pyplot as plt
from data_preprocess import DataAnalysisWidget

class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.Dataset = pd.DataFrame()
        self.Columns = []
        self.label = []
        self.features = []
        self.split_data = None
        self.model = None
        self.model_name = ""
        
        self.tab_sizes = {
            0: (1080, 650),  # Size for Part1 (Data Analysis)
            1: (800, 600)    # Size for Part2 (Model Training)
        }

    def handle_tab_changed(self, index):
        # Resize the main window
        width, height = self.tab_sizes.get(index, (800, 600))
        MainWindow.resize(width, height)
        
        # Optional: Adjust tab widget size
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, width, height))
               
    def loadDataSet(self):
        # Open file dialog
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(None, "Open Dataset File", "", "CSV Files (*.csv);;All Files (*)", options=options)

        if file_path:
            self.DatasetPath.setText(file_path)
            try:
                # Load CSV into pandas DataFrame
                df = pd.read_csv(file_path)
                self.Dataset = df.copy()
                self.Columns = list(self.Dataset.columns)
                
                # Populate the table widget
                self.populate_table(df)
            except Exception as e:
                QMessageBox.critical(None, "Error", f"Could not load dataset:\n{str(e)}")
        else:
            QMessageBox.information(None, "No File Selected", "Please select a file to load.")

    def populate_table(self, df):
        # Set row and column count
        self.DataSetTable.setRowCount(df.shape[0])
        self.DataSetTable.setColumnCount(df.shape[1])

        # Set column headers
        self.DataSetTable.setHorizontalHeaderLabels(df.columns)

        # Populate table cells
        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                value = str(df.iloc[row, col])
                self.DataSetTable.setItem(row, col, QtWidgets.QTableWidgetItem(value))

    def import_model(self):
        # Open a file dialog to choose the pickle file
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog  # Optional: Ensure a consistent look across platforms
        file_path, _ = QFileDialog.getOpenFileName(
            None,
            "Open Model File",
            "",
            "Pickle Files (*.pkl);;All Files (*)",
            options=options
        )

        if file_path:
            try:
                with open(file_path, "rb") as file:
                    data = pickle.load(file)

                # Ensure the file contains the expected data
                if not all(key in data for key in ["model", "features", "target"]):
                    raise ValueError("The selected file does not contain valid model data.")

                # Assign the loaded data to the respective variables
                self.model = data["model"]
                self.features = data["features"]
                self.label = data["target"]
                self.split_data = data["data"]
                self.model_name = data["model_name"]

                # Show a success dialog
                success_msg = QMessageBox()
                success_msg.setIcon(QMessageBox.Information)
                success_msg.setWindowTitle("Success")
                success_msg.setText("Model, features, and target have been loaded successfully!")
                success_msg.exec_()

            except Exception as e:
                # Show an error dialog
                error_msg = QMessageBox()
                error_msg.setIcon(QMessageBox.Critical)
                error_msg.setWindowTitle("Error")
                error_msg.setText("Failed to load the model.")
                error_msg.setDetailedText(str(e))
                error_msg.exec_()
    
    def save_model(self):
        # Open a file dialog to choose the save location
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog  # Optional: Ensure a consistent look across platforms
        file_path, _ = QFileDialog.getSaveFileName(
            None,
            "Save Model File",
            "",
            "Pickle Files (*.pkl);;All Files (*)",
            options=options
        )

        if file_path:
            # Ensure the file has a .pkl extension
            if not file_path.endswith(".pkl"):
                file_path += ".pkl"

            # Create a dictionary to save model, features, and target
            if isinstance(self.model, DecisionTree):
                self.model_name = "Decision Tree"
            elif isinstance(self.model, RandomForest):
                self.model_name = "Random Forest"
            elif len(self.model) == 5:
                self.model_name = "CLARANS"
            else:
                self.model_name = "DBSCAN"
                
            data_to_save = {
                "model_name":self.model_name,
                "model": self.model,
                "features": self.features,
                "target": self.label,
                "data" : self.split_data
            }

            # Save the data using pickle
            try:
                with open(file_path, "wb") as file:
                    pickle.dump(data_to_save, file)
                
                # Show a success dialog
                success_msg = QMessageBox()
                success_msg.setIcon(QMessageBox.Information)
                success_msg.setWindowTitle("Success")
                success_msg.setText("Model, features, and target have been saved successfully!")
                success_msg.exec_()

            except Exception as e:
                # Show an error dialog
                error_msg = QMessageBox()
                error_msg.setIcon(QMessageBox.Critical)
                error_msg.setWindowTitle("Error")
                error_msg.setText("Failed to save the model.")
                error_msg.setDetailedText(str(e))
                error_msg.exec_()
    
    def test_model(self):
        if self.model != None and self.split_data != None:
            if (isinstance(self.model, RandomForest) or isinstance(self.model, DecisionTree)):
                predictions = self.model.predict(self.split_data['x_test'])
                print(predictions)
                valid_indices = predictions != -1 & (~np.isnan(predictions)) & (~np.isnan(self.split_data['y_test']))
                filtered_predictions = predictions[valid_indices]
                filtered_y_test = self.split_data['y_test'][valid_indices]
                print("start calculating")
                mae = mean_absolute_error(filtered_y_test, filtered_predictions)
                mse = mean_squared_error(filtered_y_test, filtered_predictions)
                r2 = r2_score(filtered_y_test, filtered_predictions)
                text = f"Results of the loaded model : \
                                \nMAE: {mae}\
                                \nMSE: {mse}\
                                \nR²: {r2}"
            else:
                try:
                    davies_bouldin = davies_bouldin_score(self.model['dataset'].drop(['Target', 'Clusters'], axis=1), self.model['dataset']['Clusters'])
                    calinski_harabasz = calinski_harabasz_score(self.model['dataset'].drop(['Target', 'Clusters'], axis=1), self.model['dataset']['Clusters'])
                    silhouette = silhouette_score(self.model['dataset'].drop(['Target', 'Clusters'], axis=1), self.model['dataset']['Clusters'])

                    text = f"Result of the loaded model: \
                    \nDavies Bouldin score: {davies_bouldin:.2f} \
                    \nCalinski Harabasz score: {calinski_harabasz:.2f} \
                    \nSilhouette score: {silhouette:.2f}"
                except Exception as e:
                    text = f"there was an error calculating metrics\n{e}"
            
                
                features = self.model['dataset'].drop(['Target', 'Clusters'], axis=1)
                clusters = self.model['dataset']['Clusters']
                try:
                    lon = features['lon']
                    lat = features['lat']

                    plt.figure(figsize=(8, 6))
                    plt.scatter(lon, lat, c=clusters, cmap='viridis', edgecolor='k', s=50)
                    plt.title('Longitude vs Latitude', fontsize=16)
                    plt.xlabel('Longitude', fontsize=12)
                    plt.ylabel('Latitude', fontsize=12)
                    plt.colorbar(label='Cluster')
                    plt.grid(True)
                    plt.show()
                except:
                    QMessageBox.critical(None, "Error", f"Could not find lon or lat in the data")                
            self.result.setText(text)            
        else:
            QMessageBox.critical(None, "Error", f"Could not load data, or the model")
    
    def open_train_window(self):
        self.train_window = QtWidgets.QMainWindow()
        self.ui_train = Ui_Train()
        self.ui_train.setupUi(self.train_window)
        self.ui_train.sendData.connect(self.handle_confirmed_parameters)        
        self.train_window.show()

    def open_features_window(self):
        if len(self.Dataset) != 0:
            # Create the feature selection window and pass the features list
            features_list = self.Columns
            feature_window = FeatureSelectionWindow(features_list)
            feature_window.exec_()
            selected_features = feature_window.get_selected_features()
            print("Selected Features:", selected_features)
            feature_window.close()
            self.features = selected_features
        else:
            QMessageBox.critical(None, "Error", f"Please insert data before proceeding")

    def open_label_window(self):
        if len(self.Dataset) != 0:
            label_list = self.Columns
            feature_window = LabelSelectionWindow(label_list)
            feature_window.exec_()
            selected_label = feature_window.get_selected_features()
            print("Selected label:", selected_label)
            feature_window.close()
            self.label = selected_label
        else:
            QMessageBox.critical(None, "Error", f"Please insert data before proceeding")
    def handle_confirmed_parameters(self, params):
        print("Received Parameters:", params)
        try:
            X_train, X_test, y_train, y_test = train_test_split(self.Dataset[self.features], self.Dataset[self.label[0]], test_size=round(self.SplitDataSet.value(), 3), random_state=42)
            params['x_train'] = X_train
            params['y_train'] = y_train
            params['x_test'] = X_test
            params['y_test'] = y_test
            
            self.split_data = {
                'x_train' : X_train,
                'y_train' : y_train,
                'x_test' : X_test,
                'y_test' : y_test
            }
            
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Could not load dataset:\n{str(e)}")
        
        # # Create and show the loading dialog
        self.loading_dialog = LoadingDialog()
        self.loading_dialog.show()

        # Start a new thread for training to prevent freezing the UI
        # Create a QThread and move the model training to that thread
        self.thread = QtCore.QThread()
        self.worker = ModelTrainingWorker(params, self.loading_dialog)
        self.worker.moveToThread(self.thread)

        # Connect signals to start training and close the loading dialog
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.on_training_finished)

        self.thread.start()
        
    def on_training_finished(self, trained_model):
        print("Training finished!")
        # print("Trained Model:", trained_model)

        # Close the loading dialog
        self.loading_dialog.close()

        # Clean up the thread
        self.thread.quit()
        self.thread.wait()
        self.worker.deleteLater()
        self.thread.deleteLater()

        # Use the trained model as needed
        if trained_model:
            # For example, save it, make predictions, or evaluate it
            self.model = trained_model
            print("Model is ready for predictions.")

    def predict(self):
        # Open the feature form window
        if self.model is not None:
            self.feature_form_window = FeatureFormWindow(self.features, self.model, self.model_name)
            self.feature_form_window.prediction_made.connect(self.display_prediction)  # Connect the signal
            self.feature_form_window.show()
        else:
            QMessageBox.critical(None, "Error", f"Could Not find a Model, please import or train one!")
            
    def display_prediction(self, prediction):
        if isinstance(prediction, tuple):
            self.result.setText(f"Prediction result Using {self.model_name} model :\n\t {prediction[1]}\nit is from the cluster : {prediction[2]}")
            
            new_instance = prediction[0]  # This will return (lon, lat)

            features = self.model['dataset'].drop(['Target', 'Clusters'], axis=1)
            clusters = self.model['dataset']['Clusters']
            try:
                lon = features['lon']
                lat = features['lat']
                
                # Extract new instance coordinates
                new_lon, new_lat = new_instance

                plt.figure(figsize=(8, 6))
                
                # Plot the data points
                scatter = plt.scatter(lon, lat, c=clusters, cmap='viridis', edgecolor='k', s=50, label='Data Points')
                
                # Plot the new instance as a red 'X'
                plt.scatter(new_lon, new_lat, color='red', marker='X', s=200, label='New Instance')
                
                # Add titles and labels
                plt.title('Longitude vs Latitude', fontsize=16)
                plt.xlabel('Longitude', fontsize=12)
                plt.ylabel('Latitude', fontsize=12)
                
                # Add color bar and legend
                plt.colorbar(scatter, label='Cluster')
                plt.legend(fontsize=10)
                plt.grid(True)
                
                # Show the plot
                plt.show()
            except KeyError:
                QMessageBox.critical(None, "Error", "Could not find 'lon' or 'lat' in the data")
        else:
            self.result.setText(f"Prediction result Using {self.model_name} model :\n\t {prediction}")
        
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 30, 741, 541))
        self.tabWidget.setObjectName("tabWidget")
        self.Part1 = DataAnalysisWidget()
        self.Part1.setObjectName("Part1")
        self.tabWidget.addTab(self.Part1, "")
        
        self.Part2 = QtWidgets.QWidget()
        self.Part2.setObjectName("Part2")
        
        self.DatasetFrame = QtWidgets.QFrame(self.Part2)
        self.DatasetFrame.setGeometry(QtCore.QRect(50, 10, 641, 41))
        self.DatasetFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DatasetFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DatasetFrame.setObjectName("DatasetFrame")
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.DatasetFrame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 641, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.DatasetPath = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        # self.DatasetPath.setEnabled(False)
        self.DatasetPath.setReadOnly(True)
        self.DatasetPath.setObjectName("DatasetPath")
        self.horizontalLayout.addWidget(self.DatasetPath)
        
        self.SplitDataSet = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        self.SplitDataSet.setMinimum(0.001)
        self.SplitDataSet.setMaximum(0.999)
        self.SplitDataSet.setValue(0.2)
        self.SplitDataSet.setSingleStep(0.1)
        self.SplitDataSet.setObjectName("SplitDataSet")
        self.horizontalLayout.addWidget(self.SplitDataSet)
        
        self.LoadDatasetButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LoadDatasetButton.setFont(font)
        self.LoadDatasetButton.setObjectName("LoadDatasetButton")
        self.LoadDatasetButton.clicked.connect(lambda : self.loadDataSet())
        self.horizontalLayout.addWidget(self.LoadDatasetButton)
        self.horizontalLayout.addWidget(self.LoadDatasetButton)
        
        
        self.TableFrame = QtWidgets.QFrame(self.Part2)
        self.TableFrame.setGeometry(QtCore.QRect(50, 60, 641, 261))
        self.TableFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TableFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TableFrame.setObjectName("TableFrame")
        
        self.verticalLayoutWidget = QtWidgets.QWidget(self.TableFrame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 641, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.DataSetLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.DataSetLabel.setFont(font)
        self.DataSetLabel.setObjectName("DataSetLabel")
        self.verticalLayout.addWidget(self.DataSetLabel)
        self.DataSetTable = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.DataSetTable.setObjectName("tableWidget")
        self.DataSetTable.setColumnCount(0)
        self.DataSetTable.setRowCount(0)
        self.DataSetTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.verticalLayout.addWidget(self.DataSetTable)
        
        self.frame = QtWidgets.QFrame(self.Part2)
        self.frame.setGeometry(QtCore.QRect(50, 340, 641, 31))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 641, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.open_label_window)
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.open_features_window)
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        
        
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.import_model)
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.open_train_window)
        self.horizontalLayout_2.addWidget(self.pushButton)
        
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.save_model)
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.test_model)
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        
        self.Predict = QtWidgets.QPushButton(self.Part2)
        self.Predict.setGeometry(QtCore.QRect(500, 410, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Predict.setFont(font)
        self.Predict.setObjectName("Predict")
        self.Predict.clicked.connect(self.predict)
        
        self.result = QtWidgets.QTextEdit(self.Part2)
        self.result.setGeometry(QtCore.QRect(50, 390, 351, 101))
        self.result.setObjectName("result")
        self.result.setReadOnly(True)
        self.tabWidget.addTab(self.Part2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.tabWidget.currentChanged.connect(self.handle_tab_changed)
        MainWindow.resize(*self.tab_sizes[0])
        
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Algeria Climate Analysis and Prediction"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Part1), _translate("MainWindow", "Data Cleaning and Preprocessing"))
        self.LoadDatasetButton.setText(_translate("MainWindow", "Load DataSet"))
        # self.LoadDatasetButton.setText(_translate("MainWindow", "Load DataSet"))
        self.DataSetLabel.setText(_translate("MainWindow", "Data Set : "))
        self.pushButton_3.setText(_translate("MainWindow", "Select Target"))
        self.pushButton_2.setText(_translate("MainWindow", "Select Features"))
        self.pushButton_4.setText(_translate("MainWindow", "Import Model"))
        self.pushButton_5.setText(_translate("MainWindow", "Save Model"))
        self.pushButton_6.setText(_translate("MainWindow", "Test Model"))
        self.pushButton.setText(_translate("MainWindow", "Train new Model"))
        self.Predict.setText(_translate("MainWindow", "Predict Using the model"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Part2), _translate("MainWindow", "Model Training"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
