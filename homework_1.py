# def flatten(lst):
# 	return sum( ([x] if not isinstance(x, list) else flatten(x)
# 		     for x in lst), [] )
#
# lst = [1, [2, 3], 4, [[6, 7]]]
# lst = flatten(lst)
# print lst



lst = [1, [2, 3], 4, [[6, 7]]]


def ext(l):
    data = l
    result = []
    if type(data[-1]) == list and type(data) == list:
        data.sort()
        p = data[0:-1]
        p.extend(data[-1])
        result = ext(p)
        print(p)
        print(result)
        return result
    else:
        result.extend(data)
        return result


print(ext(lst))
