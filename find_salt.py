import openpyxl as pxl
from tqdm import tqdm

### ./hashcat -m 0 -a 3 D:\python_prjs\dik3\hashes.txt -O -1 89 ?1?d?d?d?d?d?d?d?d?d?d
### использована данная команда для нахождения номеров с солью


POTFILE_PATH = "D:\\Downloads\\hashcat-6.2.6\\hashcat-6.2.6\\hashcat.potfile"  ###Путь до potfile
OUTPUT_PATH = "D:\\python_prjs\\dik3\\cracked_with_salt.txt"
EXCEL_FILE_PATH = "scoring_data_v.1.3.xlsx"
NUMBERS_FILE_PATH = "numbers.txt"
CRACKED_RESULTS_FILE_PATH = "cracked_results.txt"
CRACKED_WITHOUT_SALT_FILE_PATH = "cracked_without_salt.txt"


def get_column_data(sheet, column_name):
    """Получаем данные из столбца."""
    column_data = []
    for cell in sheet[column_name]:
        if cell.value is not None:
            column_data.append(int(cell.value))
    return column_data


def read_pot_file(potfile_path, output_path):
    """Считываем номера из potfile и переписываем их в папку проекта в формате txt."""
    with open(potfile_path, 'r') as potfile, open(output_path, 'w') as number_file:
        for line in potfile:
            password = line.strip().split(':')[1]
            number_file.write(password + '\n')


def load_known_numbers(file_path):
    """Считывем известные номера в множество."""
    known_numbers = set()
    with open(file_path, 'r') as nums_file:
        for line in nums_file:
            known_numbers.add(int(line))
    return known_numbers


def find_valid_salts(numbers_with_salt, known_nums):
    """Находим соль(или соли) которая может быть использована при кодировании."""
    max_salt = (99999999999 - max(known_nums))//100
    salts_set = set()

    for salt in tqdm(range(0, max_salt + 1), desc="Ищем соль…", ascii=False, ncols=75):
        salt_ok = all((number + salt) in numbers_with_salt for number in known_nums)
        if salt_ok:
            salts_set.add(salt)
            print(f"Added salt: {salt}")

    return salts_set


def main():
    workbook = pxl.load_workbook(EXCEL_FILE_PATH)
    sheet = workbook.active

    known_nums = get_column_data(sheet, "C")

    with open(NUMBERS_FILE_PATH, 'w') as f:
        f.writelines(f"{line}\n" for line in known_nums)

    read_pot_file(POTFILE_PATH, OUTPUT_PATH)

    numbers_with_salt = set()
    with open(CRACKED_RESULTS_FILE_PATH, "r") as res:
        for line in res:
            phone = int(line.strip().split(":")[1])
            numbers_with_salt.add(phone)

    salts_set = find_valid_salts(numbers_with_salt, known_nums)

    if not salts_set:
        print("No salt was found.")
    elif len(salts_set) > 1:
        print("Not enough numbers to find the correct salt.")
    else:
        salt = next(iter(salts_set))
        print("Correct salt was found!: ", salt)

        with open(CRACKED_WITHOUT_SALT_FILE_PATH, "w") as no_salt:
            for line in numbers_with_salt:
                no_salt.write(str(int(line) - salt) + "\n")


if __name__ == "__main__":
    main()
