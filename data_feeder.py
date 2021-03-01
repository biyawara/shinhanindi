from collections import defaultdict
from datetime import datetime
import os
import pandas as pd

class DataFeeder:

    def __init__(self, shindi, **kwargs):

        self.shindi = shindi
        for k, v in kwargs:
            setattr(self, k,v)

    def request(self, queryname, **kwargs):

        queryname = queryname.upper()
        self.shindi.setQueryName(queryname)

        offset = 0
        for k,v in kwargs.items():
            self.shindi.setInputValue(offset, k,v)
            offset = offset + 1

        self.shindi.commRqData(queryname, "0000")

        return getattr(self.shindi, queryname)

