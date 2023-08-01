import os
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox
from tkinter.ttk import Style
import re
import logging
from colorama import Fore, Style, init

def search_text_in_files(folder, search_words):
    found_files = []
    file_types_to_search = ['.php', '.js', '.html', '.json', '.ini', '.css']

    # Escape special characters in each search word
    search_words_regex = [re.escape(word) for word in search_words]

    # Create a regular expression that will search for all the words
    search_text_regex = re.compile(r"|".join(search_words_regex), re.IGNORECASE)

    # Configure logging system with colors
    init(autoreset=True)  # Initialize colorama
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger('search_log')

    # Traverse all files in the folder and its subfolders
    for current_path, folders, files in os.walk(folder):
        # Exclude certain folders if necessary
        # For example, if you want to exclude the folder 'exclude_folder':
        # if 'exclude_folder' in folders:
        #     folders.remove('exclude_folder')

        for file in files:
            # Check if the file has a valid file extension
            if any(file.endswith(extension) for extension in file_types_to_search):
                full_path = os.path.join(current_path, file)

                try:
                    # Read the content of the file
                    with open(full_path, 'r', encoding='utf-8') as file_content:
                        content = file_content.read().lower()  # Convert content to lowercase
                        
                        # Print the words being searched in the current file
                        logger.info(f"{Fore.RED}Searching words in file: {full_path} - Word: {', '.join(search_words)}")

                        # Search all words in the content using the regular expression
                        results = search_text_regex.finditer(content)
                        for result in results:
                            found_files.append((full_path, result.group()))

                            # Print the result with the found word in yellow
                            colored_result = re.sub(result.group(), f"{Fore.YELLOW}{result.group()}{Fore.WHITE}", result.group())
                            logger.info(f"{Fore.WHITE}{Style.BRIGHT}Text found in file: {full_path} - Found word: {colored_result}")
                except Exception as e:
                    logger.error(f"{Fore.RED}Error while opening the file {full_path}: {e}")

    return found_files

def get_search_words():
    # Get the words to search using a dialog box
    search_words = simpledialog.askstring("Codewords v1.2 by @FreddyDeveloper", "Enter the words you want to search in the code separated by commas:")

    if not search_words:
        messagebox.showwarning("Warning", "No search words were entered.")
        return None

    # Convert the entered words into a list
    search_words = [word.strip() for word in search_words.split(",")]
    return search_words

# Create a Tkinter window for the user to select the search folder
app = tk.Tk()
app.withdraw()  # Hide the main window

# Get the words to search
search_words = get_search_words()

if search_words is None:
    messagebox.showwarning("Warning", "Exiting...")
else:
    # Select the search folder
    selected_folder = filedialog.askdirectory(title="Select a folder to start the search:")

    if not selected_folder:
        messagebox.showwarning("Warning", "No folder has been selected. Exiting...")
    else:
        # Call the function to search for words in the files
        found_files = search_text_in_files(selected_folder, search_words)

        # Print the results with custom colors and formatting
        if found_files:
            print(f"{Fore.GREEN}{Style.BRIGHT}Text found in the following files:")
            for full_path, found_word in found_files:
                print(f"{Fore.GREEN}{Style.BRIGHT}{full_path}")
                print(f"{Fore.YELLOW}{Style.BRIGHT}Found word: {found_word}{Fore.WHITE}")
        else:
            print(f"{Fore.RED}{Style.BRIGHT}Text not found in any file.")
