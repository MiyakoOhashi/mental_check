#POMSプログラム                          2020/7/8
import personal
import exdata

class Option_list:                    #選択肢リスト
    def __init__(self):
        self.option = ["まったくなかった",
                       "少しあった",
                       "まあまああった",
                       "かなりあった",
                       "非常に多くあった"
                       ]

    def print_opt(self):
        print("　＜以下の選択肢から当てはまるものを選んで下さい＞")
        for j in range(len(self.option)):
            print("    {}: {}".format(j, self.option[j]))
        print("\n")


class Entry_list:                       #テスト項目リスト
    def __init__(self):
        self.entry = ["人付き合いが楽しい                 ",
                      "希望が持てない                    ",
                      "心の中でふんがいする               ",
                      "陽気な気持ち                      ",
                      "考えがまとまらない                 ",
                      "頭がすっきりする                   ",
                      "がっかりしてやる気をなくす          ",
                      "迷惑をかけられて困る               ",
                      "疲れた                          ",
                      "集中できない                      ",
                      "いじわるしたい                    ",
                      "自分はほめられるに値しないと感じる    ",
                      "他人を思いやれる                   ",
                      "うろたえる                       ",
                      "精力がみなぎる                    ",
                      "ゆううつだ                       ",
                      "ふきげんだ                       ",
                      "神経がたかぶる                    ",
                      "積極的な気持ちだ                  ",
                      "悲しい                          ",
                      "いらいらする                      ",
                      "物事に気のりがしない               ",
                      "落ち着かない                      ",
                      "あれこれ後悔する                   ",
                      "頭が混乱する                      ",
                      "生き生きする                      ",
                      "ぐったりする                      ",
                      "怒る                             ",
                      "自分は不幸だ                      ",
                      "他人の役に立つ気がする               ",
                      "同情する                          ",
                      "どうも忘れっぽい                   ",
                      "気がはりつめる                     ",
                      "ヘトヘトだ                        ",
                      "他人を信頼する                     ",
                      "気持ちがくつろぐ                   ",
                      "孤独でさびしい                     ",
                      "すぐけんかしたくなる                 ",
                      "頭がさえわたる                     ",
                      "とほうに暮れる                     ",
                      "内心ひどく腹立たしい                 ",
                      "自分はみじめだ                     ",
                      "他人にあたたかくできる               ",
                      "だるい                            ",
                      "物事がてきぱきできる気がする          ",
                      "反抗したい                         ",
                      "気持ちが沈んで暗い                  ",
                      "もう何の望みもない                   ",
                      "不安だ                            ",
                      "元気がいっぱいだ                    ",
                      "自分では何もできない                 ",
                      "他人に裏切られた気がする              ",
                      "気がかりでそわそわする                ",
                      "心配事がなくていい気分だ              ",
                      "自分は価値がない人間だ                ",
                      "激しい怒りを感じる                   ",
                      "うんざりだ                          ",
                      "緊張する                           ",
                      "何かにおびえる                       ",
                      "物事に確信が持てない                  ",
                      "活気がわいてくる                     ",
                      "ひどくくたびれた                     ",
                      "すぐかっとなる                       ",
                      "罪悪感がある                         ",
                      "あれこれ心配だ                       "
                      ]

        self.opt = Option_list()


class Divesion:                     #因子
    def __init__(self):
        #因子設定
        self.fac = ["fa", "d", "ah", "v", "f", "c"]
        #各因子に関する項目
        self.fa = [14, 18, 23, 33, 36, 49, 53, 58, 65]
        self.d = [2, 7, 12, 16, 20, 24, 29, 37, 42, 47, 48, 51, 55, 59, 64]
        self.ah = [3, 8, 11, 17, 21, 28, 38, 41, 46, 52, 56, 63]
        self.v = [4, 15, 19, 26, 39, 50, 54, 61]
        self.f = [9, 22, 27, 34, 44, 57, 62]
        self.c = [5, 10, 25, 32, 40, 45, 60]


class Result_poms(personal.Result_data):       #データ集計＿POMS用
    def cal_poms(self, i, r_data):
        if i+1 == 36 or i+1 == 45:
            self.sum_data[i] = self.sum_data[i] + (4 - r_data)
        else:
            self.sum_data[i] = self.sum_data[i] + r_data

    def ans_add(self, opt):
        self.result.append(opt)

"""
class Judgement:  # テスト結果判定
    def __init__(self, d_re):
        pass
"""

class POMS_check:                           #フュージョンチェックメインプログラム
    def __init__(self):
        self.rs = Result_poms(1)
        self.en = Entry_list()
        self.dv = Divesion()

    def test(self):
        print("\nPOMSを開始します。\n各項目に対し、当てはまる内容を番号で回答して下さい。\n")
        for i in range(len(self.en.entry)):
            print("問{}. {}".format(i + 1, self.en.entry[i]))
            self.en.opt.print_opt()
            while True:
                self.res0 = input("回答: ")
                try:
                    self.res = int(self.res0)
                    if i+1 in self.dv.fa:
                        self.rs.cal_poms(0, self.res)
                    elif i+1 in self.dv.d:
                        self.rs.cal_poms(1, self.res)
                    elif i+1 in self.dv.ah:
                        self.rs.cal_poms(2, self.res)
                    elif i+1 in self.dv.v:
                        self.rs.cal_poms(3, self.res)
                    elif i+1 in self.dv.f:
                        self.rs.cal_poms(4, self.res)
                    elif i+1 in self.dv.c:
                        self.rs.cal_poms(5, self.res)
                    self.rs.ans_add(self.en.opt.option[self.res])
                    break
                except (IndexError, ValueError):
                    print("!!０〜４で回答して下さい!!")
            print("\n")

        #self.judge = Judgement()
        print("POMSは終了です。おつかれさまでした。")

    def print_res(self, name, date):
        self.disp = exdata.Display_data(name, date, self.rs.sum_data,
                                 None, self.en.entry, self.rs.result, self.dv.fac)
        self.out_data = exdata.Output_data("poms", name, date, self.rs.sum_data,
                                    None, self.en.entry, self.rs.result, self.dv.fac)


#poms = POMS_check()
#poms.test()
#poms.print_res()