from system_entropy import get_hardware_seed
import hashlib
from datetime import datetime

def generate(base, seed, beg, end, count):
    base = base.encode() if isinstance(base, str) else base
    seed = seed.encode() if isinstance(seed, str) else seed

    hw_seed = str(get_hardware_seed()).encode()
    rand = hashlib.sha3_512(base + hashlib.sha3_512(seed + hw_seed).digest()).hexdigest()

    rounds = 3
    while rounds != 0:
        hw_seed = str(get_hardware_seed()).encode()
        rand += hashlib.sha3_512(base + hashlib.sha3_512(seed + hw_seed).digest()).hexdigest()
        rounds -= 1
    rand = int(rand, 16)
    bit_len = (rand % (2048 - 128 + 1)) + 128
    rand = rand & ((1 << bit_len) - 1)
    rand = rand % (end - beg + 1) + beg
    from datetime import datetime

    current_time = datetime.now().strftime("%H:%M:%S")

    print(f"\n!!! Random number #{count}(session) has been generated ({current_time})!!!\n")    
    return rand