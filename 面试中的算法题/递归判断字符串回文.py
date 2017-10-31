def text(s):
    def ish(s):
        if len(s)<=1:return True
        if s[0]==s[-1]:return ish(s[1:-1])
        return False
    if len(s)<=1:return False
    return ish(s)

test=['','a','123a321','今天你吃了吗了吃你天今']

for item in test:
    print(text(item))