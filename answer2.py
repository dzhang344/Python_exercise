profit = input('Please enter profit:')
profit = int(profit)
bonus = 0
while profit > 0:
    if profit > 1000000:
        bonus += (profit-1000000) * 0.01
        profit = 1000000
    elif profit > 600000:
        bonus += (profit-600000) * 0.015
        profit = 600000
    elif profit > 400000:
        bonus += (profit-400000) * 0.03
        profit = 400000
    elif profit > 200000:
        bonus += (profit-200000) * 0.05
        profit = 200000
    elif profit > 100000:
        bonus += (profit-100000) * 0.075
        profit = 100000
    else:
        bonus += profit * 0.1
        profit = 0

print(bonus)
