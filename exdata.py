#テスト結果表示、データ吐き出し        2020/7/2
import csv

class Display_data:                         #テスト結果表示
    def __init__(self, name, date, sum_data, judge, entry, result, mod = 0):     #mod=0:FU,EQ,CES-D
        print("□□テスト結果□□")
        print("実施者氏名：　{}".format(name))
        print("実施日：　{}".format(date))
        print("結果")
        if mod == 0:                        #FU, EQ, CES-D
            print(" 合計値：　{}".format(sum_data))
            print(" 判定：　{}".format(judge))
        else:                               #POMS, TEG
            print(" 合計値：")
            for j in range(len(sum_data)):
                print("   {}: {}".format(mod[j], sum_data[j]))
        print(" 項目毎回答：")
        print(" 項目                                                                     回答")
        for i in range(len(result)):
            print("   {}. {}：　{}".format(i+1, entry[i] ,result[i]))
        print("\n")


class Output_data:                         #テスト結果CSV出力
    def __init__(self, tname, name, date, sum_data, judge, entry, result, mod = 0):   #mod=0:FU,EQ,CES-D
        with open("{}_{}_{}.csv".format(tname, name, date), "w", newline="") as f:
            self.w = csv.writer(f, delimiter=",")
            self.w.writerow(["実施者氏名：", name])
            self.w.writerow(["実施日：", date])
            self.w.writerow(["結果"])
            if mod == 0:                        #FU, EQ, CES-D
                self.w.writerow(["合計値：", sum_data])
                self.w.writerow(["判定：", judge])
            else:                               #POMS, TEG
                self.w.writerow(["合計値："])
                for j in range(len(sum_data)):
                    self.w.writerow([mod[j], sum_data[j]])
            self.w.writerow(["項目毎回答："])
            self.w.writerow(["項目","回答"])
            for i in range(len(result)):
                self.w.writerow([i+1, entry[i] ,result[i]])