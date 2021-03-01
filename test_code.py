import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

from data_feeder import DataFeeder
from  SHIndi import SHIndi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    IndiApp = SHIndi()

    IndiApp.show()

    IndiApp.connect()

    feeder = DataFeeder(IndiApp)

    #선물 종목 마스터 
    data = feeder.request(queryname="FRF_MST")

    #선물 주문 


    print("-------------------------------------\r\n")
    print(data)

    app.exec_()
