def fnf(word, alphabet, independence_relation):
    # Find all dependent letters for each.
    dep_map = {l: set(alphabet) - {l} for l in alphabet}
    for a, b in independence_relation:
        dep_map[a].discard(b)
        dep_map[b].discard(a)

    marker = 0
    stacks = {l: [] for l in alphabet}
    
    # Fill stacks.
    for l in word[::-1]:
        stacks[l].append(l)
        for dep in dep_map[l]:
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

        if not block:
            for l in alphabet:
                if stacks[l]:
                    stacks[l].pop()   
        
        for l in block:
            for d in dep_map[l]:
                if stacks[d] and stacks[d][-1] == marker:
                    stacks[d].pop()

        block = ''.join(sorted(block))
        blocks.append(block)

    blocks = ['(' + b + ')' for b in blocks]
    return ''.join(blocks)


def from_graph(dot_graph):
    pass    


