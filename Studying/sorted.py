lst = ["Кострома","Ярославль","Астрахань","Москва"]
print(sorted(lst,key = lambda x : x[0]))



a = [1,2,-5,0,5,10]
print(sorted(a)[:3])


digs = (-10,0,7,-2,3,6,-8)
print(sorted(digs,key = lambda x : x >= -1))


dict = {"+7":2345364,"+4":34560239,"+5":211953459,"+12":23543212}
print(sorted(dict.items(),key = lambda x: int(x[0])))