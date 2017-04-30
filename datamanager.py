import csv


def write_to_database(list_name, filename="database.csv"):
    """
        Saving the data to the specified file named: database.csv
        Writes the data by row by row.
    """
    with open(filename, "w") as database:
        for item in list_name:
            story = [story_lines.strip("\n") for story_lines in item]
            row = ";".join(story)
            database.write(row + "\n")


def open_from_database(filename="database.csv"):
    """
        Opens all the rows from the database.csv
    """
    try:
        with open(filename, "r") as database:
            row = database.readlines()
            elements = [item.split(";") for item in row]
            return elements
    except FileNotFoundError:
        elements = None


def generate_id(stories):
    """
        Generates an ID after each user entry
    """
    new_id = [int(id[0]) for id in stories]
    if not new_id:
        return str(1)
    return str(len(new_id) + 1)
