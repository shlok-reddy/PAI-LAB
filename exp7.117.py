states = ['Rainy', 'Sunny']
observations = ['walk', 'shop', 'clean']

start_prob = {
    'Rainy': 0.6,
    'Sunny': 0.4
}

transition_prob = {
    'Rainy': {'Rainy': 0.7, 'Sunny': 0.3},
    'Sunny': {'Rainy': 0.4, 'Sunny': 0.6}
}

emission_prob = {
    'Rainy': {'walk': 0.1, 'shop': 0.4, 'clean': 0.5},
    'Sunny': {'walk': 0.6, 'shop': 0.3, 'clean': 0.1}
}

obs_sequence = ['walk', 'shop', 'clean']

def forward_algorithm(states, observations, start_prob, transition_prob, emission_prob):
    forward = []
    f0 = {}
    for state in states:
        f0[state] = start_prob[state] * emission_prob[state][observations[0]]
    forward.append(f0)

    for i in range(1, len(observations)):
        ft = {}
        for current_state in states:
            prob = 0
            for previous_state in states:
                prob += forward[i-1][previous_state] * transition_prob[previous_state][current_state]
            ft[current_state] = prob * emission_prob[current_state][observations[i]]
        forward.append(ft)

    final_prob = sum(forward[-1][state] for state in states)
    return forward, final_prob

forward_probs, total_probability = forward_algorithm(
    states, obs_sequence, start_prob, transition_prob, emission_prob
)

print(forward_probs)
print(total_probability)
