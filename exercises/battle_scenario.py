def label_scenarios(scenarios):
    labels = []

    for scenario in scenarios:
        player_hp, enemy_hp, has_potion, has_shield = scenario

        if player_hp <= 0:
            label = "defeated"
        elif enemy_hp <= 0:
            label = "victory"
        elif player_hp <= 20 and has_shield:
            label = "last stand"
        elif player_hp <= 20 and has_potion:
            label = "comeback"
        elif player_hp > enemy_hp:
            label = "advantage"
        elif player_hp == enemy_hp:
            label = "even fight"
        else:
            label = "retreat"

        labels.append(label)

    return labels

scenarios = [
    (15, 40, False, True),
    (10, 40, True, False),
    (25, 25, False, False),
]

result = label_scenarios(scenarios)
print(result)