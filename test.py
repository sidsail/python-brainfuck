from tracemalloc import start
import interpreter


def load_file():
	with open("tests.bf" , "r") as file:
		return str(file.read())

code = load_file()
hw = "+[>[<-[]>+[>+++>[+++++++++++>][>]-[<]>-]]++++++++++<]>>>>>>----.<<+++.<-..+++.<-.>>>.<<.+++.------.>-.<<+.<."
test = "[[]"
interpreter.interpret(test)
