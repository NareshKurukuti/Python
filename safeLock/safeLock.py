def sum_code():
    if d['one']+d['two']+d['thr']+d['fou']+d['fiv']==30:
        return True


def passwd_code(n):
    if d['fiv'] + d['thr'] == 14 and d['two'] * 2 -1 == d['one'] and\
        d['two'] + 1 == d['fou'] and d['two'] + d['thr'] == 10\
          and sum_code():
                return True




for code in range(0, 100000):
    code = str(code).zfill(5)
    d = {}
    d['one']=int(code[0])
    d['two']=int(code[1])
    d['thr']=int(code[2])
    d['fou']=int(code[3])
    d['fiv']=int(code[4])
    if passwd_code(code):
        print(code)
