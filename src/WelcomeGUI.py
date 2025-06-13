"""
A graphical user interface (GUI) for an introduction to the automator and generating required text
files for input into InputGUI.py, if the user needs them

Author: Garret Wilson
Last updated: 08/08/2024
"""

#
#
# 1. go through test runs, just play around with it
#
# 2. Test pyinstaller without pandas. Just remove the display options...program will open up the
#       files anyway, so might be okay to leave that functionality out if it significantly decreases
#       size and improves start-up time of onefile
#
#


import PySimpleGUI as sg
from pathlib import Path
import os
import platform
import subprocess

import InputGUI


def more_info_howitworks_window():
    """
    function that makes a window containing more information about how the program works behind the
    scenes. Will show the equations used, and example calculations

    this is a window instead of a popup because windows are more versatile and the info needs to be
    thorough with a clean layout

    :return: None
    """
    # set the font and text size for entire window, unless specified elsewhere
    font = ("Arial", 13)
    sg.set_options(font=font)

    # theme of window
    sg.theme("Topanga")

    # top of window
    layout_top = [
        [sg.Text("How It Works",
                 font=("Arial", 16, "bold"), pad=((615, 1), (5, 5)))],
        [sg.Text("The user inputs the two necessary files: InventoryMemory.txt and InventoryData.txt. "
                 "Both of these files hold data required to calculate the total count of an inventory item using a simple mathematical equation.\n"
                 "InventoryMemory.txt is strict in its formatting, however, InventoryData.txt can support a third entry and addition operations, "
                 "as shown in Example 2 and Example 3.",
                 font=("Arial", 14), pad=((1, 1), (1, 10)))],
        [sg.HorizontalSeparator()]
    ]

    # layout of column 1
    layout_column1 = [
        [sg.Text("Example 1 - Basic",
                 font=("Arial", 14, "underline"), pad=((1, 1), (10, 10)))],
        [sg.Text("InventoryMemory.txt line:",
                 pad=((0, 0), (0, 0)))],
        [sg.Text("Large Sub Wrap, 20, 6.3\n",
                 pad=((20, 1),(0, 0)))],
        [sg.Text("InventoryData.txt line:",
                 pad=((0, 0), (0, 0)))],
        [sg.Text("Large Sub Wrap, 239.7\n",
                 pad=((20, 1),(0, 0)))],
        [sg.Text("•  These two lines have matching names, thus the program will use\n"
                 "   the data in each of these lines to calculate the total item count\n")],
        [sg.Text("•  The InventoryMemory.txt line says that a batch of 20 Large Sub\n"
                 "   Wrap has a mass of 6.3 ounces\n")],
        [sg.Text("•  The InventoryData.txt line says that all the Large Sub Wrap in the\n"
                 "   store have a mass of 239.7 ounces\n")],
        [sg.Text("•  These three numbers, the batch size, the batch mass, and the total\n"
                 "   mass will allow us to solve for the total number of items using this\n"
                 "   equation:\n")],
        [sg.Text("total count = (total mass / batch mass) × batch size\n",
                 pad=((65, 1), (1, 1)))],
        [sg.Text("•  In this example, the Large Sub Wrap would have a total count of: \n")],
        [sg.Text("total count = (239.7 / 6.3) × 20 = 760.95\n",
                 pad=((65, 1), (1, 43)))]
    ]

    # layout of column 2
    layout_column2 = [
        [sg.Text("Example 2 - Addition Operations",
                 font=("Arial", 14, "underline"), pad=((1, 1), (10, 10)))],
        [sg.Text("InventoryMemory.txt line:",
                 pad=((0, 0), (0, 0)))],
        [sg.Text("Large Sub Wrap, 20, 6.3\n",
                 pad=((20, 1),(0, 0)))],
        [sg.Text("InventoryData.txt line:",
                 pad=((0, 0), (0, 0)))],
        [sg.Text("Large Sub Wrap, 239.7 + 215.5, 200\n",
                 pad=((20, 1),(0, 0)))],
        [sg.Text("•  Here, the InventoryData.txt line says that the measured Large Sub\n"
                 "   Wrap have a mass of 239.7 + 215.5 ounces and that there are\n"
                 "   already 200 Large Sub Wrap counted\n")],
        [sg.Text("•  Using an addition operation is supported in the total mass entry\n")],
        [sg.Text("•  These four numbers, the batch size, the batch mass, the total\n"
                 "   mass, and the count value will allow us to solve for the total number\n"
                 "   of items using this equation:\n")],
        [sg.Text("total count = ((total mass / batch mass) × batch size) + count value\n",
                 pad=((25, 1), (1, 1)))],
        [sg.Text("•  In this example, the Large Sub Wrap would have a total count of: \n")],
        [sg.Text("total count = ((239.7 + 215.5) / 6.3) × 20) + 200 = 1645.08\n",
                 pad=((25, 1), (1, 100)))]
    ]

    # layout of column 3
    layout_column3 = [
        [sg.Text("Example 3 - Addition Operations",
                 font=("Arial", 14, "underline"), pad=((1, 1), (10, 10)))],
        [sg.Text("InventoryMemory.txt line:",
                 pad=((0, 0), (0, 0)))],
        [sg.Text("Large Sub Wrap, 20, 6.3\n",
                 pad=((20, 1), (0, 0)))],
        [sg.Text("InventoryData.txt line:",
                 pad=((0, 0), (0, 0)))],
        [sg.Text("Large Sub Wrap, 239.7 + 215.5, 200 + 475\n",
                 pad=((20, 1), (0, 0)))],
        [sg.Text("•  Here, the InventoryData.txt line says that the measured Large Sub\n"
                 "   Wrap have a mass of 239.7 + 215.5 ounces and that there are\n"
                 "   already 200 + 475 Large Sub Wrap counted\n")],
        [sg.Text("•  Using an addition operation is also supported in the count value\n"
                 "   entry\n")],
        [sg.Text("•  These four numbers, the batch size, the batch mass, the total\n"
                 "   mass, and the count value will allow us to solve for the total number\n"
                 "   of items using this equation:\n")],
        [sg.Text("total count = ((total mass / batch mass) × batch size) + count value\n",
                 pad=((25, 1), (1, 1)))],
        [sg.Text("•  In this example, the Large Sub Wrap would have a total count of: \n")],
        [sg.Text("total count = ((239.7 + 215.5) / 6.3) × 20) + (200 + 475) = 2120.08\n",
                 pad=((25, 1), (1, 83)))]
    ]

    # layout of entire window
    layout = [
        [layout_top],
        [sg.Column(layout_column1), sg.VerticalSeparator(), sg.Column(layout_column2), sg.VerticalSeparator(), sg.Column(layout_column3)],
        [sg.Button("Close", size=(10, 1))],
        []
    ]

    # window object
    window2 = sg.Window("More Information - How It Works", layout, size=(1310, 675),
                        location=(50, 0), finalize=True, resizable=True)

    return window2


def more_info_files_window():
    """
    function that creates a window containing more information about the two input files

    this is a window instead of a popup because windows are more versatile and the info needs to be
    thorough with a clean layout

    :return: None
    """
    # set the font and text size for entire window, unless specified elsewhere
    font = ("Arial", 13)
    sg.set_options(font=font)

    # theme of window
    sg.theme("Topanga")

    layout_top = [
        [sg.Text("The Input Files",
                 font=("Arial", 16, "bold"), pad=((535, 1), (3, 1)))],
        [sg.Text(
            "Understanding each input file and its contents is crucial for being able to use this program optimally. This may look like an overwhelming amount of information, but it's really simple once\n"
            "understood, and all of this is just to make sure everything is as clear as possible. The input files are the heart of the program, and the user is solely responsible for making sure they are\n"
            "correctly formatted and devoid of errors. However, the program will point out errors it detects along with detailed explanations that should help the user identify their mistake. Information\n"
            "about each file is given here, but can also be found in the generated files themselves.",
            font=("Arial", 14))],
        [sg.Text("Characteristics Common to Both Files",
                 font=("Arial", 14, "underline"), pad=((5, 1), (5, 5)))],
        [sg.Text("•  File types are CSV or comma separated values",
                 pad=((10, 1), (1, 1)), font=("Arial", 14, "bold"))],
        [sg.Text("•  The files are processed as lines, that is, each individual line in a file is handled separately",
                 pad=((10, 1), (1, 1)))],
        [sg.Text("•  Importantly, lines that begin with ' # ' are ignored by the program and designated as comment lines",
                 pad=((10, 1), (1, 10)))],
        [sg.HorizontalSeparator()]
    ]

    # layout of column 1
    layout_column1 = [
        [sg.Text("InventoryMemory.txt File",
                 font=("Arial", 14, "underline"), pad=((1, 400), (0, 1)))],
        [sg.Text("•  The user should not interact with this file very often. The cases in which the user might are\n"
                 "   noted below. This file holds data that are constants of the total count calculation. This\n"
                 "   includes:\n"
                 "         - item name\n"
                 "         - the batch size or number of units measured together\n"
                 "         - the batch mass\n\n"
                 "   the item name is required so that the data in a line of InventoryMemory.txt can be matched\n"
                 "   to a line in InventoryData.txt. Once the lines are matched, the program can use the batch\n"
                 "   size and the batch mass to solve for a total count, given the data recorded in\n"
                 "   InventoryData.txt.")],
        [sg.Text("•  The data in this file has been gathered by hand following a specific regimen. The regimen\n"
                 "   is referred to as BEST PRACTICE and can be followed by:\n" 
                 "         1. Measuring the mass of a batch of units (usually 20) of an item on a STABLE\n"
                 "             SURFACE in GRAMS (g)\n"
                 "                    - recommended stable surface is the ground\n"
                 "                    - grams are used for better sensitivity\n"
                 "         2. Convert the grams result to OUNCES (oz) using Google\n"
                 "         3. Record batch size, batch mass(oz) next to name\n")],
        [sg.Text("•  This file should only be modified if a product changes or a new product is added.\n"
                 "         - in the case of a product change:   follow BEST PRACTICE (2nd bullet) and update\n"
                 "           batch mass\n"
                 "         - in the case of a new product:   make a new line in the file, record name, follow\n"
                 "           BEST PRACTICE (2nd bullet), and ensure correct line format (4th bullet)\n")],
        [sg.Text("•  InventoryMemory.txt follows a strict format. Each item the user wants a total count for\n"
                 "   must have a line with three entries separated by commas:\n"
                 "         - name(no commas), batch size, batch mass(oz)\n\n"
                 "   the name cannot have any commas in it because commas are used by the program to\n"
                 "   separate individual entries (i.e., CSV file).",
                 pad=((5, 1), (1, 20)))],
    ]

    # layout of column 2
    layout_column2 = [
        [sg.Text("InventoryData.txt File",
                 font=("Arial", 14, "underline"), pad=((1, 420), (0, 1)))],
        [sg.Text("•  This is the file the user will be consistently interacting with. Data will be recorded here\n"
                 "   each time an inventory count is performed. The contents can include:\n"
                 "         - item name\n"
                 "         - total mass\n"
                 "         - count value\n\n"
                 "   the item name is required so it can be matched to an InventoryMemory.txt line. However,\n"
                 "   total mass and count value are optional entries. Both can be input, one or the other, or\n"
                 "   neither of them. In the case of neither, InventoryResult.txt will show a 0 next to the item\n"
                 "   name.")],
        [sg.Text("•  The data in this file is gathered and recorded by the user. If a total mass is being recorded,\n"
                 "   the recommended regimen to follow is:\n"
                 "         1. Measure the total mass in OUNCES (oz) of product on a STABLE SURFACE\n"
                 "                    - recommended stable surface is the ground\n"
                 "         2. Record total mass next to name\n")],
        [sg.Text("•  For adding new items: first look at what should be done in the InventoryMemory.txt file,\n"
                 "   then start a new line with the item name and record any total mass or count value\n")],
        [sg.Text("•  InventoryData.txt has a more versatile format. Each line can have either 1, 2, or 3 entries\n"
                 "   separated by commas:\n"
                 "         - If 1 entry:       name(no commas)\n"
                 "         - If 2 entries:    name(no commas), total mass\n"
                 "         - If 3 entries:    name(no commas), total mass, count value\n\n"
                 "   Furthermore, the total mass and count value entries support addition operations. This is\n"
                 "   helpful in cases where not all of the items to be measured fit on the scale at once or when\n"
                 "   multiple cases with a known count need to be added to the total count. The program will\n"
                 "   automatically calculate the sum for the user. For examples, see How It Works →\n"
                 "   MORE INFO.",
                 pad=((5, 1), (1, 50)))],
    ]

    layout = [
        [layout_top],
        [sg.Column(layout_column1, scrollable=True, vertical_scroll_only=True), sg.VerticalSeparator(), sg.Column(layout_column2, scrollable=True, vertical_scroll_only=True)],
        [sg.Button("Close", size=(10, 1), pad=((10, 1),(20, 5)))]
    ]

    # window object
    window3 = sg.Window("More Information - Input Files", layout, size=(1200, 560),
                        location=(45, 25), finalize=True, resizable=True)

    return window3


def check_inputs(values, generate_type):
    """
    function that checks if each of the required fields has been input or selected before executing
    the generation of the files. Specifically, it checks that a folder has been chosen as a location
    for the newly generated files and that it exists. Also checks if a file type (template or prefilled)
    has been selected. If any of these are invalid, will send popup

    :param values: inputs in the active window (dict)
    :param generate_type: button selection in the active window (str)
    :return: boolean
    """
    # two fields to check
    folder_path = values["-STORE_FOLDER-"]
    file_type = generate_type

    # both fields are missing input
    if folder_path == "" and file_type == "":
        sg.popup("No location selected to store new files and no file type selected\n\n ",
                 title="Invalid Fields")
        return False

    # folder to store generated files is missing
    elif folder_path == "":
        sg.popup("No location selected to store new files\n\n",
                 title="Invalid Fields")
        return False

    # folder to store generated files does not exist
    elif not Path(folder_path).exists():
        sg.popup("location selected to store new files does not exist\n\n",
                 title="Invalid Fields")
        return False

    # type of files to be generated is missing
    elif file_type == "":
        sg.popup("No file type selected\n\n",
                 title="Invalid Fields")
        return False

    return True


def create_inventory_memory(path_to_folder, generate_type):
    """
    function that will generate the InventoryMemory.txt file for the user. Will be stored in the
    folder input by user and will either be a template (contains comment instructions) or prefilled
    with data based on the users selection

    :param path_to_folder: folder chosen to store the newly generated file (str)
    :param generate_type: template or prefilled file (str)
    :return: None
    """
    # file path
    complete_path = Path(path_to_folder) / "InventoryMemory.txt"

    # template string
    content_template = ("###########################################\n"
                        "#\n"
                        "# NOTE:\n"
                        "# lines that begin with '#' are comments and ignored by the program\n"
                        "#\n"
                        "# ----------------------------------------------------------------------------------\n"
                        "#\n"
                        "# WHAT IS THIS?:\n"
                        "# InventoryMemory.txt is rarely interacted with by the user. It stores data that is constant to every execution of the calculator. This includes:\n"
                        "#    -> item name\n"
                        "#    -> the batch size or number of units measured together\n"
                        "#    -> the batch mass\n"
                        "#\n"
                        "# ----------------------------------------------------------------------------------\n"
                        "#\n"
                        "# BEST PRACTICE:\n"
                        "# on a STABLE surface, measure mass of 20 units of product in GRAMS(g) (better sensitivity). Convert grams results to ounces(oz) and record\n"
                        "#\n"
                        "# ----------------------------------------------------------------------------------\n"
                        "#\n"
                        "# IMPORTANT:\n"
                        "# this file should only be modified if a product changes or a new product needs to be added.\n"
                        "# 	 -> in the case of a product change: follow BEST PRACTICE and update the mass for that product.\n"
                        "# 	 -> in the case of a new product: make a new line then follow FILE FORMAT FOR EVERY LINE and BEST PRACTICE\n"
                        "#\n"
                        "# ----------------------------------------------------------------------------------\n"
                        "#\n"
                        "# FILE FORMAT FOR EVERY LINE:\n"
                        "# name(no commas), batch size, batch mass(oz)\n"
                        "#\n"
                        "########################################### - line 31\n"
                        "\n"
                        "\n")

    # prefilled string
    content_prefilled = ("###########################################\n"
                         "#\n"
                         "# NOTE:\n"
                         "# lines that begin with '#' are comments and ignored by the program\n"
                         "#\n"
                         "# ----------------------------------------------------------------------------------\n"
                         "#\n"
                         "# WHAT IS THIS?:\n"
                         "# InventoryMemory.txt is rarely interacted with by the user. It stores data that is constant to every execution of the calculator. This includes:\n"
                         "#    -> item name\n"
                         "#    -> the batch size or number of units measured together\n"
                         "#    -> the batch mass\n"
                         "#\n"
                         "# ----------------------------------------------------------------------------------\n"
                         "#\n"
                         "# BEST PRACTICE:\n"
                         "# on a STABLE surface, measure mass of 20 units of product in GRAMS(g) (better sensitivity). Convert grams results to ounces(oz) and record\n"
                         "#\n"
                         "# ----------------------------------------------------------------------------------\n"
                         "#\n"
                         "# IMPORTANT:\n"
                         "# this file should only be modified if a product changes or a new product needs to be added.\n"
                         "# 	 -> in the case of a product change: follow BEST PRACTICE and update the mass for that product.\n"
                         "# 	 -> in the case of a new product: make a new line then follow FILE FORMAT FOR EVERY LINE and BEST PRACTICE\n"
                         "#\n"
                         "# ----------------------------------------------------------------------------------\n"
                         "#\n"
                         "# FILE FORMAT FOR EVERY LINE:\n"
                         "# name(no commas), batch size, batch mass(oz)\n"
                         "#\n"
                         "########################################### - line 31\n"
                         "\n"
                         "\n"
                         "Bag Sub, 20, 9.13596\n"
                         "Large Sub Wrap, 20, 6.9137\n"
                         "Small Sub Wrap, 20, 2.99829\n"
                         "Tray Cinna Pizza Bowl, 20, 23.3161\n"
                         "Lid Cinna, 20, 19.0479\n"
                         "Icing Vanilla Packet, 20, 40.7767\n"
                         "Knife, 20, 3.98596\n"
                         "Fork, 20, 3.70377\n"
                         "Lid Cup 22oz, 20, 1.23459\n"
                         "Squares Small, 20, 6.24349\n"
                         "Souffle Lid, 20, 0.970034\n"
                         "Souffle Cup, 20, 1.393321\n"
                         "Salad Lid Small 32oz, 20, 14.2507\n" 
                         "Salad Lid Large 64oz, 20, 19.8592\n"
                         "Salad Bowl Small 32oz, 20, 17.2137\n"
                         "Salad Bowl Large 64oz, 20, 25.5031\n"
                         "Cup Marco's 22oz, 20, 9.94726\n"
                         "Bag Flat Bottom, 20, 9.0477712\n"
                         "\n")

    if generate_type == "-TEMPLATES-":
        with open(complete_path, "w") as inventoryMemoryFile:
            inventoryMemoryFile.write(content_template)

    else:
        with open(complete_path, "w") as inventoryMemoryFile:
            inventoryMemoryFile.write(content_prefilled)

    inventoryMemoryFile.close()


def create_inventory_data(path_to_folder, generate_type):
    """
    function that will generate the InventoryData.txt file for the user. Will be stored in the
    folder input by user and will either be a template (contains comment instructions) or prefilled
    with data based on the users selection

    :param path_to_folder: folder chosen to store the newly generated file (str)
    :param generate_type: template or prefilled file (str)
    :return:
    """
    # file path
    complete_path = Path(path_to_folder) / "InventoryData.txt"

    # template string
    content_template = ("###########################################\n"
                        "#\n"
                        "# NOTE:\n"
                        "# lines that begin with '#' are comments and ignored by the program\n"
                        "#\n"
                        "# ----------------------------------------------------------------------------------\n"
                        "#\n"
                        "# WHAT IS THIS?:\n"
                        "# InventoryData.txt is the main file users interact with. It records the total mass of all units of a product next to the name of that product.\n"
                        "# The data that recorded here is used together with the data in InventoryMemory.txt to calculate the total unit count of a product\n"
                        "#\n"
                        "# ----------------------------------------------------------------------------------\n"
                        "#\n"
                        "# BEST PRACTICE:\n"
                        "# on a STABLE surface, measure total mass in OUNCES(oz) of a product and record next to product name that matches InventoryMemory.txt\n"
                        "#\n"
                        "# ----------------------------------------------------------------------------------\n"
                        "#\n"
                        "# IMPORTANT:\n"
                        "# for adding products: first, look at IMPORTANT in InventoryMemory.txt and then add a new line with the product name here and record its total mass\n"
                        "#\n"
                        "# ----------------------------------------------------------------------------------\n"
                        "#\n"
                        "# FILE FORMAT FOR EVERY LINE:\n"
                        "# name(no commas), total mass of all units(oz)\n"
                        "#\n"
                        "# or\n"
                        "#\n"
                        "# name(no commas), total mass of all units(oz), count value\n"
                        "#\n"
                        "########################################### - line 31\n"
                        "\n"
                        "\n")

    # prefilled string
    content_prefilled = ("###########################################\n"
                         "#\n"
                         "# NOTE:\n"
                         "# lines that begin with '#' are comments and ignored by the program\n"
                         "#\n"
                         "# ----------------------------------------------------------------------------------\n"
                         "#\n"
                         "# WHAT IS THIS?:\n"
                         "# InventoryData.txt is the main file users interact with. It records the total mass of all units of a product next to the name of that product.\n"
                         "# The data that recorded here is used together with the data in InventoryMemory.txt to calculate the total unit count of a product\n"
                         "#\n"
                         "# ----------------------------------------------------------------------------------\n"
                         "#\n"
                         "# BEST PRACTICE:\n"
                         "# on a STABLE surface, measure total mass in OUNCES(oz) of a product and record next to product name that matches InventoryMemory.txt\n"
                         "#\n"
                         "# ----------------------------------------------------------------------------------\n"
                         "#\n"
                         "# IMPORTANT:\n"
                         "# for adding products: first, look at IMPORTANT in InventoryMemory.txt and then add a new line with the product name here and record its total mass\n"
                         "#\n"
                         "# ----------------------------------------------------------------------------------\n"
                         "#\n"
                         "# FILE FORMAT FOR EVERY LINE:\n"
                         "# name(no commas), total mass of all units(oz)\n"
                         "#\n"
                         "# or\n"
                         "#\n"
                         "# name(no commas), total mass of all units(oz), count value\n"
                         "#\n"
                         "########################################### - line 31\n"
                         "\n"
                         "\n"
                         "Bag Sub, \n"
                         "Large Sub Wrap, \n"
                         "Small Sub Wrap, \n"
                         "Tray Cinna Pizza Bowl, \n"
                         "Lid Cinna, \n"
                         "Icing Vanilla Packet, \n"
                         "Knife, \n"
                         "Fork, \n"
                         "Lid Cup 22oz, \n"
                         "Squares Small, \n"
                         "Souffle Lid, \n"
                         "Souffle Cup, \n"
                         "Salad Lid Small 32oz, \n" 
                         "Salad Lid Large 64oz, \n"
                         "Salad Bowl Small 32oz, \n"
                         "Salad Bowl Large 64oz, \n"
                         "Cup Marco's 22oz, \n"
                         "Bag Flat Bottom, \n"
                         "\n")

    if generate_type == "-TEMPLATES-":
        with open(complete_path, "w") as inventoryDataFile:
            inventoryDataFile.write(content_template)

    else:
        with open(complete_path, "w") as inventoryDataFile:
            inventoryDataFile.write(content_prefilled)

    inventoryDataFile.close()


def open_mem_data_files(path_to_folder):
    """
    this function will automatically open InventoryMemory.txt and InventoryData.txt when the user
    moves to the Input Window. However, only if they generated the files and a valid path to the
    files was saved

    :param path_to_folder: path to folder that generated files
    :return: None
    """
    if path_to_folder == "":
        return

    path_to_folder = Path(path_to_folder)

    if platform.system() == "Windows":
        os.startfile(path_to_folder / "InventoryMemory.txt")
        os.startfile(path_to_folder / "InventoryData.txt")
    elif platform.system() == "Darwin":  # macOS
        subprocess.call(["open", path_to_folder / "InventoryMemory.txt"])
        subprocess.call(["open", path_to_folder / "InventoryData.txt"])
    else:  # Linux
        subprocess.call(["xdg-open", path_to_folder / "InventoryMemory.txt"])
        subprocess.call(["xdg-open", path_to_folder / "InventoryData.txt"])


def welcome_gui():
    """
    function that creates the introduction graphical user interface (GUI) and utilizes all of the above
    functions

    :return: None
    """
    # set the font and text size for entire window, unless specified elsewhere
    font = ("Arial", 16)
    sg.set_options(font=font)

    # theme of window
    sg.theme("Topanga")

    # layout of window
    layout = [
        [sg.Text("Welcome to Marco's Inventory Automator!", font=("Arial", 25, "bold"), size=(100),
                 justification="center", pad=((1, 1), (1, 1)))],
        [sg.Text("Introduction", pad=((10, 10), (1, 1)), font=("Arial", 18, "bold"),
                 border_width=1)],
        [sg.Text(
            "This tool is designed to streamline and simplify the process of managing inventory for Marco's Pizza stores. By leveraging the precision of\n"
            "mass measurements, this application provides an accurate count of select store items, ensuring efficient and reliable inventory management.",
            pad=((10, 10), (5, 7)), border_width=1)],
        [sg.HorizontalSeparator()],
        [sg.Text("How It Works", pad=((10, 10), (7, 1)), font=("Arial", 18, "bold"))],
        [sg.Text(
            "The application reads data from two CSV (comma separated values) files to calculate the exact quantity of items in the store. The first\n"
            "file, InventoryMemory.txt, is rarely accessed by the user. The second file, InventoryData.txt, is regularly modified by the user. The data\n"
            "in these files is used to calculate precise inventory counts, eliminating guesswork and manual counting errors.",
            pad=((10, 10), (5, 5)), border_width=1),
         sg.Button("MORE INFO", key="-MORE_INFO_HOWITWORKS-", font=("Arial", 12))],
        [sg.HorizontalSeparator()],
        [sg.Text("Key Features", pad=((10, 10), (7, 1)), font=("Arial", 18, "bold"))],
        [sg.Text(
            "•   Accurate Inventory Counting: Automatically calculates the total number of units based on mass measurements",
            pad=((25, 1), (1, 1)))],
        [sg.Text(
            "•   User-Friendly Interface: Easy-to-navigate graphical user interface (GUI) that walks the user through using the tool",
            pad=((25, 1), (1, 1)))],
        [sg.Text(
            "•   Efficient and Time-Saving: Reduces time spent on manual counting and minimizes errors",
            pad=((25, 1), (1, 1)))],
        [sg.Text(
            "•   **Automatic File Creation**: If you are using the application for the first time or just want new, clean inventory files, the program\n"
            "    can create and set up the necessary files. These can be generated as blank templates with instructions in the file for manual \n"
            "    entry, or prefilled with the most recently recorded data, ready for modification",
            pad=((25, 10), (1, 7))),
         sg.Button("MORE INFO\nON FILES", key="-MORE_INFO_FILES-", font=("Arial", 12), )],
        [sg.HorizontalSeparator()],
        [sg.Text("Getting Started", pad=((10, 10), (7, 1)), font=("Arial", 18, "bold"))],
        [sg.Text("1.  First Time Users:", pad=((25, 1), (5, 1)))],
        [sg.Text(
            "•   Choose a location on your computer to store the two new files (desktop recommended):",
            pad=((50, 1), (1, 1))), sg.Input(key="-STORE_FOLDER-", size=(28, 1)), sg.FolderBrowse()],
        [sg.Text("•   Choose file type: ", pad=((50, 1), (1, 1))),
         sg.Button("Templates", key="-TEMPLATES-"), sg.Button("Prefilled (recommended)", key="-PREFILLED-")],
        [sg.Text("•   Generate files: ", pad=((50, 1), (1, 1))),
         sg.Button("Generate", key="-GENERATE-")],
        [sg.Text(
            "•   When you move to the Input Window, the input fields will automatically populate based on the location you chose. The two new files\n"
                 "    will also automatically open. If you chose templates, you must manually fill the files before performing the calculation.\n",
            pad=((50, 1), (1, 1)))],
        [sg.Text("2.  Returning Users:", pad=((25, 1), (1, 1)))],
        [sg.Text(
            "•   Skip to the Input Window, provide the two input files, and chose a location to store the results",
            pad=((50, 1), (1, 1)))],
        [sg.Button("Exit", pad=((63, 5), (20, 0)), s=(50, 1)),
         sg.Button("Go to Input Window", pad=((0, 0), (20, 0)), s=(50, 1))],
    ]

    # create the window object, providing a title and passing the layout
    main_window = sg.Window("Marco's Inventory Automator", layout, size=(1085, 750),
                            location=(100, 0), finalize=True)

    # set up windows for multi-window processing
    window1, window2, window3 = main_window, None, None

    # initialize variables to ensure user is not able to open up multiple of the same MORE INFO windows at once
    window2_open = False
    window3_open = False

    # initialize variable to store type of files to be generated
    generate_type = ""

    # initialize variable to store path to folder with generated files
    # initialize variable to store if fill fields on switch to CalculateInventoryGUI
    path_to_folder = ""
    fill = False

    while True:
        window, event, values = sg.read_all_windows()

        # user closes window or selects skip button
        if event == sg.WIN_CLOSED or event == "Exit" or event == "Close":
            window.close()
            if window == window2:
                window2 = None
                window2_open = False
            elif window == window3:
                window3 = None
                window3_open = False
            elif window == window1:
                break

        # window2
        elif event == "-MORE_INFO_HOWITWORKS-":
            if window2_open == False:
                window2 = more_info_howitworks_window()
                window2_open = True
            else:
                sg.popup_non_blocking("Window already open", title="Error", auto_close=True)

        # window3
        elif event == "-MORE_INFO_FILES-":
            if window3_open == False:
                window3 = more_info_files_window()
                window3_open = True
            else:
                sg.popup_non_blocking("Window already open", title="Error", auto_close=True)

        elif event == "-TEMPLATES-":
            # change button color to know which is selected
            window["-TEMPLATES-"].update(button_color=("purple", "aqua"))
            window["-PREFILLED-"].update(button_color=(sg.theme_button_color()[0], sg.theme_button_color()[1]))

            # store type of file to be generated
            generate_type = "-TEMPLATES-"
            continue

        elif event == "-PREFILLED-":
            # change button color to know which is selected
            window["-PREFILLED-"].update(button_color=("purple", "aqua"))
            window["-TEMPLATES-"].update(button_color=(sg.theme_button_color()[0], sg.theme_button_color()[1]))

            # store type of file to be generated
            generate_type = "-PREFILLED-"
            continue

        elif event == "-GENERATE-":
            # call function that makes sure all required options have been selected or input
            all_inputs_valid = check_inputs(values, generate_type)
            if all_inputs_valid == False:
                continue

            # path to folder user chooses to store the two new files
            path_to_folder = values["-STORE_FOLDER-"]

            # variable to determine if fill fields on CalculateInventoryGUI
            fill = True

            # call to function to create inventory memory
            create_inventory_memory(path_to_folder, generate_type)

            # call to function to create inventory data
            create_inventory_data(path_to_folder, generate_type)

            sg.popup(
                "Done!\n\n"
                "The two new files have been generated and stored in the specified location\n\n"
                "When you move to the Input Window your new files will automatically open\n",
                title="New Files Generated")

        elif event == "Go to Input Window":
            window.close()
            open_mem_data_files(path_to_folder)
            InputGUI.input_gui(path_to_folder, fill)
            break

    window.close()


if __name__ == "__main__":
    welcome_gui()
