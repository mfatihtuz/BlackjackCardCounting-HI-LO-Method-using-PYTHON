import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QMessageBox

class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Text, QtCore.Qt.red)
        self.newfont = QtGui.QFont("Courier New", 20, QtGui.QFont.Bold)
        self.newfont2 = QtGui.QFont("Courier New", 30, QtGui.QFont.Bold)
        self.butFont = QtGui.QFont("Helvetica", 15)
        self.creatorFont = QtGui.QFont("Helvetica", 10)
        self.butFont2 = QtGui.QFont("Arial", 15)
        self.butFont3 = QtGui.QFont("Tahoma", 12, QtGui.QFont.Bold)

        self.yazı_alanı = QtWidgets.QLabel("YENİ ELE BAŞLANIYOR...")
        self.yazı_alanı.setAlignment(Qt.AlignCenter)
        self.yazı_alanı.setFont(self.newfont)

        self.counts = QtWidgets.QLabel("")
        self.counts.setAlignment(Qt.AlignCenter)
        self.counts.setStyleSheet("color: darkred;")
        self.counts.setFont(self.newfont2)

        self.butAs = QtWidgets.QPushButton("")
        self.butAs.setStyleSheet("QPushButton{background: transparent;}")
        self.butAs.setIcon(QtGui.QIcon('Card Photos/ACES.png'))
        self.butAs.setIconSize(QtCore.QSize(64, 64))

        self.butPapaz = QtWidgets.QPushButton("")
        self.butPapaz
        self.butPapaz.setStyleSheet("QPushButton{background: transparent;}")
        self.butPapaz.setIcon(QtGui.QIcon('Card Photos/KING.png'))
        self.butPapaz.setIconSize(QtCore.QSize(64, 64))

        self.butKız = QtWidgets.QPushButton("")
        self.butKız.setStyleSheet("QPushButton{background: transparent;}")
        self.butKız.setIcon(QtGui.QIcon('Card Photos/QUEEN.png'))
        self.butKız.setIconSize(QtCore.QSize(64, 64))

        self.butVale = QtWidgets.QPushButton("")
        self.butVale.setStyleSheet("QPushButton{background: transparent;}")
        self.butVale.setIcon(QtGui.QIcon('Card Photos/VALE.png'))
        self.butVale.setIconSize(QtCore.QSize(64, 64))

        self.but10 = QtWidgets.QPushButton("")
        self.but10.setStyleSheet("QPushButton{background: transparent;}")
        self.but10.setIcon(QtGui.QIcon('Card Photos/TEN.png'))
        self.but10.setIconSize(QtCore.QSize(64, 64))

        self.but9 = QtWidgets.QPushButton("")
        self.but9.setStyleSheet("QPushButton{background: transparent;}")
        self.but9.setIcon(QtGui.QIcon('Card Photos/NINE.png'))
        self.but9.setIconSize(QtCore.QSize(64, 64))

        self.but8 = QtWidgets.QPushButton("")
        self.but8.setStyleSheet("QPushButton{background: transparent;}")
        self.but8.setIcon(QtGui.QIcon('Card Photos/EIGHT.png'))
        self.but8.setIconSize(QtCore.QSize(64, 64))

        self.but7 = QtWidgets.QPushButton("")
        self.but7.setStyleSheet("QPushButton{background: transparent;}")
        self.but7.setIcon(QtGui.QIcon('Card Photos/SEVEN.png'))
        self.but7.setIconSize(QtCore.QSize(64, 64))

        self.but6 = QtWidgets.QPushButton("")
        self.but6.setStyleSheet("QPushButton{background: transparent;}")
        self.but6.setIcon(QtGui.QIcon('Card Photos/SIX.png'))
        self.but6.setIconSize(QtCore.QSize(64, 64))

        self.but5 = QtWidgets.QPushButton("")
        self.but5.setStyleSheet("QPushButton{background: transparent;}")
        self.but5.setIcon(QtGui.QIcon('Card Photos/FIVE.png'))
        self.but5.setIconSize(QtCore.QSize(64, 64))

        self.but4 = QtWidgets.QPushButton("")
        self.but4.setStyleSheet("QPushButton{background: transparent;}")
        self.but4.setIcon(QtGui.QIcon('Card Photos/FOUR.png'))
        self.but4.setIconSize(QtCore.QSize(64, 64))

        self.but3 = QtWidgets.QPushButton("")
        self.but3.setStyleSheet("QPushButton{background: transparent;}")
        self.but3.setIcon(QtGui.QIcon('Card Photos/THREE.png'))
        self.but3.setIconSize(QtCore.QSize(64, 64))

        self.but2 = QtWidgets.QPushButton("")
        self.but2.setStyleSheet("QPushButton{background: transparent;}")
        self.but2.setIcon(QtGui.QIcon('Card Photos/TWO.png'))
        self.but2.setIconSize(QtCore.QSize(64, 64))


        self.butReset = QtWidgets.QPushButton("RESET")
        self.butUndo = QtWidgets.QPushButton("Geri Al")
        self.butRedo = QtWidgets.QPushButton("İleri Al")

        self.labelAs = QtWidgets.QLabel("A : 32")
        self.labelAs.setAlignment(Qt.AlignCenter)
        self.labelAs.setStyleSheet('QLabel {background-color: yellow; color : black }')
        self.labelPapaz = QtWidgets.QLabel("K : 32")
        self.labelPapaz.setAlignment(Qt.AlignCenter)
        self.labelPapaz.setStyleSheet('QLabel {background-color: yellow; color : black }')
        self.labelKız = QtWidgets.QLabel("Q : 32")
        self.labelKız.setAlignment(Qt.AlignCenter)
        self.labelKız.setStyleSheet('QLabel {background-color: yellow; color : black }')
        self.labelVale = QtWidgets.QLabel("J : 32")
        self.labelVale.setAlignment(Qt.AlignCenter)
        self.labelVale.setStyleSheet('QLabel {background-color: yellow; color : black }')
        self.label10 = QtWidgets.QLabel("10 : 32")
        self.label10.setAlignment(Qt.AlignCenter)
        self.label10.setStyleSheet('QLabel {background-color: yellow; color : black }')
        self.label9 = QtWidgets.QLabel("9 : 32")
        self.label9.setAlignment(Qt.AlignCenter)
        self.label9.setStyleSheet('QLabel {background-color: yellow; color : black }')
        self.label8 = QtWidgets.QLabel("8 : 32")
        self.label8.setAlignment(Qt.AlignCenter)
        self.label8.setStyleSheet('QLabel {background-color: yellow; color : black }')
        self.label7 = QtWidgets.QLabel("7 : 32")
        self.label7.setAlignment(Qt.AlignCenter)
        self.label7.setStyleSheet('QLabel {background-color: yellow; color : black }')
        self.label6 = QtWidgets.QLabel("6 : 32")
        self.label6.setAlignment(Qt.AlignCenter)
        self.label6.setStyleSheet('QLabel {background-color: yellow; color : black }')
        self.label5 = QtWidgets.QLabel("5 : 32")
        self.label5.setAlignment(Qt.AlignCenter)
        self.label5.setStyleSheet('QLabel {background-color: yellow; color : black }')
        self.label4 = QtWidgets.QLabel("4 : 32")
        self.label4.setAlignment(Qt.AlignCenter)
        self.label4.setStyleSheet('QLabel {background-color: yellow; color : black }')
        self.label3 = QtWidgets.QLabel("3 : 32")
        self.label3.setAlignment(Qt.AlignCenter)
        self.label3.setStyleSheet('QLabel {background-color: yellow; color : black }')
        self.label2 = QtWidgets.QLabel("2 : 32")
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setStyleSheet('QLabel {background-color: yellow; color : black }')


        self.butAs.setFont(self.butFont2)
        self.butPapaz.setFont(self.butFont2)
        self.butKız.setFont(self.butFont2)
        self.butVale.setFont(self.butFont2)
        self.but10.setFont(self.butFont2)
        self.but9.setFont(self.butFont2)
        self.but8.setFont(self.butFont2)
        self.but7.setFont(self.butFont2)
        self.but6.setFont(self.butFont2)
        self.but5.setFont(self.butFont2)
        self.but4.setFont(self.butFont2)
        self.but3.setFont(self.butFont2)
        self.but2.setFont(self.butFont2)

        self.labelAs.setFont(self.butFont3)
        self.labelPapaz.setFont(self.butFont3)
        self.labelKız.setFont(self.butFont3)
        self.labelVale.setFont(self.butFont3)
        self.label10.setFont(self.butFont3)
        self.label9.setFont(self.butFont3)
        self.label8.setFont(self.butFont3)
        self.label7.setFont(self.butFont3)
        self.label6.setFont(self.butFont3)
        self.label5.setFont(self.butFont3)
        self.label4.setFont(self.butFont3)
        self.label3.setFont(self.butFont3)
        self.label2.setFont(self.butFont3)


        self.butReset.setFont(self.butFont)
        self.butReset.setStyleSheet('QPushButton {background-color: black; color: red;}')

        self.say = 0
        self.cards = 416
        self.gecici = 0
        self.deste = 8
        self.durum = 0
        self.bettingbirim = 35

        self.asSayisi = 32
        self.papazSayisi = 32
        self.kizSayisi = 32
        self.valeSayisi = 32
        self.onSayisi = 32
        self.dokuzSayisi = 32
        self.sekizSayisi = 32
        self.yediSayisi = 32
        self.altiSayisi = 32
        self.besSayisi = 32
        self.dortSayisi = 32
        self.ucSayisi = 32
        self.ikiSayisi = 32

        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(self.butAs)
        h_box.addWidget(self.butPapaz)
        h_box.addWidget(self.butKız)
        h_box.addWidget(self.butVale)
        h_box.addWidget(self.but10)
        h_box.addWidget(self.but9)
        h_box.addWidget(self.but8)
        h_box.addWidget(self.but7)
        h_box.addWidget(self.but6)
        h_box.addWidget(self.but5)
        h_box.addWidget(self.but4)
        h_box.addWidget(self.but3)
        h_box.addWidget(self.but2)

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addWidget(self.labelAs)
        h_box2.addWidget(self.labelPapaz)
        h_box2.addWidget(self.labelKız)
        h_box2.addWidget(self.labelVale)
        h_box2.addWidget(self.label10)
        h_box2.addWidget(self.label9)
        h_box2.addWidget(self.label8)
        h_box2.addWidget(self.label7)
        h_box2.addWidget(self.label6)
        h_box2.addWidget(self.label5)
        h_box2.addWidget(self.label4)
        h_box2.addWidget(self.label3)
        h_box2.addWidget(self.label2)

        self.creator = QtWidgets.QLabel("Created by MFT - 2019 ©")
        self.creatorSTR = "Created by MFT"
        self.creator.setAlignment(Qt.AlignCenter)
        self.creator.setFont(self.creatorFont)
        # self.mySTR = ""
        # for i in range (len(self.creatorSTR)):
        #     self.tempSTR = self.creatorSTR[i] + "\n"
        #     self.mySTR += self.tempSTR
        #     self.creator.setText(self.mySTR)
        #
        # h_box3 = QtWidgets.QHBoxLayout()
        # h_box3.addWidget(self.creator)
        # h_box3.addStretch()
        # h_box3.addWidget(self.yazı_alanı)
        # h_box3.addStretch()
        # h_box3.addWidget(self.creator)


        v_box2 = QtWidgets.QVBoxLayout()
        v_box2.addStretch()
        v_box2.addLayout(h_box)
        v_box2.addLayout(h_box2)
        #v_box2.addLayout(h_box3)
        v_box2.addWidget(self.yazı_alanı)
        v_box2.addStretch()
        v_box2.addWidget(self.counts)
        v_box2.addStretch()
        v_box2.addWidget(self.butReset)
        v_box2.addStretch()
        v_box2.addWidget(self.creator)
        v_box2.addStretch()


        self.setLayout(v_box2)

        self.butAs.clicked.connect(self.clickAs)
        self.butPapaz.clicked.connect(self.clickPapaz)
        self.butKız.clicked.connect(self.clickKiz)
        self.butVale.clicked.connect(self.clickVale)
        self.but10.clicked.connect(self.clickOn)
        self.but9.clicked.connect(self.clickDokuz)
        self.but8.clicked.connect(self.clickSekiz)
        self.but7.clicked.connect(self.clickYedi)
        self.but6.clicked.connect(self.clickAlti)
        self.but5.clicked.connect(self.clickBes)
        self.but4.clicked.connect(self.clickDort)
        self.but3.clicked.connect(self.clickUc)
        self.but2.clicked.connect(self.clickIki)
        self.butReset.clicked.connect(self.clickReset)


        self.show()
    def clickAs(self):
        self.say -= 1
        self.cards -= 1
        self.gecici = (self.cards // 26)
        self.deste = self.gecici / 2 + 0.5
        self.durum = round(self.say / self.deste, 3)
        self.asSayisi -= 1
        if (self.asSayisi>0):
            self.labelAs.setText("A : " + str(self.asSayisi) + "\n% " + str(round((self.asSayisi / self.cards) * 100, 2)))
            self.labelPapaz.setText(
                "K : " + str(self.papazSayisi) + "\n% " + str(round((self.papazSayisi / self.cards) * 100, 2)))
            self.labelKız.setText("Q : " + str(self.kizSayisi) + "\n% " + str(round((self.kizSayisi / self.cards) * 100, 2)))
            self.labelVale.setText("J : " + str(self.valeSayisi) + "\n% " + str(round((self.valeSayisi / self.cards) * 100, 2)))
            self.label10.setText("10 : " + str(self.onSayisi) + "\n% " + str(round((self.onSayisi / self.cards) * 100, 2)))
            self.label9.setText("9 : " + str(self.dokuzSayisi) + "\n% " + str(round((self.dokuzSayisi / self.cards) * 100, 2)))
            self.label8.setText("8 : " + str(self.sekizSayisi) + "\n% " + str(round((self.sekizSayisi / self.cards) * 100, 2)))
            self.label7.setText("7 : " + str(self.yediSayisi) + "\n% " + str(round((self.yediSayisi / self.cards) * 100, 2)))
            self.label6.setText("6 : " + str(self.altiSayisi) + "\n% " + str(round((self.altiSayisi / self.cards) * 100, 2)))
            self.label5.setText("5 : " + str(self.besSayisi) + "\n% " + str(round((self.besSayisi / self.cards) * 100, 2)))
            self.label4.setText("4 : " + str(self.dortSayisi) + "\n% " + str(round((self.dortSayisi / self.cards) * 100, 2)))
            self.label3.setText("3 : " + str(self.ucSayisi) + "\n% " + str(round((self.ucSayisi / self.cards) * 100, 2)))
            self.label2.setText("2 : " + str(self.ikiSayisi) + "\n% " + str(round((self.ikiSayisi / self.cards) * 100, 2)))
            self.counts.setText("\nAkan Sayaç (Running Count) : " + str(self.say) + "\nAsıl Sayaç (True Count) : " + str(self.durum))
            if self.durum>1:
                self.yazı_alanı.setText("\nKalan Kart Sayısı : " + str(self.cards) + "\nKalan Yaklaşık Deste Sayısı : " +
                                        str(self.deste) + "\n\nEKSTRA yapılabilecek bahis sayısı " + str((round(self.durum, 0) - 1)) + " birim" +
                                        "\n\n10'lu gelme ihtimali --> % " +
                                        str(round(((self.papazSayisi + self.kizSayisi + self.valeSayisi + self.onSayisi) / self.cards)*100,2))
                                        )
            else:
                self.yazı_alanı.setText(
                    "\nKalan Kart Sayısı : " + str(self.cards) + "\nKalan Yaklaşık Deste Sayısı : " +
                    str(self.deste) + "\n\nEKSTRA yapılabilecek bahis sayısı 0.0 birim" +
                    "\n\n10'lu gelme ihtimali --> % " +
                    str(round(
                        ((self.papazSayisi + self.kizSayisi + self.valeSayisi + self.onSayisi) / self.cards) * 100, 2))
                    )
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Bu deste yenilenmediği sürece A kartı çıkmayacak!")
            msg.setWindowTitle("KART BİTTİ")
            msg.exec_()


    def clickPapaz(self):
        self.say -= 1
        self.cards -= 1
        self.gecici = (self.cards // 26)
        self.deste = self.gecici / 2 + 0.5
        self.durum = round(self.say / self.deste, 3)
        self.papazSayisi -= 1

        if (self.papazSayisi>0):
            self.labelAs.setText("A : " + str(self.asSayisi) + "\n% " + str(round((self.asSayisi / self.cards) * 100, 2)))
            self.labelPapaz.setText(
                "K : " + str(self.papazSayisi) + "\n% " + str(round((self.papazSayisi / self.cards) * 100, 2)))
            self.labelKız.setText("Q : " + str(self.kizSayisi) + "\n% " + str(round((self.kizSayisi / self.cards) * 100, 2)))
            self.labelVale.setText("J : " + str(self.valeSayisi) + "\n% " + str(round((self.valeSayisi / self.cards) * 100, 2)))
            self.label10.setText("10 : " + str(self.onSayisi) + "\n% " + str(round((self.onSayisi / self.cards) * 100, 2)))
            self.label9.setText("9 : " + str(self.dokuzSayisi) + "\n% " + str(round((self.dokuzSayisi / self.cards) * 100, 2)))
            self.label8.setText("8 : " + str(self.sekizSayisi) + "\n% " + str(round((self.sekizSayisi / self.cards) * 100, 2)))
            self.label7.setText("7 : " + str(self.yediSayisi) + "\n% " + str(round((self.yediSayisi / self.cards) * 100, 2)))
            self.label6.setText("6 : " + str(self.altiSayisi) + "\n% " + str(round((self.altiSayisi / self.cards) * 100, 2)))
            self.label5.setText("5 : " + str(self.besSayisi) + "\n% " + str(round((self.besSayisi / self.cards) * 100, 2)))
            self.label4.setText("4 : " + str(self.dortSayisi) + "\n% " + str(round((self.dortSayisi / self.cards) * 100, 2)))
            self.label3.setText("3 : " + str(self.ucSayisi) + "\n% " + str(round((self.ucSayisi / self.cards) * 100, 2)))
            self.label2.setText("2 : " + str(self.ikiSayisi) + "\n% " + str(round((self.ikiSayisi / self.cards) * 100, 2)))
            self.counts.setText("\nAkan Sayaç (Running Count) : " + str(self.say) + "\nAsıl Sayaç (True Count) : " + str(self.durum))
            if self.durum > 1:
                self.yazı_alanı.setText(
                    "\nKalan Kart Sayısı : " + str(self.cards) + "\nKalan Yaklaşık Deste Sayısı : " +
                    str(self.deste) + "\n\nEKSTRA yapılabilecek bahis sayısı " + str((round(self.durum, 0) - 1)) + " birim" +
                    "\n\n10'lu gelme ihtimali --> % " +
                    str(round(
                        ((self.papazSayisi + self.kizSayisi + self.valeSayisi + self.onSayisi) / self.cards) * 100, 2))
                    )
            else:
                self.yazı_alanı.setText(
                    "\nKalan Kart Sayısı : " + str(self.cards) + "\nKalan Yaklaşık Deste Sayısı : " +
                    str(self.deste) + "\n\nEKSTRA yapılabilecek bahis sayısı 0.0 birim" +
                    "\n\n10'lu gelme ihtimali --> % " +
                    str(round(
                        ((self.papazSayisi + self.kizSayisi + self.valeSayisi + self.onSayisi) / self.cards) * 100, 2))
                )
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Bu deste yenilenmediği sürece K kartı çıkmayacak!")
            msg.setWindowTitle("KART BİTTİ")
            msg.exec_()

    def clickKiz(self):
        self.say -= 1
        self.cards -= 1
        self.gecici = (self.cards // 26)
        self.deste = self.gecici / 2 + 0.5
        self.durum = round(self.say / self.deste, 3)
        self.kizSayisi -= 1
        if (self.kizSayisi > 0):
            self.labelAs.setText(
                "A : " + str(self.asSayisi) + "\n% " + str(round((self.asSayisi / self.cards) * 100, 2)))
            self.labelPapaz.setText(
                "K : " + str(self.papazSayisi) + "\n% " + str(round((self.papazSayisi / self.cards) * 100, 2)))
            self.labelKız.setText(
                "Q : " + str(self.kizSayisi) + "\n% " + str(round((self.kizSayisi / self.cards) * 100, 2)))
            self.labelVale.setText(
                "J : " + str(self.valeSayisi) + "\n% " + str(round((self.valeSayisi / self.cards) * 100, 2)))
            self.label10.setText(
                "10 : " + str(self.onSayisi) + "\n% " + str(round((self.onSayisi / self.cards) * 100, 2)))
            self.label9.setText(
                "9 : " + str(self.dokuzSayisi) + "\n% " + str(round((self.dokuzSayisi / self.cards) * 100, 2)))
            self.label8.setText(
                "8 : " + str(self.sekizSayisi) + "\n% " + str(round((self.sekizSayisi / self.cards) * 100, 2)))
            self.label7.setText(
                "7 : " + str(self.yediSayisi) + "\n% " + str(round((self.yediSayisi / self.cards) * 100, 2)))
            self.label6.setText(
                "6 : " + str(self.altiSayisi) + "\n% " + str(round((self.altiSayisi / self.cards) * 100, 2)))
            self.label5.setText(
                "5 : " + str(self.besSayisi) + "\n% " + str(round((self.besSayisi / self.cards) * 100, 2)))
            self.label4.setText(
                "4 : " + str(self.dortSayisi) + "\n% " + str(round((self.dortSayisi / self.cards) * 100, 2)))
            self.label3.setText(
                "3 : " + str(self.ucSayisi) + "\n% " + str(round((self.ucSayisi / self.cards) * 100, 2)))
            self.label2.setText(
                "2 : " + str(self.ikiSayisi) + "\n% " + str(round((self.ikiSayisi / self.cards) * 100, 2)))
            self.counts.setText("\nAkan Sayaç (Running Count) : " + str(self.say) + "\nAsıl Sayaç (True Count) : " + str(self.durum))
            if self.durum > 1:
                self.yazı_alanı.setText(
                    "\nKalan Kart Sayısı : " + str(self.cards) + "\nKalan Yaklaşık Deste Sayısı : " +
                    str(self.deste) + "\n\nEKSTRA yapılabilecek bahis sayısı " + str((round(self.durum, 0) - 1)) + " birim" +
                    "\n\n10'lu gelme ihtimali --> % " +
                    str(round(
                        ((self.papazSayisi + self.kizSayisi + self.valeSayisi + self.onSayisi) / self.cards) * 100, 2))
                    )
            else:
                self.yazı_alanı.setText(
                    "\nKalan Kart Sayısı : " + str(self.cards) + "\nKalan Yaklaşık Deste Sayısı : " +
                    str(self.deste) + "\n\nEKSTRA yapılabilecek bahis sayısı 0.0 birim" +
                    "\n\n10'lu gelme ihtimali --> % " +
                    str(round(
                        ((self.papazSayisi + self.kizSayisi + self.valeSayisi + self.onSayisi) / self.cards) * 100, 2))
                )
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Bu deste yenilenmediği sürece Q kartı çıkmayacak!")
            msg.setWindowTitle("KART BİTTİ")
            msg.exec_()

    def clickVale(self):
        self.say -= 1
        self.cards -= 1
        self.gecici = (self.cards // 26)
        self.deste = self.gecici / 2 + 0.5
        self.durum = round(self.say / self.deste, 3)
        self.valeSayisi -= 1
        if (self.valeSayisi > 0):
            self.labelAs.setText(
                "A : " + str(self.asSayisi) + "\n% " + str(round((self.asSayisi / self.cards) * 100, 2)))
            self.labelPapaz.setText(
                "K : " + str(self.papazSayisi) + "\n% " + str(round((self.papazSayisi / self.cards) * 100, 2)))
            self.labelKız.setText(
                "Q : " + str(self.kizSayisi) + "\n% " + str(round((self.kizSayisi / self.cards) * 100, 2)))
            self.labelVale.setText(
                "J : " + str(self.valeSayisi) + "\n% " + str(round((self.valeSayisi / self.cards) * 100, 2)))
            self.label10.setText(
                "10 : " + str(self.onSayisi) + "\n% " + str(round((self.onSayisi / self.cards) * 100, 2)))
            self.label9.setText(
                "9 : " + str(self.dokuzSayisi) + "\n% " + str(round((self.dokuzSayisi / self.cards) * 100, 2)))
            self.label8.setText(
                "8 : " + str(self.sekizSayisi) + "\n% " + str(round((self.sekizSayisi / self.cards) * 100, 2)))
            self.label7.setText(
                "7 : " + str(self.yediSayisi) + "\n% " + str(round((self.yediSayisi / self.cards) * 100, 2)))
            self.label6.setText(
                "6 : " + str(self.altiSayisi) + "\n% " + str(round((self.altiSayisi / self.cards) * 100, 2)))
            self.label5.setText(
                "5 : " + str(self.besSayisi) + "\n% " + str(round((self.besSayisi / self.cards) * 100, 2)))
            self.label4.setText(
                "4 : " + str(self.dortSayisi) + "\n% " + str(round((self.dortSayisi / self.cards) * 100, 2)))
            self.label3.setText(
                "3 : " + str(self.ucSayisi) + "\n% " + str(round((self.ucSayisi / self.cards) * 100, 2)))
            self.label2.setText(
                "2 : " + str(self.ikiSayisi) + "\n% " + str(round((self.ikiSayisi / self.cards) * 100, 2)))
            self.counts.setText("\nAkan Sayaç (Running Count) : " + str(self.say) + "\nAsıl Sayaç (True Count) : " + str(self.durum))
            if self.durum > 1:
                self.yazı_alanı.setText(
                    "\nKalan Kart Sayısı : " + str(self.cards) + "\nKalan Yaklaşık Deste Sayısı : " +
                    str(self.deste) + "\n\nEKSTRA yapılabilecek bahis sayısı " + str((round(self.durum, 0) - 1)) + " birim" +
                    "\n\n10'lu gelme ihtimali --> % " +
                    str(round(
                        ((self.papazSayisi + self.kizSayisi + self.valeSayisi + self.onSayisi) / self.cards) * 100, 2))
                    )
            else:
                self.yazı_alanı.setText(
                    "\nKalan Kart Sayısı : " + str(self.cards) + "\nKalan Yaklaşık Deste Sayısı : " +
                    str(self.deste) + "\n\nEKSTRA yapılabilecek bahis sayısı 0.0 birim" +
                    "\n\n10'lu gelme ihtimali --> % " +
                    str(round(
                        ((self.papazSayisi + self.kizSayisi + self.valeSayisi + self.onSayisi) / self.cards) * 100, 2))
                )
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Bu deste yenilenmediği sürece J kartı çıkmayacak!")
            msg.setWindowTitle("KART BİTTİ")
            msg.exec_()

    def clickOn(self):
        self.say -= 1
        self.cards -= 1
        self.gecici = (self.cards // 26)
        self.deste = self.gecici / 2 + 0.5
        self.durum = round(self.say / self.deste, 3)
        self.onSayisi -= 1
        if (self.onSayisi > 0):
            self.labelAs.setText(
                "A : " + str(self.asSayisi) + "\n% " + str(round((self.asSayisi / self.cards) * 100, 2)))
            self.labelPapaz.setText(
                "K : " + str(self.papazSayisi) + "\n% " + str(round((self.papazSayisi / self.cards) * 100, 2)))
            self.labelKız.setText(
                "Q : " + str(self.kizSayisi) + "\n% " + str(round((self.kizSayisi / self.cards) * 100, 2)))
            self.labelVale.setText(
                "J : " + str(self.valeSayisi) + "\n% " + str(round((self.valeSayisi / self.cards) * 100, 2)))
            self.label10.setText(
                "10 : " + str(self.onSayisi) + "\n% " + str(round((self.onSayisi / self.cards) * 100, 2)))
            self.label9.setText(
                "9 : " + str(self.dokuzSayisi) + "\n% " + str(round((self.dokuzSayisi / self.cards) * 100, 2)))
            self.label8.setText(
                "8 : " + str(self.sekizSayisi) + "\n% " + str(round((self.sekizSayisi / self.cards) * 100, 2)))
            self.label7.setText(
                "7 : " + str(self.yediSayisi) + "\n% " + str(round((self.yediSayisi / self.cards) * 100, 2)))
            self.label6.setText(
                "6 : " + str(self.altiSayisi) + "\n% " + str(round((self.altiSayisi / self.cards) * 100, 2)))
            self.label5.setText(
                "5 : " + str(self.besSayisi) + "\n% " + str(round((self.besSayisi / self.cards) * 100, 2)))
            self.label4.setText(
                "4 : " + str(self.dortSayisi) + "\n% " + str(round((self.dortSayisi / self.cards) * 100, 2)))
            self.label3.setText(
                "3 : " + str(self.ucSayisi) + "\n% " + str(round((self.ucSayisi / self.cards) * 100, 2)))
            self.label2.setText(
                "2 : " + str(self.ikiSayisi) + "\n% " + str(round((self.ikiSayisi / self.cards) * 100, 2)))
            self.counts.setText("\nAkan Sayaç (Running Count) : " + str(self.say) + "\nAsıl Sayaç (True Count) : " + str(self.durum))
            if self.durum > 1:
                self.yazı_alanı.setText(
                    "\nKalan Kart Sayısı : " + str(self.cards) + "\nKalan Yaklaşık Deste Sayısı : " +
                    str(self.deste) + "\n\nEKSTRA yapılabilecek bahis sayısı " + str((round(self.durum, 0) - 1)) + " birim" +
                    "\n\n10'lu gelme ihtimali --> % " +
                    str(round(
                        ((self.papazSayisi + self.kizSayisi + self.valeSayisi + self.onSayisi) / self.cards) * 100, 2))
                    )
            else:
                self.yazı_alanı.setText(
                    "\nKalan Kart Sayısı : " + str(self.cards) + "\nKalan Yaklaşık Deste Sayısı : " +
                    str(self.deste) + "\n\nEKSTRA yapılabilecek bahis sayısı 0.0 birim" +
                    "\n\n10'lu gelme ihtimali --> % " +
                    str(round(
                        ((self.papazSayisi + self.kizSayisi + self.valeSayisi + self.onSayisi) / self.cards) * 100, 2))
                )
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Bu deste yenilenmediği sürece 10 kartı çıkmayacak!")
            msg.setWindowTitle("KART BİTTİ")
            msg.exec_()

    def clickDokuz(self):
        self.cards -= 1
        self.gecici = (self.cards // 26)
        self.deste = self.gecici / 2 + 0.5
        self.durum = round(self.say / self.deste, 3)
        self.dokuzSayisi -= 1
        if (self.dokuzSayisi > 0):
            self.labelAs.setText(
                "A : " + str(self.asSayisi) + "\n% " + str(round((self.asSayisi / self.cards) * 100, 2)))
            self.labelPapaz.setText(
                "K : " + str(self.papazSayisi) + "\n% " + str(round((self.papazSayisi / self.cards) * 100, 2)))
            self.labelKız.setText(
                "Q : " + str(self.kizSayisi) + "\n% " + str(round((self.kizSayisi / self.cards) * 100, 2)))
            self.labelVale.setText(
                "J : " + str(self.valeSayisi) + "\n% " + str(round((self.valeSayisi / self.cards) * 100, 2)))
            self.label10.setText(
                "10 : " + str(self.onSayisi) + "\n% " + str(round((self.onSayisi / self.cards) * 100, 2)))
            self.label9.setText(
                "9 : " + str(self.dokuzSayisi) + "\n% " + str(round((self.dokuzSayisi / self.cards) * 100, 2)))
            self.label8.setText(
                "8 : " + str(self.sekizSayisi) + "\n% " + str(round((self.sekizSayisi / self.cards) * 100, 2)))
            self.label7.setText(
                "7 : " + str(self.yediSayisi) + "\n% " + str(round((self.yediSayisi / self.cards) * 100, 2)))
            self.label6.setText(
                "6 : " + str(self.altiSayisi) + "\n% " + str(round((self.altiSayisi / self.cards) * 100, 2)))
            self.label5.setText(
                "5 : " + str(self.besSayisi) + "\n% " + str(round((self.besSayisi / self.cards) * 100, 2)))
            self.label4.setText(
                "4 : " + str(self.dortSayisi) + "\n% " + str(round((self.dortSayisi / self.cards) * 100, 2)))
            self.label3.setText(
                "3 : " + str(self.ucSayisi) + "\n% " + str(round((self.ucSayisi / self.cards) * 100, 2)))
            self.label2.setText(
                "2 : " + str(self.ikiSayisi) + "\n% " + str(round((self.ikiSayisi / self.cards) * 100, 2)))
            self.counts.setText("\nAkan Sayaç (Running Count) : " + str(self.say) + "\nAsıl Sayaç (True Count) : " + str(self.durum))
            if self.durum > 1:
                self.yazı_alanı.setText(
                    "\nKalan Kart Sayısı : " + str(self.cards) + "\nKalan Yaklaşık Deste Sayısı : " +
                    str(self.deste) + "\n\nEKSTRA yapılabilecek bahis sayısı " + str((round(self.durum, 0) - 1)) + " birim" +
                    "\n\n10'lu gelme ihtimali --> % " +
                    str(round(
                        ((self.papazSayisi + self.kizSayisi + self.valeSayisi + self.onSayisi) / self.cards) * 100, 2))
                    )
            else:
                self.yazı_alanı.setText(
                    "\nKalan Kart Sayısı : " + str(self.cards) + "\nKalan Yaklaşık Deste Sayısı : " +
                    str(self.deste) + "\n\nEKSTRA yapılabilecek bahis sayısı 0.0 birim" +
                    "\n\n10'lu gelme ihtimali --> % " +
                    str(round(
                        ((self.papazSayisi + self.kizSayisi + self.valeSayisi + self.onSayisi) / self.cards) * 100, 2))
                )
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Bu deste yenilenmediği sürece 9 kartı çıkmayacak!")
            msg.setWindowTitle("KART BİTTİ")
            msg.exec_()

    def clickSekiz(self):
        self.cards -= 1
        self.gecici = (self.cards // 26)
        self.deste = self.gecici / 2 + 0.5
        self.durum = round(self.say / self.deste, 3)
        self.sekizSayisi -= 1
        if (self.sekizSayisi > 0):
            self.labelAs.setText(
                "A : " + str(self.asSayisi) + "\n% " + str(round((self.asSayisi / self.cards) * 100, 2)))
            self.labelPapaz.setText(
                "K : " + str(self.papazSayisi) + "\n% " + str(round((self.papazSayisi / self.cards) * 100, 2)))
            self.labelKız.setText(
                "Q : " + str(self.kizSayisi) + "\n% " + str(round((self.kizSayisi / self.cards) * 100, 2)))
            self.labelVale.setText(
                "J : " + str(self.valeSayisi) + "\n% " + str(round((self.valeSayisi / self.cards) * 100, 2)))
            self.label10.setText(
                "10 : " + str(self.onSayisi) + "\n% " + str(round((self.onSayisi / self.cards) * 100, 2)))
            self.label9.setText(
                "9 : " + str(self.dokuzSayisi) + "\n% " + str(round((self.dokuzSayisi / self.cards) * 100, 2)))
            self.label8.setText(
                "8 : " + str(self.sekizSayisi) + "\n% " + str(round((self.sekizSayisi / self.cards) * 100, 2)))
            self.label7.setText(
                "7 : " + str(self.yediSayisi) + "\n% " + str(round((self.yediSayisi / self.cards) * 100, 2)))
            self.label6.setText(
                "6 : " + str(self.altiSayisi) + "\n% " + str(round((self.altiSayisi / self.cards) * 100, 2)))
            self.label5.setText(
                "5 : " + str(self.besSayisi) + "\n% " + str(round((self.besSayisi / self.cards) * 100, 2)))
            self.label4.setText(
                "4 : " + str(self.dortSayisi) + "\n% " + str(round((self.dortSayisi / self.cards) * 100, 2)))
            self.label3.setText(
                "3 : " + str(self.ucSayisi) + "\n% " + str(round((self.ucSayisi / self.cards) * 100, 2)))
            self.label2.setText(
                "2 : " + str(self.ikiSayisi) + "\n% " + str(round((self.ikiSayisi / self.cards) * 100, 2)))
            self.counts.setText("\nAkan Sayaç (Running Count) : " + str(self.say) + "\nAsıl Sayaç (True Count) : " + str(self.durum))
            if self.durum > 1:
                self.yazı_alanı.setText(
                    "\nKalan Kart Sayısı : " + str(self.cards) + "\nKalan Yaklaşık Deste Sayısı : " +
                    str(self.deste) + "\n\nEKSTRA yapılabilecek bahis sayısı " + str((round(self.durum, 0) - 1)) + " birim" +
                    "\n\n10'lu gelme ihtimali --> % " +
                    str(round(
                        ((self.papazSayisi + self.kizSayisi + self.valeSayisi + self.onSayisi) / self.cards) * 100, 2))
                    )
            else:
                self.yazı_alanı.setText(
                    "\nKalan Kart Sayısı : " + str(self.cards) + "\nKalan Yaklaşık Deste Sayısı : " +
                    str(self.deste) + "\n\nEKSTRA yapılabilecek bahis sayısı 0.0 birim" +
                    "\n\n10'lu gelme ihtimali --> % " +
                    str(round(
                        ((self.papazSayisi + self.kizSayisi + self.valeSayisi + self.onSayisi) / self.cards) * 100, 2))
                )
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Bu deste yenilenmediği sürece 8 kartı çıkmayacak!")
            msg.setWindowTitle("KART BİTTİ")
            msg.exec_()

    def clickYedi(self):
        self.cards -= 1
        self.gecici = (self.cards // 26)
        self.deste = self.gecici / 2 + 0.5
        self.durum = round(self.say / self.deste, 3)
        self.yediSayisi -= 1
        if (self.yediSayisi > 0):
            self.labelAs.setText(
                "A : " + str(self.asSayisi) + "\n% " + str(round((self.asSayisi / self.cards) * 100, 2)))
            self.labelPapaz.setText(
                "K : " + str(self.papazSayisi) + "\n% " + str(round((self.papazSayisi / self.cards) * 100, 2)))
            self.labelKız.setText(
                "Q : " + str(self.kizSayisi) + "\n% " + str(round((self.kizSayisi / self.cards) * 100, 2)))
            self.labelVale.setText(
                "J : " + str(self.valeSayisi) + "\n% " + str(round((self.valeSayisi / self.cards) * 100, 2)))
            self.label10.setText(
                "10 : " + str(self.onSayisi) + "\n% " + str(round((self.onSayisi / self.cards) * 100, 2)))
            self.label9.setText(
                "9 : " + str(self.dokuzSayisi) + "\n% " + str(round((self.dokuzSayisi / self.cards) * 100, 2)))
            self.label8.setText(
                "8 : " + str(self.sekizSayisi) + "\n% " + str(round((self.sekizSayisi / self.cards) * 100, 2)))
            self.label7.setText(
                "7 : " + str(self.yediSayisi) + "\n% " + str(round((self.yediSayisi / self.cards) * 100, 2)))
            self.label6.setText(
                "6 : " + str(self.altiSayisi) + "\n% " + str(round((self.altiSayisi / self.cards) * 100, 2)))
            self.label5.setText(
                "5 : " + str(self.besSayisi) + "\n% " + str(round((self.besSayisi / self.cards) * 100, 2)))
            self.label4.setText(
                "4 : " + str(self.dortSayisi) + "\n% " + str(round((self.dortSayisi / self.cards) * 100, 2)))
            self.label3.setText(
                "3 : " + str(self.ucSayisi) + "\n% " + str(round((self.ucSayisi / self.cards) * 100, 2)))
            self.label2.setText(
                "2 : " + str(self.ikiSayisi) + "\n% " + str(round((self.ikiSayisi / self.cards) * 100, 2)))
            self.counts.setText("\nAkan Sayaç (Running Count) : " + str(self.say) + "\nAsıl Sayaç (True Count) : " + str(self.durum))
            if self.durum > 1:
                self.yazı_alanı.setText(
                    "\nKalan Kart Sayısı : " + str(self.cards) + "\nKalan Yaklaşık Deste Sayısı : " +
                    str(self.deste) + "\n\nEKSTRA yapılabilecek bahis sayısı " + str((round(self.durum, 0) - 1)) + " birim" +
                    "\n\n10'lu gelme ihtimali --> % " +
                    str(round(
                        ((self.papazSayisi + self.kizSayisi + self.valeSayisi + self.onSayisi) / self.cards) * 100, 2))
                    )
            else:
                self.yazı_alanı.setText(
                    "\nKalan Kart Sayısı : " + str(self.cards) + "\nKalan Yaklaşık Deste Sayısı : " +
                    str(self.deste) + "\n\nEKSTRA yapılabilecek bahis sayısı 0.0 birim" +
                    "\n\n10'lu gelme ihtimali --> % " +
                    str(round(
                        ((self.papazSayisi + self.kizSayisi + self.valeSayisi + self.onSayisi) / self.cards) * 100, 2))
                )
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Bu deste yenilenmediği sürece 7 kartı çıkmayacak!")
            msg.setWindowTitle("KART BİTTİ")
            msg.exec_()

    def clickAlti(self):
        self.say += 1
        self.cards -= 1
        self.gecici = (self.cards // 26)
        self.deste = self.gecici / 2 + 0.5
        self.durum = round(self.say / self.deste, 3)
        self.altiSayisi -= 1
        if (self.altiSayisi > 0):
            self.labelAs.setText(
                "A : " + str(self.asSayisi) + "\n% " + str(round((self.asSayisi / self.cards) * 100, 2)))
            self.labelPapaz.setText(
                "K : " + str(self.papazSayisi) + "\n% " + str(round((self.papazSayisi / self.cards) * 100, 2)))
            self.labelKız.setText(
                "Q : " + str(self.kizSayisi) + "\n% " + str(round((self.kizSayisi / self.cards) * 100, 2)))
            self.labelVale.setText(
                "J : " + str(self.valeSayisi) + "\n% " + str(round((self.valeSayisi / self.cards) * 100, 2)))
            self.label10.setText(
                "10 : " + str(self.onSayisi) + "\n% " + str(round((self.onSayisi / self.cards) * 100, 2)))
            self.label9.setText(
                "9 : " + str(self.dokuzSayisi) + "\n% " + str(round((self.dokuzSayisi / self.cards) * 100, 2)))
            self.label8.setText(
                "8 : " + str(self.sekizSayisi) + "\n% " + str(round((self.sekizSayisi / self.cards) * 100, 2)))
            self.label7.setText(
                "7 : " + str(self.yediSayisi) + "\n% " + str(round((self.yediSayisi / self.cards) * 100, 2)))
            self.label6.setText(
                "6 : " + str(self.altiSayisi) + "\n% " + str(round((self.altiSayisi / self.cards) * 100, 2)))
            self.label5.setText(
                "5 : " + str(self.besSayisi) + "\n% " + str(round((self.besSayisi / self.cards) * 100, 2)))
            self.label4.setText(
                "4 : " + str(self.dortSayisi) + "\n% " + str(round((self.dortSayisi / self.cards) * 100, 2)))
            self.label3.setText(
                "3 : " + str(self.ucSayisi) + "\n% " + str(round((self.ucSayisi / self.cards) * 100, 2)))
            self.label2.setText(
                "2 : " + str(self.ikiSayisi) + "\n% " + str(round((self.ikiSayisi / self.cards) * 100, 2)))
            self.counts.setText("\nAkan Sayaç (Running Count) : " + str(self.say) + "\nAsıl Sayaç (True Count) : " + str(self.durum))
            if self.durum > 1:
                self.yazı_alanı.setText(
                    "\nKalan Kart Sayısı : " + str(self.cards) + "\nKalan Yaklaşık Deste Sayısı : " +
                    str(self.deste) + "\n\nEKSTRA yapılabilecek bahis sayısı " + str((round(self.durum, 0) - 1)) + " birim" +
                    "\n\n10'lu gelme ihtimali --> % " +
                    str(round(
                        ((self.papazSayisi + self.kizSayisi + self.valeSayisi + self.onSayisi) / self.cards) * 100, 2))
                    )
            else:
                self.yazı_alanı.setText(
                    "\nKalan Kart Sayısı : " + str(self.cards) + "\nKalan Yaklaşık Deste Sayısı : " +
                    str(self.deste) + "\n\nEKSTRA yapılabilecek bahis sayısı 0.0 birim" +
                    "\n\n10'lu gelme ihtimali --> % " +
                    str(round(
                        ((self.papazSayisi + self.kizSayisi + self.valeSayisi + self.onSayisi) / self.cards) * 100, 2))
                )
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Bu deste yenilenmediği sürece 6 kartı çıkmayacak!")
            msg.setWindowTitle("KART BİTTİ")
            msg.exec_()

    def clickBes(self):
        self.say += 1
        self.cards -= 1
        self.gecici = (self.cards // 26)
        self.deste = self.gecici / 2 + 0.5
        self.durum = round(self.say / self.deste, 3)
        self.besSayisi -= 1
        if (self.besSayisi > 0):
            self.labelAs.setText(
                "A : " + str(self.asSayisi) + "\n% " + str(round((self.asSayisi / self.cards) * 100, 2)))
            self.labelPapaz.setText(
                "K : " + str(self.papazSayisi) + "\n% " + str(round((self.papazSayisi / self.cards) * 100, 2)))
            self.labelKız.setText(
                "Q : " + str(self.kizSayisi) + "\n% " + str(round((self.kizSayisi / self.cards) * 100, 2)))
            self.labelVale.setText(
                "J : " + str(self.valeSayisi) + "\n% " + str(round((self.valeSayisi / self.cards) * 100, 2)))
            self.label10.setText(
                "10 : " + str(self.onSayisi) + "\n% " + str(round((self.onSayisi / self.cards) * 100, 2)))
            self.label9.setText(
                "9 : " + str(self.dokuzSayisi) + "\n% " + str(round((self.dokuzSayisi / self.cards) * 100, 2)))
            self.label8.setText(
                "8 : " + str(self.sekizSayisi) + "\n% " + str(round((self.sekizSayisi / self.cards) * 100, 2)))
            self.label7.setText(
                "7 : " + str(self.yediSayisi) + "\n% " + str(round((self.yediSayisi / self.cards) * 100, 2)))
            self.label6.setText(
                "6 : " + str(self.altiSayisi) + "\n% " + str(round((self.altiSayisi / self.cards) * 100, 2)))
            self.label5.setText(
                "5 : " + str(self.besSayisi) + "\n% " + str(round((self.besSayisi / self.cards) * 100, 2)))
            self.label4.setText(
                "4 : " + str(self.dortSayisi) + "\n% " + str(round((self.dortSayisi / self.cards) * 100, 2)))
            self.label3.setText(
                "3 : " + str(self.ucSayisi) + "\n% " + str(round((self.ucSayisi / self.cards) * 100, 2)))
            self.label2.setText(
                "2 : " + str(self.ikiSayisi) + "\n% " + str(round((self.ikiSayisi / self.cards) * 100, 2)))
            self.counts.setText("\nAkan Sayaç (Running Count) : " + str(self.say) + "\nAsıl Sayaç (True Count) : " + str(self.durum))
            if self.durum > 1:
                self.yazı_alanı.setText(
                    "\nKalan Kart Sayısı : " + str(self.cards) + "\nKalan Yaklaşık Deste Sayısı : " +
                    str(self.deste) + "\n\nEKSTRA yapılabilecek bahis sayısı " + str((round(self.durum, 0) - 1)) + " birim" +
                    "\n\n10'lu gelme ihtimali --> % " +
                    str(round(
                        ((self.papazSayisi + self.kizSayisi + self.valeSayisi + self.onSayisi) / self.cards) * 100, 2))
                    )
            else:
                self.yazı_alanı.setText(
                    "\nKalan Kart Sayısı : " + str(self.cards) + "\nKalan Yaklaşık Deste Sayısı : " +
                    str(self.deste) + "\n\nEKSTRA yapılabilecek bahis sayısı 0.0 birim" +
                    "\n\n10'lu gelme ihtimali --> % " +
                    str(round(
                        ((self.papazSayisi + self.kizSayisi + self.valeSayisi + self.onSayisi) / self.cards) * 100, 2))
                )
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Bu deste yenilenmediği sürece 5 kartı çıkmayacak!")
            msg.setWindowTitle("KART BİTTİ")
            msg.exec_()

    def clickDort(self):
        self.say += 1
        self.cards -= 1
        self.gecici = (self.cards // 26)
        self.deste = self.gecici / 2 + 0.5
        self.durum = round(self.say / self.deste, 3)
        self.dortSayisi -= 1
        if (self.dortSayisi > 0):
            self.labelAs.setText(
                "A : " + str(self.asSayisi) + "\n% " + str(round((self.asSayisi / self.cards) * 100, 2)))
            self.labelPapaz.setText(
                "K : " + str(self.papazSayisi) + "\n% " + str(round((self.papazSayisi / self.cards) * 100, 2)))
            self.labelKız.setText(
                "Q : " + str(self.kizSayisi) + "\n% " + str(round((self.kizSayisi / self.cards) * 100, 2)))
            self.labelVale.setText(
                "J : " + str(self.valeSayisi) + "\n% " + str(round((self.valeSayisi / self.cards) * 100, 2)))
            self.label10.setText(
                "10 : " + str(self.onSayisi) + "\n% " + str(round((self.onSayisi / self.cards) * 100, 2)))
            self.label9.setText(
                "9 : " + str(self.dokuzSayisi) + "\n% " + str(round((self.dokuzSayisi / self.cards) * 100, 2)))
            self.label8.setText(
                "8 : " + str(self.sekizSayisi) + "\n% " + str(round((self.sekizSayisi / self.cards) * 100, 2)))
            self.label7.setText(
                "7 : " + str(self.yediSayisi) + "\n% " + str(round((self.yediSayisi / self.cards) * 100, 2)))
            self.label6.setText(
                "6 : " + str(self.altiSayisi) + "\n% " + str(round((self.altiSayisi / self.cards) * 100, 2)))
            self.label5.setText(
                "5 : " + str(self.besSayisi) + "\n% " + str(round((self.besSayisi / self.cards) * 100, 2)))
            self.label4.setText(
                "4 : " + str(self.dortSayisi) + "\n% " + str(round((self.dortSayisi / self.cards) * 100, 2)))
            self.label3.setText(
                "3 : " + str(self.ucSayisi) + "\n% " + str(round((self.ucSayisi / self.cards) * 100, 2)))
            self.label2.setText(
                "2 : " + str(self.ikiSayisi) + "\n% " + str(round((self.ikiSayisi / self.cards) * 100, 2)))
            self.counts.setText("\nAkan Sayaç (Running Count) : " + str(self.say) + "\nAsıl Sayaç (True Count) : " + str(self.durum))
            if self.durum > 1:
                self.yazı_alanı.setText(
                    "\nKalan Kart Sayısı : " + str(self.cards) + "\nKalan Yaklaşık Deste Sayısı : " +
                    str(self.deste) + "\n\nEKSTRA yapılabilecek bahis sayısı " + str((round(self.durum, 0) - 1)) + " birim" +
                    "\n\n10'lu gelme ihtimali --> % " +
                    str(round(
                        ((self.papazSayisi + self.kizSayisi + self.valeSayisi + self.onSayisi) / self.cards) * 100, 2))
                    )
            else:
                self.yazı_alanı.setText(
                    "\nKalan Kart Sayısı : " + str(self.cards) + "\nKalan Yaklaşık Deste Sayısı : " +
                    str(self.deste) + "\n\nEKSTRA yapılabilecek bahis sayısı 0.0 birim" +
                    "\n\n10'lu gelme ihtimali --> % " +
                    str(round(
                        ((self.papazSayisi + self.kizSayisi + self.valeSayisi + self.onSayisi) / self.cards) * 100, 2))
                )
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Bu deste yenilenmediği sürece 4 kartı çıkmayacak!")
            msg.setWindowTitle("KART BİTTİ")
            msg.exec_()

    def clickUc(self):
        self.say += 1
        self.cards -= 1
        self.gecici = (self.cards // 26)
        self.deste = self.gecici / 2 + 0.5
        self.durum = round(self.say / self.deste, 3)
        self.ucSayisi -= 1
        if (self.ucSayisi > 0):
            self.labelAs.setText(
                "A : " + str(self.asSayisi) + "\n% " + str(round((self.asSayisi / self.cards) * 100, 2)))
            self.labelPapaz.setText(
                "K : " + str(self.papazSayisi) + "\n% " + str(round((self.papazSayisi / self.cards) * 100, 2)))
            self.labelKız.setText(
                "Q : " + str(self.kizSayisi) + "\n% " + str(round((self.kizSayisi / self.cards) * 100, 2)))
            self.labelVale.setText(
                "J : " + str(self.valeSayisi) + "\n% " + str(round((self.valeSayisi / self.cards) * 100, 2)))
            self.label10.setText(
                "10 : " + str(self.onSayisi) + "\n% " + str(round((self.onSayisi / self.cards) * 100, 2)))
            self.label9.setText(
                "9 : " + str(self.dokuzSayisi) + "\n% " + str(round((self.dokuzSayisi / self.cards) * 100, 2)))
            self.label8.setText(
                "8 : " + str(self.sekizSayisi) + "\n% " + str(round((self.sekizSayisi / self.cards) * 100, 2)))
            self.label7.setText(
                "7 : " + str(self.yediSayisi) + "\n% " + str(round((self.yediSayisi / self.cards) * 100, 2)))
            self.label6.setText(
                "6 : " + str(self.altiSayisi) + "\n% " + str(round((self.altiSayisi / self.cards) * 100, 2)))
            self.label5.setText(
                "5 : " + str(self.besSayisi) + "\n% " + str(round((self.besSayisi / self.cards) * 100, 2)))
            self.label4.setText(
                "4 : " + str(self.dortSayisi) + "\n% " + str(round((self.dortSayisi / self.cards) * 100, 2)))
            self.label3.setText(
                "3 : " + str(self.ucSayisi) + "\n% " + str(round((self.ucSayisi / self.cards) * 100, 2)))
            self.label2.setText(
                "2 : " + str(self.ikiSayisi) + "\n% " + str(round((self.ikiSayisi / self.cards) * 100, 2)))
            self.counts.setText("\nAkan Sayaç (Running Count) : " + str(self.say) + "\nAsıl Sayaç (True Count) : " + str(self.durum))
            if self.durum > 1:
                self.yazı_alanı.setText(
                    "\nKalan Kart Sayısı : " + str(self.cards) + "\nKalan Yaklaşık Deste Sayısı : " +
                    str(self.deste) + "\n\nEKSTRA yapılabilecek bahis sayısı " + str((round(self.durum, 0) - 1)) + " birim" +
                    "\n\n10'lu gelme ihtimali --> % " +
                    str(round(
                        ((self.papazSayisi + self.kizSayisi + self.valeSayisi + self.onSayisi) / self.cards) * 100, 2))
                    )
            else:
                self.yazı_alanı.setText(
                    "\nKalan Kart Sayısı : " + str(self.cards) + "\nKalan Yaklaşık Deste Sayısı : " +
                    str(self.deste) + "\n\nEKSTRA yapılabilecek bahis sayısı 0.0 birim" +
                    "\n\n10'lu gelme ihtimali --> % " +
                    str(round(
                        ((self.papazSayisi + self.kizSayisi + self.valeSayisi + self.onSayisi) / self.cards) * 100, 2))
                )
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Bu deste yenilenmediği sürece 3 kartı çıkmayacak!")
            msg.setWindowTitle("KART BİTTİ")
            msg.exec_()

    def clickIki(self):
        self.say += 1
        self.cards -= 1
        self.gecici = (self.cards // 26)
        self.deste = self.gecici / 2 + 0.5
        self.durum = round(self.say / self.deste, 3)
        self.ikiSayisi -= 1
        if (self.ikiSayisi > 0):
            self.labelAs.setText(
                "A : " + str(self.asSayisi) + "\n% " + str(round((self.asSayisi / self.cards) * 100, 2)))
            self.labelPapaz.setText(
                "K : " + str(self.papazSayisi) + "\n% " + str(round((self.papazSayisi / self.cards) * 100, 2)))
            self.labelKız.setText(
                "Q : " + str(self.kizSayisi) + "\n% " + str(round((self.kizSayisi / self.cards) * 100, 2)))
            self.labelVale.setText(
                "J : " + str(self.valeSayisi) + "\n% " + str(round((self.valeSayisi / self.cards) * 100, 2)))
            self.label10.setText(
                "10 : " + str(self.onSayisi) + "\n% " + str(round((self.onSayisi / self.cards) * 100, 2)))
            self.label9.setText(
                "9 : " + str(self.dokuzSayisi) + "\n% " + str(round((self.dokuzSayisi / self.cards) * 100, 2)))
            self.label8.setText(
                "8 : " + str(self.sekizSayisi) + "\n% " + str(round((self.sekizSayisi / self.cards) * 100, 2)))
            self.label7.setText(
                "7 : " + str(self.yediSayisi) + "\n% " + str(round((self.yediSayisi / self.cards) * 100, 2)))
            self.label6.setText(
                "6 : " + str(self.altiSayisi) + "\n% " + str(round((self.altiSayisi / self.cards) * 100, 2)))
            self.label5.setText(
                "5 : " + str(self.besSayisi) + "\n% " + str(round((self.besSayisi / self.cards) * 100, 2)))
            self.label4.setText(
                "4 : " + str(self.dortSayisi) + "\n% " + str(round((self.dortSayisi / self.cards) * 100, 2)))
            self.label3.setText(
                "3 : " + str(self.ucSayisi) + "\n% " + str(round((self.ucSayisi / self.cards) * 100, 2)))
            self.label2.setText(
                "2 : " + str(self.ikiSayisi) + "\n% " + str(round((self.ikiSayisi / self.cards) * 100, 2)))
            self.counts.setText("\nAkan Sayaç (Running Count) : " + str(self.say) + "\nAsıl Sayaç (True Count) : " + str(self.durum))
            if self.durum > 1:
                self.yazı_alanı.setText(
                    "\nKalan Kart Sayısı : " + str(self.cards) + "\nKalan Yaklaşık Deste Sayısı : " +
                    str(self.deste) + "\n\nEKSTRA yapılabilecek bahis sayısı " + str((round(self.durum, 0) - 1)) + " birim" +
                    "\n\n10'lu gelme ihtimali --> % " +
                    str(round(
                        ((self.papazSayisi + self.kizSayisi + self.valeSayisi + self.onSayisi) / self.cards) * 100, 2))
                    )
            else:
                self.yazı_alanı.setText(
                    "\nKalan Kart Sayısı : " + str(self.cards) + "\nKalan Yaklaşık Deste Sayısı : " +
                    str(self.deste) + "\n\nEKSTRA yapılabilecek bahis sayısı 0.0 birim" +
                    "\n\n10'lu gelme ihtimali --> % " +
                    str(round(
                        ((self.papazSayisi + self.kizSayisi + self.valeSayisi + self.onSayisi) / self.cards) * 100, 2))
                )
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Bu deste yenilenmediği sürece 2 kartı çıkmayacak!")
            msg.setWindowTitle("KART BİTTİ")
            msg.exec_()



    def clickReset(self):
        self.say = 0
        self.cards = 416
        self.gecici = 0
        self.deste = 8
        self.durum = 0
        self.bettingbirim = 35

        self.asSayisi = 32
        self.papazSayisi = 32
        self.kizSayisi = 32
        self.valeSayisi = 32
        self.onSayisi = 32
        self.dokuzSayisi = 32
        self.sekizSayisi = 32
        self.yediSayisi = 32
        self.altiSayisi = 32
        self.besSayisi = 32
        self.dortSayisi = 32
        self.ucSayisi = 32
        self.ikiSayisi = 32

        self.labelAs.setText("A : " + str(self.asSayisi) + "\n% " + str(round((self.asSayisi / self.cards) * 100, 2)))
        self.labelPapaz.setText(
            "K : " + str(self.asSayisi) + "\n% " + str(round((self.papazSayisi / self.cards) * 100, 2)))
        self.labelKız.setText("Q : " + str(self.asSayisi) + "\n% " + str(round((self.kizSayisi / self.cards) * 100, 2)))
        self.labelVale.setText(
            "J : " + str(self.asSayisi) + "\n% " + str(round((self.valeSayisi / self.cards) * 100, 2)))
        self.label10.setText("10 : " + str(self.asSayisi) + "\n% " + str(round((self.onSayisi / self.cards) * 100, 2)))
        self.label9.setText("9 : " + str(self.asSayisi) + "\n% " + str(round((self.dokuzSayisi / self.cards) * 100, 2)))
        self.label8.setText("8 : " + str(self.asSayisi) + "\n% " + str(round((self.sekizSayisi / self.cards) * 100, 2)))
        self.label7.setText("7 : " + str(self.asSayisi) + "\n% " + str(round((self.yediSayisi / self.cards) * 100, 2)))
        self.label6.setText("6 : " + str(self.asSayisi) + "\n% " + str(round((self.altiSayisi / self.cards) * 100, 2)))
        self.label5.setText("5 : " + str(self.asSayisi) + "\n% " + str(round((self.besSayisi / self.cards) * 100, 2)))
        self.label4.setText("4 : " + str(self.asSayisi) + "\n% " + str(round((self.dortSayisi / self.cards) * 100, 2)))
        self.label3.setText("3 : " + str(self.asSayisi) + "\n% " + str(round((self.ucSayisi / self.cards) * 100, 2)))
        self.label2.setText("2 : " + str(self.asSayisi) + "\n% " + str(round((self.ikiSayisi / self.cards) * 100, 2)))

        self.counts.setText("\nAkan Sayaç (Running Count) : 0 \nAsıl Sayaç (True Count) : 0")
        self.yazı_alanı.setText("\nKARTLAR RESETLENDİ \t--->\t YENİ ELE BAŞLANIYOR...\nDurum : " + str(
            self.say) + "  ***  " + "Kart Sayısı : " + str(self.cards))


app = QtWidgets.QApplication(sys.argv)


pencere = Pencere()
pencere.setWindowTitle("Card Counting 'HI-LO' Method")
pencere.setWindowIcon(QtGui.QIcon("Card Photos/bj.jpg"))
pencere.setGeometry(100,100,500,200)

sys.exit(app.exec_())
