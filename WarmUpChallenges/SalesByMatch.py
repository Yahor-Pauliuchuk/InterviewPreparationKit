class SalesByMatch:
    def sockMerchant(self, socksColors):
        if self.__isProvidedArrayValid(socksColors):
            raise ValueError("The count of socks should be greater than 0 and less than 101.")

        possiblePairs = []
        couples = 0

        for i in socksColors:
            possiblePairs.append(i)

            if self.__isPairForColorExist(possiblePairs, i):
                couples += 1
                possiblePairs = self.__removeMatchedSocks(possiblePairs, i)

        return couples

    def __isProvidedArrayValid(self, socksColors):
        MIN = 1
        MAX = 100
        return True if (len(socksColors) < MIN or len(socksColors) > MAX) else False

    def __isPairForColorExist(self, possiblePairs, color):
        PAIR = 2
        return True if possiblePairs.count(color) == PAIR else False

    def __removeMatchedSocks(self, possiblePairs, color):
        return [j for j in possiblePairs if j != color]
