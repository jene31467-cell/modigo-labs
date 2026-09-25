def find_phone_number(contacts, name):
    return dict(contacts).get(name, 'Not found')

    # TODO: build a dict from `contacts` (list of (name, phone) tuples),
    # then return the phone number for `name`, or "Not found"
print(find_phone_number([('Ada', '0801'), ('Bola', '0802')], 'Ada'))