from typing import Tuple
from openai import OpenAI

from sklearn.metrics.pairwise import cosine_similarity
from utils.readFile import readTextFileFromGameData

# APIキーの設定
client = OpenAI(api_key=readTextFileFromGameData("key.txt"))

def calcSimilarity(userAnswer: str) -> Tuple[float, bool]:
    """
    正解単語とユーザー回答単語との類似度を計算する

    openai Embeddingsを利用し2単語の埋め込みベクトルを取得
    コサイン類似度(-1~1)を計算
    """
    # 実際の解答
    correctAnswer = readTextFileFromGameData("answer.txt")
    texts = [correctAnswer, userAnswer]
    # 2単語の埋め込みベクトルを取得
    embeddings = get_embeddings(texts)
    # コサイン類似度を計算
    similarity = cosine_similarity([embeddings[0].embedding], [embeddings[1].embedding])[0][0]
    print(similarity)

    # 完全一致の場合
    if userAnswer == correctAnswer:
        return (similarity, True)

    return (similarity, False)

# 埋め込みを取得する関数
def get_embeddings(texts):
    response = client.embeddings.create(
        input=texts,
        model="text-embedding-3-large"
    )
    return response.data