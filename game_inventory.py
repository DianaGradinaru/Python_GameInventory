# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the requirements.

import csv


def display_inventory(inventory):
    """Display the contents of the inventory in a simple way."""
    for key in inventory:
        print(f"{key}: {inventory[key]}")


def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items."""
    for item in added_items:
        if inventory[item] != None:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


def remove_from_inventory(inventory, removed_items):
    """Remove from the inventory dictionary a list of items from removed_items."""
    for item in removed_items:
        if inventory[item] == 1:
            del inventory[item]
        else:
            inventory[item] -= 1
    return inventory


def print_table(inventory, order):
    """
    Display the contents of the inventory in an ordered, well-organized table with
    each column right-aligned.
    """
    header = "item name | count"
    headers = header.split("|")
    output = []

    direction = True if order == "desc" else False
    sorted_inventory = sorted(
        inventory.items(), key=lambda tupl: tupl[1], reverse=direction
    )

    left_text = 0
    right_text = 0
    for item in sorted_inventory:
        left_text = max([len(headers[0]), len(str(item[0])) + 1, left_text])
        right_text = max([len(headers[1]), len(str(item[1])) + 1, right_text])

    output.append(header)
    output.append("-" * (1 + left_text + right_text))

    for item in sorted_inventory:
        # left_text count of spaces
        lft = (" " * left_text) + str(item[0]) + " "
        # left_text characters from the end
        lft = lft[-left_text:]

        rgt = (" " * right_text) + str(item[1])
        rgt = rgt[-right_text:]

        output.append(lft + "|" + rgt)

    print("\n".join(output))


def import_inventory(inventory, filename="import_inventory.csv"):
    try:
        with open(filename) as f:
            for row in csv.reader(f):
                for item in row:
                    try:
                        inventory[item] += 1
                    except KeyError:
                        inventory[item] = 1
        display_inventory(inventory)
            
    except FileNotFoundError:
        print(f"File '{filename}' not found!")
        


def export_inventory(inventory, filename):
    """Export the inventory into a CSV file."""

    pass


if __name__ == "__main__":
    # display_inventory({"rope": 1, "torch": 6})
    # print_table(
    #     {"rope": 1, "torch": 6, "battleaxe": 1, "dagger": 3, "gold coin": 1}, "desc"
    # )
    import_inventory({}, "test_inventory.csv")