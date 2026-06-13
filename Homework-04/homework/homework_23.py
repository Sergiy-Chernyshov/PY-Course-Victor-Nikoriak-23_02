#Task1
def question1(first_list, second_list):
    res = []
    for el in first_list:          # n
        if el in second_list:     # n (linear search)
            res.append(el)
    return res

def question2(n: int) -> int:
    for _ in range(10):   # константа
        n **= 3
    return n

def question3(first_list, second_list):
    temp = first_list[:]

    for el_second_list in second_list:      # n
        flag = False
        for check in temp:                  # n
            if el_second_list == check:
                flag = True
                break
        if not flag:
            temp.append(el_second_list)

    return temp

def question4(input_list):
    res = 0
    for el in input_list:   # n
        if el > res:
            res = el
    return res

def question5(n: int):
    res = []
    for i in range(n):        # n
        for j in range(n):    # n
            res.append((i, j))
    return res

def question6(n: int):
    while n > 1:
        n /= 2
    return n