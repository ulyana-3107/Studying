def train(t1, t2, final_train):
    i = j = 0
    for k in range(len(final_train)):
        if i >= len(t1) or j >= len(t2):
            return False
        if t1[i] == final_train[k]:
            i += 1
        elif t2[j] == final_train[k]:
            j += 1
        else:
            return False
    return True


# True
t1, t2, final_train = [1, 2, 1, 3], [1, 4, 2, 1], [1, 1, 2, 4, 2, 1, 3, 1]

# False
t1_, t2_, final_train_ = [1, 2, 1, 3], [1, 4, 2, 1], [1, 1, 1, 2, 1, 2, 3, 4]
print(train(t1, t2, final_train))
print(train(t1_, t2_, final_train_))
