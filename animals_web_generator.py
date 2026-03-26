import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def get_animals_data():
    animals_data = load_data('animals_data.json')
    return animals_data


def generate_animals_data(animals_data):
    output = ""
    for animal in animals_data:
        output += "<li class='cards__item'>"
        if "name" in animal:
            output += f"Name: {animal['name']}<br/>\n"

        # Check if characteristics exists, then check if diet and type exist
        if "characteristics" in animal:
            characteristic = animal['characteristics']

            if "diet" in characteristic:
                output += f"Diet: {characteristic['diet']}<br/>\n"

            if "type" in characteristic:
                output += f"Type: {characteristic['type']}<br/>\n"

        # Check if location exists and not empty
        if "locations" in animal and len(animal['locations']) > 0:
            output += f"Location: {animal['locations'][0]}<br/>\n"

        output += "</li>"

    return output

animals_info = generate_animals_data(get_animals_data())

with open("animals_template.html", "r") as file:
    current_html = file.read()

new_html = current_html.replace("__REPLACE_ANIMALS_INFO__", animals_info)

with open("animals.html", "w") as file:
    file.write(new_html)