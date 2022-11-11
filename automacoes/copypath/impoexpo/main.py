import shutil
import os

# Exemplo de como a pasta na função = move_file() deve ser passada
# windows_way_home = "C:/Users/gulima/Desktop/impacta/automacoes/copypath/exemplo_sinqia"
# destination = "C:/Users/gulima/Desktop/impacta/automacoes/copypath/importacoes"


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
        pass


def main():

    origin_search = "C:/Users/gulima/Desktop/impacta/automacoes/copypath/exemplo_sinqia"
    destination_search = "C:/Users/gulima/Desktop/impacta/automacoes/copypath/importacoes"
    files_for_move_search = ["BVBG.028.02", "BVBG.086.01"]

    for file_for_move in files_for_move_search:
        move_file(file_for_move, origin_search, destination_search)

    origin = "C:/Users/gulima/Desktop/impacta/automacoes/copypath/exemplo_sinqia"
    destination = "C:/Users/gulima/Desktop/impacta/automacoes/copypath/importacoes"
    files_for_move = ["BVBG.043.01", "BVBG.044.01",
                      "BVBG.024.01", "Indic_", "Premio"]
    for file_for_move in files_for_move:
        move_file(file_for_move, origin, destination)


if __name__ == "__main__":
    main()
