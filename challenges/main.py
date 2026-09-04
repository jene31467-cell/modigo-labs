def remove_duplicates(items):
    new_list = []
    for item in items:
        if item not in new_list:
            new_list.append(item)

    return new_list 

print(remove_duplicates([1,2,2,3,1]))

    # TODO: use a loop to build a new list with duplicates removed, keeping first occurrences