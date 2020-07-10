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


class FU_check:                           #フュージョンチェックメインプログラム
    def __init__(self):
        self.rs = personal.Result_data()
        self.en = Entry_list()

    def test(self):
        print("\nフュージョン尺度チェックを開始します。\n各項目に対し、当てはまる内容を番号で回答して下さい。\n")
        for i in range(len(self.en.entry)):
            print("問{}. {}".format(i + 1, self.en.entry[i]))
            self.en.opt.print_opt()
            while True:             #エラー時再入力処理
                self.res0 = input("回答: ")
                try:
                    self.res = int(self.res0)
                    self.rs.cal(self.res, self.en.opt.option[self.res - 1])
                    break
                except (IndexError, ValueError):
                    print("!!１〜７で回答して下さい!!")
            print("\n")

        self.judge = Judgement(self.rs.sum_data)
        print("フュージョンチェックは終了です。おつかれさまでした。\n")

    def print_res(self, tkey, name, date):
        self.disp = exdata.Display_data(name, date, self.rs.sum_data,
                                 self.judge.judge0, self.en.entry, self.rs.result)
        self.out_data = exdata.Output_data(tkey, name, date, self.rs.sum_data,
                                    self.judge.judge0, self.en.entry, self.rs.result)


#fu = FU_check()
#fu.test()
#fu.print_res()