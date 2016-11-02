def flatten(lst):
	return sum( ([x] if not isinstance(x, list) else flatten(x)
		     for x in lst), [] )

lst = [1, [2, 3], 4, [[6, 7]]]
lst = flatten(lst)
print lst