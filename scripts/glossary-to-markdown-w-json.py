#!/usr/bin/python3
import sys
import json
#print(str(sys.argv))


def write_json_to_file(filename, data):
    print('Writing to: {}'.format(filename))
    with open(filename, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=1)
        #md_file.write(data)
    return


def glossary_to_markdown(filename, glossary_input):
    with open(filename, 'w') as f:
        # Sort terms alphabetically (ignoring case)
        for term in sorted(glossary_input, key=lambda v: v.upper()):
            #print('# {}\n\n{}\n\n'.format(term, glossary_input[term]))
            f.write('# {}\n\n{}\n\n'.format(term, glossary_input[term]))

    return

def main(argv):
    file = argv[0]
    with open(file) as f:
        lines = [line.rstrip('\n') for line in f]

    glossary = {}
    #[print(line) for line in lines]
    for x in range(0, len(lines)):
        if (x % 2) == 0:
            # TODO: Check for duplicate definition
            glossary[lines[x]] = lines[x+1]

    #print(glossary)
    glossary_to_markdown('{}.md'.format(file), glossary)
    write_json_to_file('{}.json'.format(file), glossary)


if __name__ == "__main__":
   main(sys.argv[1:])
