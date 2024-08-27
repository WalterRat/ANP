import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import scrolledtext


# Функция для загрузки параметров из файла
def load_parameters_from_file(filename):
    """
    Читает файл и извлекает параметры, разделяя их по пробелам.
    Возвращает список параметров.
    """
    try:
        with open(filename, "r") as file:
            content = file.read()
            parameters = content.split()
            return parameters
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []


# Функция для подключения файла и загрузки параметров
def connect_file():
    """
    Открывает диалоговое окно для выбора файла и загружает параметры.
    Обновляет интерфейс с новыми параметрами.
    """
    filename = filedialog.askopenfilename(
        title="Выберите файл с параметрами",
        filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
    )
    if filename:
        parameters = load_parameters_from_file(filename)
        if parameters:
            update_parameters(parameters)


# Функция для обновления параметров в интерфейсе
def update_parameters(parameters):
    """
    Обновляет интерфейс с новыми параметрами.
    Очищает старые элементы интерфейса и добавляет новые на основе загруженных параметров.
    """
    global param_vars, all_parameters
    all_parameters = parameters

    # Очищаем предыдущие элементы интерфейса
    for widget in param_frame.winfo_children():
        widget.destroy()

    # Обновляем интерфейс новыми параметрами
    param_vars = {}
    num_params = len(all_parameters)
    cols = 2
    rows = (num_params + cols - 1) // cols

    for index, param in enumerate(all_parameters):
        col = index // rows
        row = index % rows
        ttk.Label(param_frame, text=f"{param}:").grid(column=col * 2, row=row, sticky=tk.W, padx=5, pady=5)
        param_var = tk.StringVar()
        param_vars[param] = param_var
        ttk.Entry(param_frame, textvariable=param_var).grid(column=col * 2 + 1, row=row, sticky=tk.EW, padx=5, pady=5)

    # Перепозиционирование кнопок и окна
    generate_button.grid(column=0, row=rows, columnspan=cols * 2, pady=10)
    view_button.grid(column=0, row=rows + 1, columnspan=cols * 2, pady=10)
    result_label.grid(column=0, row=rows + 2, columnspan=cols * 2, pady=5)

    param_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))


# Функция для генерации параметров для auditd
def generate_audit_log():
    """
    Генерирует параметры на основе введённых параметров и записывает её в файл audit_log.txt.
    """
    params = {}
    for param, var in param_vars.items():
        value = var.get()
        if value:
            params[param] = value

    command = " ".join([f"{k}={v}" for k, v in params.items()])
    try:
        with open("audit_log.txt", "a") as log_file:
            log_file.write(command + "\n")
        result_label.config(text="Лог успешно сгенерирован и добавлен в файл")
    except Exception as e:
        result_label.config(text=f"Ошибка: {e}")


# Функция для отображения содержимого audit_log.txt
def view_audit_log():
    """
    Открывает новое окно и отображает содержимое файла audit_log.txt.
    """
    try:
        with open("audit_log.txt", "r") as log_file:
            content = log_file.read()
        log_window = tk.Toplevel(root)
        log_window.title("Просмотр audit_log.txt")
        log_window.iconbitmap("icon.ico")
        text_area = scrolledtext.ScrolledText(log_window, wrap=tk.WORD, width=80, height=20)
        text_area.pack(expand=True, fill=tk.BOTH)
        text_area.insert(tk.END, content)
        text_area.configure(state='disabled')
    except FileNotFoundError:
        result_label.config(text="Файл audit_log.txt не найден")


# Инициализация GUI
root = tk.Tk()
root.title("ANP")
root.iconbitmap("icon.ico")

# Рамка для скролла
canvas = tk.Canvas(root)
canvas.grid(row=0, column=0, sticky="nsew")

scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.grid(row=0, column=1, sticky="ns")

canvas.configure(yscrollcommand=scrollbar.set)

param_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=param_frame, anchor="nw")

# Начальные переменные
param_vars = {}
all_parameters = []

# Кнопка для подключения файла
connect_button = ttk.Button(root, text="Подключить файл с параметрами", command=connect_file)
connect_button.grid(column=0, row=1, columnspan=2, pady=10)

# Кнопка для генерации лога
generate_button = ttk.Button(root, text="Сгенерировать лог", command=generate_audit_log)

# Кнопка для просмотра содержимого audit_log.txt
view_button = ttk.Button(root, text="Просмотреть audit_log.txt", command=view_audit_log)

# Результат выполнения
result_label = ttk.Label(root, text="")
result_label.grid(column=0, row=2, columnspan=2, pady=5)

# Настройки для адаптивности интерфейса
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()
