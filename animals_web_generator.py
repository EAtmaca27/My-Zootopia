import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def get_animals_data():
    """ Loads the animals data from animals_data.json """
    animals_data = load_data('animals_data.json')
    return animals_data


def generate_animals_data(animals_data):
    """
    Generates our main content.
    Uses the serialize_animal function to seperate the
    styling of our content.

    :param animals_data:
    :return: output
    """
    output = ""
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)
    return output


def load_animal_template_html():
    """ Loads the animals_template.html file """
    with open("animals_template.html", "r") as file:
        current_html = file.read()


def replace_content(current_html, animals_info):
    """
    Replaces the content of the animals_template.html file with the animals_info
    to create our animals.html file.

    :param current_html:
    :param animals_info:
    :return:
    """
    animals_info = generate_animals_data(get_animals_data())

    new_html = current_html.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    with open("animals.html", "w") as file:
        file.write(new_html)


def serialize_animal(animal_obj):
    """
    Seperates and formats the animal data into HTML.
    Styling is seperated from generate_animals_data function.

    :param animal_obj:
    :return: output
    """
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
    """
    Gets the skin types from animals_data.

    :param animals_data:
    :return: skin_types
    """
    skin_types = []
    for animal in animals_data:
        skin_type = animal.get("characteristics", {}).get("skin_type")
        if skin_type in skin_types:
            continue
        else:
            skin_types.append(skin_type)
    return skin_types


def print_skin_types(skin_types):
    """
    Prints the skin types to the console.

    :param skin_types:
    :return:
    """
    for skin_type in skin_types:
        print(skin_type)


def choose_and_display_animals_skin_type():
    """
    Uses the user's input to choose a skin type.
    Generates a list of animals with the chosen skin type.

    :return: animals_with_certain_skin_type
    """
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
    """
    Main function
    Generates an animals.html file with only the animals of a certain skin type,
    based on the user's input.
    Uses the animals_template.html file as a template.

    :return:
    """
    animals_data = choose_and_display_animals_skin_type()
    animals_html = generate_animals_data(animals_data)


    with open("animals_template.html", "r") as file:
        template = file.read()

    final_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    with open("animals.html", "w") as file:
        file.write(final_html)


if __name__ == "__main__":
    main()