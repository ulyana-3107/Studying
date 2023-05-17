# Проверить соблюдаются ли приоритеты логических операций (отрицание, конъюнкции и дизъюнкции) в питоне.
# Составить пару примеров для проверки.


var1 = not True
var2 = not False
var3 = True and False
var4 = True or False

var5 = not True and False
var6 = True and not False
var7 = False and not True
var8 = not (True and False)
var9 = True or not True
var10 = True or not False
var11 = False or not False
var12 = False or not True

var13 = not True or False
var14 = not (True or False)
var15 = False or not True and True and False
var16 = True and False or False and not True
var17 = not True and False or False and not True


results = [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]


if __name__ == '__main__':
    for i in range(1, 18):
        name = eval('var' + str(i))
        print(name, name == bool(results[i - 1]), '\n')
