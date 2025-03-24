def parseData():
    with open("data/day19.txt","r") as f:
        patterns = [pattern.strip() for pattern in f.readline().split(',')]
        designs = [line.strip() for line in f.readlines()[1:]]

    return patterns, designs

patterns, designs = parseData()
pat_set = set(patterns)
winners = set()

for i, design in enumerate(designs):
    print(f"Starting pattern {i} - {design}")

    queue = [('',design)]
    searching = True
    while len(queue)>0 and searching:
        hist, rem = queue.pop()
        if rem == '':
            winners.add(design)
            print(f"Pattern {i} is good ({len(winners)})")
            searching = False
        else:
            paths = set()
            for pattern in pat_set:
                if rem.startswith(pattern):
                    new_hist = hist+pattern
                    queue.append((new_hist,rem[len(pattern):]))
                    paths.add(new_hist)
            pat_set.update(paths)
    if searching:
        print(f"Pattern {i} is bad ({len(winners)})")
print(len(winners))
