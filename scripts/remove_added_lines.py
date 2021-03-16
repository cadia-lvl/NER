import sys


def load_tsv_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    return lines

gold_file = sys.argv[1]
guess_file = sys.argv[2]

gold_lines = load_tsv_file(gold_file)
guess_lines = load_tsv_file(guess_file)


i = 0



for guess_line in guess_lines:
    gold_line = gold_lines[i]
    gold_parts = gold_line.split('\t')
    guess_parts = guess_line.split('\t')

    if len(gold_parts) != len(guess_parts):
        del guess_lines[i]
    i += 1


with open(guess_file, 'w') as f:
    for line in guess_lines:
        f.write(line)


