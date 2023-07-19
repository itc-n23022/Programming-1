numbers = [1, 1, 2, 3, 5, 8, 13, 21]
x = 0
for n in numbers:
    if n > 10:
        break
    x += n  # 10以下の数字の合計が表示されるので答えは③20
print(x)
