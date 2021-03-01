class OrderType(object):
    """sendOrder의 orderType에 대응되는 주문"""

    BSType = {
        B : "매수",
        S : "매도"
    }
    
    PRCTYPE = {
        1: "지정가",
        2: "시장가",
        3: "STOP MARKET",
        4: "STOP LIMIT",
    }


class ChejanGubun(object):

    TYPE= {"0": "주문접수/주문체결", "1": "잔고통보", "3": "특이신호"}


class FidList(object):
    """ receiveChejanData() 이벤트 메서드로 전달되는 FID 목록 """

    # 선물 종목 마스터
    FRT_MST = {
        "CODE",                 # 종목코드
        "NAME",                 # 종목명
        "EXCHANGE_CODE",        # 거래소 코드 
        "PRICE_DOT",            # 가격 소수점
        "NUMERIC_SYSTEM",       # 진법
        "QTE_UNIT",             # 호가단위
        "LIST_DATE",            # 상장일자
        "FIRST_TRADE",          # 최초 거래일
        "LAST_TRADE",           # 최종 거래일   
        "REMAIN_DAY",           # 잔존일수
        "TRADE_ITEM",           # 거래대상코드
        "ACTIVE_TP",            # ACTIVE 여부 
        "MIN_VOL",              # 최소 가격 변동 금액
        "SPREAD_TP",            # 스프레드 여부 
        "SPREAD_BASIC",         
        "SPREAD_REF",
    }


    ALL = {
        "9201": "ACCOUNT_NO",  # 계좌번호
        "9203": "ORDER_NO",  # 주문번호
        #"9205": "관리자사번",
        "9001": "TICKER",  # 종목코드
        "912": "주문업무분류",
        "913": "ORDER_STATUS",  # 주문상태: "접수", "체결"
        "302": "NAME",  # 종목명
        "900": "ORDER_QTY",  # 주문수량
        "901": "ORDER_PRICE",  # 주문가격
        "902": "UNEX_QTY",  # 미체결수량
        "903": "체결누계금액",
        "904": "ORIGINAL_ORDER_NO",
        "905": "ORDER_GUBUN",  # 주문구분: "+매수", "-매도", "매수취소" ..
        "906": "HOGA_TYPE",  # 매매구분: "보통", "시장가"..
        "907": "SELL_BUY_GUBUN",  # 매도수구분 : (1:매도, 2:매수, 주문상태; 접수인 경우)
        "908": "ORDER_TRAN_TIME",  # 주문/체결시간
        "909": "TRAN_NO",  # 체결번호
        "910": "체결가",
        "911": "체결량",
        "10": "현재가",
        "27": "(최우선)매도호가",
        "28": "(최우선)매수호가",
        "914": "TRAN_PRICE",  # 단위체결가
        "915": "TRAN_QTY",  # 단위체결량
        "938": "당일매매수수료",
        "939": "당일매매세금",
        "919": "거부사유",
        "920": "화면번호",
        "921": "터미널신호",
        "922": "신용구분",
        "923": "대출일",
        "917": "신용구분",
        "916": "대출일",
        "930": "보유수량",
        "931": "매입단가",
        "932": "총매입가",
        "933": "주문가능수량",
        "945": "당일순매수수량",
        "946": "BUY_SELL_GUBUN",  # 매도/매수구분 (주문상태: 체결인 경우)
        "950": "당일총매도손익",
        "951": "예수금",
        "307": "기준가",
        "8019": "손익율",
        "957": "신용금액",
        "958": "신용이자",
        "959": "담보대출수량",
        "918": "만기일",
        "990": "당일실현손익(유가)",
        "991": "당일신현손익률(유가)",
        "992": "당일실현손익(신용)",
        "993": "당일실현손익률(신용)",
        "397": "파생상품거래단위",
        "305": "상한가",
        "306": "하한가",
    }

    # DB에 저장할 column은 key를 영어로 작성
    SUBMITTED = {
        "9201": "ACCOUNT_NO",  # 계좌번호
        "9203": "ORDER_NO",  # 주문번호
        "906": "HOGA_TYPE",  # 매매구분: "보통", "시장가"..
        "905": "ORDER_GUBUN",  # 주문구분: "+매수", "-매도", "매수취소" ..
        "901": "ORDER_PRICE",  # 주문가격
        "900": "ORDER_QTY",  # 주문수량
        "913": "ORDER_STATUS",  # 주문상태: "접수", "체결"
        "908": "ORDER_TRAN_TIME",  # 주문/체결시간
        "904": "ORIGINAL_ORDER_NO",
        "907": "SELL_BUY_GUBUN",  # 매도수구분 : (1:매도, 2:매수, 주문상태; 접수인 경우)
        "9001": "TICKER",  # 종목코드
        "302": "NAME",  # 종목명
        "902": "UNEX_QTY",  # 미체결수량
    }
    CANCELLED = {
        "9201": "ACCOUNT_NO",  # 계좌번호
        "906": "HOGA_TYPE",  # 매매구분: "보통", "시장가"..
        "302": "NAME",  # 종목명
        "905": "ORDER_GUBUN",  # 주문구분: "+매수", "-매도", "매수취소" ..
        "9203": "ORDER_NO",  # 주문번호
        "901": "ORDER_PRICE",  # 주문가격
        "900": "ORDER_QTY",  # 주문수량
        "913": "ORDER_STATUS",  # 주문상태: "접수", "체결"
        "908": "ORDER_TRAN_TIME",  # 주문/체결시간
        "904": "ORIGINAL_ORDER_NO",
        "907": "SELL_BUY_GUBUN",  # 매도수구분 : (1:매도, 2:매수, 주문상태; 접수인 경우)
        "9001": "TICKER",  # 종목코드
    }
    EXECUTED = {
        "9201": "ACCOUNT_NO",  # 계좌번호
        "9203": "ORDER_NO",  # 주문번호
        "9001": "TICKER",  # 종목코드
        "913": "ORDER_STATUS",  # 주문상태: "접수", "체결"
        "302": "NAME",  # 종목명
        "900": "ORDER_QTY",  # 주문수량
        "901": "ORDER_PRICE",  # 주문가격
        "902": "UNEX_QTY",  # 미체결수량
        "904": "ORIGINAL_ORDER_NO",
        "905": "ORDER_GUBUN",  # 주문구분: "+매수", "-매도", "매수취소" ..
        "906": "HOGA_TYPE",  # 매매구분: "보통", "시장가"..
        "907": "SELL_BUY_GUBUN",  # 매도수구분 : (1:매도, 2:매수, 주문상태; 접수인 경우)
        "908": "ORDER_TRAN_TIME",  # 주문/체결시간
        "909": "TRAN_NO",  # 체결번호
        "914": "TRAN_PRICE",  # 단위체결가
        "915": "TRAN_QTY",  # 단위체결량
    }
class ReturnCode(object):
    """ 키움 OpenApi+ 함수들이 반환하는 값 """

    OP_ERR_NONE = 0  # 정상처리
    OP_ERR_FAIL = -10  # 실패
    
    CAUSE = {
        0: "정상처리",
        -10: "실패",
    }


class TRName:
    RC = "해외주식현재가"
    TR_RCHART = "해외주식차트조회"
    

