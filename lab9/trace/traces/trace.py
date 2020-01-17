from collections import defaultdict


def trace(word, independence_relation):
    # Build independence map.
    ind_map = defaultdict(set)
    for a, b in independence_relation:
        ind_map[a].add(b)
        ind_map[b].add(a)

    # Get lexicographically smallest trace (think bubble sort).
    trace = list(word) 

    for i in range(len(trace) - 1):
        swapped = False

        for j in range(len(trace) - 1, i, -1):
            left, right = trace[j - 1], trace[j]
            are_independent = left in ind_map[right]

            if are_independent and left > right:
                swapped = True
                trace[j], trace[j - 1] = left, right

        if not swapped:
            break

    return ''.join(trace)


# TODO: we actually want ALL trace elements!
