#EQ(脱中心化)尺度チェックプログラム            2020/6/30
import personal
import exdata

class Option_list:                    #選択肢リスト
    def __init__(self):
        self.option = ["全く当てはまらない",
                       "いく分当てはまる",
                       "どちらでもない",
                       "かなりよく当てはまる",
                       "非常によく当てはまる"
                       ]

    def print_opt(self):
        print("　＜以下の選択肢から当てはまるものを選んで下さい＞")
        for j in range(len(self.option)):
            print("    {}: {}".format(j + 1, self.option[j]))
        print("\n")


class Entry_list:                       #テスト項目リスト
    def __init__(self):
        self.entry = ["私は、自分自身をあるがままに受け入れることができる                                   ",
                      "私は、ストレスを感じている時であっても、自分の考えを落ち着かせることができる              ",
                      "私は、自分の考えや感情から自分自身を切り離すことができる                              ",
                      "私は、周囲の状況に対して落ち着いて応じることができる                                  ",
                      "私は、自分自身を思いやりを持って扱うことができる                                     ",
                      "私は、不快な感情に飲み込まれることなく、その感情を観察することができる                   ",
                      "私は、自分の周囲や自分自身の内側で起きてることに十分気づいている感覚がある                ",
                      "私は、自分自身が自分の思考とは別物であることを実際に認識できる                          ",
                      "私は、自分の身体の感覚全体を意識的に感じるようにしている                               ",
                      "私は、より広い視野で物事を捉える                                                  "
                      ]

        self.opt = Option_list()


class Judgement:                        #テスト結果判定（脱中心化度）
    def __init__(self, s_data):
        if s_data >= 25:
            self.judge0 = "思考と距離を置き、思考に巻き込まれずに判断している傾向：高い"
        else:
            self.judge0 = "思考と距離を置き、思考に巻き込まれずに判断している傾向：低い"


class EQ_check:                           #脱中心化チェックメインプログラム
    def __init__(self):
        self.rs = personal.Result_data()
        self.en = Entry_list()

    def test(self):
        print("\n脱中心化チェックを開始します。\n各項目に対し、当てはまる内容を番号で回答して下さい。\n")
        for i in range(len(self.en.entry)):
            print("問{}. {}".format(i + 1, self.en.entry[i]))
            self.en.opt.print_opt()
            while True:                     #エラー時再入力処理
                self.res0 = input("回答: ")
                try:
                    self.res = int(self.res0)
                    self.rs.cal(self.res, self.en.opt.option[self.res - 1])
                    break
                except (IndexError, ValueError):
                    print("!!１〜５で回答して下さい!!")
            print("\n")

        self.judge = Judgement(self.rs.sum_data)
        print("脱中心化チェックは終了です。おつかれさまでした。\n")

    def print_res(self, tkey, name, date):
        self.disp = exdata.Display_data(name, date, self.rs.sum_data,
                                 self.judge.judge0, self.en.entry, self.rs.result)
        self.out_data = exdata.Output_data(tkey, name, date, self.rs.sum_data,
                                    self.judge.judge0, self.en.entry, self.rs.result)


#eq = EQ_check()
#eq.test()
#eq.print_res()