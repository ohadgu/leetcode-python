def max_profit(prices):
    lowest = prices[0]
    max_delta = 0
    for p in prices[1:]:
        if p < lowest:
            lowest = p
        elif p - lowest > max_delta:
            max_delta = p - lowest
    return max_delta


# -------------------------------------------------
prices = [7,1,5,3,6,4]
max_p = max_profit(prices)
print(max_p)
input("end")
