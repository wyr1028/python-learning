def findMinAndMax(L):
    if len(L)==0:
        return (None, None)
    else:
        min_val = max_val = L[0]
        for x in L:
            if x < min_val:
                min_val = x
            if x > max_val:
                max_val = x
        return (min_val, max_val)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
