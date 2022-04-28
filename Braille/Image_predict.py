import operator


class Predict():
    result = []

    def Predict(self, model, real):
        my_list = model.predict(real)
        index, value = max(enumerate(my_list[0]), key=operator.itemgetter(1))
        print(index, alpha(index))
        self.result.append(alpha(index))

        return self.result

    def reset(self):
        self.result = []


def chk_trans():
    for i in range(0, 27):
        print(str(i) + ':' + alpha(i), end='  ')
        if i % 3 == 2:
            print()


def alpha(num):
    if num == 26:
        return ' '
    else:
        num_tr = num + 97
        return chr(num_tr)