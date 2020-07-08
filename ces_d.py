#CES-Dテスト実施プログラム            2020/6/30
import personal
import exdata

class Option_list:                    #選択肢リスト
    def __init__(self):
        self.option = ["ない",
                       "１ー２日",
                       "３ー４日",
                       "５日以上"
                       ]

    def print_opt(self, i):
        print("　＜以下の選択肢から当てはまるものを選んで下さい＞")
        for j in range(len(self.option)):
            if i == 3 or i == 7 or i == 15:
                print("    {}: {}".format(j, self.option[3-j]))
            else:
                print("    {}: {}".format(j, self.option[j]))
        print("\n")


class Entry_list:                       #テスト項目リスト
    def __init__(self):
        self.entry = ["普段は何でもないことがわずらわしい                ",
                      "食べなくない。食欲が落ちた。                     ",
                      "家族や友達に励ましてもらっても、気分が晴れない      ",
                      "他の人と同じ程度には、能力があると思う             ",
                      "物事に集中できない                             ",
                      "ゆううつだ                                   ",
                      "何をするにも面倒だ                             ",
                      "これから先のことについて積極的に考えることができる   ",
                      "過去のことについてくよくよ考える                  ",
                      "何か恐ろしい気持ちがする                       ",
                      "なかなか寝られない                            ",
                      "生活について不満なく過ごせる                    ",
                      "普段より口数が少ない、口が重い                   ",
                      "一人ぼっちでさみしい                           ",
                      "皆がよそよそしいと思う                         ",
                      "毎日が楽しい                                 ",
                      "急に泣き出すことがある                         ",
                      "悲しいと感じる                                ",
                      "皆が自分を嫌っていると感じる                    ",
                      "仕事が手に付かない                             "
                      ]

        self.opt = Option_list()


class Judgement:                        #テスト結果判定（うつ度）
    def __init__(self, s_data):
        if s_data >= 26:
            self.judge0 = "重度抑うつ"
        elif s_data >= 21:
            self.judge0 = "中度抑うつ"
        elif s_data >= 17:
            self.judge0 = "軽度抑うつ"
        else:
            self.judge0 = "正常"

"""
class Display_data:                         #テスト結果表示
    def __init__(self, name, date, sum_data, judge, entry, result):
        print("実施者氏名：　{}".format(name))
        print("実施日：　{}".format(date))
        print("結果")
        print(" 合計値：　{}".format(sum_data))
        print(" 判定：　{}".format(judge))
        print(" 項目毎回答：")
        print(" 項目                                                                                     回答")
        for i in range(len(result)):
            print("   {}. {}：　{}".format(i+1, entry[i] ,result[i]))


class Output_data:                         #テスト結果CSV出力
    def __init__(self, name, date, sum_data, judge, entry, result):
        with open("ces_{}_{}.csv".format(name, date), "w", newline="") as f:
            self.w = csv.writer(f, delimiter=",")
            self.w.writerow(["実施者氏名：", name])
            self.w.writerow(["実施日：", date])
            self.w.writerow(["結果"])
            self.w.writerow(["合計値：", sum_data])
            self.w.writerow(["判定：", judge])
            self.w.writerow(["項目毎回答："])
            self.w.writerow(["項目","回答"])
            for i in range(len(result)):
                self.w.writerow([i+1, entry[i] ,result[i]])

"""

class CES_D:                           #CES-Dメインプログラム
    def __init__(self):
        self.p = personal.Personal_data()
        self.en = Entry_list()

    def test(self):
        print("\nCES-Dテストを開始します。\n各項目に対し、当てはまる内容を番号で回答して下さい。\n")
        for i in range(len(self.en.entry)):
            print("問{}. {}".format(i + 1, self.en.entry[i]))
            self.en.opt.print_opt(i)
            self.res0 = input("回答: ")
            try:
                self.res = int(self.res0)
                if i == 3 or i == 7 or i == 15:
                    self.p.cal(self.res, self.en.opt.option[3 - self.res])
                else:
                    self.p.cal(self.res, self.en.opt.option[self.res])
            except (IndexError, ValueError):
                print("０〜３で回答して下さい")
            print("\n")

        self.judge = Judgement(self.p.sum_data)
        print("CES-Dテストは終了です。おつかれさまでした。")

    def print_res(self):
        self.disp = exdata.Display_data(self.p.name, self.p.date, self.p.sum_data,
                                 self.judge.judge0, self.en.entry, self.p.result)
        self.out_data = exdata.Output_data("ces", self.p.name, self.p.date, self.p.sum_data,
                                    self.judge.judge0, self.en.entry, self.p.result)


#ces = CES_D()
#ces.test()
#ces.print_res()