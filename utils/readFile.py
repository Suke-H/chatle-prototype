import os

def readTextFileFromGameData(fileName: str) -> str:
    """
    GameDataフォルダにあるtxtファイルを読み込む
    """

    base_path = os.path.dirname(__file__)  # 現在のファイルのディレクトリ
    path = os.path.join(base_path, '../GameData', fileName)
    # path = f"/GameData/{fileName}"

    with open(path) as f:
        contents = f.read()

    return contents
