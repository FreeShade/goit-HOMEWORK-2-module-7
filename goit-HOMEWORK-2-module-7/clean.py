import os
import shutil


def normalize(filename):
    # Словник для транслітерації кириличних символів на латиницю
    translit_dict = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "є": "ie",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "і": "i",
        "ї": "i",
        "й": "i",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ь": "",
        "ю": "iu",
        "я": "ia",
        "А": "A",
        "Б": "B",
        "В": "V",
        "Г": "G",
        "Д": "D",
        "Е": "E",
        "Є": "Ye",
        "Ж": "Zh",
        "З": "Z",
        "И": "I",
        "І": "I",
        "Ї": "Yi",
        "Й": "Y",
        "К": "K",
        "Л": "L",
        "М": "M",
        "Н": "N",
        "О": "O",
        "П": "P",
        "Р": "R",
        "С": "S",
        "Т": "T",
        "У": "U",
        "Ф": "F",
        "Х": "Kh",
        "Ц": "Ts",
        "Ч": "Ch",
        "Ш": "Sh",
        "Щ": "Shch",
        "Ь": "",
        "Ю": "Yu",
        "Я": "Ya",
    }

    normalized = ""
    for char in filename:
        if char.isalpha() and char in translit_dict:
            normalized += translit_dict[char]
        elif char.isalpha() or char.isdigit():
            normalized += char
        else:
            normalized += "_"

    return normalized


def process_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = file.split(".")[-1].upper()
            normalized_filename = normalize(file)

            if file_extension in ["JPEG", "PNG", "JPG", "SVG"]:
                # Зображення
                destination_folder = "images"
            elif file_extension in ["AVI", "MP4", "MOV", "MKV"]:
                # Відео файли
                destination_folder = "video"
            elif file_extension in ["DOC", "DOCX", "TXT", "PDF", "XLSX", "PPTX"]:
                # Документи
                destination_folder = "documents"
            elif file_extension in ["MP3", "OGG", "WAV", "AMR"]:
                # Музика
                destination_folder = "audio"
            elif file_extension in ["ZIP", "GZ", "TAR"]:
                # Архіви
                destination_folder = "archives"
                archive_folder_name = os.path.splitext(normalized_filename)[0]
                destination_folder = os.path.join(
                    destination_folder, archive_folder_name
                )
                os.makedirs(destination_folder, exist_ok=True)
                shutil.unpack_archive(file_path, destination_folder)
                continue
            else:
                # Невідомі розширення
                continue

            destination_path = os.path.join(destination_folder, normalized_filename)
            shutil.move(file_path, destination_path)


def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: python sort.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    process_folder(folder_path)


if __name__ == "__main__":
    main()