def build_profile(first, last, **user_info):
    p = {}
    p['first_name']=first
    p['last_name']=last
    for k,v in user_info.items():
        p[k]=v
    return p

m = build_profile("naresh", "K", location="AP", age="26", role="SE")
print(m)
