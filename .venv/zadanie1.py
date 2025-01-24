def shorten():
    """The function takes a caption and returns an acronym of the caption."""
    caption = input("Enter a caption: ")
    acronym = []
    try:
        acronym.append(caption[0]) #adding the first letter of the first word
    except IndexError:
        return "Please enter your caption."

    try:
        space_plus_one_indexes = find_spaces(caption) #using the function to find space indexes + 1
    except IndexError:
        return "Please enter your caption."

    for index in space_plus_one_indexes:
        acronym.append(caption[index]) #adding first letters after spaces

    shortened = "".join(acronym).upper()


    return shortened

def find_spaces(caption):
    """The function finds spaces in the caption and returns the indexes of the characters right after the space."""
    space_plus_one_indexes = []
    for i, character in enumerate(caption):
        if character == " " :
            space_plus_one_indexes.append(i + 1)
    return space_plus_one_indexes


print(shorten())


