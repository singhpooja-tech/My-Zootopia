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


def main():
    animals_data = load_data('animals_data.json')


# Run the main function
if __name__ == "__main__":
    main()