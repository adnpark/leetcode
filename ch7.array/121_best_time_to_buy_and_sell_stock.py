'''
1. 최저 가격 시점을 찾는다.
2. 해당 시점 이후의 가장 높은 가격을 찾는다.
3. 가장 높은 가격에서 최저 가격을 뺀 값을 리턴한다.
잘못된 풀이 ex) [2,4,1,2]
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = min(prices)
        min_index = prices.index(min_price)

        if (min_index == len(prices) - 1):
            return 0

        sliced_prices = prices[min_index + 1:]
        max_price = max(sliced_prices)

        max_profit = max_price - min_price
        if (max_profit < 0):
            return 0
        return max_profit


'''
1. 가격 리스트를 순회하는 반복문을 작성한다.
2. 현재 인덱스의 가격을 저점이라고 가정하고, 이후의 고점을 찾는다. 
3. Max Profit을 계산해나간다.
잘못된 풀이 => O(n^2) 타임아웃
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in enumerate(prices):
            profit = 0
            min_price = prices[i]
            max_price = max(prices[i + 1:])
            if max_price < min_price:
                profit = 0
            else:
                profit = max_price - min_price
            if max_profit < profit:
                max_profit = profit
        return max_profit


'''
1. prices를 순회하는 반복문을 작성한다.
2. 반복문을 순회하며 최소값과 최대값을 갱신한다.
3. 최소값과 현재 price와의 차이를 계산하여 최대값을 갱신한다.
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit
