def interpret(code: str):
	code = code.replace(" ", "")
	arr = []
	m = {}
	for i, v in enumerate(code):
		if v == "[":
			arr.append(i)
		if v == "]":
			try:
				a = arr.pop()
			except IndexError:
				raise Exception("braces mismatch(more closing than opening)")
			m[a] = i
	if len(arr) != 0:
		raise Exception("braces mismatch(more opening then closing)")

	tape = [0]
	p = 0
	cp = 0
	l = len(tape)
	lc = len(code)
	output = ""
	while cp < lc:
		if code[cp] == "":
			cp += 1
			continue
		if code[cp] == " ":
			cp += 1
			continue
		if code[cp] == "+":
			tape[p] += 1
		if code[cp] == "-":
			if tape[p] == 0:
				tape[p] = 255
			tape[p] -= 1
		if code[cp] == ">":
			if p == l-1:
				tape.append(0)
				l += 1
			p += 1
		if code[cp] == "<":
			if p == 0:
				raise Exception("trying to go before tape start")
			p -= 1
		if code[cp] == "[":
			if tape[p] == 0:
				cp = m[cp]
				continue
		if code[cp] == ".":
			output += chr(tape[p])
		if code[cp] == ",":
			i = input("> ")
			tape[p] = ord(i)
		if code[cp] == "]":
			if tape[p] != 0:
				keys = [k for k, v in m.items() if v == cp]
				cp = keys[0]
				continue

		cp += 1
	return output
