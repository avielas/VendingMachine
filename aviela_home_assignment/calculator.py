

class Calculator:
    """
    Calculator class for handle calculation
    """
    def CalculateMinimum(self, coins: dict, change: int) -> dict:
        """
        Calculate the minimum number of coins to produce the amount of change required
        @param coins: Dictionary of coins [(val,quantity), ...]
        @type coins: Dictionary
        @param change: change to calculate the returned coins
        @type change: Integer
        @return: None if don't exists amount of coins whose sum is the change, else Dictionary of coins which should be returned to user
        @rtype: None or Dictionary
        """
        minimalMatch = None
        minimalCount = -1
        subset = coins

        for x in range(0, len(coins)):
            matches = self.__CalculateFinite(subset, change, 0)
            if matches is not None:
                matchCount = sum(matches.values())
                if minimalMatch is None or matchCount < minimalCount:
                    minimalMatch = matches
                    minimalCount = matchCount
            first_key = list(coins.keys())[0]
            del subset[first_key]

        return minimalMatch

    def __CalculateFinite(self, coins: dict, change: int, start: int) -> dict:
        """
        The function calculate the number of coins which should be returned to user (which may not be the MINIMUM).
        This function implement algorithm which run on coins (from bigger to smaller. it assumes the dictionary is sorted) and try to find
        if exists amount of coins whose sum is the change
        @param coins: Dictionary of coins [(val,quantity), ...]
        @type coins: Dictionary
        @param change: change to calculate the returned coins
        @type change: Integer
        @param start: Next index for the recursion
        @type start: Integer
        @return: None if don't exists amount of coins whose sum is the change, else Dictionary of coins which should be returned to user
        @rtype: None or Dictionary
        """
        for x in range(start, len(coins)):
            # get current key and value
            coinValue = int(list(coins.keys())[x])
            coinCount = list(coins.values())[x]
            # no point calculating anything if no coins exist or the
            # current Value is too high
            if coinCount > 0 and coinValue <= change:
                reminder = change % coinValue
                if reminder < change:
                    howMany = min(coinCount, (change - reminder) / coinValue)
                    matches = dict([])
                    matches[str(coinValue)] = int(howMany)

                    amount = howMany * coinValue
                    changeLeft = change - amount
                    if changeLeft == 0:
                        return matches

                    subCalc = self.__CalculateFinite(coins, changeLeft, x + 1)

                    if subCalc is not None:
                        matches.update(subCalc)
                        return matches
        return None
