class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n_letter, n_word, curr = 0, 0, []
        lines = []
        for word in words:
            if n_letter + n_word + len(word) > maxWidth:
                if len(curr) == 1:
                    lines.append(curr[0]+' '*(maxWidth-n_letter))

                else:
                    n_space, mod = divmod(maxWidth - n_letter, n_word-1)
                    for i in range(mod):
                        curr[i] += ' '
                    lines.append((' '*n_space).join(curr))
                n_letter = len(word)
                n_word = 1
                curr = [word]
            else:
                n_letter += len(word)
                n_word += 1
                curr.append(word)
        lines.append(' '.join(curr) + ' '*(maxWidth - len(curr)-n_letter+1))
        return lines
