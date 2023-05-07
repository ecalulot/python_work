#2-3
kr = "Kerri Russell"
print(f"Hello, I am the actress {kr}.")
print("\n")
#2-4
print(kr.lower())
print(kr.upper())
print(kr.title())
print("\n")
#2-5
stoic_author = 'Seneca'
author_quote = 'It is the power of the mind to be unconquerable.'
print(f'{stoic_author} once said, "{author_quote}"')
print('\n')
#2-6, repeat 2-5 using variables
famous_person = 'Randy Pausch'
message = "Complaining does not work as a strategy. We all have finite \
time and energy. Any time we spend whining is unlikely to help us achieve \
our goals. And it won't make us any happier."
print(f'{famous_person} once said, "{message}"')
print('\n')
#2-7
ma = " \t\tMarcus Aurelius\n \t"
print(f"Unaltered: {ma}")
print(f"Left strip: {ma.lstrip()}")
print(f"Right strip: {ma.rstrip()}")
print(f"Strip all white space: {ma.strip()}")
print('\n')
#2-8 removesuffix() and removeprefix() methods
filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))
print(filename.removeprefix('python_notes'))
print('\n')

