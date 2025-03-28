def parseData():
    with open("data/day19winners.txt","r") as f:
        patterns = [pattern.strip() for pattern in f.readline().split(',')]
        designs = [line.strip() for line in f.readlines()[1:]]

    return patterns, designs

patterns, designs = parseData()
pat_set = set([(pattern, pattern, 1) for pattern in patterns])
print(pat_set)
#pat_set = set(patterns)
winners = set()
total_count = 0
total_iterations = 0

for i, design in enumerate(designs):
    print(f"Starting pattern {i} - {design}")

    local_count = 0
    queue = [('','',design,1)]
    searching = True
    space_set = set()
    while len(queue)>0:
        total_iterations +=1
        hist, space_hist, rem, count = queue.pop()
        if rem == '':
            local_count+=count
            total_count+=count
            print(f"Pattern {i} is good +{local_count} ({total_count})")
            searching = False
        else:
            paths = set()
            for pat in pat_set:
                #print(type(pat),pat)
                pattern, spaces, value = pat
                if rem.startswith(pattern):
                    new_spaces = space_hist + " " + spaces
                    new_spaces = new_spaces.strip()
                    if new_spaces not in space_set:
                        new_hist = hist + pattern
                        new_val = count*value
                        space_set.add(new_spaces)
                        queue.append((new_hist,new_spaces,rem[len(pattern):],new_val))
                        paths.add((new_hist,new_spaces,new_val))
            pat_set.update(paths)
    if searching:
        print(f"Pattern {i} is bad ({len(winners)})")

    pass
print(f"Total count: {total_count}")
print(f"Total iterations: {total_iterations}")


#Event the first one is greater that 250k
#Sample should be less than 54 iterations and have 16 count