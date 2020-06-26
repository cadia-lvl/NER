import sys


def adjust_string_for_XML(stri):
    # if '&' in stri:
    #     stri = stri.replace('&', '&amp;')
    # if '<' in stri:
    #     stri = stri.replace('<', '&lt;')
    # if '>' in stri:
    #     stri = stri.replace('>', '&gt;')
    #
    # if '"' in stri:
    #     stri = stri.replace('"', '&quot;')
    # if "'" in stri:
    #     stri = stri.replace("'", "&apos;")

    return stri

NO_arguments = len(sys.argv) - 1


# print(NO_arguments)

if NO_arguments <= 0:
    exit()

input_file = sys.argv[1]

with open(input_file, 'r') as f:
    tokens = f.readlines()

print('<?xml version="1.0" encoding="UTF-8"?>')
print('<NAF xml:lang="en" version="v3">')
print('\t<text>')
sent_nr = 1
word_nr = 1
next_offset = 0
for line in tokens:
    parts = line.split('\t')
    word = adjust_string_for_XML(parts[0])
    if len(parts) != 2:
        sent_nr += 1
    else:
        print('\t\t<wf id="w{0}" sent="{1}" offset="{2}" length="{3}">{4}</wf>'.format(word_nr, sent_nr, next_offset, len(parts[0]), word))
        word_nr += 1
        next_offset += len(parts[0]) + 1

# print('\t\t<wf id="w1" sent="1" offset="0" length="4">Hvað</wf>')
# print('\t\t<wf id="w2" sent="1" offset="5" length="2">er</wf>')
# print('\t\t<wf id="w3" sent="1" offset="8" length="1">í</wf> ')
# print('\t\t<wf id="w4" sent="1" offset="10" length="5">gangi</wf>')
# print('\t\t<wf id="w5" sent="1" offset="16" length="5">hérna</wf>')
# print('\t\t<wf id="w6" sent="1" offset="22" length="1">í</wf>')
# print('\t\t<wf id="w7" sent="1" offset="24" length="9">Reykjavík</wf>')
# print('\t\t<wf id="w8" sent="1" offset="34" length="1">?</wf>')
print('\t</text>')
term_nr = 1
print('\t<terms>')
for line in tokens:
    parts = line.split('\t')
    if len(parts) != 2:
        continue
    else:

        print('\t\t<term id="t{}">'.format(term_nr))
        print('\t\t\t<span>')
        print('\t\t\t\t<target id="w{}"/>'.format(term_nr))
        print('\t\t\t</span>')
        print('\t\t</term>')
        term_nr += 1

# print('\t\t<term id="t2">')
# print('\t\t\t<span>')
# print('\t\t\t\t<target id="w2"/>')
# print('\t\t\t</span>')
# print('\t\t</term>')
#
# print('\t\t<term id="t3">')
# print('\t\t\t<span>')
# print('\t\t\t\t<target id="w3"/>')
# print('\t\t\t</span>')
# print('\t\t</term>')
#
# print('\t\t<term id="t4">')
# print('\t\t\t<span>')
# print('\t\t\t\t<target id="w4" />')
# print('\t\t\t</span>')
# print('\t\t</term>')
#
# print('\t\t<term id="t5">')
# print('\t\t\t<span>')
# print('\t\t\t\t<target id="w5" />')
# print('\t\t\t</span>')
# print('\t\t</term>')
#
# print('\t\t<term id="t6">')
# print('\t\t\t<span>')
# print('\t\t\t\t<target id="w6" />')
# print('\t\t\t</span>')
# print('\t\t</term>')
#
# print('\t\t<term id="t7">')
# print('\t\t\t<span>')
# print('\t\t\t\t<target id="w7" />')
# print('\t\t\t</span>')
# print('\t\t</term>')
#
# print('\t\t<term id="t8">')
# print('\t\t\t<span>')
# print('\t\t\t\t<target id="w8" />')
# print('\t\t\t</span>')
# print('\t\t</term>')



print('\t</terms>')

print('</NAF>')

