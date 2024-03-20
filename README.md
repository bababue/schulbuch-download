# Schulbuch-Downloader

Mit diesem Programm können digitale Schulbücher diverser Verlage in PDFs umgewandelt werden

## Unterstützte Verlage

- Westermann Verlag (BiBox2)
- Merkur Verlag Rinteln (Merkur Medien)

## Installation

1.  Das Repository klonen

    ```
    git clone https://github.com/bababue/schulbuch-downlaod.git

    cd ./schulbuch-downlaod
    ```

2.  Dependencies installieren

    ```
    pip3 install -r requirements.txt
    ```

3.  Das Programm starten

    ```
    python3 main.py
    ```

## Benutzung

Wähle zuerst den gewünschten Verlag aus. Gib anschließend deine Email und dein Passwort ein, danach die [BookID](#bookid) und zuletzt die letzte Seitenzahl des Buches.

## BookID

| Verlag        | Beispiel-Url                                                        | entsprechende BookId | Notizen                                                                                   |
| ------------- | ------------------------------------------------------------------- | -------------------- | ----------------------------------------------------------------------------------------- |
| Westermann    | https://bibox2.westermann.de/book/374/page/1                        | 374                  |                                                                                           |
| Merkur Medien | https://www.merkur-medien.de/dlm/zippo/936/3847/preview/big/280.jpg | 936/3847             | Um an die URL zu kommen, erst Rechtsklick auf ein Bild und dies in einem neuen tab öffnen |
|               |                                                                     |                      |                                                                                           |
