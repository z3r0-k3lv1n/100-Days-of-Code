# FUNCTIONS WITH OUTPUTS

def format_name(f_name, m_name, l_name):
  '''Takes a first name, middle name and last name and format it to return the title case of the name.'''
  if f_name == "" or l_name == "":
    return "You didn't enter valid inputs!"
  formatted_f_name = f_name.title() # title() changes the input to title case. eg stePhen becomes Stephen
  formatted_m_name = m_name.title()
  formatted_l_name = l_name.title()
  return f"Result: G'day {formatted_f_name} {formatted_m_name} {formatted_l_name}. How are you today?"

print(format_name(input("What is your first name? "), input("If you have a middle name enter it here: "), input("What is your family name? ")))
print(format_name.__doc__)


# DOCSTRINGS
# Docstrings are the string literals that appear right after the definition of a function, method, class or module.
# Docstrings are used to document the code.
# They are different to comments as comments are ignored by the python interpreter and usually are used to indicate the intent behind specific aspects of the code.
# The __doc__ attribute can later be used to retrieve the docstring.
# Docstrings are created by using '''<ENTER DOCSTRING TEXT HERE>'''
# If you make this a variable it becomes part of the code
# EG
def example():
  '''example() is a docstring example function'''
  a = ''' === This text is now a variable ==='''
  return a

# eg
def square(n):
  '''Takes in a number 'n', returns the square of that number'''

  return f"The square of {n} is {n**2}"

print("\n")
print(square(int(input("What number would you like to know the square of? "))))
print(f"The square function {square.__doc__}")

print("\n")
print(example())
print(example.__doc__)