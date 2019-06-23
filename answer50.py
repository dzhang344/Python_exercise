
# 题目050：输出一个随机数。

import random

print(random.random())
print(random.uniform(0, 100))
print(random.randrange(0, 100, 2))
print(random.randint(0, 100))

seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
print(random.choice(seed))
print(random.sample(seed, 3))
print(''.join(random.sample(seed, 3)))
