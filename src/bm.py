from typing import Dict


def make_km_table(pattern: str) -> Dict[str, int]:
    table = dict()
    for i in range(len(pattern)):
        table[pattern[i]] = len(pattern)-i-1
    return table 


class Bm(object):
    def __init__(self, text: str, pattern: str):
        self.text = text
        self.text_len = len(text)
        self.pattern = pattern
        self.pattern_len = len(pattern)
        self.table = make_km_table(pattern)

    def decide_slide_width(self, c: str) -> int:
        assert len(c) == 1
        width = self.table.get(c, self.pattern_len)
        return width

    def search(self) -> int:
        pattern_pos = self.pattern_len - 1
        text_pos = self.pattern_len - 1
        slide_width = 0

        while text_pos <= self.text_len - 1:
            while pattern_pos >= 0 and \
                    self.text[text_pos] == self.pattern[pattern_pos]:
                text_pos -= 1
                pattern_pos -= 1

            if pattern_pos < 0:
                return text_pos + 1
            else:
                slide_width = self.decide_slide_width(self.text[text_pos])
                text_pos += slide_width
                pattern_pos = self.pattern_len - 1

        return -1
