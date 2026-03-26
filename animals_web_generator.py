import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def get_animals_data():
    animals_data = load_data('animals_data.json')
    return animals_data


def print_animals_data(animals_data):
    """
    Takes a list of animal dictionaries and prints
    details about each animal, such as their name, diet, type
    and the first location if information is provided.

    :param animals_data: A list of dictionaries, each representing
    an animal and its associated data.
    :return: None
    """
    for animal in animals_data:
        if "name" in animal:
            print(f"Name: {animal['name']}")

        # Check if characteristics exists, then check if diet and type exist
        if "characteristics" in animal:
            characteristic = animal['characteristics']

            if "diet" in characteristic:
                print(f"Diet: {characteristic['diet']}")

            if "type" in characteristic:
                print(f"Type: {characteristic['type']}")

        # Check if location exists and not empty
        if "locations" in animal and len(animal['locations']) > 0:
            print(f"Location: {animal['locations'][0]}")

        print()
