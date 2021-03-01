from collections import deque, defaultdict
from datetime import datetime as dt
import functools
import os
import time
import signal

import pandas as pd
import numpy as np

#import pandas as pd
from PyQt5.QAxContainer import QAxWidget
from PyQt5.QtCore import QEventLoop, QTimer
from PyQt5.QtWidgets import QMainWindow

from _logger import Logger
import errors 

class SHIndi(QMainWindow):

    __instance = None
    
    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod 
    def instance(cls, *args, **kwargs):
        cls.__instance = cls(*args, **kwargs)
        cls.instance = cls.__getInstance
        return cls.__instance


    def __init__(self):
        super().__init__()

        self.IndiTR = QAxWidget("GIEXPERTCONTROL.GiExpertControlCtrl.1")
        self.IndiTR.ReceiveData.connect(self.OnReceiveData)
        self.IndiTR.ReceiveSysMsg.connect(self.OnReceiveSysMsg)

        self.IndiReal = QAxWidget("GIEXPERTCONTROL.GiExpertControlCtrl.1")
        self.IndiReal.ReceiveRTData.connect(self.OnReceiveRealData)

        # Loop 변수 : 비동기 방식으로 동작되는 이벤트를 동기화 
        self.logingLoop = None
        self.requestLoop = None
        self.orderLoop = None
        self.conditionLoop = None

        # 서버구분 
        self.serverStatus = None

        # 연속조회 구분 
        self.isNext = 0
        self.rqidD = {}

        # logging 
        self.homepath = os.environ.get("userprofile")
        self.logger = Logger(path=self.log_path, name="SH Indi")

        # 메세지 처리 
        self.msg = ""


    ##----------------------------------------------------------------------------------------------------------------------
    ## Function method block 
    ##----------------------------------------------------------------------------------------------------------------------

    @property
    def log_path(self):
        path = os.path.join(self.homepath, 'log')
        if not os.path.exists(path):
            os.mkdir(path)
        
        return path
    

    def connect(self):

        while True:
            blogin = self.IndiTR.StartIndi('biyawara', 'koscom@1', 'choi9880@1', 'C:\SHINHAN-i\Indi GX\giexpertstarter.exe')
            
            if blogin == True :
                self.logger.info("정상 접속 하였습니다")                    
                break

    
    def setQueryName(self, value):
        self.IndiTR.dynamicCall("SetQueryName(QString)",value)
        

    # TRCODE에 맞는 값을 설정한다. 
    def setInputValue(self, index, key, value):
        """ TR 전송에 필요한 값을 설정한다.

        Parameters
        ----------
        key: str
            TR에 명시된 input 이름, ex) 계좌번호, 종목코드
        value: str
            key에 해당하는 값, ex) 88231524, 005930
        """
    
        if not isinstance(key, str):
            key = str(key)

        if not isinstance(value, str):
            value = str(value)

        self.IndiTR.dynamicCall("SetSingleData(int, QString)", index, value)


    def commRqData(self, query_name, inquire):
        returnCode = self.IndiTR.dynamicCall("RequestData()")
        if returnCode <= 0:  # 0이외엔 실패
            self.logger.error(
                "commRqData {} Request Failed!".format(query_name)
               )
            raise errors.ProcessingError()

        self.rqidD[returnCode] = query_name

        # 루프 생성: eventReceiveTrData() 메서드에서 루프를 종료시킨다.
        self.logger.debug("{}  commRqData {}".format(dt.now(), query_name))
        self.requestLoop = QEventLoop()
        self.requestLoop.exec_()


    ##----------------------------------------------------------------------------------------------------------------------
    ## Async Event Processing block
    ##----------------------------------------------------------------------------------------------------------------------
    def OnReceiveData(self, rqid):
        
        queryname = self.rqidD[rqid]
        print(queryname)

        # 해외 호가의 경우 
        if queryname == "RH":
            data = "TEST"  #<-- 이곳에서 데이터 파징
        elif queryname == "FRF_MST":
            self.TR_FRF_MST()          
            data = "TEST"  #<-- 이곳에서 데이터 파징


        setattr(self, queryname, data)

        # EXIT LOOP 
        try:
            self.requestLoop.exit()
        except AttributeError:
            pass 


    # system event로 보임 
    def OnReceiveSysMsg(self, msgID):
        print(msgID)


    # 실시간 데이터
    def OnReceiveRealData(self, realId) :
        print(realId)


    ##----------------------------------------------------------------------------------------------------------------------
    ## TR 처리 구문 
    ##----------------------------------------------------------------------------------------------------------------------        
    
    # FRF_MST // 선물 마스터 
    def TR_FRF_MST(self):
        
        nCnt = self.IndiTR.dynamicCall("GetMultiRowCount()")

        for i in range(0, nCnt):
            code = self.IndiTR.dynamicCall("GetMultiData(int, int)", i, 0)
            name = self.IndiTR.dynamicCall("GetMultiData(int, int)", i, 0)
            exchange_code = self.IndiTR.dynamicCall("GetMultiData(int, int)", i, 0)
            price_point = self.IndiTR.dynamicCall("GetMultiData(int, int)", i, 0)
            ns = self.IndiTR.dynamicCall("GetMultiData(int, int)", i, 0)
            qte_unit = self.IndiTR.dynamicCall("GetMultiData(int, int)", i, 0)
            
