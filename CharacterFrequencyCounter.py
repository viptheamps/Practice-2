def count_character_frequency(input_string):
    frequency = {}
    for char in input_string:
        if char != ' ':
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return frequency

def print_character_frequency(frequency):
    print("Character frequency:")
    for char, count in frequency.items():
        print(char + ":", count)

# Main program
input_string = input("Enter a string: ")
frequency = count_character_frequency(input_string)
print_character_frequency(frequency)
