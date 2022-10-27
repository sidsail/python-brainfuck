import interpreter
import time

def load_file():
	with open("helloworld.bf" , "r") as file:
		return str(file.read())

code = load_file()

def test(code):
	output = interpreter.interpret(code)
	return output
output = test(code)
print(output)