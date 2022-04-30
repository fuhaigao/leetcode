class Solution:
    def entityParser(self, text: str) -> str:
        replaceDict = {"&quot;": '"', "&apos;": "'",
                       "&amp;": "&", "&gt;": ">", "&lt;": "<", "&frasl;": "/"}
        foundSpecialC = False
        out = ""
        keyWord = ""
        for c in text:
            if c == '&':
                out += keyWord
                foundSpecialC = True
                keyWord = '&'
            elif foundSpecialC:
                keyWord += c
                if c == ';':
                    replaceWord = replaceDict.get(keyWord, keyWord)
                    out += replaceWord
                    keyWord = ""
                    foundSpecialC = False
            else:
                out += c
        if foundSpecialC:
            out += keyWord
        return out
