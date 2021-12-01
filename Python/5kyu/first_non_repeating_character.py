def first_non_repeating_letter(string):
    # List to store string and use list comprehension
    characters = [i for i in string if string.lower().count(i.lower()) == 1]
    
    # Return the first non repeating character in list
    return characters[0] if len(characters) > 0 else ''