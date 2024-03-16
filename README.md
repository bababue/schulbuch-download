# Schulbuch-Downloader

Mit diesem Programm können digitale Schulbücher diverser Verlage in PDFs umgewandelt werden

## Unterstützte Seiten

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

Wähle als ersten Schritt deinen Anbieter aus, gib deine Email, deinen Benutzernamen, deine BookId und die letzt Seite des Buches an, und den Rest sollte das Programm erledigen.

Die BookId ist dabei von Anbieter zu Anbieter unterschiedlich formatiert

Westermann: https://bibox2.westermann.de/book/374/page/1 >> BookId ist 374

Merkur Medien: Als erstes Rechtsklick auf Buchseite, in neuem Tab öffnen

https://www.merkur-medien.de/dlm/zippo/936/3847/preview/big/280.jpg >> BookId ist 936/3847
