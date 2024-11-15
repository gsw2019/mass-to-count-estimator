"""
Calculate inventory counts using simple CSV input files. Two input files are needed, InventoryMemory.txt
and the InventoryData.txt

Author: Garret Wilson
Last updated: 08/08/2024
"""

import PySimpleGUI as sg
import random
import time

import ItemClass


def open_inventory_memory(inventory_memory_file):
    """
    read in the InventoryMemory.txt file and clean it

    the format and entries in each line of InventoryMemory.txt have already been verified in
    InputGUI.py

    The memory file holds the name, number of units measured together, and the mass of that group
    of units. This description is exactly what a line will always look like:
    name, batch size, batch mass

    :param inventory_memory_file: a .txt file (str)
    :return: inventory_memory: list with all the cleaned lines (2-D list)
    """
    # read in the .txt file as a list of lines
    raw_inventory_memory = inventory_memory_file.open("r").readlines()

    # cleaning each entry of a line and adding each line to a list (making 2-D list)
    inventory_memory = []
    for line in raw_inventory_memory:
        if line.startswith("#") or line.strip() == "":
            continue

        line_lst = line.split(",")

        # clean individual entries and create list that is equivalent to a line
        # InputGUI.check_valid_inputs ensures correct types at each position
        entry1 = line_lst[0].strip()
        entry2 = float(line_lst[1])
        entry3 = float(line_lst[2])

        new_line = [entry1, entry2, entry3]

        # add line to 2-D list
        inventory_memory.append(new_line)

    # 2-D list with each line as an element
    # print(inventory_memory)
    return inventory_memory


def create_items(inventory_memory):
    """
    function to create Item objects from the in InventoryMemory.txt file

    utilizes ItemClass.py

    :param inventory_memory: a list with each element as a list representing a line (2-D list)
    :return: item_dict: holds all Item objects (dict)
    """
    # initialize dictionary
    item_dict = {}

    # iterate through lines, create Item objects from line, store in item_dict{}
    for line in inventory_memory:
        # always 3 entries or error popup will display
        item = ItemClass.Item(line[0], line[1], line[2])
        # first entry is a name
        item_dict[line[0]] = item

    # print(item_dict)
    return item_dict


def open_inventory_data(inventory_data_file):
    """
    read in the InventoryData.txt file and clean it

    the format and entries in each line of InventoryData.txt have already been verified in
    InputGUI.py

    the data file can hold just the name of an item. This description is exactly what a line could
    look like:
    name

    the data file can hold the name of an item and the total mass of all the units. This description
    is exactly what a line could look like:
    name, total mass of all units

    the data file might also hold the name of an item, total mass of all the units, and a count value.
    This description is exactly what a line could look like:
    name, total mass of all units, count value

    :param inventory_data_file: a .txt file (str)
    :return: inventory_data: list with all the cleaned lines (2-D list)
    """
    # read in the CSV file as a list of lines
    raw_inventory_data = inventory_data_file.open("r").readlines()

    # Initialize new list to hold cleaned lines
    inventory_data = []

    line_number = 1

    for line in raw_inventory_data:
        if line.startswith("#") or line.strip() == "":
            line_number += 1
            continue

        line_lst = line.split(",")

        #
        # InventoryData.txt line with 1 entry
        #
        if len(line_lst) == 1:
            entry1 = line_lst[0].strip()
            entry2 = 0

            new_line = [entry1, entry2]
            inventory_data.append(new_line)

            line_number += 1

            continue

        #
        # InventoryData.txt line with 2 entries
        #
        if len(line_lst) == 2:
            # clean individual entries and create list that is equivalent to a line
            # InputInterfaceGUI.check_valid_inputs has ensured correct types at each position

            # entry1 was already checked to be string
            entry1 = line_lst[0].strip()
            # entry 2 getting coerced
            entry2 = line_lst[1].strip()

            # left blank, make entry2 0, thus result 0.0
            if entry2 == "":
                entry2 = 0

            # 0 entry, makes result 0.0
            elif entry2 == "0" or entry2 == "0.0":
                entry2 = 0

            # sum multiple measurements
            elif "+" in entry2:
                entry2 = add_multiple_measurements(entry2)

            else:
                entry2 = float(entry2)

            new_line = [entry1, entry2]
            inventory_data.append(new_line)

            line_number += 1

            continue

        #
        # InventoryData.txt line with 3 entries
        #
        elif len(line_lst) == 3:
            # clean individual entries and create list that is equivalent to a line
            # InputInterfaceGUI.check_valid_inputs has ensured correct types at each position

            # entry1 already checked to be a string
            entry1 = line_lst[0].strip()

            # entry2 getting coerced to appropriate type
            entry2 = line_lst[1].strip()

            # left blank, thus no total va;ue but will still add count value
            if entry2 == "":
                entry2 = 0

            # 0 entry, makes result 0.0
            elif entry2 == "0" or entry2 == "0.0":
                entry2 = 0

            # sum multiple measurements
            elif "+" in entry2:
                entry2 = add_multiple_measurements(entry2)

            else:
                entry2 = float(entry2)

            # entry3 getting coerced to appropriate type
            entry3 = line_lst[2].strip()

            # left blank, no count to add, thus line is just name and total count
            if entry3 == "":
                new_line = [entry1, entry2]
                inventory_data.append(new_line)
                line_number += 1
                continue

            # set to 0, no count to add, thus line is just name and total count
            elif entry3 == "0" or entry3 == "0.0":
                new_line = [entry1, entry2]
                inventory_data.append(new_line)
                line_number += 1
                continue

            # sum multiple measurements in entry3
            elif "+" in entry3:
                entry3 = add_multiple_measurements(entry3)
                new_line = [entry1, entry2, entry3]
                inventory_data.append(new_line)
                line_number += 1
                continue

            else:
                entry3 = float(entry3)

            new_line = [entry1, entry2, entry3]
            inventory_data.append(new_line)

            line_number += 1

            continue

    return inventory_data


def add_multiple_measurements(entry):
    """
    this function handles the addition of multiple measurements in an InventoryData.txt line. it
    adds the values together and returns the sum

    :param entry: an entry in an InventoryData.txt line (str)
    :return: float
    """
    addends = entry.split("+")

    result_sum = 0
    for addend in addends:
        result_sum += float(addend)

    return float(result_sum)


def progress_bar_window():
    """
    this function makes a fun animation to show the user the program is currently working

    :return: None
    """
    # make a layout
    layout = [
        [sg.ProgressBar(max_value=200, orientation="h", size_px=(500, 7), key="-PROGRESS-", style="default",
                        bar_color=("gold3")), sg.Cancel()]
    ]

    # open window and make variable for progress bar
    window = sg.Window(title="Finishing up...", layout=layout)
    progress_bar = window["-PROGRESS-"]

    # track same progress given to progress_bar
    progress = 0

    while progress <= 200:
        event, values = window.read(timeout=10)

        # user can cancel, should return to InputGUI.py window
        if event == 'Cancel' or event == sg.WIN_CLOSED or event is None:
            window.close()
            return False

        progress_update = random.uniform(1, 90)
        progress += progress_update
        progress_bar.update(current_count=progress)

        update_interval = random.uniform(0.05, 0.5)
        time.sleep(update_interval)

    window.close()


def write_inventory_results(item_dict, inventory_data_file, output_file_path):
    """
    function to calculate inventory numbers and return them in an InventoryResults.txt file

    generates a popup that details Items not found in memory

    :param item_dict: dictionary with all Items from inventory memory (dict)
    :param inventory_data_file: 2-D list with all the cleaned lines from inventory data (2-D list)
    :param output_file_path: path to directory and file to write results (str)
    :return: None
    """
    # create a file to write the results to
    result_file = output_file_path.open("w")

    # write some comment lines describing results
    result_file.write("###########################################\n"
                      "#\n"
                      "# name, result of calculation\n"
                      "#\n"
                      "###########################################\n\n\n")

    # list to hold unknown names
    unknown_names_list = []

    # loop through the inventory data file lines and get name of item
    for line in inventory_data_file:

        # case where InventoryData.txt has a line with 2 entries
        # lines with just a name are given a second entry of "0" in open_inventory_data(inventory_data_file)
        if len(line) == 2:

            name = line[0]
            total_mass = line[1]

            # find Item object in item_dict matching item from InventoryData.txt
            if name in item_dict.keys():
                item_object = item_dict[name]
                result = item_object.calculate_total_count_v1(total_mass)
                result_file.write(name + ", " + str(result) + "\n")
                continue

            # track unknown items
            else:
                str_line = f"{name}, {total_mass}"
                unknown_names_list.append(str_line)
                continue

        # case where InventoryData.txt has a line with 3 entries
        elif len(line) == 3:

            name = line[0]
            total_mass = line[1]
            count_value = line[2]

            # find Item object in item_dict matching item from data
            if name in item_dict.keys():
                item_object = item_dict[name]
                result = item_object.calculate_total_count_v2(total_mass, count_value)
                result_file.write(name + ", " + str(result) + "\n")
                continue

            # track unknown items
            else:
                str_line = f"{name}, {total_mass}, {count_value}"
                unknown_names_list.append(str_line)
                continue

    # check for unknown items
    # if any send popup
    if len(unknown_names_list) > 0:
        unknown_names_str = "\n".join(unknown_names_list)

        sg.popup_non_blocking(unknown_names_str,
                              f"\nThese item names could not be found in the memory items.\n\n"
                              f"You will need to update the inventory data or the inventory memory and rerun the program.\n",
                              non_blocking=True, keep_on_top=True, location=(50, 200), title="Unknown Items", line_width=90)

    result_file.close()


def main(inventory_memory_path, inventory_data_path, output_file_path):
    """
    runs the ResultGenerator.py script and starts a very short progress bar animation

    :param inventory_memory_path: path to InventoryMemory.txt (Path)
    :param inventory_data_path: path to InventoryData.txt (Path)
    :param output_file_path: path to InventoryResults.txt (Path)
    :return: None or Boolean
    """
    inventory_memory = open_inventory_memory(inventory_memory_path)
    inventory_data = open_inventory_data(inventory_data_path)

    items_dict = create_items(inventory_memory)

    # if user cancels on progress bar window, exits main function and doesn't write results
    if progress_bar_window() == False:
        return False

    write_inventory_results(items_dict, inventory_data, output_file_path)
