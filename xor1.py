givenStr = "label"

flag = "crypto{"
for s in givenStr:
	uni = ord(s)
	doXor = uni ^ 13
	strXor = chr(doXor)
	flag += strXor

flag += "}"

print("Flag:", flag)
