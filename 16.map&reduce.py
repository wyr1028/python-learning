def normalize(name):
    def first_upper(s):
        return s[0].upper() + s[1:].lower()
    return first_upper(name)

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
