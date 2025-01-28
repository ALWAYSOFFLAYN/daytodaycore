def generate_list(mode, start, finish, filename="list.txt"):
    try:
        # Open the file for writing
        with open(filename, "w") as file:
            # Mode 'n' for numbers
            if mode == "n":
                start = int(start)
                finish = int(finish)
                for num in range(start, finish + 1):
                    file.write(f"{num}\n")
            # Mode 'l' for letters
            elif mode == "l":
                start = ord(start.lower())
                finish = ord(finish.lower())
                if start > finish:
                    print("Error: Start letter must be earlier in the alphabet than finish letter.")
                    return
                for char in range(start, finish + 1):
                    file.write(f"{chr(char)}\n")
            else:
                print("Error: Invalid mode. Use 'n' for numbers or 'l' for letters.")
                return
        print("Done! (Generated values written to list.txt)")
    except ValueError:
        print("Error: Invalid input. Ensure numbers for 'n' mode or letters for 'l' mode.")

# Input example
if __name__ == "__main__":
    mode = input("Enter mode ('n' for numbers, 'l' for letters): ").strip()
    start = input("Enter start value: ").strip()
    finish = input("Enter finish value: ").strip()
    generate_list(mode, start, finish)
