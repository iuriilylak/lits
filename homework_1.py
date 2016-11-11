lst = [1, [2, 3], 4, [[6, 7]]]

def first():
    result = []
    for i in lst:
        if type(i) != list :
            result.append(i)
        elif type(i) == list:
            result.extend(i)
            while True:
                if type(result[-1]) == list:
                    l = result[-1]
                    result = result[0:-1]
                    result.extend(l)
                    continue
                else:
                    break
    return result

def second():
    str1 = ''.join(str(e) for e in lst)
    str1 = str1.replace("[", "")
    str1 = str1.replace("]", "")
    str1 = str1.replace(",", "")
    str1 = str1.replace(" ", "")
    result = []
    for i in str1:
        result.append(i)
    return result



a = first()
b = second()

print(a)
print(b)


# def ext(l):
#     data = l
#     data.sort()
#     result = []
#     if type(data[-1]) == list and type(data) == list:
#         data.sort()
#         p = data[0:-1]
#         p.extend(data[-1])
#         result = ext(p)
#         return result
#     else:
#         result.extend(data)
#         return result