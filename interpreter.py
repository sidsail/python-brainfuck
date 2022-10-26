def interpret(code: str):
	tape = [0]
	p = 0
	cp = 0
	l = len(tape)
	lc = len(code)
	output = ""
	stack = []
	while cp < lc:
		if code[cp] == " ":
			cp += 1
			continue

		if code[cp] == "+":
			if tape[p] == 255:
				tape[p] = 0
				continue
			tape[p] += 1

		if code[cp] == "-":
			if tape[p] == 0:
				tape[p] = 255
				continue
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
				c = 1
				for i, v in enumerate(code[cp+1:]):
					print(code[:cp])
					if v == "[":
						c += 1
					if v == "]":
						c -= 1
					if c == 0:
						cp = i
						continue
				else:
					raise Exception("mismatched braces")
			else:
				stack.append(cp)

		if code[cp] == "]":
			if tape[p] != 0:
				cp = stack.pop()
				continue
		
		if code[cp] == ".":
			output += chr(tape[p])

		if code[cp] == ",":
			i = input("> ")
			tape[p] = ord(i)

		cp += 1	

	return output
