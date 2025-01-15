import sys

# Get the command-line arguments (excluding the script name)
arguments = sys.argv[1:]

if arguments:
    print("Command-line arguments:")
    for index, arg in enumerate(arguments, start=1):
        print(f"{index}: {arg}")
else:
    print("No command-line arguments provided.")
