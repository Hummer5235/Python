# t = "hello world"
# t2 = 'хелло ворлд'
#
# c = list(zip(t,t2))
# print(c)

# a = "hello_world"
# b = "хелло_ворлд"
# c = zip(a,b)
# for x in c:
#     a = a.replace(x[0], x[1])
# print(a)

t = """Куда ты скачешь, гордый конь,
       И где опустишь ты копыта?
       О мощный властелин судьбы!
       Не так ли ты над самой бездной, 
       На высоте, уздой железной
       Россию поднял на дыбы?"""

def every_second_word(string):
    a = string.split()
    lst = []
    for x in range(len(a)):
        if x%2 == 1:
            lst.append(a[x])
    lst.sort()
    return lst

print(every_second_word(t))
#
# lst = [a[x] for x in range(len(a)) if x % 2 == 1]


