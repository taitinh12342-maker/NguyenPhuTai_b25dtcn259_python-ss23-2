import math

def calculate_disk_blocks(size_bytes):
    return math.ceil(size_bytes / 4096)