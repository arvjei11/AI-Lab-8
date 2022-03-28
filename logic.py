def validator(expression):
-
expression_object = Resolver(expression)
expression_object_type = expression_object.recognizer()
parsed_expression = expression_object.expression_parser()
if expression_object_type == "Pure":
if "NOT" in expression_object.get():
temp_inverted = expression_object.temp_negative_inverter()
if temp_inverted not in knowledge_dict:
proof_dict[expression_object] = None
return None
elif knowledge_dict[temp_inverted] is True:
proof_dict[expression_object] = False
return False
else:
proof_dict[expression_object] = True
return True

else:
if expression_object not in knowledge_dict:
proof_dict[expression_object] = None
return None
else:
proof_dict[expression_object] = knowledge_dict[
expression_object]
return proof_dict[expression_object]
elif expression_object.is_pure_proposition() is True:
proof_dict[expression_object] =
expression_object.general_resolver()
else:

proof_dict[expression_object] =
expression_object.general_resolver()

if expression_object.recognizer() == "Conditional":
for expression in parsed_expression.values():
expression_type = expression.recognizer()
if expression_type != "Pure" and expression_type !=

"Broken":

validator(expression.get())

else:
for expression in parsed_expression:
expression_type = expression.recognizer()
if expression_type != "Pure" and expression_type !=

"Broken":

validator(expression.get())

#
--------------------------------------------------------------------------
----
if __name__ == '__main__':
knowledge_dict = dict()
user_input = ""
print("Please keep entering the logical arguments you would like to" +
" define.\nTo see the results and further validate new

arguments" +

" based on your arguments enter -1.")
input_list = list()
while user_input != "-1":
user_input = input("\nNew argument:\t")
if user_input != "-1":
expression_object = Expression(user_input)

if expression_object.recognizer() == "Broken":
print("Incorrect Syntax. Please try again: ")
continue
elif expression_object.recognizer() == "Pure":
if expression_object.valid_parentheses_checker() is False:
print("Parentheses do not exist or aren't in a valid

form.")

continue

input_list.append(user_input)

failed_expression = set()
for count in range(2):
for expression in input_list:
try:
interpreter(expression)
except Exception:
failed_expression.add(expression)

for expression in failed_expression:
print("\nThis expression could not be submitted due to a problem:
",

expression)

print(40 * "-" + "\nExpressions and arguments you defined: ")
for expression in knowledge_dict:
print(expression.get(), "--->", knowledge_dict[expression])
print(40 * "-" + "\nEnter the new argument you would like to validate:
" +

"\nEnter 'view' at any time to see the full list of arguments

and" +

" their results\nEnter 'exit' to quit.")
proof_dict = knowledge_dict.copy()
while user_input != "exit":
user_input = input("\nValidate:\t")

if user_input != "exit":
if user_input == "view":
for expression in proof_dict:
print(expression.get(), "--->",

proof_dict[expression])
else:
for i in range(2):
try:
validator(user_input)
except Exception:
"There is a problem with this argument."
continue

for expression in proof_dict:
if expression.get() == user_input:
print(user_input, "----->",

proof_dict[expression])
