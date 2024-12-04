programming_words = {
	'variable': 'references information (memory) associated with the variable',
	'loop': 'programming structure used to repeat simple code a series of times',
	'list': 'data structure used to store and access multiple variables',
	'dictionary': 'data structure used to model real-world scenarios and store different kinds of information',
	'boolean_expression': 'a test that outputs either a True or False result',
	'if statement': 'used to test whether or not a certain condition is true',
	'if-elif-else statement': 'tests one condition if there are multiple factors',
	'integer': 'a data type that is a simple number, i.e 4, -4, 2, 0',
	'float': 'a data type with multiple digits; not a simple number, i.e 3.4, 2.6, 3.9, -2.346',
	'string': 'a simple data type that is not seen as code, i.e a person\'s name',
	}

for term, meaning in programming_words.items():
	print(f"{term.title()}: \n\t{meaning}\n")