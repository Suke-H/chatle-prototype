from typing import Tuple
from openai import OpenAI

from utils.readFile import readTextFileFromGameData
from utils.checkLanguage import checkJA

# APIキーの設定
client = OpenAI(api_key=readTextFileFromGameData("key.txt"))

def askGPT(questionContent: str) -> Tuple[str, bool]:
    """
    ChatGPTに質問する

    質問形式：
    f"{correctAnswer}は{questionContent}ですか？"
    
    回答形式：
    いいえ～はいの5段階評価
    """

    # ルール
    rule = readTextFileFromGameData("ChatGPTRules.txt")
    # 実際の解答
    correctAnswer = readTextFileFromGameData("answer.txt")

    # ユーザの質問事項が日本語であるか確認
    isJA = checkJA(questionContent)
    # 日本語でなければ終了
    if not isJA:
        return ("日本語で入力してください", False)

    # 質問形式にあてはめ
    question = f"{correctAnswer}は{questionContent}ですか？"
    # ChatGPTの利用
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": rule},
        {"role": "user", "content": question},
    ],
    max_tokens=15)
    responseText = response.choices[0].message.content

    print(responseText)

    # 数字抽出。できなければエラー
    # responseText = ...

    return (responseText, True)