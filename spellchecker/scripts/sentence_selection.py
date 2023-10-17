import re
from razdel import sentenize
from os import listdir, remove
from os.path import splitext, join


#
#
#

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def split_to_files(sent):
    answer = True
    if len(re.findall(r"\w+", sent, re.U)) > 13:
        answer = False
    # Перечень символов, которые не проходят валидацию
    if answer and re.search(r"[\[\]{}()0-9IVXLDMivxldm]", sent, re.U):
        answer = False
    return answer


if __name__ == "__main__":
    source_path = "source"
    result_path = "result"

    # Удаление файлов после предыдущего использования скрипта
    if listdir(result_path):
        for f in listdir(result_path):
            remove(join(result_path, f))

    onlyfiles = []
    for f in listdir(source_path):
        if splitext(f)[1] == ".txt":
            onlyfiles.append(f)

    for path in onlyfiles:
        with open(join(source_path, path), "rt") as f:
            lines = f.readlines()

            chunk_lines = chunks(lines, 20000)
            ind = 0
            for chunck in chunk_lines:
                ind += 1
                more_than_13 = open(join(result_path, f"{path}.more_than_13.{ind}.txt"), "wt")
                with open(join(result_path, f"{path}.{ind}.txt"), "wt") as wf:
                    for line in chunck:
                        sentences = sentenize(line)
                        for sent in sentences:
                            if len(sent.text) == 0:
                                continue
                            if split_to_files(sent.text):
                                wf.write(sent.text + '\n')
                            else:
                                more_than_13.write(sent.text + '\n')
            more_than_13.close()
