#メンタルチェックプログラム　                 2020/7/8
import personal
import fu_check
import eq_check
import ces_d
import poms
import teg

class Test_list:                        #各種test表示
    def __init__(self):
        self.tkey = ["fu", "eq", "ces", "poms", "teg"]
        self.test_option = ["フュージョンチェック",
                            "脱中心化チェック",
                            "CES-D",
                            "POMS",
                            "TEG"]

    def print_opt(self):
        print("　＊＊実施可能なテストプログラム＊＊")
        for j in range(len(self.test_option)):
            print("    {}: {}".format(j+1, self.test_option[j]))
        print("\n")


class Mental_check:                     #test選択及び各test実行
    def __init__(self):
        print("◇︎◇︎◇︎メンタルチェックプログラム◇︎◇︎◇︎\n")
        t_list = Test_list()
        p = personal.Personal_data()

        while True:
            print(" 以下より実施するテストの番号を選んで入力してください")
            print("  **終了の際は'q'を入力してください**\n")
            t_list.print_opt()
            select = input("選択：　")

            if select == "1":                 #Fフュージョンチェック
                fu = fu_check.FU_check()
                fu.test()
                fu.print_res(t_list.tkey[0], p.name, p.date)

            elif select == "2":               #脱中心化チェック
                eq = eq_check.EQ_check()
                eq.test()
                eq.print_res(t_list.tkey[1], p.name, p.date)

            elif select == "3":               #CES-D
                ces = ces_d.CES_D()
                ces.test()
                ces.print_res(t_list.tkey[2], p.name, p.date)

            elif select == "4":               #POMS
                poms_t = poms.POMS_check()
                poms_t.test()
                poms_t.print_res(t_list.tkey[3], p.name, p.date)

            elif select == "5":               #TEG
                teg_t = teg.TEG_check()
                teg_t.test()
                teg_t.print_res(t_list.tkey[4], p.name, p.date)

            elif select == "q":               #プログラム終了
                print("\nプログラムを終了します。おつかれさまでした。")
                break

            else:                             #入力エラー時
                print("\nその選択肢はありません。選択し直してください。")

            select1 = input("他のテストを受ける場合はリターンキーを押してください。終了の場合は'q'を入力してください。: ")
            if select1 == "q":
                print("\nプログラムを終了します。おつかれさまでした。")
                break

mental_check = Mental_check()