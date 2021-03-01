import os
import sys

class Executor:

    def __init__(self, shindi):
        self.shindi= shindi


    def createOrderSpec(
        self,
        rqname,
        scrNo,
        accNo,
        orderType,
        code,
        qty,
        price,
        hogaType,
        originOrderNo = "",
    ):

        orderSpecDict = {
            "rqName" : reName,
            "scrNo" : scrNo,
            "accNo" : accNo,
            "orderType" : orderType,
            "code" : code,
            "qty" : qty,
            "price" : price,
            "hogaType":hogaType,
            "originOrderNo":originOrderNo,
        }

        return orderSpecDict
    
    def sendOrder(
        self,
        rqName,
        scrNo,
        accNo,
        orderType,
        code,
        qty,
        price,
        hogaType,
        originOrderNo="",
    ):
        """ API(shindi)를 통해 주문을 제출하는 메서드
        매개변수 설명은 createOrderSpec() 매서드 참고

        params
        ===============================================
        """
        if not isinstance(orderType, int):
            orderType = int(orderType)

        if not isinstance(qty, int):
            qty = int(qty)

        if not isinstance(price, int):
            price = int(price)

        self.shindi.sendOrder(
            rqName, scrNo, accNo, orderType, code, qty, price, hogaType, originOrderNo,
        )
        return getattr(self.shindi, "orderResponse")