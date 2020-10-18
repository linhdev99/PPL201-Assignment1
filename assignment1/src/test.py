value = r" abc ' xyz"
possible = ['\b', '\t', '\n', '\f', '\r', '\'', '\\']
if value[-1] in possible:
	print("illigal")
else:
    print(value)
