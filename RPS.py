def player(prev_play, opponent_history=[]):
    from collections import defaultdict, Counter

    if prev_play:
        opponent_history.append(prev_play)

    guess = "R"

    if len(opponent_history) < 4:
        return guess

    n = 4
    model = defaultdict(list)

    for i in range(len(opponent_history) - n):
        key = "".join(opponent_history[i:i+n])
        next_move = opponent_history[i+n]
        model[key].append(next_move)

    last_pattern = "".join(opponent_history[-n:])
    if last_pattern in model:
        prediction = Counter(model[last_pattern]).most_common(1)[0][0]
        guess = {"R": "P", "P": "S", "S": "R"}[prediction]

    return guess
