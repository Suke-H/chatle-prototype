import unicodedata

def checkJA(word: str):
    """
    単語の全文字が日本語であるかチェック
    """
    for letter in word:
        letterType = unicodedata.name(letter)

        if "CJK UNIFIED" in letterType \
            or "HIRAGANA" in letterType \
            or "KATAKANA" in letterType \
            or "DIGIT" in letterType:
            continue
        else:
            return False
    
    return True
