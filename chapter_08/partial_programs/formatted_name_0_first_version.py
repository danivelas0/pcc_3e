def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"  # what is going to return?
    return full_name.title()


# where to store the returned value?
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
