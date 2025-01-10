lines = [line.strip() for line in open(0)]
conj = lines[0].lower()
words = lines[1:]
if len(words) == 1:
    print(words[0])
elif len(words) == 2:
    print(words[0], conj, words[1])
else:
    print(f"{''.join(map(lambda x: x + ', ', words[:-1]))}{conj} {words[-1]}")
