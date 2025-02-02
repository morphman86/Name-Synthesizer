# Name Synth | Phonetic Name Generation and Translation

This project demonstrates a set of Python scripts designed to process, generate, and translate names based on their phonetic components. It includes the following functionalities:

- **Syllable Parsing**: Splits names into phonetic syllables.
- **Random Name Generation**: Generates random names using syllables from an existing dataset.
- **Phonetic to English Translation**: Converts phonetic representations of names back to readable English.

## Project Structure

`name_synth/`
├── `db/`
│   ├── `syllables.json`          # JSON file containing syllable data from names
│   └── `names.txt`               # Text file containing a list of names to process
├── `dict/`
│   └── `phonemes_english.txt`    # Dictionary mapping phonemes to English characters
└── `__init__.py`                 # For if you want to turn this into a package
├── `syllable_parser.py`          # Script to parse names into phonetic syllables
├── `phoneme_to_text.py`          # Script to convert phonemes into readable English
├── `phonetic_name_generator.py`  # Script to generate random names from syllables
├── `.gitignore`                  # Git ignore file
└── `README.md`                   # Project README file
└── `LICENSE.md`                  # License agreement

## Usage

Each script has an example usage that demonstrate how to process and generate names, as well as translate them from phonetic to English.
You can run each script on their own, as-is.

The order to run the scripts:

- syllable_parser.py
** This turns a list of names into its phonetic syllables and store in an output json file
- phoneme_to_text.py
**This assembles new names based on the syllables in the input JSON file (the output JSON file from the previous step)
** The phonetic syllables are then translated to readable text.
** This file only translates the phonemes to text, it uses phonetic_name_generator.generate_names for the name generation

To make your own random name generator:

- Create a list of names in a plain text file, one name per line
- Run syllable_parser.generate_json(input_file, output_file, debug)
** Alternatively change the settings in the example usage section of syllable_parser.py and run the file directly
- Now you can use phonetic_name_generator.generate_names(input_file, num_names, min_middle_syllables, max_middle_syllables)
** This will generate num_names number of names represented phonetically using the ARPAbet denotation
- Run phoneme_to_text.phonetic_to_english(name, phoneme_to_char, debug) on each name generated to give them their plain text names
**Alternatively, you can skip phonetic_name_generator completely and run translate_generated_names(phoneme_repository, phoneme_dictionary_file, num_names_to_generate, debug)
** This method will generate num_names_to_generate names and translate them to text for you
- Whichever method you use, you should now see any phonetic syllables not yet "translated" in the terminal output
** Either create a new dictionary, or update `dict/phonemes_english.dict` with the missing phonemes.
*** You can search your input JSON file (default: `db/syllables_english.json`) for any phonetic syllables you are unsure of the spelling for
- Congratulations, you now have a program that can create new names using the same grammatical structure as your input names.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.

## Author

Chris Karlsson
Email: <ckskola@gmail.com>
