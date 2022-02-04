class MyDict(dict):
    def add(self, item: str) -> None:
        """add new value to dict"""
        if item in self:
            self[item] += 1
        else:
            self[item] = 1

    def sort(self):
        """insertion sort firstly by value then by key"""
        temp = MyDict({k: v for k, v in (sorted(self.items(), key=lambda item: item[0]))[::-1]})
        return MyDict({k: v for k, v in (sorted(temp.items(), key=lambda item: item[1]))[::-1]})

    def to_string(self):
        """return string form of dict"""
        text = ""
        for item in self:
            text += item + " " + str(self[item]) + "\n"
        return text


def frequency_analysis() -> None:
    """Read number of words and words, then sort and return each word and number of repeating of it"""
    string = input().split()

    words = MyDict()
    for word in string:
        words.add(word)

    words = words.sort()

    print(words.to_string())


if __name__ == "__main__":
    number_of_words = int(input())
    if number_of_words:
        frequency_analysis()
