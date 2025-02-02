import json
import pronouncing

def group_syllables(pronunciation):
    syllables, current_syllable = [], ""
    for phone in pronunciation.split():
        if phone[-1] in '012':  # Stress markers (0, 1, 2)
            if current_syllable: syllables.append(current_syllable)
            current_syllable = phone
        else:
            current_syllable += phone
    if current_syllable: syllables.append(current_syllable)
    return syllables

def get_phonetic_syllables(name, debug):
    pronunciation_list = pronouncing.phones_for_word(name)
    if debug: print(f"Pronunciation list for {name}: {pronunciation_list}")
    return group_syllables(pronunciation_list[0]) if pronunciation_list else None

def generate_json(input_file, output_file, debug=False):
    with open(input_file, 'r') as file:
        result = [
            {"full_name": name.strip(), "syllables": get_phonetic_syllables(name.strip(), debug)}
            for name in file if get_phonetic_syllables(name.strip(), debug)
        ]
        skipped_names = [name.strip() for name in file if not get_phonetic_syllables(name.strip(), debug)]

    with open(output_file, 'w') as json_file:
        json.dump(result, json_file, indent=4)

    if skipped_names: print("Names that could not be processed:\n" + '\n'.join(skipped_names))

# example usage
if __name__ == "__main__":
    input_file = './db/names.txt'  # Replace with your text file with names
    output_file = './db/syllables_english.json'  # Output file to use to store phonetic syllables, created if it doesn't exist, can use path
    debug = False  # Set to True to enable detailed debug output

    generate_json(input_file, output_file, debug)
