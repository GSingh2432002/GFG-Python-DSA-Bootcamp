# Stock buy and sell
def maxProfit(price,n):
    if n < 2:
        return "Array should have atleast two elements to make profit."
    profit = 0
    for i in range(1,n):
        if price[i] > price[i-1]:
            profit += price[i] - price[i-1]
    return profit
user_input = input("Enter a list of stock prices separated by spaces: ")
prices = list(map(int, user_input.split()))
result = maxProfit(prices, len(prices))
print("Maximum profit that can be achieved is:", result)
    