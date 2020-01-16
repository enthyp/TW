import os


def read_input(path):
    with open(path, 'r') as input_file:
        lines = input_file.readlines()
    
    alphabet = lines[0].strip()
    word = lines[-1].strip()
    pairs = [tuple(line.split()) for line in lines[1:-1]]
    
    return alphabet, pairs, word
