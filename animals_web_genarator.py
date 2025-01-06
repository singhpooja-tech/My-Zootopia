import json


def load_data(file_path):
    """Loads a JSON file."""
    try:
        with open(file_path, "r") as handle:
            return json.load(handle)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from the file '{file_path}'.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred while loading the file: {e}")
        return []


def serialize_animal(animal_obj):
    """Serializes a single animal object into an HTML list item."""
    output = ''
    try:
        output += '<li class="cards__item">\n'

        # Add the Name field in a div with class "card__title"
        if 'name' in animal_obj:
            output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'

        # Add the Diet, Location, and Type fields inside a paragraph with class "card__text"
        output += '  <p class="card__text">\n'

        # Add the Diet field (inside 'characteristics')
        if 'characteristics' in animal_obj and 'diet' in animal_obj['characteristics']:
            output += f'      <strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n'

        # Add the Location field (first element in 'locations')
        if 'locations' in animal_obj and animal_obj['locations']:
            output += f'      <strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n'

        # Add the Type field (inside 'characteristics')
        if 'characteristics' in animal_obj and 'type' in animal_obj['characteristics']:
            output += f'      <strong>Type:</strong> {animal_obj["characteristics"]["type"]}<br/>\n'

        # Close the paragraph and list item
        output += '  </p>\n'
        output += '</li>\n'

        return output
    except KeyError as e:
        print(f"Error: Missing expected key {e} in animal data.")
        return ''
    except Exception as e:
        print(f"An unexpected error occurred while serializing the animal: {e}")
        return ''


def generate_animal_info(animals_data):
    """Generates a string with all animals' information formatted as HTML."""
    output = ""  # Initialize an empty string to accumulate the animal information

    for animal in animals_data:
        # Use the serialize_animal function for each animal
        animal_info = serialize_animal(animal)
        if animal_info:  # Only append if there's valid data
            output += animal_info

    return output


def load_template(template_path):
    """Loads the HTML template."""
    try:
        with open(template_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The template file '{template_path}' was not found.")
        return ''
    except Exception as e:
        print(f"An unexpected error occurred while loading the template: {e}")
        return ''


def write_html(output_data, output_file_path):
    """Writes the generated HTML content to a new file."""
    try:
        with open(output_file_path, "w") as file:
            file.write(output_data)
    except Exception as e:
        print(f"An unexpected error occurred while writing to the file: {e}")


def main():
    try:
        # Step 1: Load data from the JSON file
        animals_data = load_data('animals_data.json')

        if not animals_data:
            print("Error: No data found in the JSON file. Exiting.")
            return

        # Step 2: Generate a string with animal information formatted as HTML
        animal_info = generate_animal_info(animals_data)

        if not animal_info:
            print("Error: No animal information to generate.")
            return

        # Step 3: Load the HTML template
        html_template = load_template('animals_template.html')

        if not html_template:
            print("Error: The template could not be loaded. Exiting.")
            return

        # Step 4: Replace the placeholder with the generated animal information
        new_html_content = html_template.replace('__REPLACE_ANIMALS_INFO__', animal_info)

        # Step 5: Write the final HTML content to a new file
        write_html(new_html_content, 'animals.html')

        print("HTML file 'animals.html' has been generated successfully.")

    except Exception as e:
        print(f"An unexpected error occurred during the execution: {e}")


# Run the main function
if __name__ == "__main__":
    main()
