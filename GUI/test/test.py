/********************************************************************************
** Form generated from reading UI file 'GUI.ui'
**
** Created by: Qt User Interface Compiler version 5.15.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef TEST_H
#define TEST_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFrame>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QTabWidget *tabWidget;
    QWidget *Part1;
    QWidget *Part2;
    QFrame *DatasetFrame;
    QWidget *horizontalLayoutWidget;
    QHBoxLayout *horizontalLayout;
    QLineEdit *DatasetPath;
    QPushButton *LoadDatasetButton;
    QFrame *TableFrame;
    QWidget *verticalLayoutWidget;
    QVBoxLayout *verticalLayout;
    QLabel *DataSetLabel;
    QTableWidget *tableWidget;
    QFrame *frame;
    QWidget *horizontalLayoutWidget_2;
    QHBoxLayout *horizontalLayout_2;
    QPushButton *pushButton_3;
    QPushButton *pushButton_2;
    QPushButton *pushButton;
    QPushButton *Predict;
    QTextEdit *result;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(800, 600);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        tabWidget = new QTabWidget(centralwidget);
        tabWidget->setObjectName(QString::fromUtf8("tabWidget"));
        tabWidget->setGeometry(QRect(30, 30, 741, 541));
        Part1 = new QWidget();
        Part1->setObjectName(QString::fromUtf8("Part1"));
        tabWidget->addTab(Part1, QString());
        Part2 = new QWidget();
        Part2->setObjectName(QString::fromUtf8("Part2"));
        DatasetFrame = new QFrame(Part2);
        DatasetFrame->setObjectName(QString::fromUtf8("DatasetFrame"));
        DatasetFrame->setGeometry(QRect(50, 10, 641, 41));
        DatasetFrame->setFrameShape(QFrame::StyledPanel);
        DatasetFrame->setFrameShadow(QFrame::Raised);
        horizontalLayoutWidget = new QWidget(DatasetFrame);
        horizontalLayoutWidget->setObjectName(QString::fromUtf8("horizontalLayoutWidget"));
        horizontalLayoutWidget->setGeometry(QRect(0, 0, 641, 41));
        horizontalLayout = new QHBoxLayout(horizontalLayoutWidget);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        horizontalLayout->setContentsMargins(0, 0, 0, 0);
        DatasetPath = new QLineEdit(horizontalLayoutWidget);
        DatasetPath->setObjectName(QString::fromUtf8("DatasetPath"));
        DatasetPath->setEnabled(false);

        horizontalLayout->addWidget(DatasetPath);

        LoadDatasetButton = new QPushButton(horizontalLayoutWidget);
        LoadDatasetButton->setObjectName(QString::fromUtf8("LoadDatasetButton"));
        QFont font;
        font.setPointSize(10);
        LoadDatasetButton->setFont(font);

        horizontalLayout->addWidget(LoadDatasetButton);

        TableFrame = new QFrame(Part2);
        TableFrame->setObjectName(QString::fromUtf8("TableFrame"));
        TableFrame->setGeometry(QRect(50, 60, 641, 261));
        TableFrame->setFrameShape(QFrame::StyledPanel);
        TableFrame->setFrameShadow(QFrame::Raised);
        verticalLayoutWidget = new QWidget(TableFrame);
        verticalLayoutWidget->setObjectName(QString::fromUtf8("verticalLayoutWidget"));
        verticalLayoutWidget->setGeometry(QRect(0, 0, 641, 261));
        verticalLayout = new QVBoxLayout(verticalLayoutWidget);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        DataSetLabel = new QLabel(verticalLayoutWidget);
        DataSetLabel->setObjectName(QString::fromUtf8("DataSetLabel"));
        QFont font1;
        font1.setPointSize(16);
        DataSetLabel->setFont(font1);

        verticalLayout->addWidget(DataSetLabel);

        tableWidget = new QTableWidget(verticalLayoutWidget);
        tableWidget->setObjectName(QString::fromUtf8("tableWidget"));

        verticalLayout->addWidget(tableWidget);

        frame = new QFrame(Part2);
        frame->setObjectName(QString::fromUtf8("frame"));
        frame->setGeometry(QRect(50, 340, 641, 31));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        horizontalLayoutWidget_2 = new QWidget(frame);
        horizontalLayoutWidget_2->setObjectName(QString::fromUtf8("horizontalLayoutWidget_2"));
        horizontalLayoutWidget_2->setGeometry(QRect(0, 0, 641, 31));
        horizontalLayout_2 = new QHBoxLayout(horizontalLayoutWidget_2);
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        horizontalLayout_2->setContentsMargins(0, 0, 0, 0);
        pushButton_3 = new QPushButton(horizontalLayoutWidget_2);
        pushButton_3->setObjectName(QString::fromUtf8("pushButton_3"));

        horizontalLayout_2->addWidget(pushButton_3);

        pushButton_2 = new QPushButton(horizontalLayoutWidget_2);
        pushButton_2->setObjectName(QString::fromUtf8("pushButton_2"));

        horizontalLayout_2->addWidget(pushButton_2);

        pushButton = new QPushButton(horizontalLayoutWidget_2);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));

        horizontalLayout_2->addWidget(pushButton);

        Predict = new QPushButton(Part2);
        Predict->setObjectName(QString::fromUtf8("Predict"));
        Predict->setGeometry(QRect(500, 410, 201, 51));
        QFont font2;
        font2.setPointSize(12);
        Predict->setFont(font2);
        result = new QTextEdit(Part2);
        result->setObjectName(QString::fromUtf8("result"));
        result->setGeometry(QRect(50, 390, 351, 101));
        tabWidget->addTab(Part2, QString());
        MainWindow->setCentralWidget(centralwidget);

        retranslateUi(MainWindow);

        tabWidget->setCurrentIndex(1);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(Part1), QCoreApplication::translate("MainWindow", "Partie 1", nullptr));
        LoadDatasetButton->setText(QCoreApplication::translate("MainWindow", "Load DataSet", nullptr));
        DataSetLabel->setText(QCoreApplication::translate("MainWindow", "Data Set : ", nullptr));
        pushButton_3->setText(QCoreApplication::translate("MainWindow", "Select Target", nullptr));
        pushButton_2->setText(QCoreApplication::translate("MainWindow", "Select X", nullptr));
        pushButton->setText(QCoreApplication::translate("MainWindow", "Train new Model", nullptr));
        Predict->setText(QCoreApplication::translate("MainWindow", "Predict Using the model", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(Part2), QCoreApplication::translate("MainWindow", "Partie 2", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // TEST_H
