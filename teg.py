#TEGプログラム                          2020/7/8
import personal
import exdata

class Option_list:                    #選択肢リスト
    def __init__(self):
        self.option = ["いいえ",
                       "どちらでもない",
                       "はい"
                       ]

    def print_opt(self):
        print("　＜以下の選択肢から当てはまるものを選んで下さい＞")
        for j in range(len(self.option)):
            print("    {}: {}".format(j, self.option[j]))
        print("\n")


class Entry_list:                       #テスト項目リスト
    def __init__(self):
        self.entry = ["他人の言うことに左右されやすい              ",
                      "納得のいかないことに抗議する               ",
                      "ユーモアのセンスがある                    ",
                      "他人の評価が気になる                      ",
                      "寛大である                              ",
                      "他人の話を聞くときに根拠を求める            ",
                      "他人の目を気にして行動することが多い         ",
                      "心が広い                               ",
                      "一度決めたことがよくぐらつく               ",
                      "いつも楽しいことを探している               ",
                      "物事には常に原因があるから結果があると考える  ",
                      "理屈っぽい                              ",
                      "人の気持ちがよくわかる                    ",
                      "良いと思うことは貫く                      ",
                      "議論を好む                              ",
                      "何かを始める前には情報を集める              ",
                      "新しいことをやってみることが多い            ",
                      "のびのびと振る舞うことができる              ",
                      "他人に指図されることが多い                 ",
                      "夜更かしをすることがまったくない            ",
                      "何気ない気配りをする                      ",
                      "人見知りをしない                         ",
                      "自分に厳しい                            ",
                      "一度決めたことはやりとおす                 ",
                      "人の気持ちがなごむように話をする            ",
                      "責任感が強い                            ",
                      "夢を見たことがない                        ",
                      "しばしば人から言われた通りに行動してしまう    ",
                      "他人に指図されるより指図する方が多い         ",
                      "人を笑わせることが得意である               ",
                      "人の顔色をうかがってしまう                 ",
                      "人助けをすることに喜びを感じる              ",
                      "物事を言葉できちんと説明できる              ",
                      "人の言うことが気になる                     ",
                      "親身になって行動する                      ",
                      "優柔不断である                           ",
                      "常にその場を楽しむことができる              ",
                      "事実の確認を行う                          ",
                      "予測して行動する                          ",
                      "人に優しい言葉をかける                     ",
                      "良くないことは指摘する                     ",
                      "論理的である                             ",
                      "筋道立てて考える                          ",
                      "みんなとにぎやかに騒ぐのが好きだ             ",
                      "明るい                                  ",
                      "決断することが苦手である                    ",
                      "風邪を引いたことがまったくない               ",
                      "人には温かく接している                     ",
                      "よく笑う                                 ",
                      "言うべきことは言う                         ",
                      "ついリーダーシップをとってしまう             ",
                      "人の役に立つように行動する                  ",
                      "常に向上心を持つ                          "
                      ]

        self.opt = Option_list()


class Divesion:                     #因子
    def __init__(self):
        #因子設定
        self.fac = ["cp", "np", "a", "fc", "ac", "l"]
        #各因子に関する項目
        self.cp = [2, 14, 23, 24, 26, 29, 41, 50, 51, 53]
        self.np = [5, 8, 13, 21, 25, 32, 35, 40, 48, 52]
        self.a = [6, 11, 12, 15, 16, 33, 38, 39, 42, 43]
        self.fc = [3, 10, 17, 18, 22, 30, 37, 44, 45, 49]
        self.ac = [1, 4, 7, 9, 19, 28, 31, 34, 46, 46]
        self.l = [20, 27, 47]


class Personal_data_teg(personal.Personal_data):           #データ集計＿TEG用
    def cal_teg(self, i, r_data):
        self.sum_data[i] = self.sum_data[i] + r_data

    def ans_add(self, opt):
        self.result.append(opt)


class Judgement:  # テスト結果判定
    def __init__(self, d_re):
        pass


class TEG_check:                           #フュージョンチェックメインプログラム
    def __init__(self):
        self.p = Personal_data_teg(1)
        self.en = Entry_list()
        self.dv = Divesion()

    def test(self):
        print("\nPOMSを開始します。\n各項目に対し、当てはまる内容を番号で回答して下さい。\n")
        for i in range(len(self.en.entry)):
            print("問{}. {}".format(i + 1, self.en.entry[i]))
            self.en.opt.print_opt()
            self.res0 = input("回答: ")
            try:
                self.res = int(self.res0)
                if i+1 in self.dv.cp:
                    self.p.cal_teg(0, self.res)
                elif i+1 in self.dv.np:
                    self.p.cal_teg(1, self.res)
                elif i+1 in self.dv.a:
                    self.p.cal_teg(2, self.res)
                elif i+1 in self.dv.fc:
                    self.p.cal_teg(3, self.res)
                elif i+1 in self.dv.ac:
                    self.p.cal_teg(4, self.res)
                elif i+1 in self.dv.l:
                    self.p.cal_teg(5, self.res)
                self.p.ans_add(self.en.opt.option[self.res])

            except (IndexError, ValueError):
                print("０〜２で回答して下さい")
            print("\n")

        #self.judge = Judgement()
        print("TEGは終了です。おつかれさまでした。")

    def print_res(self):
        self.disp = exdata.Display_data(self.p.name, self.p.date, self.p.sum_data,
                                 None, self.en.entry, self.p.result, self.dv.fac)
        self.out_data = exdata.Output_data("teg", self.p.name, self.p.date, self.p.sum_data,
                                    None, self.en.entry, self.p.result, self.dv.fac)


#teg = TEG_check()
#teg.test()
#teg.print_res()