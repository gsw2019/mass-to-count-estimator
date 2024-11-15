"""
A graphical user interface (GUI) for the inventory calculator program

Author: Garret Wilson
Last updated: 08/08/2024
"""

# this import was not being found by PyInstaller and so had to manually import it:  --hidden import "uuid"
#
#
#
# 1. Find an icon for the application
#
# 2.
#
#
#


from pathlib import Path
import PySimpleGUI as sg
import json
import sys
import os
import subprocess
import platform

import ResultGenerator
import WelcomeGUI
import EasterEggs


# def display_memory(inventory_memory_path):
#     """
#     function that will display the InventoryMemory.txt file contents in a popup. Will send an error
#     popup if there is no InventoryMemory.txt file selected to display because the input field is
#     empty
#
#     :param inventory_memory_path: path to InventoryMemory.txt (str)
#     :return: None
#     """
#     # check there is input in the inventory memory field
#     if inventory_memory_path == "":
#         sg.popup("No Inventory Memory file selected to display\n",
#                  title="Missing File")
#         return
#
#     elif not Path(inventory_memory_path).exists():
#         sg.popup("Invalid file\n\n"
#                  "The Inventory Memory file does not exist\n",
#                  title="Invalid file")
#         return
#
#     # call check valid inputs
#     # function will send popup if catches invalid formats
#     elif check_valid_mem(Path(inventory_memory_path)) == False:
#         return
#
#     # read in csv file as dataframe
#     # doesn't require preprocessing because file follows strict format
#     df = pd.read_csv(inventory_memory_path, comment="#", header=None)
#
#     # convert data frame to string so can add header and adjust display settings
#     header = ["name", "batch size", "batch mass(oz)"]
#     df_str = df.to_string(index=False, justify="center", header=header)
#
#     # get name of file so can have title in popup window
#     filename = Path(inventory_memory_path).name
#
#     # use a monospaced font in the popup so data is displayed nicely
#     sg.popup_scrolled(df_str, title=filename, font=("Courier New", 12))


def display_memory_temp():
    sg.popup("Not currently available\n",
             title="Failed")

# def display_data(inventory_data_path):
#     """
#     function that will display the InventoryData.txt file contents in a popup. Will send an error
#     popup if there is no InventoryData.txt file selected to display because the input field is
#     empty
#
#     :param inventory_data_path: path to InventoryData.txt (str)
#     :return: None
#     """
#     # check there is input in the inventory data field
#     if inventory_data_path == "":
#         sg.popup("No Inventory Data file selected to display\n", title="Missing File")
#         return
#
#     elif not Path(inventory_data_path).exists():
#         sg.popup("Invalid file\n\n"
#                  "The Inventory Data file does not exist\n",
#                  title="Invalid file")
#         return
#
#     # call check_valid_inputs
#     # function will send popup if catches
#     elif check_valid_data(Path(inventory_data_path)) == False:
#         return
#
#     # preprocess the file because of variable format
#     # Want to display 0s in each blank entries
#     cleaned_lines = []
#     with open(inventory_data_path, 'r') as file:
#         for line in file:
#             if line.startswith("#") or line.strip() == "":
#                 continue
#
#             entries = line.strip().split(",")
#
#             # just the name
#             if len(entries) == 1:
#                 entries = [entries[0], "0", "0"]
#
#             # name and one other entry
#             elif len(entries) == 2:
#                 if entries[1].strip() == "":
#                     entries = [entries[0], "0", "0"]
#                 else:
#                     entries = [entries[0], entries[1], "0"]
#
#             # name and no entries or name and one entry
#             elif len(entries) == 3:
#                 if entries[1].strip() == "" and entries[2].strip() == "":
#                     entries = [entries[0], "0", "0"]
#                 elif entries[1].strip() != "" and entries[2].strip() == "":
#                     entries = [entries[0], entries[1], "0"]
#                 elif entries[1].strip() == "" and entries[2].strip() != "":
#                     entries = [entries[0], "0", entries[2]]
#
#             cleaned_lines.append(",".join(entries))
#
#     inventory_data = "\n".join(cleaned_lines)
#
#     # specify column names
#     col_names = ["name", "total mass(oz)", "count value"]
#
#     # read in csv file as dataframe
#     # use StringIO() to help pandas read as a file
#     df = pd.read_csv(StringIO(inventory_data), dtype="str", comment="#", header=None, names=col_names, na_values="0")
#
#     # convert data frame to string so can add header and adjust display settings
#     df_str = df.to_string(index=False, justify="center", header=col_names, na_rep="0")
#
#     # get name of file so can have title in popup window
#     filename = Path(inventory_data_path).name
#
#     # use a monospaced font in the popup so data is displayed nicely
#     sg.popup_scrolled(df_str, title=filename, font=("Courier New", 12))


def display_data_temp():
    sg.popup("Not currently available\n",
             title="Failed")


def check_secret_inputs(values):
    """
    function that checks if any of the inputs are a secret value

    :param values: inputs in the currently active window (dict)
    :return: boolean
    """
    if values["-IN_0-"] == "pizza" or values["-IN_1-"] == "pizza" or values["-OUT_0-"] == "pizza":
        EasterEggs.popup_secret_word_input()
        return True

    return False


def check_inputs(values):
    """
    function that checks if there are inputs in each of the required input fields of the window
    before executing the main calculation. Will call another function that checks file existence,
    correct formatting, and valid entries

    :param values: inputs in the currently active window (dict)
    :return: calls check_valid_inputs(values)
    """
    if not values["-IN_0-"] or not values["-IN_1-"] or not values["-OUT_0-"]:
        no_inventory_memory = values["-IN_0-"] == ""
        no_inventory_data = values["-IN_1-"] == ""
        no_output_folder = values["-OUT_0-"] == ""

        # specify which input is missing
        if (no_inventory_memory is True and no_inventory_data is True and
                no_output_folder is True):
            sg.popup("No files selected and no output folder specified\n\n"
                     "Please select files for inventory memory and inventory data. Also, "
                     "select an output folder for the results and try again\n",
                     title="Missing Files And Output Location")
            return False
        elif no_inventory_memory is True and no_inventory_data is True:
            sg.popup("No files selected\n\n"
                     "Please select a file for inventory memory and a file for inventory "
                     "data and try again\n", title="Missing Files")
            return False
        elif no_inventory_memory is True:
            sg.popup("No file selected for inventory memory\n\n"
                     "Please select a file and try again\n", title="Missing File")
            return False
        elif no_inventory_data is True:
            sg.popup("No file selected for inventory data\n\n"
                     "Please select a file and try again\n", title="Missing File")
            return False
        elif no_output_folder is True:
            sg.popup("No location specified for results\n\n"
                     "Please select a folder for the output location and try again\n",
                     title="Missing Output Location")
            return False
    else:
        return check_valid_inputs(values)


def check_valid_inputs(values):
    """
    function that will check if the input files appear to be in the correct input fields. That is,
    it will check if InventoryData.txt is in its respective input field and that InventorMemory.txt
    is also in its respective input field. This check will be based on file type and the contents of
    the files and the file format. The folder selector should limit the user to folders.

    :param values: inputs in the currently active window (dict)
    :return: boolean
    """
    # getting the user inputs from the respective fields and coercing to Paths
    inventoryMemoryField = Path(values["-IN_0-"])
    inventoryDataField = Path(values["-IN_1-"])

    #
    # checking correct file extension (.txt) and existence
    #

    # checking the end of the paths includes .txt
    if inventoryMemoryField.suffix != ".txt":
        sg.popup("Invalid File Type\n\n"
                 "The Inventory Memory file must be a .txt file.\n\n"
                 "Please make sure you select a text file with a .txt extension and try again.\n",
                 title="Invalid File Type")
        return False

    # checking file exists. Should almost never occur if user selects file from browse
    if not inventoryMemoryField.exists():
        sg.popup("Invalid File\n\n"
                 "The input Inventory Memory file does not exist.\n",
                 title="Invalid File")
        return False

    # checking the end of the paths includes .txt
    if inventoryDataField.suffix != ".txt":
        sg.popup("Invalid File Type\n\n"
                 "The Inventory Data file must be a .txt file.\n\n"
                 "Please make sure you select a text file with a .txt extension and try again.\n",
                 title="Invalid File Type")
        return False

    # checking file exists. Should almost never occur if user selects file from browse
    if not inventoryDataField.exists():
        sg.popup("Invalid File\n\n"
                 "The input Inventory Data file does not exist.\n",
                 title="Invalid File")
        return False

    #
    # memory file format and entries check
    #
    if check_valid_mem(inventoryMemoryField) == False:
        return False

    #
    # data file format and entries check
    #
    if check_valid_data(inventoryDataField) == False:
        return False

    return True


def check_valid_mem(inventoryMemoryField):
    """
    this function checks that InventoryMemory.txt has correct formatting in the file. Each line
    should have 3 entries: a name, batch size, and batch mass

    :param inventoryMemoryField: path to InventoryMemory.txt (Path)
    :return: boolean
    """
    with (inventoryMemoryField.open("r") as file):
        memFile = file.readlines()

        line_number = 1

        for line in memFile:
            if line.startswith("#") or line.strip() == "":
                line_number += 1
                continue

            line_list = line.split(",")

            # memory file has 3 elements per line
            if len(line_list) != 3:
                sg.popup(
                    f"Error:  Each line in the InventoryMemory.txt file should contain exactly 3 entries separated by commas:\n\n"
                    f"------------------------------------------------------------\n"
                    f"Name (no commas), Batch size, Batch mass\n"
                    f"------------------------------------------------------------\n\n"
                    f"The error occurred in line {line_number}  --  line contents:    {line}\n"
                    f"Please check the file and ensure each line follows the correct format.\n",
                    title="Invalid Format", line_width=104)
                return False

            # check first element is str
            if line_list[0].strip().isdigit() or line_list[0].strip().replace(".", "", 1).isdigit():
                sg.popup(f"Error:  Invalid name in line {line_number} of InventoryMemory.txt\n\n\n"
                         f"Line contents:    {line}\n\n"
                         f"Expected format:  name (no commas), batch size, batch mass\n",
                         title="Invalid Value", line_width=66)
                return False

            # check second element is integer
            try:
                int(line_list[1])
            except ValueError:
                sg.popup(
                    f"Error:  Invalid batch size in line {line_number} of InventoryMemory.txt\n\n\n"
                    f"Line contents:    {line}\n\n"
                    f"Expected format:  name (no commas), batch size, batch mass\n",
                    title="Invalid Value", line_width=72)
                return False

            # check third element is integer or float
            try:
                float(line_list[2])
            except ValueError:
                sg.popup(
                    f"Error:  Invalid batch mass in line {line_number} of InventoryMemory.txt\n\n\n"
                    f"Line contents:    {line}\n\n"
                    f"Expected format:  name (no commas), batch size, batch mass\n", title="Invalid Value",
                    line_width=72)
                return False

            line_number += 1

    file.close()

    return True


def check_valid_data(inventoryDataField):
    """
    this function checks that InventoryData.txt has correct formatting in the file. Each line
    should have either 1, 2 or 3 entries.

    if 1 entry: name

    if 2 entries: name, total mass of all items

    if 3 entries: name, total mass of all items, count of items

    :param inventoryDataField: path to InventoryData.txt (Path)
    :return: boolean
    """
    #
    # data file format check
    #
    with inventoryDataField.open("r") as file:
        dataFile = file.readlines()

        line_number = 1

        for line in dataFile:
            if line.startswith("#") or line.strip() == "":
                line_number += 1
                continue

            line_list = line.split(",")

            # data file has 1, 2 or in some cases 3 elements per line
            if len(line_list) > 3:
                sg.popup(
                    f"Error:  No line in the InventoryData.txt should exceed 3 entries, each separated by a comma\n\n"
                    f"If 1 entry:\n"
                    f"      Name (no commas)\n\n"
                    f"If 2 entries:\n"
                    f"      Name (no commas), Total mass of all units\n\n"
                    f"If 3 entries:\n"
                    f"      Name (no commas), Total mass of all units, Count value\n\n\n"
                    f"The error occurred in line {line_number}  --  line contents:    {line}\n\n"
                    f"Please check the file and ensure each line follows the correct format.\n",
                    title="Invalid Format", line_width=110)
                return False

            elif len(line_list) == 1:
                line_entries_count = 1

                entry1 = line_list[0]

                # check first element is str
                if check_valid_data_entry1(entry1, line, line_number, line_entries_count) == False:
                    return False

            elif len(line_list) == 2:
                line_entries_count = 2

                entry1 = line_list[0]
                entry2 = line_list[1]

                # check first element is str
                if check_valid_data_entry1(entry1, line, line_number, line_entries_count) == False:
                    return False

                # check second element is empty string, integer, float or addition string
                elif check_valid_data_entry2(entry2, line, line_number, line_entries_count) == False:
                    return False

            elif len(line_list) == 3:
                line_entries_count = 3

                entry1 = line_list[0]
                entry2 = line_list[1]
                entry3 = line_list[2]

                # check first element is str
                if check_valid_data_entry1(entry1, line, line_number, line_entries_count) == False:
                    return False

                # check second element is empty string, integer, float or addition string
                elif check_valid_data_entry2(entry2, line, line_number, line_entries_count) == False:
                    return False

                # check third element is 'c' followed by int
                elif check_valid_data_entry3(entry3, line, line_number) == False:
                    return False

            line_number += 1

    file.close()

    return True


def check_valid_data_entry1(entry1, line, line_number, line_entries_count):
    """
    this function simply checks if the first entry in a line of InventoryData.txt is a string

    :param entry1: the first entry in a line of InventoryData.txt (str)
    :param line: the entire contents of a line in InventoryData.txt (str)
    :param line_number: the line number currently being checked (int)
    :param line_entries_count: number of entries in line, specifies error popup (int)
    :return: boolean
    """
    # check first element is str
    if entry1.strip().isdigit() or entry1.strip().replace(".", "", 1).isdigit() or entry1.strip() == "":
        if line_entries_count == 2:
            sg.popup(f"Error:  Invalid name in line {line_number} of InventoryData.txt\n\n\n"
                     f"Line contents:    {line}\n\n"
                     f"Expected format:  name (no commas), total mass of units\n",
                     title="Invalid Value",
                     line_width=64)
            return False

        elif line_entries_count == 1:
            sg.popup(f"Error:  Invalid name in line {line_number} of InventoryData.txt\n\n\n"
                     f"Line contents:    {line}\n\n"
                     f"Expected format:  name (no commas)\n",
                     title="Invalid Value",
                     line_width=64)

        else:
            sg.popup(f"Error:  Invalid name in line {line_number} of InventoryData.txt\n\n\n"
                     f"Line contents:    {line}\n\n"
                     f"Expected format:  name (no commas), total mass of units, count value\n",
                     title="Invalid Value",
                     line_width=64)
            return False

    return True


def check_valid_data_entry2(entry2, line, line_number, line_entries_count):
    """
    this function checks if the second entry is empty, 0, an addition operation, or a number

    :param entry2: the second entry in a line of InventoryData.txt (str)
    :param line: the entire contents of a line in InventoryData.txt (str)
    :param line_number: the line number currently being checked (int)
    :param line_entries_count: number of entries in line, specifies error popup (int)
    :return: boolean
    """
    # initialize error_type so send correct popup
    error_type = 0

    # check second element is empty string, integer, float or addition string
    try:
        # empty string
        if entry2.strip() == "":
            return True

        # addition string
        elif "+" in entry2:

            # each individual addend in a list
            addends = entry2.split("+")

            # check each addend is valid
            for addend in addends:
                addend = addend.strip()

                # invalid float, accepts floats such as .5 or .10
                if addend.endswith("."):
                    error_type = 1
                    raise ValueError

                try:
                    float(addend)
                except ValueError:
                    error_type = 1
                    raise ValueError

        # integer or float
        else:
            float(entry2)

    except ValueError:
        if error_type == 0 and line_entries_count == 2:
            sg.popup(
                f"Error:  Invalid total mass of all units in line {line_number} of InventoryData.txt\n\n\n"
                f"Line contents:    {line}\n\n"
                f"Expected format:  name (no commas), total mass of units\n",
                title="Invalid Value",
                line_width=83)
            return False

        elif error_type == 0 and line_entries_count == 3:
            sg.popup(
                f"Error:  Invalid total mass of all units in line {line_number} of InventoryData.txt\n\n\n"
                f"Line contents:    {line}\n\n"
                f"Expected format:  name (no commas), total mass of units, count value\n",
                title="Invalid Value",
                line_width=83)
            return False

        elif error_type == 1 and line_entries_count == 2:
            sg.popup(
                f"Error:  Failed addition operation in line {line_number} of InventoryData.txt\n\n\n"
                f"Line contents:    {line}\n\n"
                f"Expected format:  name (no commas), number + number + number....\n",
                title="Invalid Addition Operation",
                line_width=77)
            return False

        elif error_type == 1 and line_entries_count == 3:
            sg.popup(
                f"Error:  Failed addition operation in line {line_number} of InventoryData.txt\n\n\n"
                f"Line contents:    {line}\n\n"
                f"Expected format:  name (no commas), number + number + number..., count value\n",
                title="Invalid Addition Operation",
                line_width=77)
            return False

    return True


def check_valid_data_entry3(entry3, line, line_number):
    """
    this function checks if the third entry is empty, 0, an addition operation, or a number. In
    most cases, it should be an integer.

    :param entry3: the second entry in a line of InventoryData.txt (str)
    :param line: the entire contents of a line in InventoryData.txt (str)
    :param line_number: the line number currently being checked (int)
    :return: boolean
    """
    # initialize error_type so send correct popup
    error_type = 0

    # check third element is empty string, integer, float or addition string
    try:
        # empty string
        if entry3.strip() == "":
            return True

        # addition string
        elif "+" in entry3:

            # each individual addend in a list
            addends = entry3.split("+")

            for addend in addends:
                addend = addend.strip()

                if addend.endswith("."):
                    error_type = 1
                    raise ValueError

                try:
                    float(addend)
                except ValueError:
                    error_type = 1
                    raise ValueError

        # integer or float
        else:
            float(entry3)

    except ValueError:
        if error_type == 0:
            sg.popup(
                f"Error:  Invalid count value in line {line_number} of InventoryData.txt\n\n\n"
                f"Line contents:    {line}\n\n"
                f"Expected format:  name (no commas), total mass of all units, count value\n",
                title="Invalid Count Value",
                line_width=71)
            return False

        else:
            sg.popup(
                f"Error:  Invalid addition operation in line {line_number} of InventoryData.txt\n\n\n"
                f"Line contents:    {line}\n\n"
                f"Expected format:  name (no commas), total mass of all units, number + number...\n",
                title="Invalid Addition Operation",
                line_width=71)
            return False

    return True


def fill_fields_on_window_open(window, path_to_folder):
    """
    function that will automatically fill the input fields of the InputGUI if the user generated
    files on the Welcome Window.

    :param window: input_gui window (object)
    :param path_to_folder: path the user saved the newly generated files to (Path)
    :return: None
    """
    inventoryMemoryField = Path(path_to_folder) / "InventoryMemory.txt"
    inventoryDataField = Path(path_to_folder) / "InventoryData.txt"
    outputFolderField = path_to_folder

    window["-IN_0-"].update(inventoryMemoryField)
    window["-IN_1-"].update(inventoryDataField)
    window["-OUT_0-"].update(outputFolderField)


def create_JSON(inventoryMemoryField, inventoryDataField, outputFolderField):
    """
    function to create a JSON file that will store the users paths once they have generated results
    for the first time. Used for autofill function

    :param inventoryMemoryField: path to InventoryMemory.txt (Path)
    :param inventoryMemoryField: path to InventoryData.txt (Path)
    :param inventoryMemoryField: path to output folder (Path)
    :return: None
    """
    # store in dict for JSON dump
    # strings because JSON cant handle paths
    user_data = {
        "inventoryMemoryFile": str(inventoryMemoryField),
        "inventoryDataFile": str(inventoryDataField),
        "outputFolder": str(outputFolderField)
    }

    # Get the current script directory depending on if ran as script or executable
    if getattr(sys, 'frozen', False):
        script_dir = Path(sys.executable).parent
    else:
        script_dir = Path(__file__).parent

    # define JSON path
    json_path = script_dir / "user_data_DO_NOT_DELETE.json"

    with open(json_path, "w") as json_file:
        json.dump(user_data, json_file, indent=4)


def auto_fill(window):
    """
    function that will read from a file saved in the same directory as the program and input the
    fields saved from previously running the program

    :param window: CalculateInventoryGUI (object)
    :return: None
    """
    # Get the current script directory depending on if ran as script or executable
    if getattr(sys, 'frozen', False):
        script_dir = Path(sys.executable).parent
    else:
        script_dir = Path(__file__).parent

    expected_json_path = script_dir / "user_data_DO_NOT_DELETE.json"

    if expected_json_path.exists():
        with open(expected_json_path, "r") as json_file:
            user_data = json.load(json_file)
    else:
        sg.popup("No saved paths found\n\n"
                 "You must select files and run the program at least once to save paths for the autofill function\n",
                 title="No Saved Paths Found", line_width=80)
        return

    inventoryMemoryField = user_data["inventoryMemoryFile"]
    inventoryDataField = user_data["inventoryDataFile"]
    outputFolderField = user_data["outputFolder"]

    window["-IN_0-"].update(inventoryMemoryField)
    window["-IN_1-"].update(inventoryDataField)
    window["-OUT_0-"].update(outputFolderField)


def open_mem_data_files():
    """
    this function will automatically open InventoryMemory.txt and InventoryData.txt when the user
    opens the Input Window if a json file can be found. If not, nothing happens
    :return: None
    """
    # Get the current script directory depending on if ran as script or executable
    if getattr(sys, 'frozen', False):
        script_dir = Path(sys.executable).parent
    else:
        script_dir = Path(__file__).parent

    expected_json_path = script_dir / "user_data_DO_NOT_DELETE.json"

    if expected_json_path.exists():
        with open(expected_json_path, "r") as json_file:
            user_data = json.load(json_file)
    else:
        return

    inventory_memory_file = Path(user_data["inventoryMemoryFile"])
    inventory_data_file = Path(user_data["inventoryDataFile"])

    # check files exist
    if inventory_memory_file.exists() and inventory_data_file.exists():

        if platform.system() == "Windows":
            os.startfile(inventory_memory_file)
            os.startfile(inventory_data_file)
        elif platform.system() == "Darwin":  # macOS
            subprocess.call(["open", inventory_memory_file])
            subprocess.call(["open", inventory_data_file])
        else:  # Linux
            subprocess.call(["xdg-open", inventory_memory_file])
            subprocess.call(["xdg-open", inventory_data_file])


def open_results(result_file_path):
    """
    function that automatically opens the results file

    :param result_file_path: path to result file (Path)
    :return: None
    """
    if platform.system() == "Windows":
        os.startfile(result_file_path)
    elif platform.system() == "Darwin":  # macOS
        subprocess.call(["open", result_file_path])
    else:  # Linux
        subprocess.call(["xdg-open", result_file_path])


def input_gui(path_to_folder, fill):
    """
    function that creates the input graphical user interface (GUI) and utilizes all of the above
    functions. Also, automatically opens InventoryMemory.txt and InventoryData.txt

    :param path_to_folder: if user generated files in Intro Window, stores path to that directory (Path)
    :param fill: whether to autopopulate the input fields or not (boolean)
    :return: None
    """
    # open InventoryMemory.txt and InventoryData.txt if they can be found
    open_mem_data_files()

    # set the font and text size for entire window unless specified elsewhere
    font = ("Arial", 16)
    sg.set_options(font=font)

    # theme of window
    sg.theme("Topanga")

    # each line in the 2-D list is a line in the window
    layout = [
        [sg.Button("Edit files",
                   size=(15, 1), pad=((15, 25), (10, 30))),
         sg.Text(text="Marco's Inventory Automator",
                 size=(30, 1), pad=((0, 25), (10, 30)),font=("Helvetica", 25), justification="c", tooltip=" enter 'pizza' "),
         sg.Button("Auto-Fill", size=(15, 1), pad=((0, 5), (10, 30)), tooltip=" Auto-fill last entries ")],
        [sg.Text("REMINDER:",
                 font=("Arial", 16, "underline"), pad=((5, 5), (1, 1)))],
        [sg.Text("• InventoryData.txt:",
                 font=("Helvetica", 16, "bold"), pad=((15, 5), (1, 1))),
         sg.Text("Update this file with the total mass and/or count value for each item every inventory cycle",
                 pad=((0, 0), (1, 1)))],
        [sg.Text("• InventoryMemory.txt:",
                 font=("Helvetica", 16, "bold"), pad=((15, 5), (1, 1))),
         sg.Text("Only edit this file under special circumstances such as adding or changing items",
                 pad=((0, 0), (1, 1)))],
        [sg.Text("• InventoryResults.txt:",
                 font=("Helvetica", 16, "bold"), pad=((15, 5), (1, 30))),
         sg.Text("Must be closed before the file will update with results",
                 pad=((0, 0), (1, 30)))],
        [sg.Text(text="Inventory memory file:"), sg.Input(key="-IN_0-", size=(60, 1), pad=((5, 5), (0, 0))),
         sg.FileBrowse()],
        [sg.Text(text="Inventory data file:"), sg.Input(key="-IN_1-", size=(60, 1), pad=((31, 5), (0, 0))),
         sg.FileBrowse()],
        [sg.Text(text="Results output folder:"), sg.Input(key="-OUT_0-", size=(60, 1), pad=((10, 5), (0, 0))),
         sg.FolderBrowse()],
        [sg.Button("Generate results",
                   s=(16, 1), pad=((1, 1), (20, 1))),
         sg.Button("Display memory",
                   s=(16, 1), pad=((7, 1), (20, 1))),
         sg.Button("Display data",
                   s=(16, 1), pad=((7, 1), (20, 1))),
         sg.Button("Back",
                   s=(16, 1), pad=((7, 1), (20, 1))),
         sg.Button("Exit",
                   s=(16, 1), pad=((7, 1), (20, 1)))]
    ]

    # create the window, providing a title and passing the layout
    window = sg.Window("Marco's Inventory Automator", layout, size=(820, 375), location=(300, 200),
                       finalize=True, keep_on_top=False, return_keyboard_events=True, resizable=True)

    # if the user generated files on startup, fill the input fields, so they don't have to
    if fill:
        fill_fields_on_window_open(window, path_to_folder)

    # Event Loop
    while True:
        event, values = window.read()

        # user selects exit button or closes window
        if event == sg.WIN_CLOSED or event == "Exit":
            break

        # go back to intro window
        elif event == "Back":
            window.close()
            WelcomeGUI.welcome_gui()
            break

        # make popups for no input field
        elif event == "Display memory":
            # display_memory(values["-IN_0-"])
            display_memory_temp()
            continue

        # make popups for no input field
        elif event == "Display data":
            # display_data(values["-IN_1-"])
            display_data_temp()
            continue

        elif event == "Edit files":
            sg.popup(" Feature coming soon ")

        elif event == "Auto-Fill":
            auto_fill(window)

        # main execution
        # find return/enter key for windows
        elif event == "Generate results" or event == "Return:603979789":
            # check for secret inputs
            secret_input = check_secret_inputs(values)
            if secret_input is True:
                continue

            # check there are required inputs and that they are valid
            all_inputs_valid = check_inputs(values)
            if all_inputs_valid is False:
                continue

            # execute calculation and write results
            # get the paths to the memory and data files
            inventory_memory_path = Path(values["-IN_0-"])
            inventory_data_path = Path(values["-IN_1-"])

            # get path to the output directory
            output_directory_path = Path(values["-OUT_0-"])
            output_file_path = output_directory_path / "InventoryResults.txt"

            # call main function in ResultGenerator.py
            if ResultGenerator.main(inventory_memory_path, inventory_data_path, output_file_path) == False:
                continue

            # call function to write a JSON file that holds the users input fields after executed
            # at least once
            create_JSON(inventory_memory_path, inventory_data_path, output_directory_path)

            # send a done message in a popup
            # sg.popup("Done!", keep_on_top=True)

            # call function to open results file
            open_results(output_file_path)

        # test to see keyboard event values
        # else:
        #     print(f"Event = {event}")

    window.close()
