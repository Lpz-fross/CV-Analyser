import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print the tool header."""
    print("=" * 60)
    print("       CV & JOB DESCRIPTION ANALYSER")
    print("       Powered by Claude (Anthropic)")
    print("=" * 60)
    print()

def list_txt_files(folder=".", exclude=None):
    """List all .txt files in a folder."""
    if exclude is None:
        exclude = []
    files = [
        f for f in os.listdir(folder)
        if f.endswith(".txt") and f not in exclude
    ]
    files.sort()
    return files

def select_file(files, label):
    """Show a numbered list of files and ask the user to pick one."""
    if not files:
        print(f"No {label} files found.")
        print(f"Add a .txt file to your cv-analyser folder and try again.")
        exit()

    print(f"Available {label} files:")
    for i, filename in enumerate(files, start=1):
        print(f"  {i}. {filename}")
    print()

    while True:
        try:
            choice = input(f"Select your {label} (enter number): ")
            index = int(choice) - 1
            if 0 <= index < len(files):
                selected = files[index]
                print(f"Selected: {selected}\n")
                return selected
            else:
                print(f"Please enter a number between 1 and {len(files)}.")
        except ValueError:
            print("Please enter a number.")

def ask_run_again():
    """Ask the user if they want to run another analysis."""
    print()
    while True:
        choice = input("Run another analysis? (y/n): ").strip().lower()
        if choice in ["y", "yes"]:
            return True
        elif choice in ["n", "no"]:
            return False
        else:
            print("Please enter y or n.")