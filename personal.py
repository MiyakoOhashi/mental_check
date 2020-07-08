#個人データモジュール         2020/7/1
import datetime

class Personal_data:                #実施者個人データ
    def __init__(self, mod = 0):
        self.date = datetime.date.today()
        self.name = input("実施者氏名： ")
        self.result = []
        if mod == 0:            # FU, EQ, CES-D用
            self.sum_data = 0
        else:                   # POMS
            for i in range(6):
                self.sum_data = [0, 0, 0, 0, 0, 0]

    def cal(self, r_data, opt):
        self.sum_data = self.sum_data + r_data
        self.result.append(opt)