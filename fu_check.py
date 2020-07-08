#フュージョン(FU)尺度チェックプログラム      2020/6/29
import personal
import exdata

class Option_list:                    #選択肢リスト
    def __init__(self):
        self.option = ["全く当てはまらない",
                       "極稀に当てはまる",
                       "稀に当てはまる",
                       "時に当てはまる",
                       "かなり当てはまる",
                       "ほとんどいつも当てはまる",
                       "いつも当てはまる"
                       ]

    def print_opt(self):
        print("　＜以下の選択肢から当てはまるものを選んで下さい＞")
        for j in range(len(self.option)):
            print("    {}: {}".format(j + 1, self.option[j]))
        print("\n")


class Entry_list:                       #テスト項目リスト
    def __init__(self):
        self.entry = ["自分の思考が、苦悩や心の痛みの原因になっている                                           ",
                      "考えていることに囚われすぎて、自分が一番したいことをすることができない                        ",
                      "自分に役に立たない位にまで、状況の分析をしすぎてしまう                                     ",
                      "自分自身の考えと苦闘する                                                             ",
                      "特定のことを考えてしまうことで、自分に動揺する                                           ",
                      "自分の考えにかなり巻き込まれがちだ                                                     ",
                      "動揺するような考えに執着しないほうが自分の役に立つと分かっていても、そうすることにとても苦労する   "
                      ]

        self.opt = Option_list()


class Judgement:                        #テスト結果判定（フュージョン傾向）
    def __init__(self, s_data):
        if s_data > 27:
            self.judge0 = "思考と現実を混同し、考え込みやすい傾向があります"
        elif s_data == 27:
            self.judge0 = "一般平均値です"
        else:
            self.judge0 = "思考と現実を混同しやすい傾向は薄いです"

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
        with open("fu_{}_{}.csv".format(name, date), "w", newline="") as f:
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

class FU_check:                           #フュージョンチェックメインプログラム
    def __init__(self):
        self.p = personal.Personal_data()
        self.en = Entry_list()

    def test(self):
        print("\nフュージョン尺度チェックを開始します。\n各項目に対し、当てはまる内容を番号で回答して下さい。\n")
        for i in range(len(self.en.entry)):
            print("問{}. {}".format(i + 1, self.en.entry[i]))
            self.en.opt.print_opt()
            self.res0 = input("回答: ")
            try:
                self.res = int(self.res0)
                self.p.cal(self.res, self.en.opt.option[self.res - 1])
            except (IndexError, ValueError):
                print("１〜７で回答して下さい")
            print("\n")

        self.judge = Judgement(self.p.sum_data)
        print("フュージョンチェックは終了です。おつかれさまでした。")

    def print_res(self):
        self.disp = exdata.Display_data(self.p.name, self.p.date, self.p.sum_data,
                                 self.judge.judge0, self.en.entry, self.p.result)
        self.out_data = exdata.Output_data("fu", self.p.name, self.p.date, self.p.sum_data,
                                    self.judge.judge0, self.en.entry, self.p.result)


#fu = FU_check()
#fu.test()
#fu.print_res()