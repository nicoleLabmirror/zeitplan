def get_german_day_name(english_day_name):
    german_translation_for_day_name = {
        "Monday": "Montag",
        "Tuesday": "Dienstag",
        "Wednesday": "Mittwoch",
        "Thursday": "Donnerstag",
        "Friday": "Freitag",
        "Saturday": "Samstag",
        "Sunday": "Sonntag"
    }

    german_day_name = german_translation_for_day_name[english_day_name]

    return german_day_name
