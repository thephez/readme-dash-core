#!/usr/bin/python3
import sys
import json

def glossary_to_markdown(filename, glossary_input):
    with open(filename, 'w') as f:
        # Sort terms alphabetically (ignoring case)
        for term in sorted(glossary_input, key=lambda v: v.upper()):
            #print('# {}\n\n{}\n\n'.format(term, glossary_input[term]))
            f.write('# {}\n\n{}\n\n'.format(term, glossary_input[term]))


def main(argv):
    file = argv[0]
    with open(file) as f:
        lines = [line.rstrip('\n') for line in f]

    glossary = {}
    for x in range(0, len(lines)):
        # Term and definition are on alternating lines
        if (x % 2) == 0:
            # TODO: Check for duplicate definition
            glossary[lines[x]] = lines[x+1]

    glossary_to_markdown('{}.md'.format(file), glossary)
    print('Glossary written to `{}.md`'.format(file))


if __name__ == "__main__":
    # Run like: `glossary-to-markdown.py <input-file>`
   main(sys.argv[1:])
