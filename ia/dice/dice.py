
# États du jeu
states = range(7)
nonterminal_states = states[1:]

# Modèle du jeu
model = {}

for s in nonterminal_states:
    model[s] = [
        {
            'name': 'terminate',
            'reward': s,
            'target': [[1., 0]]   
        },
        {
            'name': 'rethrow',
            'reward': -1,
            'target': [[1/6., t] for t in range(1,7)]   
        },
    ]

# Algorithme de Value Iteration
values = {s: 0 for s in states}

changed = True
while changed:
    changed = False
    for s in nonterminal_states:
        possible_values = []
        for a in model[s]:
            value = a['reward']
            for p, s_target in a['target']:
                value = value + p * values[s_target]
            possible_values.append(value)
        new_value = max(possible_values)
        if new_value != values[s]:
            changed = True
            values[s] = new_value

# Affichage des meilleures actions possibles dans chaque état        
for s in nonterminal_states:
    print('== State %d, v=%f' % (s, values[s]))
    for a in model[s]:
        returns = a['reward']
        for p, s_target in a['target']:
            returns = returns + p * values[s_target]
        if returns == values[s]:
            print('- optimal action: %s' % a['name'])

