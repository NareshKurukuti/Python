def make_pizza(size, *toppings):
    print('\n making pizza with '+ str(size))
    for topping in toppings:
        print('__', topping.title())





def Test(list1, list2):
    while list1:
        p = list1.pop()
        list2.append(p)
        print(list2)
    return list2

lone = ['h1', 'h2', 'h3', 'h4']
ltwo = ['s1', 's2', 's3', 's4']

Test(lone,ltwo)
lone.extend(ltwo)


def buildProfile(fname, lname, **user_info):
    p = {}
    p['first_name']=fname
    p['last_name']=lname
    for k,v in user_info.items():
        p[k]=v
    return p

m = buildProfile("naresh", "K", location="AP", role="SE")
print(m)
    
