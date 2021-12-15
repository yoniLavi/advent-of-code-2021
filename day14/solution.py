from collections import Counter


def parse_input(filename):
    rules = {}
    with open(filename) as f:
        template = f.readline().strip()
        f.readline()
        for line in f:
            pair, insertion = line.strip().split(' -> ')
            rules[tuple(pair)] = insertion
    return rules, template


def pair_counter_to_elem_counter(pair_counter, boundaries):
    elem_counter = Counter()
    for pair, multiplicity in pair_counter.items():
        elem_counter[pair[0]] += multiplicity
        elem_counter[pair[1]] += multiplicity
    
    for elem in elem_counter.keys():
        elem_counter[elem] //= 2
    elem_counter += Counter(boundaries)
    return elem_counter


def run_simulation(rules, template, steps):
    boundaries = template[0], template[-1]
    main_counter = Counter(zip(template, template[1:]))
    for _ in range(steps):
        temp_counter = Counter()
        for pair, multiplicity in main_counter.items():
            insertion_elem = rules.get(pair)
            if insertion_elem:
                temp_counter[(pair[0], insertion_elem)] += multiplicity
                temp_counter[(insertion_elem, pair[1])] += multiplicity
            else:
                temp_counter[pair] += multiplicity
        main_counter = temp_counter

    elem_counts = pair_counter_to_elem_counter(main_counter, boundaries).most_common()
    return elem_counts[0][1] - elem_counts[-1][1]
        

if __name__ == '__main__':
    rules, template = parse_input('day14/input.txt')
    print(f'Part A: {run_simulation(rules, template, 10)=}')
    print(f'Part B: {run_simulation(rules, template, 40)=}')
