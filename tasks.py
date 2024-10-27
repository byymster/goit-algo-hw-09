import time

# Жадібний алгоритм для видачі решти
def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    for coin in coins:
        if amount == 0:
            break
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    return result

# Динамічне програмування для видачі мінімальної кількості монет
def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    if dp[amount] == float('inf'):
        return {}

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

# Приклад використання
amount = 113
print("Жадібний алгоритм для видачі решти:", find_coins_greedy(amount))
print("Динамічне програмування для видачі мінімальної кількості монет:", find_min_coins(amount))

# Велике число для замірів
large_amount = 123456789

# Замір часу для жадібного алгоритму
start_time = time.time()
greedy_result = find_coins_greedy(large_amount)
greedy_time = time.time() - start_time

# Замір часу для алгоритму динамічного програмування
start_time = time.time()
dp_result = find_min_coins(large_amount)
dp_time = time.time() - start_time

print(f"\nЧас виконання жадібного алгоритму для {large_amount}: {greedy_time:.6f} секунди")
print(f"Кількість монет для жадібного алгоритму: {sum(greedy_result.values())}")
print(f"Час виконання динамічного програмування для {large_amount}: {dp_time:.6f} секунди")
print(f"Кількість монет для динамічного програмування: {sum(dp_result.values())}")