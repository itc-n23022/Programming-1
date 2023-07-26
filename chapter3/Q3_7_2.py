with open("number.txt", "r") as f:
    sum = 0
    for data in f:
        num = int(data)
        sum += num
    print(sum)  # 表示される答えは55なので答えは④
