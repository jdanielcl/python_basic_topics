chain = "hello WORLD!"
print(chain)

chain = chain.upper()
print(chain)

chain = chain.lower()
print(chain)

chain = chain.capitalize()
print(chain)

chain = chain.count('l')
print(chain)

chain = "hello WORLD!"
chain = chain.find('W')
print(chain)

chain = "hello WORLD!"
chain = chain.isdigit()
print(chain)

chain = "10"
chain = chain.isdigit()
print(chain)

chain = "helloWORLD123"
chain = chain.isalnum()
print(chain)

chain = "helloWORLD"
chain = chain.isalpha()
print(chain)

chain = "  hello WORLD i'm here "
chain = chain.split()
print(chain)
chain = "  hello WORLD i'm here "
f,s,t,f = chain.split()
print(f'{f}, {s}, {t}, {f}')

chain = "  hello WORLD i'm here "
print(chain)
chain = chain.strip()
print(chain)

chain = chain.replace('WORLD','universe')
print(chain)

chain = chain.rfind('o')
print(chain)

