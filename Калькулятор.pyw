import tkinter as tk
from tkinter import messagebox
import math

# Глобальные переменные
easter_egg_active = False
current_number = 1000
language = "Русский"  # Язык по умолчанию

# Полный словарь переводов для 35 языков
translations = {
    "English": {
        "title": "Engineering Calculator",
        "themes": "Themes",
        "language": "Language",
        "about": "About",
        "author": "Author: walababa",
        "error": "Error",
        "invalid_expression": "Invalid expression: {e}",
        "clear": "Clear",
        "evaluate": "Evaluate",
    },
    "Русский": {
        "title": "Инженерный калькулятор",
        "themes": "Темы",
        "language": "Язык",
        "about": "О программе",
        "author": "Автор: walababa",
        "error": "Ошибка",
        "invalid_expression": "Неверное выражение: {e}",
        "clear": "Очистить",
        "evaluate": "Вычислить",
    },
    "Español": {
        "title": "Calculadora de Ingeniería",
        "themes": "Temas",
        "language": "Idioma",
        "about": "Acerca de",
        "author": "Autor: walababa",
        "error": "Error",
        "invalid_expression": "Expresión inválida: {e}",
        "clear": "Limpiar",
        "evaluate": "Evaluar",
    },
    "Français": {
        "title": "Calculatrice d'ingénieur",
        "themes": "Thèmes",
        "language": "Langue",
        "about": "À propos",
        "author": "Auteur : walababa",
        "error": "Erreur",
        "invalid_expression": "Expression invalide : {e}",
        "clear": "Effacer",
        "evaluate": "Évaluer",
    },
    "Deutsch": {
        "title": "Ingenieurrechner",
        "themes": "Themen",
        "language": "Sprache",
        "about": "Über",
        "author": "Autor: walababa",
        "error": "Fehler",
        "invalid_expression": "Ungültiger Ausdruck: {e}",
        "clear": "Löschen",
        "evaluate": "Auswerten",
    },
    "Italiano": {
        "title": "Calcolatrice Ingegneristica",
        "themes": "Temi",
        "language": "Lingua",
        "about": "Informazioni",
        "author": "Autore: walababa",
        "error": "Errore",
        "invalid_expression": "Espressione non valida: {e}",
        "clear": "Cancella",
        "evaluate": "Valuta",
    },
    "Português": {
        "title": "Calculadora de Engenharia",
        "themes": "Temas",
        "language": "Idioma",
        "about": "Sobre",
        "author": "Autor: walababa",
        "error": "Erro",
        "invalid_expression": "Expressão inválida: {e}",
        "clear": "Limpar",
        "evaluate": "Avaliar",
    },
    "日本語": {
        "title": "工学用計算機",
        "themes": "テーマ",
        "language": "言語",
        "about": "について",
        "author": "作者: walababa",
        "error": "エラー",
        "invalid_expression": "無効な式: {e}",
        "clear": "クリア",
        "evaluate": "評価",
    },
    "한국어": {
        "title": "공학용 계산기",
        "themes": "테마",
        "language": "언어",
        "about": "정보",
        "author": "저자: walababa",
        "error": "오류",
        "invalid_expression": "잘못된 표현식: {e}",
        "clear": "지우기",
        "evaluate": "평가",
    },
    "中文": {
        "title": "工程计算器",
        "themes": "主题",
        "language": "语言",
        "about": "关于",
        "author": "作者: walababa",
        "error": "错误",
        "invalid_expression": "无效表达式: {e}",
        "clear": "清除",
        "evaluate": "计算",
    },
    # Остальные языки остаются в словаре, но не отображаются в меню
}

# Функция для вычисления выражения
def evaluate_expression():
    global easter_egg_active, current_number

    try:
        expression = entry.get()
        if expression == "1000-7":  # Проверка на пасхалку
            easter_egg_active = True
            current_number = 1000  # Сбрасываем начальное значение
            start_easter_egg()
            return

        result = eval(expression, {"__builtins__": None}, {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "asin": math.asin,
            "acos": math.acos,
            "atan": math.atan,
            "sinh": math.sinh,
            "cosh": math.cosh,
            "tanh": math.tanh,
            "log": math.log,
            "log10": math.log10,
            "sqrt": math.sqrt,
            "exp": math.exp,
            "factorial": math.factorial,
            "abs": abs,
            "pow10": lambda x: 10 ** x,
            "pi": math.pi,
            "e": math.e,
            "phi": (1 + math.sqrt(5)) / 2  # Золотое сечение
        })
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror(translations[language]["error"], translations[language]["invalid_expression"].format(e=e))

# Функция для очистки поля ввода
def clear_entry():
    entry.delete(0, tk.END)

# Функция для изменения темы
def change_theme(theme_name):
    theme_colors = {
        "Белая": {"bg": "white", "fg": "black", "btn_bg": "lightgray", "btn_fg": "black"},
        "Чёрная": {"bg": "black", "fg": "white", "btn_bg": "darkgray", "btn_fg": "white"},
        "Серая": {"bg": "gray", "fg": "white", "btn_bg": "dimgray", "btn_fg": "white"},
        "Красная": {"bg": "red", "fg": "white", "btn_bg": "darkred", "btn_fg": "white"},
        "Синяя": {"bg": "blue", "fg": "white", "btn_bg": "navy", "btn_fg": "white"},
        "Зелёная": {"bg": "green", "fg": "white", "btn_bg": "darkgreen", "btn_fg": "white"},
        "Жёлтая": {"bg": "yellow", "fg": "black", "btn_bg": "gold", "btn_fg": "black"},
        "Фиолетовая": {"bg": "purple", "fg": "white", "btn_bg": "indigo", "btn_fg": "white"},
        "Оранжевая": {"bg": "orange", "fg": "black", "btn_bg": "darkorange", "btn_fg": "black"},
        "Розовая": {"bg": "pink", "fg": "black", "btn_bg": "hotpink", "btn_fg": "black"},
        "Голубая": {"bg": "cyan", "fg": "black", "btn_bg": "teal", "btn_fg": "black"},
        "Коричневая": {"bg": "brown", "fg": "white", "btn_bg": "saddlebrown", "btn_fg": "white"}
    }
    
    colors = theme_colors.get(theme_name, theme_colors["Серая"])  # По умолчанию серая тема
    root.configure(bg=colors["bg"])
    entry.configure(bg=colors["bg"], fg=colors["fg"])
    for button in buttons:
        button.configure(bg=colors["btn_bg"], fg=colors["btn_fg"])

# Функция для запуска пасхалки
def start_easter_egg():
    global current_number, easter_egg_active

    if easter_egg_active and current_number > 0:
        # Создаем новое окно с текущим числом
        window = tk.Toplevel(root)
        window.title("")
        window.geometry("200x100")
        window.resizable(False, False)
        label = tk.Label(window, text=str(current_number), font=("Arial", 20))
        label.pack(expand=True)

        # Уменьшаем число на 7
        current_number -= 7

        # Запускаем следующее окно через 100 мс
        root.after(100, start_easter_egg)
    else:
        # Останавливаем пасхалку, если число <= 0
        easter_egg_active = False

# Функция для изменения языка
def change_language(lang):
    global language
    language = lang
    root.title(translations[language]["title"])
    update_menu()

# Функция для обновления меню
def update_menu():
    menu.delete(0, tk.END)
    theme_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label=translations[language]["themes"], menu=theme_menu)

    # Словарь с цветами тем
    theme_colors = {
        "Белая": {"bg": "white", "fg": "black", "btn_bg": "lightgray", "btn_fg": "black"},
        "Чёрная": {"bg": "black", "fg": "white", "btn_bg": "darkgray", "btn_fg": "white"},
        "Серая": {"bg": "gray", "fg": "white", "btn_bg": "dimgray", "btn_fg": "white"},
        "Красная": {"bg": "red", "fg": "white", "btn_bg": "darkred", "btn_fg": "white"},
        "Синяя": {"bg": "blue", "fg": "white", "btn_bg": "navy", "btn_fg": "white"},
        "Зелёная": {"bg": "green", "fg": "white", "btn_bg": "darkgreen", "btn_fg": "white"},
        "Жёлтая": {"bg": "yellow", "fg": "black", "btn_bg": "gold", "btn_fg": "black"},
        "Фиолетовая": {"bg": "purple", "fg": "white", "btn_bg": "indigo", "btn_fg": "white"},
        "Оранжевая": {"bg": "orange", "fg": "black", "btn_bg": "darkorange", "btn_fg": "black"},
        "Розовая": {"bg": "pink", "fg": "black", "btn_bg": "hotpink", "btn_fg": "black"},
        "Голубая": {"bg": "cyan", "fg": "black", "btn_bg": "teal", "btn_fg": "black"},
        "Коричневая": {"bg": "brown", "fg": "white", "btn_bg": "saddlebrown", "btn_fg": "white"}
    }

    # Добавляем цвета в меню вместо названий тем
    for theme_name, colors in theme_colors.items():
        theme_menu.add_command(
            label=colors["bg"],  # Отображаем цвет фона
            background=colors["bg"],  # Цвет фона пункта меню
            foreground=colors["fg"],  # Цвет текста
            command=lambda t=theme_name: change_theme(t)
        )

    language_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label=translations[language]["language"], menu=language_menu)

    # Ограничение списка языков до 10
    languages = [
        "English", "Русский", "Español", "Français", "Deutsch",
        "Italiano", "Português", "日本語", "한국어", "中文"
    ]

    for lang in languages:
        language_menu.add_command(label=lang, command=lambda l=lang: change_language(l))

    menu.add_command(label=translations[language]["about"], command=show_about)

# Функция для отображения информации об авторе
def show_about():
    messagebox.showinfo(translations[language]["about"], translations[language]["author"])

# Создание главного окна
root = tk.Tk()
root.title(translations[language]["title"])
root.geometry("400x600")
root.resizable(False, False)

# Поле ввода
entry = tk.Entry(root, font=("Arial", 20), justify="right", bd=10)
entry.grid(row=0, column=0, columnspan=6, pady=10)

# Кнопки
button_texts = [
    "7", "8", "9", "/", "(", ")",
    "4", "5", "6", "*", "π", "e",
    "1", "2", "3", "-", "φ", "sqrt",
    "0", ".", "=", "+", "C", "log",
    "sin", "cos", "tan", "%", "abs", "pow10",
    "asin", "acos", "atan", "log10", "exp", "!"
]

buttons = []
for i, text in enumerate(button_texts):
    row = i // 6 + 1
    col = i % 6
    if text == "=":
        btn = tk.Button(root, text=text, font=("Arial", 16), command=evaluate_expression)
    elif text == "C":
        btn = tk.Button(root, text=text, font=("Arial", 16), command=clear_entry)
    elif text in ("π", "e", "φ"):
        btn = tk.Button(root, text=text, font=("Arial", 16),
                        command=lambda t=text: entry.insert(tk.END, t))
    elif text == "!":
        btn = tk.Button(root, text=text, font=("Arial", 16),
                        command=lambda: entry.insert(tk.END, "factorial("))
    else:
        btn = tk.Button(root, text=text, font=("Arial", 16),
                        command=lambda t=text: entry.insert(tk.END, t))
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    buttons.append(btn)

# Настройка размеров кнопок
for i in range(8):  # Увеличиваем количество строк из-за дополнительных кнопок
    root.grid_rowconfigure(i, weight=1)
for j in range(6):
    root.grid_columnconfigure(j, weight=1)

# Меню
menu = tk.Menu(root)
root.config(menu=menu)
update_menu()

# Установка серой темы по умолчанию
change_theme("Серая")

# Запуск главного цикла
root.mainloop()
