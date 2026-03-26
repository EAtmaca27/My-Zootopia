import json

from sympy import dirichlet_eta
from torch.serialization import location_tag


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def get_animals_data():
    animals_data = load_data('animals_data.json')
    return animals_data


def generate_animals_data(animals_data):
    output = ""
    diet = ""
    type_ = ""
    location = ""

    for animal in animals_data:
        output += "<li class='cards__item'>"
        if "name" in animal:
            output += f"<div class='card__title'>{animal['name']}</div>"

        output += '<p class="card__text">'

        # Check if characteristics exists, then check if diet and type exist
        if "characteristics" in animal:
            characteristic = animal['characteristics']

            if "diet" in characteristic:
                diet = f"<strong>Diet:</strong> {characteristic['diet']}<br/>\n"

            if "type" in characteristic:
                type_ = f"<strong>Type:</strong> {characteristic['type']}<br/>\n"

        # Check if location exists and not empty
        if "locations" in animal and len(animal['locations']) > 0:
            location = f"<strong>Location:</strong> {animal['locations'][0]}<br/>\n"

        output += diet
        output += location
        output += type_
        output += "</p>"
        output += "</li>"

    return output

animals_info = generate_animals_data(get_animals_data())

with open("animals_template.html", "r") as file:
    current_html = file.read()

new_html = current_html.replace("__REPLACE_ANIMALS_INFO__", animals_info)

with open("animals.html", "w") as file:
    file.write(new_html)