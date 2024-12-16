import argparse
import os
from automation.script_selector import list_available_scripts, select_script

def run_cli():
    parser = argparse.ArgumentParser(description="CLI Interface for AGI Project")
    parser.add_argument("--list", action="store_true", help="List all available scripts")
    parser.add_argument("--select", type=str, help="Select a script by criteria")
    parser.add_argument("--directory", type=str, default="./automation", help="Directory to search for scripts")

    args = parser.parse_args()

    if args.list:
        print("Listing available scripts...")
        scripts = list_available_scripts(args.directory)
        print("Available scripts:", scripts)

    if args.select:
        print(f"Selecting script based on criteria: {args.select}")
        scripts = list_available_scripts(args.directory)
        selected_script = select_script(scripts, args.select)
        if selected_script:
            print("Selected script:", selected_script)
        else:
            print("No script matched the criteria.")

if __name__ == "__main__":
    run_cli()