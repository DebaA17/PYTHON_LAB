def sum_odd_factors(n):
    return sum(i for i in range(1, n+1, 2) if n % i == 0)

print(sum_odd_factors(12))  # 1 + 3 = 4
