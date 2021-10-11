import unidecode


def format_string(string):
  # Formats string by removing case and accents
    unicode_string = u'{}'.format(string.lower())
    unaccented_string = unidecode.unidecode(unicode_string)
    clean_string = "".join(unaccented_string.split('.'))
    return clean_string
