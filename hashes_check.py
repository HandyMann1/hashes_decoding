import openpyxl as pxl
import hashlib
from find_salt import load_known_numbers

NUMBERS_WITHOUT_SALT_PATH = "cracked_without_salt.txt"

unsalted_numbers = load_known_numbers(NUMBERS_WITHOUT_SALT_PATH)
unsalted_numbers = [str(number) for number in unsalted_numbers]

NUM_SALT = 123
LETTER_SALT_1 = "a"
LETTER_SALT_3 = "abo"
LETTER_SALT_5 = "aboba"
COMBINATED_SALT = "a1b"

hashed_numbers_sha1 = []
hashed_numbers_sha256 = []
hashed_numbers_sha512 = []

hashed_numbers_sha1_num_salt = []
hashed_numbers_sha256_num_salt = []
hashed_numbers_sha512_num_salt = []

hashed_numbers_sha1_letter_salt_1 = []
hashed_numbers_sha256_letter_salt_1 = []
hashed_numbers_sha512_letter_salt_1 = []

hashed_numbers_sha1_letter_salt_3 = []
hashed_numbers_sha256_letter_salt_3 = []
hashed_numbers_sha512_letter_salt_3 = []

hashed_numbers_sha1_letter_salt_5 = []
hashed_numbers_sha256_letter_salt_5 = []
hashed_numbers_sha512_letter_salt_5 = []

hashed_numbers_sha1_combined_salt = []
hashed_numbers_sha256_combined_salt = []
hashed_numbers_sha512_combined_salt = []

for number in unsalted_numbers:
    hashed_number_sha1 = hashlib.sha1(number.encode()).hexdigest()
    hashed_numbers_sha1.append(hashed_number_sha1)

    hashed_number_sha256 = hashlib.sha256(number.encode()).hexdigest()
    hashed_numbers_sha256.append(hashed_number_sha256)

    hashed_number_sha512 = hashlib.sha512(number.encode()).hexdigest()
    hashed_numbers_sha512.append(hashed_number_sha512)

for number in unsalted_numbers:
    hashed_number_sha1 = hashlib.sha1((number + str(NUM_SALT)).encode()).hexdigest()
    hashed_numbers_sha1_num_salt.append(hashed_number_sha1)

    hashed_number_sha256 = hashlib.sha256((number + str(NUM_SALT)).encode()).hexdigest()
    hashed_numbers_sha256_num_salt.append(hashed_number_sha256)

    hashed_number_sha512 = hashlib.sha512((number + str(NUM_SALT)).encode()).hexdigest()
    hashed_numbers_sha512_num_salt.append(hashed_number_sha512)

for number in unsalted_numbers:
    hashed_number_sha1 = hashlib.sha1((number + LETTER_SALT_1).encode()).hexdigest()
    hashed_numbers_sha1_letter_salt_1.append(hashed_number_sha1)

    hashed_number_sha256 = hashlib.sha256((number + LETTER_SALT_1).encode()).hexdigest()
    hashed_numbers_sha256_letter_salt_1.append(hashed_number_sha256)

    hashed_number_sha512 = hashlib.sha512((number + LETTER_SALT_1).encode()).hexdigest()
    hashed_numbers_sha512_letter_salt_1.append(hashed_number_sha512)

    hashed_number_sha1 = hashlib.sha1((number + LETTER_SALT_3).encode()).hexdigest()
    hashed_numbers_sha1_letter_salt_3.append(hashed_number_sha1)

    hashed_number_sha256 = hashlib.sha256((number + LETTER_SALT_3).encode()).hexdigest()
    hashed_numbers_sha256_letter_salt_3.append(hashed_number_sha256)

    hashed_number_sha512 = hashlib.sha512((number + LETTER_SALT_3).encode()).hexdigest()
    hashed_numbers_sha512_letter_salt_3.append(hashed_number_sha512)

    hashed_number_sha1 = hashlib.sha1((number + LETTER_SALT_5).encode()).hexdigest()
    hashed_numbers_sha1_letter_salt_5.append(hashed_number_sha1)

    hashed_number_sha256 = hashlib.sha256((number + LETTER_SALT_5).encode()).hexdigest()
    hashed_numbers_sha256_letter_salt_5.append(hashed_number_sha256)

    hashed_number_sha512 = hashlib.sha512((number + LETTER_SALT_5).encode()).hexdigest()
    hashed_numbers_sha512_letter_salt_5.append(hashed_number_sha512)

for number in unsalted_numbers:
    hashed_number_sha1 = hashlib.sha1((number + COMBINATED_SALT).encode()).hexdigest()
    hashed_numbers_sha1_combined_salt.append(hashed_number_sha1)

    hashed_number_sha256 = hashlib.sha256((number + COMBINATED_SALT).encode()).hexdigest()
    hashed_numbers_sha256_combined_salt.append(hashed_number_sha256)

    hashed_number_sha512 = hashlib.sha512((number + COMBINATED_SALT).encode()).hexdigest()
    hashed_numbers_sha512_combined_salt.append(hashed_number_sha512)


def write_to_file(filename, data):
    with open(filename, 'w') as f:
        for item in data:
            f.write(f"{item}\n")

write_to_file("hashed_no_salts_SHA-1.txt", hashed_numbers_sha1)
write_to_file("hashed_no_salts_SHA-256.txt", hashed_numbers_sha256)
write_to_file("hashed_no_salts_SHA-512.txt", hashed_numbers_sha512)

write_to_file("hashed_num_salts_SHA-1.txt", hashed_numbers_sha1_num_salt)
write_to_file("hashed_num_salts_SHA-256.txt", hashed_numbers_sha256_num_salt)
write_to_file("hashed_num_salts_SHA-512.txt", hashed_numbers_sha512_num_salt)

write_to_file("hashed_letter_salts_SHA-1_Letter_Salt_1.txt", hashed_numbers_sha1_letter_salt_1)
write_to_file("hashed_letter_salts_SHA-256_Letter_Salt_1.txt", hashed_numbers_sha256_letter_salt_1)
write_to_file("hashed_letter_salts_SHA-512_Letter_Salt_1.txt", hashed_numbers_sha512_letter_salt_1)

write_to_file("hashed_letter_salts_SHA-1_Letter_Salt_3.txt", hashed_numbers_sha1_letter_salt_3)
write_to_file("hashed_letter_salts_SHA-256_Letter_Salt_3.txt", hashed_numbers_sha256_letter_salt_3)
write_to_file("hashed_letter_salts_SHA-512_Letter_Salt_3.txt", hashed_numbers_sha512_letter_salt_3)

write_to_file("hashed_letter_salts_SHA-1_Letter_Salt_5.txt", hashed_numbers_sha1_letter_salt_5)
write_to_file("hashed_letter_salts_SHA-256_Letter_Salt_5.txt", hashed_numbers_sha256_letter_salt_5)
write_to_file("hashed_letter_salts_SHA-512_Letter_Salt_5.txt", hashed_numbers_sha512_letter_salt_5)

write_to_file("hashed_combined_salts_SHA-1.txt", hashed_numbers_sha1_combined_salt)
write_to_file("hashed_combined_salts_SHA-256.txt", hashed_numbers_sha256_combined_salt)
write_to_file("hashed_combined_salts_SHA-512.txt", hashed_numbers_sha512_combined_salt)
