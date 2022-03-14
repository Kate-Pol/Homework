stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}

total = {k: prices[k]*stock[k] for k in prices}
sum_total = sum(prices[k]*stock[k] for k in prices)
print(total)
print('Total price of all stocks is:', sum_total)

#Question 1: if no stock, but has a price - same as apples = 0. Please correct me if i'm wrong.
# Im just a bit confused.