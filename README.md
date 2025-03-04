# OrganizadorWindows
A free organizer for windows by type


Example:

Antes:
├── foto.jpg
├── video.mp4
├── documento.pdf
├── texto.txt
├── planilha.xlsx
├── arquivo.zip
├── script.py
├── musica.mp3
├── desconhecido.xyz

Depois:
├── Imagens
│   ├── foto.jpg
├── Videos
│   ├── video.mp4
├── PDFs
│   ├── documento.pdf
├── Textos
│   ├── texto.txt
├── Documentos
│   ├── planilha.xlsx
├── Arquivos Compactados
│   ├── arquivo.zip
├── Codigos
│   ├── script.py
├── Audio
│   ├── musica.mp3
├── Diversos
│   ├── desconhecido.xyz


## CMDS ##
# EXEC REAL TIME FOR EDITION: flet organizador_flet.py
# EXEC: python organizador_flet.py

## REQUIREMENTS
Python
Flet
pyinstaller

## Creating a .exe // Will be salved int the dist folder
go to the folder project and execute
# CMD
pyinstaller --onefile --windowed organizador_flet.py
