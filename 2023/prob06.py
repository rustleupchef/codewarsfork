for line in open(0):
    h, w, t = map(lambda x: x if x in 'SD' else int(x), line.split())
    if h == 0 and w == 0 and t == 'S': break
    if t == 'S':
        print(f"Square {2 * (h+40 + w)}")
    else:
        print(f"Diagonal {2 * (h+80 + w+80)}")
