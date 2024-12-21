def parseData():
    with open("data/day19.txt","r") as f:
        patterns = [pattern.strip() for pattern in f.readline().split(',')]
        designs = [line.strip() for line in f.readlines()[1:]]

    return patterns, designs

patterns, designs = parseData()
pat_set = set(patterns)

goods = set()
bads = set()

count = 0
for i,design in enumerate(designs):
    potentials = [(design,"")]
    good = False
    options = set()
    while len(potentials)>0:
        current_design,past = potentials.pop()

        if current_design == "" or current_design in goods:
            count+=1
            good = True
            goods.add(design)
            if design not in pat_set:
                patterns.append(design)
                pat_set.add(design)
            #print(f"{i} - {design} - {count}")
            break

        if current_design in bads:
            continue
            #200(low) when using break
            #219(high) when using continue
            #compare outputs of each and investigate the difference

        found = False
        for pattern in patterns:
            if current_design.startswith(pattern):
                found = True
                next = current_design.lstrip(pattern)
                new_past = past+pattern
                if new_past not in pat_set:
                    patterns.append(new_past)
                    pat_set.add(new_past)
                if next not in options:
                    options.add(next)
                    j = 0
                    while j<len(potentials) and len(next)<len(potentials[j][0]):
                        j+=1
                    potentials.insert(j,(next,new_past))
        if not found:
            bads.add(current_design)


    if not good:
        bads.add(design)
    print(f"{i} - {'good' if good else 'bad'} - {design} - {count}")
print(count)

#200 is too low
#219 is too high
