def rev(num):
    num = str(num)
    if len(num) == 1:
        return num
    return int(num[-1] + num[1:-2] + num[0])
