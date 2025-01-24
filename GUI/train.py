from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject


class Ui_Train(QObject):
    sendData = pyqtSignal(dict)
    
    def confirmDT(self):
        data = {
            "name" : "Decision Tree",
            "min_split" : int(self.min_sample_split.value()),
            "max_depth" : int(self.max_depth.value()),
            "n_features": None if self.n_features.value() == 0 else int(self.n_features.value())
        }
        self.sendData.emit(data)
    
    def confirmRF(self):
        data = {
            "name" : "Random Forest",
            "n_trees": int(self.n_trees.value()),
            "min_split" : int(self.min_sample_split_2.value()),
            "max_depth" : int(self.max_depth_2.value()),
            "n_features": None if self.n_features.value() == 0 else int(self.n_features.value())
        }
        self.sendData.emit(data)
        
    def confirmCLARANS(self):
        data = {
            "name" : "CLARANS",
            "number_clusters":self.num_clusters.value(),
            "num_local":self.num_local.value(),
            "max_neighbors":self.max_neighbors.value(),
        }
        self.sendData.emit(data)
    
    def confirmDBSCAN(self):
        data = {
            "name" : "DBSCAN",
            "eps":self.eps.value(),
            "min_samples":self.min_samples.value()
        }
        self.sendData.emit(data)
    
    def setupUi(self, Train):
        Train.setObjectName("Train")
        Train.resize(447, 316)
        self.centralwidget = QtWidgets.QWidget(Train)
        self.centralwidget.setObjectName("centralwidget")
        self.TrainWidgets = QtWidgets.QTabWidget(self.centralwidget)
        self.TrainWidgets.setGeometry(QtCore.QRect(20, 40, 401, 241))
        font = QtGui.QFont()
        font.setPointSize(10)
        
        self.TrainWidgets.setFont(font)
        self.TrainWidgets.setObjectName("TrainWidgets")
        self.DecisionTreeWidget = QtWidgets.QWidget()
        self.DecisionTreeWidget.setObjectName("DecisionTreeWidget")
        self.DecisionTreeForm = QtWidgets.QFrame(self.DecisionTreeWidget)
        self.DecisionTreeForm.setGeometry(QtCore.QRect(40, 10, 321, 181))
        self.DecisionTreeForm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DecisionTreeForm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DecisionTreeForm.setObjectName("DecisionTreeForm")
        
        self.formLayoutWidget = QtWidgets.QWidget(self.DecisionTreeForm)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 301, 161))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        
        self.min_sample_split = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.min_sample_split.setObjectName("min_sample_split")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.min_sample_split)
        
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        
        self.max_depth = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.max_depth.setObjectName("max_depth")
        self.max_depth.setMaximum(999)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.max_depth)
        
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        
        self.n_features = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.n_features.setObjectName("n_features")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.n_features)
        
        self.DT_Confirm = QtWidgets.QPushButton(self.formLayoutWidget)
        self.DT_Confirm.setObjectName("Confirm")
        self.DT_Confirm.clicked.connect(lambda : self.confirmDT())
        
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.DT_Confirm)
        self.TrainWidgets.addTab(self.DecisionTreeWidget, "")
        self.RandomForestWidget = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(10)
        
        self.RandomForestWidget.setFont(font)
        self.RandomForestWidget.setObjectName("RandomForestWidget")
        
        self.RandomForestForm = QtWidgets.QFrame(self.RandomForestWidget)
        self.RandomForestForm.setGeometry(QtCore.QRect(40, 10, 321, 181))
        self.RandomForestForm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RandomForestForm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RandomForestForm.setObjectName("RandomForestForm")
        
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.RandomForestForm)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 301, 161))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.min_sample_split_2 = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.min_sample_split_2.setObjectName("min_sample_split_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.min_sample_split_2)
        
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.max_depth_2 = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.max_depth_2.setObjectName("max_depth_2")
        self.max_depth_2.setMaximum(999)
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.max_depth_2)
        
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.n_features_2 = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.n_features_2.setObjectName("n_features_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.n_features_2)
        
        self.RF_Confirm = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.RF_Confirm.setObjectName("Confirm_2")
        self.RF_Confirm.clicked.connect(lambda : self.confirmRF())
        
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.RF_Confirm)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.n_trees = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.n_trees.setObjectName("n_trees")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.n_trees)
        
        self.TrainWidgets.addTab(self.RandomForestWidget, "")
        self.ClaransWidget = QtWidgets.QWidget()
        self.ClaransWidget.setObjectName("ClaransWidget")
        
        self.CLARANSForm = QtWidgets.QFrame(self.ClaransWidget)
        self.CLARANSForm.setGeometry(QtCore.QRect(40, 10, 321, 181))
        self.CLARANSForm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CLARANSForm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CLARANSForm.setObjectName("CLARANSForm")
        
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.CLARANSForm)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 301, 161))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.CLARANS_confirm = QtWidgets.QPushButton(self.formLayoutWidget_3)
        self.CLARANS_confirm.setObjectName("Confirm_3")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.CLARANS_confirm)
        self.CLARANS_confirm.clicked.connect(lambda : self.confirmCLARANS())
        
        
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_11)
        
        self.num_clusters = QtWidgets.QSpinBox(self.formLayoutWidget_3)
        self.num_clusters.setObjectName("num_clusters")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.num_clusters)
        
        self.num_local = QtWidgets.QSpinBox(self.formLayoutWidget_3)
        self.num_local.setObjectName("num_local")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.num_local)
        
        self.max_neighbors = QtWidgets.QSpinBox(self.formLayoutWidget_3)
        self.max_neighbors.setObjectName("max_neighbors")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.max_neighbors)
        
    
        self.TrainWidgets.addTab(self.ClaransWidget, "")
        self.DBScanWidget = QtWidgets.QWidget()
        self.DBScanWidget.setObjectName("DBScanWidget")
        self.DBSCANForm = QtWidgets.QFrame(self.DBScanWidget)
        self.DBSCANForm.setGeometry(QtCore.QRect(40, 10, 321, 181))
        self.DBSCANForm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DBSCANForm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DBSCANForm.setObjectName("DBSCANForm")
        
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.DBSCANForm)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 301, 161))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_15.setObjectName("label_15")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_15)
        
        self.eps = QtWidgets.QDoubleSpinBox(self.formLayoutWidget_4)
        self.eps.setObjectName("eps")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.eps)
        
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_12.setObjectName("label_12")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_12)
        
        self.min_samples = QtWidgets.QSpinBox(self.formLayoutWidget_4)
        self.min_samples.setObjectName("min_samples")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.min_samples)
        
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_14.setObjectName("label_14")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_14)
        
        self.DBSCAN_confirm = QtWidgets.QPushButton(self.formLayoutWidget_4)
        self.DBSCAN_confirm.setObjectName("Confirm_4")
        self.DBSCAN_confirm.clicked.connect(lambda : self.confirmDBSCAN())
        
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.DBSCAN_confirm)
        self.TrainWidgets.addTab(self.DBScanWidget, "")
        Train.setCentralWidget(self.centralwidget)

        self.retranslateUi(Train)
        self.TrainWidgets.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Train)

    def retranslateUi(self, Train):
        _translate = QtCore.QCoreApplication.translate
        Train.setWindowTitle(_translate("Train", "Entrainement du modele"))
        self.label.setText(_translate("Train", "Minimum Sample Split "))
        self.label_2.setText(_translate("Train", "Max depth"))
        self.label_3.setText(_translate("Train", "Number of features"))
        self.DT_Confirm.setText(_translate("Train", "Confirm Parameters"))
        self.TrainWidgets.setTabText(self.TrainWidgets.indexOf(self.DecisionTreeWidget), _translate("Train", "Decision Tree"))
        self.label_4.setText(_translate("Train", "Minimum Sample Split "))
        self.label_5.setText(_translate("Train", "Max depth"))
        self.label_6.setText(_translate("Train", "Number of features"))
        self.RF_Confirm.setText(_translate("Train", "Confirm Parameters"))
        self.label_7.setText(_translate("Train", "Number of Trees"))
        self.TrainWidgets.setTabText(self.TrainWidgets.indexOf(self.RandomForestWidget), _translate("Train", "Random Forest"))
        self.label_8.setText(_translate("Train", "Num Local"))
        self.label_9.setText(_translate("Train", "Max Iterations"))
        self.CLARANS_confirm.setText(_translate("Train", "Confirm Parameters"))
        self.label_11.setText(_translate("Train", "Number of Clusters"))
        self.TrainWidgets.setTabText(self.TrainWidgets.indexOf(self.ClaransWidget), _translate("Train", "CLARANS"))
        self.label_15.setText(_translate("Train", "Maximum distance"))
        self.label_12.setText(_translate("Train", "Min Samples"))
        
        self.DBSCAN_confirm.setText(_translate("Train", "Confirm Parameters"))
        self.TrainWidgets.setTabText(self.TrainWidgets.indexOf(self.DBScanWidget), _translate("Train", "DBSCAN"))

