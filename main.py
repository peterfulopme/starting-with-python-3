words = "This is a sample statement".split()
print(words)

lcomp = {len(word) for word in words}
print(lcomp)
print(type(lcomp))
