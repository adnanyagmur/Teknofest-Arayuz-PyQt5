# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ihason.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QPixmap
from sys import argv
from PIL import Image
from PIL.ImageQt import ImageQt

####verialma####

from dronekit import connect, VehicleMode
import time
import random

#Set up option parsing to get connection string
import argparse  
parser = argparse.ArgumentParser(description='Print out vehicle state information. Connects to SITL on local PC by default.')
parser.add_argument('--connect', 
                   help="vehicle connection target string. If not specified, SITL automatically started and used.")
args = parser.parse_args()

connection_string = args.connect
sitl = None


#Start SITL if no connection string specified
if not connection_string: 
    import dronekit_sitl
    sitl = dronekit_sitl.start_default()
    connection_string = sitl.connection_string()


# Connect to the Vehicle. 
#   Set `wait_ready=True` to ensure default attributes are populated before `connect()` returns.
print("\nConnecting to vehicle on: %s" % connection_string)
vehicle = connect(connection_string, wait_ready=False)

vehicle.wait_ready(True,timeout=250)

####verialmason####


a = vehicle.groundspeed * -20 ### burda x y z eksenleri olabilir teste göre ayarlıcaz

b = vehicle.gimbal._vehicle._roll * -55  ## roll değeri ile yapılacak roll komutu emin olmamakla birlikte bu komut

c = vehicle.location.global_frame.alt  ## teste göre katsayı ayarlıcaz

d = vehicle.heading * -1 ## 0 ila 360 arası veriyor pusulaya göre ayarlancak

e =vehicle.heading * -1 ## drone yönünü gösteriyor yukarıyla aynı olacak

f = vehicle.velocity  ## irtifa olarak veriyor değerine bakıp açı kat sayısına evrilecek

v = vehicle.battery.voltage  # batarya durumu

k = vehicle.armed     # armed disarmed durumu




def hiz(aci1):
    hzgos = Image.open("./hzibre.png")
    hzgos = hzgos.rotate(aci1)
    qt_hzgos = ImageQt(hzgos)
    print(qt_hzgos)
    return qt_hzgos
hzgos = hiz(a)

def durum(aci2):
    drmcyro = Image.open("./durumcyro oynar.png")
    drmcyro = drmcyro.rotate(aci2)
    qt_drmcyro = ImageQt(drmcyro)
    return qt_drmcyro
drmcyro = durum(b)

def alti(aci3):
    if  (aci3 <= 0 or aci3 == None)  :
        print(aci3, "ilk gelen değer")
        aci3 = 0
        print(aci3,"son değer")
        altime = Image.open("./alti ibre.png")
        altime= altime.rotate(aci3)
        qt_altime = ImageQt(altime)
        return qt_altime
    
    else:
        print(aci3 , "işlem öncesi")
        aci3 = int(360-((360/50)*aci3))
        print(aci3 , "işlem sonrası ")
        altime = Image.open("./alti ibre.png")
        altime= altime.rotate(aci3)
        qt_altime = ImageQt(altime)
        return qt_altime
altime = alti(c)

def pusula(aci4):
    psla= Image.open("./pslibre.png")
    psla= psla.rotate(aci4)
    qt_psla = ImageQt(psla)
    return qt_psla
psla = pusula(d)

def istik(aci5):
    istk= Image.open("istkoynr.png")
    istk= istk.rotate(aci5)
    qt_istk = ImageQt(istk)
    return qt_istk
istk = istik(e)

def dikey(aci6):
    dkyhz= Image.open("./dikeyhzibre.png")
    dkyhz= dkyhz.rotate(aci6)
    qt_dkyhz = ImageQt(dkyhz)
    return qt_dkyhz
dkyhz = dikey(f[2] * 100)

class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1350, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txt_arkaplan = QtWidgets.QLabel(self.centralwidget)
        self.txt_arkaplan.setGeometry(QtCore.QRect(0, 0, 1350, 768))
        self.txt_arkaplan.setStyleSheet("")
        self.txt_arkaplan.setText("")
        self.txt_arkaplan.setPixmap(QtGui.QPixmap("deneme.png"))
        self.txt_arkaplan.setScaledContents(True)
        self.txt_arkaplan.setObjectName("txt_arkaplan")
        self.hizyazi = QtWidgets.QLabel(self.centralwidget)
        self.hizyazi.setGeometry(QtCore.QRect(70, 340, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.hizyazi.setFont(font)
        self.hizyazi.setStyleSheet("color: rgb(238, 238, 236);\n"
"")
        self.hizyazi.setObjectName("hizyazi")
        self.drmguroyazi = QtWidgets.QLabel(self.centralwidget)
        self.drmguroyazi.setGeometry(QtCore.QRect(350, 340, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.drmguroyazi.setFont(font)
        self.drmguroyazi.setStyleSheet("color: rgb(238, 238, 236);")
        self.drmguroyazi.setObjectName("drmguroyazi")
        self.altiyazi = QtWidgets.QLabel(self.centralwidget)
        self.altiyazi.setGeometry(QtCore.QRect(630, 340, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.altiyazi.setFont(font)
        self.altiyazi.setStyleSheet("color: rgb(238, 238, 236);")
        self.altiyazi.setObjectName("altiyazi")
        self.pusulayazi = QtWidgets.QLabel(self.centralwidget)
        self.pusulayazi.setGeometry(QtCore.QRect(110, 600, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pusulayazi.setFont(font)
        self.pusulayazi.setStyleSheet("color: rgb(238, 238, 236);")
        self.pusulayazi.setObjectName("pusulayazi")
        self.vayroyazi = QtWidgets.QLabel(self.centralwidget)
        self.vayroyazi.setGeometry(QtCore.QRect(570, 600, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.vayroyazi.setFont(font)
        self.vayroyazi.setStyleSheet("color: rgb(238, 238, 236);")
        self.vayroyazi.setObjectName("vayroyazi")
        self.istikametyazi = QtWidgets.QLabel(self.centralwidget)
        self.istikametyazi.setGeometry(QtCore.QRect(310, 600, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.istikametyazi.setFont(font)
        self.istikametyazi.setStyleSheet("color: rgb(238, 238, 236);")
        self.istikametyazi.setObjectName("istikametyazi")
        self.altisbt = QtWidgets.QLabel(self.centralwidget)
        self.altisbt.setGeometry(QtCore.QRect(620, 180, 141, 141))
        self.altisbt.setText("")
        self.altisbt.setPixmap(QtGui.QPixmap("altimetre.png"))
        self.altisbt.setScaledContents(True)
        self.altisbt.setObjectName("altisbt")
        self.hzsbt = QtWidgets.QLabel(self.centralwidget)
        self.hzsbt.setGeometry(QtCore.QRect(80, 170, 161, 151))
        self.hzsbt.setText("")
        self.hzsbt.setPixmap(QtGui.QPixmap("hizsbt.png"))
        self.hzsbt.setScaledContents(True)
        self.hzsbt.setObjectName("hzsbt")
        self.altiibre = QtWidgets.QLabel(self.centralwidget)
        self.altiibre.setGeometry(QtCore.QRect(620, 180, 141, 141))
        self.altiibre.setText("")
        self.altiibre.setPixmap(QtGui.QPixmap.fromImage(altime))
        self.altiibre.setScaledContents(True)
        self.altiibre.setObjectName("altiibre")
        self.drmcyro = QtWidgets.QLabel(self.centralwidget)
        self.drmcyro.setGeometry(QtCore.QRect(360, 170, 141, 131))
        self.drmcyro.setText("")
        self.drmcyro.setPixmap(QtGui.QPixmap("durumcyro.png"))
        self.drmcyro.setScaledContents(True)
        self.drmcyro.setObjectName("drmcyro")
        self.drmcyroynr = QtWidgets.QLabel(self.centralwidget)
        self.drmcyroynr.setGeometry(QtCore.QRect(360, 170, 141, 131))
        self.drmcyroynr.setText("")
        self.drmcyroynr.setPixmap(QtGui.QPixmap.fromImage(drmcyro))
        self.drmcyroynr.setScaledContents(True)
        self.drmcyroynr.setObjectName("drmcyroynr")
        self.hzibre = QtWidgets.QLabel(self.centralwidget)
        self.hzibre.setGeometry(QtCore.QRect(80, 170, 161, 151))
        self.hzibre.setText("")
        self.hzibre.setPixmap(QtGui.QPixmap.fromImage(hzgos))
        self.hzibre.setScaledContents(True)
        self.hzibre.setObjectName("hzibre")
        self.dkyhzgossbt = QtWidgets.QLabel(self.centralwidget)
        self.dkyhzgossbt.setGeometry(QtCore.QRect(600, 420, 151, 141))
        self.dkyhzgossbt.setText("")
        self.dkyhzgossbt.setPixmap(QtGui.QPixmap("dikeyhiz.png"))
        self.dkyhzgossbt.setScaledContents(True)
        self.dkyhzgossbt.setObjectName("dkyhzgossbt")
        self.dkhzibre = QtWidgets.QLabel(self.centralwidget)
        self.dkhzibre.setGeometry(QtCore.QRect(600, 420, 151, 141))
        self.dkhzibre.setText("")
        self.dkhzibre.setPixmap(QtGui.QPixmap.fromImage(dkyhz))
        self.dkhzibre.setScaledContents(True)
        self.dkhzibre.setObjectName("dkhzibre")
        self.istkmgryosbt = QtWidgets.QLabel(self.centralwidget)
        self.istkmgryosbt.setGeometry(QtCore.QRect(340, 430, 151, 151))
        self.istkmgryosbt.setText("")
        self.istkmgryosbt.setPixmap(QtGui.QPixmap("istksbt.png"))
        self.istkmgryosbt.setScaledContents(True)
        self.istkmgryosbt.setObjectName("istkmgryosbt")
        self.istikmoynar = QtWidgets.QLabel(self.centralwidget)
        self.istikmoynar.setGeometry(QtCore.QRect(340, 430, 151, 151))
        self.istikmoynar.setText("")
        self.istikmoynar.setPixmap(QtGui.QPixmap.fromImage(istk))
        self.istikmoynar.setScaledContents(True)
        self.istikmoynar.setObjectName("istikmoynar")
        self.pslsbt = QtWidgets.QLabel(self.centralwidget)
        self.pslsbt.setGeometry(QtCore.QRect(90, 430, 141, 141))
        self.pslsbt.setText("")
        self.pslsbt.setPixmap(QtGui.QPixmap("pslsbt.png"))
        self.pslsbt.setScaledContents(True)
        self.pslsbt.setWordWrap(False)
        self.pslsbt.setOpenExternalLinks(False)
        self.pslsbt.setObjectName("pslsbt")
        self.pslibreoynr = QtWidgets.QLabel(self.centralwidget)
        self.pslibreoynr.setGeometry(QtCore.QRect(152, 472, 21, 51))
        self.pslibreoynr.setText("")
        self.pslibreoynr.setPixmap(QtGui.QPixmap.fromImage(psla))
        self.pslibreoynr.setScaledContents(True)
        self.pslibreoynr.setObjectName("pslibreoynr")
        self.volt = QtWidgets.QLCDNumber(self.centralwidget)
        self.volt.setGeometry(QtCore.QRect(900, 30, 171, 41))
        self.volt.setStyleSheet("color: rgb(211, 215, 207);")
        self.volt.setObjectName("volt")
        self.volt.setProperty("intValue", v)

        self.armm = QtWidgets.QLCDNumber(self.centralwidget)
        self.armm.setGeometry(QtCore.QRect(1150, 40, 100, 25))
        self.armm.setStyleSheet("color: rgb(211, 215, 207);")
        self.armm.setObjectName("armm")
        self.armm.setProperty("intValue", k)

        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Setting up thread
        self.worker = WidgetUpdater()
        self.worker.updateWidgetsSignal.connect(self.updateWidgets)

        self.thread = QtCore.QThread()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.thread.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.hizyazi.setText(_translate("MainWindow", "HIZ GÖSTERGESİ"))
        self.drmguroyazi.setText(_translate("MainWindow", "DURUM CAYROSU"))
        self.altiyazi.setText(_translate("MainWindow", "ALTİMETRE"))
        self.pusulayazi.setText(_translate("MainWindow", "PUSULA"))
        self.vayroyazi.setText(_translate("MainWindow", "DİKEY HIZ GÖSTERGESİ"))
        self.istikametyazi.setText(_translate("MainWindow", "İSTİKAMET CAYROSU"))
        

    @QtCore.pyqtSlot(list)
    def updateWidgets(self, values:list):
        print("DEBUG: Main thread: Setting pixmap for altiibre: ", alti(values[2]))
        #TO-DO: Update all widgets  -> THIS CODE RUNS IN MAIN THREAD

        pixmap0=QtGui.QPixmap.fromImage(hiz(values[0]))
        self.hzibre.setPixmap(pixmap0)

        pixmap1 = QtGui.QPixmap.fromImage(durum(values[1]))
        self.drmcyroynr.setPixmap(pixmap1)

        pixmap2 = QtGui.QPixmap.fromImage(alti(values[2]))
        self.altiibre.setPixmap(pixmap2)

        pixmap3 = QtGui.QPixmap.fromImage(pusula(values[3]))
        self.pslibreoynr.setPixmap(pixmap3)

        pixmap4 = QtGui.QPixmap.fromImage(istik(values[4]))
        self.istikmoynar.setPixmap(pixmap4)

        pixmap5 = QtGui.QPixmap.fromImage(dikey(values[5]))
        self.dkhzibre.setPixmap(pixmap5)

        self.volt.setProperty("intValue",values[6])	

        self.armm.setProperty("intValue",values[7])
	

        # hiz(values[0])
        # durum(values[1])
        # alti(values[2])
        # pusula(values[3])
        # istik(values[4])
        # dikey(values[5])

class WidgetUpdater(QtCore.QObject):
    updateWidgetsSignal = QtCore.pyqtSignal(list)

    def __init__(self):
        super().__init__()

    def run(self):
        #TO-DO: update widgets -> THIS CODE RUNS IN PARALLEL THREAD
        while True:
            a = vehicle.groundspeed * -20 ### burda x y z eksenleri olabilir teste göre ayarlıcaz
            b = vehicle.gimbal._vehicle._roll *-55 ## roll değeri ile yapılacak roll komutu emin olmamakla birlikte bu komut

            c = vehicle.location.global_frame.alt  ## teste göre katsayı ayarlıcaz
            d = vehicle.heading * -1 ## 0 ila 360 arası veriyor pusulaya göre ayarlancak
            e = vehicle.heading * -1 ## drone yönünü gösteriyor yukarıyla aynı olacak
            f = vehicle.velocity  ## irtifa olarak veriyor değerine bakıp açı kat sayısına evrilecek   
            v = vehicle.battery.voltage
            k = vehicle.armed
            
           

            print(f"Debug: Worker thread: gimbal is: ", b)

            self.updateWidgetsSignal.emit([a,b,c,d,e,f[2],v,k])
            time.sleep(0.7)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

