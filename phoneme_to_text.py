from phonetic_name_generator import generate_names

def load_phoneme_to_char(filename):
    with open(filename, 'r') as file:
        return {line.split(' = ')[0]: line.split(' = ')[1] for line in map(str.strip, file) if line}

def phonetic_to_english(phonemes, phoneme_to_char, debug=False):
    name_parts = [phoneme_to_char.get(syllable, syllable) for syllable in phonemes.split()]
    if debug:
        for syllable in phonemes.split():
            if syllable not in phoneme_to_char:
                print(f"Unspecified syllable: {syllable}")
    return ''.join(name_parts).capitalize()

def translate_generated_names(input_file, phoneme_file, num_names=5, debug=False):
    phoneme_to_char = load_phoneme_to_char(phoneme_file)
    random_names = generate_names(input_file, num_names, 1, 1)
    
    return [
        phonetic_to_english(name, phoneme_to_char, debug) if not debug else (
            print(f"Debug: Original: {name} -> Translated: {phonetic_to_english(name, phoneme_to_char, debug)}"),
            phonetic_to_english(name, phoneme_to_char, debug)
        )[1]
        for name in random_names
    ]

# Example usage:
if __name__ == "__main__":
    phoneme_repository = './db/syllables_english.json' # Replace with your actual JSON file containing syllables
    phoneme_dictionary_file = './dict/phonemes_english.dict' # Replace with your actual file containing your phonetic dictionary
    num_names_to_generate = 10 # Specify how many names to generate
    debug = False # Set to True to enable detailed debug output

    english_names = translate_generated_names(phoneme_repository, phoneme_dictionary_file, num_names_to_generate, debug)
    
    if not debug:
        print(f"Here are {num_names_to_generate} randomly generated names (phonetic to English conversion):")
        print('\n'.join(english_names))
