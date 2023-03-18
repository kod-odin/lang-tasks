from razdel import sentenize, tokenize
from os import listdir, remove
from os.path import splitext, join


def generating_valid_characters(lst):
    global valid_characters
    for element in lst:
        for c in element:
            if c == "\n":
                continue
            valid_characters.append(c)


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


if __name__ == "__main__":
    source_path = "source"  # Название папки, из которой происходит чтение текстовых документов
    result_path = "result"  # Название папки, в которую производится вывод итогового результата

    valid_characters = []
    invalid_characters = []

    with open("valid_characters.txt", "r") as vc:
        characters = vc.readlines()
    generating_valid_characters(characters)

    if listdir(result_path):
        for f in listdir(result_path):
            remove(join(result_path, f))

    # Перебор всех документов в директории
    only_files = []
    for f in listdir(source_path):
        if splitext(f)[1] == ".txt":
            only_files.append(f)

    print(only_files)
    with open(join(result_path, "invalid_characters.txt"), "wt") as ic:
        for path in only_files:
            with open(join(source_path, path), "rt") as f:
                lines = f.readlines()

                chunk_lines = chunks(lines, 20000)
                for chunk in chunk_lines:
                    for line in chunk:
                        sentences = sentenize(line)
                        for sent in sentences:
                            tokens = tokenize(sent.text)
                            for token in tokens:
                                for char in token.text:
                                    if char not in valid_characters:
                                        ic.write(f"Symbol: '{char}'; code: '{ord(char)}'; word: '{token.text}'; sentence: '{sent.text}'; file: '{path}'\n")
                                        if char not in invalid_characters:
                                            invalid_characters.append(char)

    with open(join(result_path, "list_of_invalid_characters.txt"), "wt") as f:
        for char in invalid_characters:
            f.write(char + "\n")
