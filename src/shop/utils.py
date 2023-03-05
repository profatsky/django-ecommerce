def translate(string: str):
    return string.lower().translate(
        str.maketrans(
            "абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
            "abvgdeejzijklmnoprstufhzcss_y_eua"
        ))
