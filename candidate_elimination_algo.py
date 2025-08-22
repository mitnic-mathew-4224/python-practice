def get_domains(data):
    domains = [set() for _ in range(len(data[0]) - 1)]
    for row in data:
        for i in range(len(row) - 1):
            domains[i].add(row[i])
    return [list(d) for d in domains]

def more_general(h1, h2):
    more_general_parts = []
    for x, y in zip(h1, h2):
        mg = x == "?" or (x != "0" and (x == y or y == "0"))
        more_general_parts.append(mg)
    return all(more_general_parts)

def fulfills(hypothesis, example):
    return all(h == e or h == '?' for h, e in zip(hypothesis, example))

def min_generalizations(h, x):
    new_h = list(h)
    for i in range(len(h)):
        if h[i] == '0':
            new_h[i] = x[i]
        elif h[i] != x[i]:
            new_h[i] = '?'
    return [new_h]

def min_specializations(h, domains, x):
    results = []
    for i in range(len(h)):
        if h[i] == '?':
            for val in domains[i]:
                if x[i] != val:
                    new_h = h.copy()
                    new_h[i] = val
                    results.append(new_h)
        elif h[i] != '0':
            new_h = h.copy()
            new_h[i] = '0'
            results.append(new_h)
    return results

def candidate_elimination_algorithm(data):
    domains = get_domains(data)
    n_features = len(data[0]) - 1
    S = [['0'] * n_features]
    G = [['?'] * n_features]

    for i, instance in enumerate(data):
        x, label = instance[:-1], instance[-1]
        if label == "Yes":
            G = [g for g in G if fulfills(g, x)]
            S_temp = []
            for s in S:
                if not fulfills(s, x):
                    S_temp.extend(min_generalizations(s, x))
                else:
                    S_temp.append(s)
            S = [h for h in S_temp if any(more_general(g, h) for g in G)]
        else:
            S = [s for s in S if not fulfills(s, x)]
            G_temp = []
            for g in G:
                if fulfills(g, x):
                    G_temp.extend(min_specializations(g, domains, x))
                else:
                    G_temp.append(g)
            G = [h for h in G_temp if any(more_general(h, s) for s in S)]

        # Remove duplicates
        G = [list(x) for x in set(tuple(x) for x in G)]
        S = [list(x) for x in set(tuple(x) for x in S)]

    return S, G

# Example usage
if __name__ == "__main__":
    data = [
        ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
        ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
        ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
        ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
    ]

    S_final, G_final = candidate_elimination_algorithm(data)

    print("Final Specific Hypothesis S:")
    for s in S_final:
        print(s)

    print("\nFinal General Hypotheses G:")
    for g in G_final:
        print(g)
