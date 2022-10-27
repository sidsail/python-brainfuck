import sys
def interpret(code: str):
	m = {}
	arr = []
	for i, v in enumerate(code):
		if v == "[":
			arr.append(i)
		if v == "]":
			x = arr.pop()
			m[x] = i
			m[i] = x
	if len(arr) != 0:
		raise Exception("mismatched braces")
	tape = [0]
	p = 0
	cp = 0
	l = len(tape)
	lc = len(code)
	while cp < lc:
		token = code[cp]
		if token == "+":
			if tape[p] == 255:
				tape[p] = 0
				cp += 1
				continue
			tape[p] += 1
		if token == "-":
			if tape[p] == 0:
				tape[p] = 255
				cp += 1
				continue
			tape[p] -= 1
		if token == ">":
			if p == l-1:
				tape.append(0)
				l += 1
			p += 1
		if token == "<":
			if p != 0:
				p -= 1
		if token == "[":
			if tape[p] == 0:
				cp = m[cp]
				continue
		if token == ".":
			sys.stdout.write(chr(tape[p]))
		if token == ",":
			tape[p] = ord(sys.stdin.read(1))
		if token == "]":
			if tape[p] != 0:
				cp = m[cp]
		cp += 1
