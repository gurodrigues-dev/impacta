import shutil
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv('environment.env'))


def move_file(name_file: str, origin: str, destination: str):
    try:
        for root, dirs, files in os.walk(origin):
            list = []
            for file in files:

                data = os.path.getatime(f"{root}/{file}")

                if name_file in file:
                    list.append((data, file, root))

        list.sort(reverse=True)

        file = list[0][1]
        old_file_path = os.path.join(list[0][2], file)
        new_file_path = os.path.join(destination, file)

        shutil.copy(old_file_path, new_file_path)

        print(f"Arquivo {file} movido com sucesso!")

        return

    except Exception as err:
        print(err)


def main():

    origin_old = os.getenv('originOld')
    destination_old = os.getenv('destinationOld')
    files_for_move_old = ["BVBG.028.02", "BVBG.086.01"]

    for file_for_move in files_for_move_old:
        move_file(file_for_move, origin_old, destination_old)

    '''

    origin_old_fee = os.getenv('originOldFee')
    destination_old_fee = os.getenv('destinationOldFee')
    files_for_move_old_fee = ["BVBG.043.01", "BVBG.044.01",
                              "BVBG.024.01"]
    for file_for_move in files_for_move_old_fee:
        move_file(files_for_move_old_fee, origin_old_fee, destination_old_fee)

    files_for_move_old_continue = ["Indic_", "Premio"]

    for file_for_move in files_for_move_old_continue:
        move_file(files_for_move_old_continue, origin_old, destination_old)

    '''


if __name__ == "__main__":
    main()
