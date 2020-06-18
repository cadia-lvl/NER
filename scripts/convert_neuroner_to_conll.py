def convert_file(input, output):
    with open(input) as f:
        lines = f.readlines()
    with open(output, 'w') as f:
        for line in lines:
            parts = line.split()
            if len(parts) > 1:
                write_str = '{}\t{}\n'.format(parts[0], parts[len(parts)-1])
            else:
                write_str = '\n'
            f.write(write_str)

batches = ['200K', '400K', '600K', '800K', '1000K']

for batch in batches:
    convert_file('{}-test.txt'.format(batch), 'correct_{}.tsv'.format(batch))


