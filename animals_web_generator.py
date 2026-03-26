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
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)
    return output


def load_animal_template_html():
    with open("animals_template.html", "r") as file:
        current_html = file.read()


def replace_content(current_html, animals_info):
    animals_info = generate_animals_data(get_animals_data())

    new_html = current_html.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    with open("animals.html", "w") as file:
        file.write(new_html)


def serialize_animal(animal_obj):
    output = ''
    output += '<li class="cards__item">\n'
    name = animal_obj.get("name", "Unknown Animal")
    output += f'<div class="card__title">{name}</div>\n'

    characteristics = animal_obj.get("characteristics", {})

    diet = characteristics.get("diet")

    output += "<div class = 'card__text'>"
    output += '<ul>\n'

    if diet:
        output += f'<li><strong>Diet:</strong> {diet}</li></br>\n'

    locations = animal_obj.get("locations", [])
    if locations:
        output += f'<li><strong>Location:</strong> {locations[0]}</li></br>\n'

    type_ = characteristics.get("type")
    if type_:
        output += f'<li><strong>Type:</strong> {type_}</li></br>\n'

    output += '</ul>\n'
    output += '</div>\n'
    output += '</li>'

    return output


def get_skin_type(animals_data):
    skin_types = []
    for animal in animals_data:
        skin_type = animal.get("characteristics", {}).get("skin_type")
        if skin_type in skin_types:
            continue
        else:
            skin_types.append(skin_type)
    return skin_types


def print_skin_types(skin_types):
    for skin_type in skin_types:
        print(skin_type)


def choose_and_display_animals_skin_type():
    animals_data = get_animals_data()
    skin_types = get_skin_type(animals_data)
    print_skin_types(skin_types)
    skin_type = input("Choose a skin type: ")
    animals_with_certain_skin_type = []
    for animal in animals_data:
        if animal.get("characteristics", {}).get("skin_type") == skin_type:
            animals_with_certain_skin_type.append(animal)
        else:
            continue
    return animals_with_certain_skin_type


def main():
    animals_data = choose_and_display_animals_skin_type()
    animals_html = generate_animals_data(animals_data)


    with open("animals_template.html", "r") as file:
        template = file.read()

    final_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    with open("animals.html", "w") as file:
        file.write(final_html)


if __name__ == "__main__":
    main()