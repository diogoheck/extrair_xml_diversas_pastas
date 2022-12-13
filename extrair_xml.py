import os
import shutil
print(os.listdir())
for nome_pasta in os.listdir():
    # se é uma pasta
    if os.path.isdir(nome_pasta):
        pasta = f"{os.getcwd()}\{nome_pasta}\\"
        for nome_arquivo in os.listdir(pasta):
            arquivo_mover = f'{pasta}\{nome_arquivo}'
            shutil.move(arquivo_mover, os.getcwd())
        os.rmdir(pasta)
