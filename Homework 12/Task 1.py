class CardDeck:
    def __init__(self):
        self.length = 52
        self.index = 0
        self.__SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.__RANKS = [*range(2, 11), "J", "Q", "K", "A"]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.length:
            raise StopIteration
        else:
            suits = self.__SUITS[self.index // 13]
            ranks = self.__RANKS[self.index % 13]
            self.index += 1
            return f"{suits} {ranks}"


asd = CardDeck()
for card in asd:
    print(card)
