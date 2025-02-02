import json
import random
from collections import defaultdict

def read_syllables_from_json(input_file):
    syllable_groups = defaultdict(list)

    with open(input_file, 'r') as json_file:
        data = json.load(json_file)

        for entry in data:
            syllables = entry["syllables"]
            
            if len(syllables) == 1:
                syllable_groups["first"].append(syllables[0])
                syllable_groups["last"].append(syllables[0])
            else:
                syllable_groups["first"].append(syllables[0])
                syllable_groups["last"].append(syllables[-1])
                if len(syllables) > 2:
                    syllable_groups["middle"].extend(syllables[1:-1])

    return syllable_groups

def generate_random_names(syllable_groups, min_middle_syllables, max_middle_syllables, num_names=5):
    generated_names = []

    for _ in range(num_names):
        first = random.choice(syllable_groups["first"])
        last = random.choice(syllable_groups["last"])
        
        # Randomly choose a number of middle syllables between the min and max
        num_middle = random.randint(min_middle_syllables, max_middle_syllables)

        middle = []
        if num_middle > 0 and syllable_groups["middle"]:
            middle_choice = random.sample(syllable_groups["middle"], min(num_middle, len(syllable_groups["middle"])))
            middle.extend(middle_choice)

        new_name = ' '.join([first] + middle + [last])
        generated_names.append(new_name)

    return generated_names

def generate_names(input_file, num_names=5, min_middle_syllables=0, max_middle_syllables=3):
    syllable_groups = read_syllables_from_json(input_file)
    return generate_random_names(syllable_groups, min_middle_syllables, max_middle_syllables, num_names)

# Example usage:
if __name__ == "__main__":
    phoneme_repository = './db/syllables_english.json'  # Replace with your actual JSON file containing syllables
    num_names_to_generate = 10  # Specify how many names to generate
    min_syllables = 1  # Minimum number of middle syllables
    max_syllables = 3  # Maximum number of middle syllables

    random_names = generate_names(phoneme_repository, num_names_to_generate, min_middle_syllables=min_syllables, max_middle_syllables=max_syllables)
    
    print(f"Here are {num_names_to_generate} randomly generated names:")
    for name in random_names:
        print(name)
