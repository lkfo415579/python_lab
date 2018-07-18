class Text2Int:

    def __init__(self):
        numwords = {}
        units = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen",
        ]

        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        scales = ["hundred", "thousand", "million", "billion", "trillion"]
        scales_dict = {"hundred": 100, "thousand": 1000, "million": 1000 ** 2, "billion":  1000 ** 3, "trillion": 1000 ** 4}

        numwords["and"] = (1, 0)
        for idx, word in enumerate(units):
            numwords[word] = (1, idx)
        for idx, word in enumerate(tens):
            numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales):
            numwords[word] = (10 ** (idx * 3 or 2), 0)
        #
        self.numwords = numwords
        self.scales_dict = scales_dict

    def isfloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def Full_text2int(self, textnum):
        current = result = 0
        for word in textnum.split():
            # if word not in self.numwords:
            #     raise Exception("Illegal word: " + word)
            scale, increment = self.numwords[word]
            current = current * scale + increment
            if scale > 100:
                result += current
                current = 0

        return result + current

    def is_text_contains_number(self, words):
        for word in words:
            if self.isfloat(word):
                return True
        return False

    # return float
    def text2int(self, text):
        # check whole is number or not
        if self.isfloat(text):
            return float(text)
        # 11.5 million case
        words = text.split()
        if self.is_text_contains_number(words):
            sum = 0.0
            for index, word in enumerate(words):
                if self.isfloat(word):
                    # Fucked there is a number
                    scale = self.scales_dict[words[index + 1]]
                    sum += float(word) * scale
            return sum
        # all words
        return float(self.Full_text2int(text))


text2int_Gen = Text2Int()

print text2int_Gen.text2int("four hundred eighty thousand")
print text2int_Gen.text2int("three billion nine hundred million")
print text2int_Gen.text2int("11.363 million 5 thousand")
