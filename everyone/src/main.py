import sys
from utils.greetings import greetings

def main():
    # Determine output destination
    if len(sys.argv) > 1:
        output_file = sys.argv[1]
        with open(output_file, "w") as file:
            for i, greeting in enumerate(greetings, start=1):
                file.write(f"{i}. \"{greeting}\"\n")
        print(f"The list of 'Hello World!' variants has been written to {output_file}.")
    else:
        for i, greeting in enumerate(greetings, start=1):
            print(f"{i}. \"{greeting}\"")
        print("\nMy way of saying Hello!")

if __name__ == "__main__":
    main()

