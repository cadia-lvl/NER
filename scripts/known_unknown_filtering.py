
import sys, os


def get_full_entity(token_tag_pairs, current_index):
    all_tokens = []
    current_pair = token_tag_pairs[current_index]
    parts = current_pair.split('\t')
    all_tokens.append(parts[0])
    next_pair_parts = token_tag_pairs[current_index+1].split('\t')
    if len(next_pair_parts) == 2:
        while next_pair_parts[1][:1] == 'I':
            all_tokens.append(next_pair_parts[0])
            current_index += 1
            next_pair_parts = token_tag_pairs[current_index + 1].split('\t')
            if len(next_pair_parts) != 2:
                break
    return ' '.join(all_tokens), len(all_tokens)


def load_tsv_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    return lines




def get_all_named_entities(lines):
    named_entities = []
    for i in range(len(lines)):
        line = lines[i]
        if len(line.split('\t')) != 2:
            continue

        parts = line.split('\t')
        if parts[1] == 'O':
            continue
        elif parts[1][:2] == 'B-':
            entity, _ = get_full_entity(lines, i)
            named_entities.append(entity)
    return named_entities


def find_known_and_unknown_indices(lines):
    unknown_indices = []
    known_indices = []
    for i in range(len(lines)):
        line = lines[i]
        if len(line.split('\t')) != 2:
            continue

        parts = line.split('\t')
        if parts[1] == 'O':
            continue
        elif parts[1][:2] == 'B-':
            entity, length = get_full_entity(lines, i)
            if is_known_entity(entity):
                for j in range(i, i + length):
                    known_indices.append(j)
            else:
                for j in range(i, i + length):
                    unknown_indices.append(j)
    known_indices.sort(reverse=True)
    unknown_indices.sort(reverse=True)
    return known_indices, unknown_indices


def is_known_entity(entity):
    return entity in unique_known_entities


corpus_folder = sys.argv[1]


train_path = '{}/train/train'.format(corpus_folder)

train_lines = load_tsv_file(train_path)

train_entities = get_all_named_entities(train_lines)

train_entities.sort()
unique_trained_entities = set(train_entities)

if len(sys.argv) > 5:
    valid_path = '{}/valid/valid'.format(corpus_folder)

    valid_lines = load_tsv_file(valid_path)

    valid_entities = get_all_named_entities(valid_lines)

    valid_entities.sort()
    unique_valid_entities = set(train_entities)
    # unique_valid_entities.sort()

    all_known_entities = train_entities + valid_entities
    all_known_entities.sort()
    unique_known_entities = set(all_known_entities)
    # all_known_entities.sort()

else:
    unique_known_entities = unique_trained_entities


gold_file = sys.argv[2]
guess_file = sys.argv[3]
guess_file_name = guess_file.split('/')[len(guess_file.split('/'))-1]

output_folder = sys.argv[4]

gold_lines = load_tsv_file(gold_file)
guess_lines = load_tsv_file(guess_file)

known_indices, unknown_indices = find_known_and_unknown_indices(gold_lines)

known_only_gold = gold_lines.copy()
known_only_guess = guess_lines.copy()
for i in unknown_indices:
    del known_only_gold[i]
    del known_only_guess[i]


with open('known_gold', 'w') as f:
    for line in known_only_gold:
        f.write(line)

guess_file.split('/')

os.system('mkdir {}/unknown_only'.format(output_folder))
os.system('mkdir {}/known_only'.format(output_folder))
known_only_output_file = '{}//known_only/{}'.format(output_folder, guess_file_name)
unknown_only_output_file = '{}//unknown_only/{}'.format(output_folder, guess_file_name)

with open(known_only_output_file, 'w') as f:
    for line in known_only_guess:
        f.write(line)

unknown_only_gold = gold_lines.copy()
unknown_only_guess = guess_lines.copy()

for i in known_indices:
    del unknown_only_gold[i]
    del unknown_only_guess[i]

with open('unknown_gold', 'w') as f:
    for line in unknown_only_gold:
        f.write(line)

with open(unknown_only_output_file, 'w') as f:
    for line in unknown_only_guess:
        f.write(line)

# unique_trained_entities.sort()


# known_entities = train_entities + valid_entities
# known_entities.sort()
# unique_known_entities = set(known_entities)
#
# test_path = '{}/test/test'.format(corpus_folder)
# test_lines = load_tsv_file(test_path)
# test_entities = get_all_named_entities(test_lines)
# test_entities.sort()
# unique_test_entities = set(test_entities)
#
# unknown_entities_count = 0
# known_entities_count = 0
#
# for ent in unique_test_entities:
#     if ent in unique_known_entities:
#         known_entities_count += 1
#     else:
#         unknown_entities_count += 1
#
#
# print(len(unique_test_entities))
# print(known_entities_count)
# print(unknown_entities_count)