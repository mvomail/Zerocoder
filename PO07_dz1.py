import tkinter as tk

def greet():
    # Получаем имя из поля ввода
    name = entry.get()
    # Формируем приветственное сообщение
    greeting = f"Привет, {name}!"
    # Обновляем текст метки для отображения сообщения
    label.config(text=greeting)

# Создаем главное окно приложения
root = tk.Tk()
root.title("Приветствие")

# Создаем поле ввода
entry = tk.Entry(root, width=60)
entry.pack(pady=10)

# Создаем кнопку, которая вызывает функцию greet
button = tk.Button(root, text="Поприветствовать", command=greet)
button.pack(pady=5)

# Создаем метку для отображения приветственного сообщения
label = tk.Label(root, text="", font=("Arial", 14))
label.pack(pady=10)

# Запускаем главный цикл обработки событий
root.mainloop()