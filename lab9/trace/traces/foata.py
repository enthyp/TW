def fnf(word, system):
    # Find all dependent letters for each.
    alphabet = system.alphabet
    dep_rel = system.dep_relation

    marker = 0
    stacks = {l: [] for l in alphabet}
 
    # Fill stacks.
    for l in word[::-1]:
        stacks[l].append(l)
        for dep in dep_rel[l] - {l}:
            stacks[dep].append(marker)

    # Get normal form blocks.
    blocks = []

    while True:
        block = []
        empty = True

        for l in alphabet:
            if stacks[l]:
                empty = False
                if stacks[l][-1] != marker:
                    block.append(stacks[l].pop())
                    
        if empty: 
            break                
        
        for l in block:
            for d in dep_rel[l] - {l}:
                if stacks[d] and stacks[d][-1] == marker:
                    stacks[d].pop()

        block = ''.join(sorted(block))
        blocks.append(block)

    blocks = ['(' + b + ')' for b in blocks]
    return ''.join(blocks)

