import tkinter as tk   # Py3
from tkinter import filedialog   # Py3, okna dialogowe
from tkinter import messagebox   # Py3
from tkinter import ttk   # themed widgets
import random

OPCJE = ["kamien", "papier", "nozyce"]

def losowanie(wybrana):
    wylosowana = random.choice(OPCJE)

    if wybrana == wylosowana:
        wynik = "Remis!"
    elif (wybrana == "kamien" and wylosowana == "nozyce") or \
         (wybrana == "papier" and wylosowana == "kamien") or \
         (wybrana == "nozyce" and wylosowana == "papier"):
        wynik = "Wygrałeś!"
    else:
        wynik = "Przegrałeś, spróbuj ponownie"
    
    wybor_uzytkownika_napis.config(text=f"Twój wybór: {wybrana.upper()}")
    wylosowana_napis.config(text=f"Wybór Komputera: {wylosowana.upper()}")
    wynik_napis.config(text=f"Wynik: {wynik}")



root = tk.Tk() # ustawienie głównego okna aplikacji
root.title("Kamień-Papier-Nożyce") # opcjonalny tytuł okna, domyślny tytuł to "tk"

label = ttk.Label(root, text="Wybierz opcję, aby rozpocząć grę:")
label.grid(row=0, column=0, columnspan=3)

kamien = tk.Button(root,
    text="KAMIEŃ",
    width=15,
    height=3,
    bg="blue",
    fg="yellow",
    command=lambda: losowanie("kamien"), 
)
kamien.grid(row=1, column=0)

papier = tk.Button(root,
    text="PAPIER",
    width=15,
    height=3,
    bg="blue",
    fg="yellow",
    command=lambda: losowanie("papier"), 
)
papier.grid(row=1, column=1)

nozyce = tk.Button(root,
    text="NOŻYCE",
    width=15,
    height=3,
    bg="blue",
    fg="yellow",
    command=lambda: losowanie("nozyce"), 
)
nozyce.grid(row=1, column=2)

wybor_uzytkownika_napis = ttk.Label(root, text="Twój wybór: ---")
wybor_uzytkownika_napis.grid(row=2, column=0, columnspan=3)

wylosowana_napis = ttk.Label(root, text="Wybór Komputera: ---")
wylosowana_napis.grid(row=3, column=0, columnspan=3)

wynik_napis = ttk.Label(root, text="Wynik: Czekam na Twój ruch...")
wynik_napis.grid(row=4, column=0, columnspan=3)

root.mainloop()