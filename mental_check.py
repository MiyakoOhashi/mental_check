#メンタルチェックプログラム　                 2020/7/8
import fu_check
import eq_check
import ces_d
import poms
import teg

class Test_list:                        #各種test表示
    def __init__(self):
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
        test_l = Test_list()
        select = 0

        while select != "q":
            print(" 以下より実施するテストの番号を選んで入力してください")
            print("  *終了の際は'q'を入力してください*\n")
            test_l.print_opt()
            select = input("選択：　")

            if select == "1":                 #Fフュージョンチェック
                print("\nフュージョンチェックを実施します")
                fu = fu_check.FU_check()
                fu.test()
                fu.print_res()

            elif select == "2":               #脱中心化チェック
                print("\n脱中心化チェックを実施します")
                eq = eq_check.EQ_check()
                eq.test()
                eq.print_res()

            elif select == "3":               #CES-D
                print("\nCES-Dを実施します")
                ces = ces_d.CES_D()
                ces.test()
                ces.print_res()

            elif select == "4":               #POMS
                print("\nPOMSを実施します")
                poms_t = poms.POMS_check()
                poms_t.test()
                poms_t.print_res()

            elif select == "5":               #TEG
                print("\nTEGを実施します")
                teg_t = teg.TEG_check()
                teg_t.test()
                teg_t.print_res()

            elif select == "q":
                print("プログラムを終了します。おつかれさまでした。")

            else:
                print("その選択肢はありません。選択し直してください。\n")

mental_check = Mental_check()