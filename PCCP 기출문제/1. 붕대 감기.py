def solution(bandage, health, attacks):
    band_time, hp_gen, hp_bonus = bandage
    time = 0
    max_health = health
    for attack_time, damage in attacks:
        health -= hp_gen
        health = min(max_health, health + (attack_time - time) * hp_gen + ((attack_time - time - 1) // band_time) * hp_bonus)
        health -= damage
        if health <= 0:
            return -1
        time = attack_time
    return health
