# https://stackoverflow.com/questions/2673385/how-to-generate-a-random-number-with-a-specific-amount-of-digits
import random

def n_len_rand(len_, floor=1):
    top = 10**len_
    if floor > top:
        raise ValueError(f"Floor '{floor}' must be less than requested top '{top}'")
    return f'{random.randrange(floor, top):0{len_}}'