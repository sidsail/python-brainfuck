import interpreter

def load_file():
	with open("helloworld.bf" , "r") as file:
		return str(file.read())

#code = load_file()
code = "[]"

def test(code):
	output = interpreter.interpret(code)
	print(output)

test(code)