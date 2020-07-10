#個人データモジュール         2020/7/1
import datetime

class Personal_data:                #実施者個人データ
    def __init__(self):
        while True:
            self.name = input("実施者氏名： ")
            if len(self.name) != 0:
                break
            else:
                print("\n!!実施者氏名を記入してください。!!\n")
        self.date = datetime.date.today()


class Result_data:                  #実施データまとめ
    def __init__(self, mod = 0):
        self.result = []
        if mod == 0:            # FU, EQ, CES-D用
            self.sum_data = 0
        else:                   # POMS, TEG用
            for i in range(6):
                self.sum_data = [0, 0, 0, 0, 0, 0]

    def cal(self, r_data, opt):     #FU, EQ, CES-S用
        self.sum_data = self.sum_data + r_data
        self.result.append(opt)