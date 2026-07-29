from functools import reduce

def str2float(s):
    DIGITS={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':-1}
    def index(s):
        return DIGITS[s]
    def index_dot(s):
            for i in range(len(s)):
                if s[i]=='.':
                    return int(len(s)-i-1)
    a=index_dot(s)
    s=map(index,s)
    def fn(x,y):
        if y!=-1:
            return x*10+y
        else:
            return x
    return reduce(fn,s)/ 10**a

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
