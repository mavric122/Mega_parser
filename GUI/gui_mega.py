from tkinter import ttk, BOTH
import tkinter as tk

def mega_frame(frame):
    # добавляем виджеты на вкладку "Мегамаркет"
    label_megamarket = tk.Label(frame, text="Поиск по имени")
    label_megamarket.pack(pady=10)
    button_megamarket = tk.Button(frame, text="Поиск")
    button_megamarket.pack(pady=10)
