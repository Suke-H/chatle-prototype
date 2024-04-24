from api.askGPT import askGPT
from api.calcSimilarity import calcSimilarity

def main():
    ask_count = 0
    calc_count = 0
    ask_limit = 15
    calc_limit = 5

    while calc_count < calc_limit:
        print(f"質問回数: {ask_count}/{ask_limit}")
        print(f"類似度計算回数: {calc_count}/{calc_limit}")
        print("====================================")

        # 質問するか類似度計算するかを決定
        a = input("質問する場合は1、類似度計算する場合は2を入力してください: ")
        if a == "1":
            if ask_count < ask_limit:
                ask_count += 1
                ask = input("それは○○ですか？: ")
                response = askGPT(ask)
            else:
                print("質問回数の上限に達しました。")

        elif a == "2":
            calc_count += 1
            answer = input("解答内容を入力してください: ")
            response = calcSimilarity(answer)

            if response[1]:
                print("クリア！！")
                return

        else:
            print("1か2を入力してください。")

        print("\n\n")

    print("ゲームオーバー")

if __name__ == "__main__":
    main()

