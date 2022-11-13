import shutil
import os

origin = "C:/Users/gulima/Desktop/impacta/linguagem"
destination = "C:/Users/gulima/Desktop/impacta/linguagem/desafios"

for root, dirs, files in os.walk(origin):
    for file in files:

        if ".py" in file:

            old_file_path = os.path.join(origin, file)
            new_file_path = os.path.join(destination, file)

            shutil.move(old_file_path, new_file_path)
