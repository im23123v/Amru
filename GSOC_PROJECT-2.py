def flames_game(name1, name2):
    # Convert to lowercase and remove spaces
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()

    # Convert names to lists
    list1 = list(name1)
    list2 = list(name2)

    # Remove common characters
    for ch in name1:
        if ch in list2:
            list1.remove(ch)
            list2.remove(ch)

    # Count remaining letters
    count = len(list1) + len(list2)

    # FLAMES logic
    flames = ["F", "L", "A", "M", "E", "S"]
    index = 0

    while len(flames) > 1:
        index = (index + count - 1) % len(flames)
        flames.pop(index)

    # Meaning map
    result_map = {
        "F": "Friends",
        "L": "Love",
        "A": "Affection",
        "M": "Marriage",
        "E": "Enemies",
        "S": "Siblings"
    }

    return flames[0], result_map[flames[0]]


# Test with given names
symbol, meaning = flames_game("ABHINAYA", "VISHWANATH")
print("FLAMES Result:", symbol)
print("Relationship:", meaning)
