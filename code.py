import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("MessageBOX")
window.geometry("500x600")

quiz_data = [
    {"question": "Яка столиця України?", "options": ["Київ", "Львів", "Одеса", "Харків"], "correct_index": 0},
    {"question": "Який колір неба в ясну погоду?", "options": ["Зелений", "Синій", "Червоний", "Жовтий"], "correct_index": 1}
]

current_question_index = [0]
selected_answer_index = [None]

def select_answer(answer_index):
    selected_answer_index[0] = answer_index
    selected_answer_label.config(text="Ваш вибір: " + quiz_data[current_question_index[0]]['options'][answer_index])

def check_answer():
    correct_index = quiz_data[current_question_index[0]]["correct_index"]
    if selected_answer_index[0] is None:
        messagebox.showwarning("Увага", "Будь ласка, оберіть відповідь!")
        return
    if selected_answer_index[0] == correct_index:
        result_label.config(text="Правильно!", fg="green")
    else:
        correct_answer_text = quiz_data[current_question_index[0]]["options"][correct_index]
        result_label.config(text="Неправильно! Правильна відповідь: " + correct_answer_text, fg="red")
    next_button.pack()

def next_question():
    current_question_index[0] += 1
    selected_answer_index[0] = None
    if current_question_index[0] >= len(quiz_data):
        messagebox.showinfo("Тест завершено", "Всі питання пройдено!")
        window.quit()
        return
    question_data = quiz_data[current_question_index[0]]
    question_label.config(text=question_data["question"])
    for i, button in enumerate(option_buttons):
        button.config(text=question_data["options"][i], command=lambda i=i: select_answer(i))
    selected_answer_label.config(text="Ваш вибір: Нічого не вибрано")
    result_label.config(text="")
    next_button.pack_forget()

def add_custom_test():
    question_text = entry_question.get().strip()
    answer_options = [
        entry_ans1.get().strip(),
        entry_ans2.get().strip(),
        entry_ans3.get().strip(),
        entry_ans4.get().strip()
    ]
    try:
        correct_answer_index = int(entry_correct.get().strip()) - 1
    except ValueError:
        correct_answer_index = -1

    if not question_text or not all(answer_options):
        messagebox.showerror("Помилка", "Всі поля повинні бути заповнені!")
        return
    if correct_answer_index not in range(4):
        messagebox.showerror("Помилка", "Правильна відповідь повинна бути від 1 до 4!")
        return

    quiz_data.append({
        "question": question_text,
        "options": answer_options,
        "correct_index": correct_answer_index
    })

    for entry in [entry_question, entry_ans1, entry_ans2, entry_ans3, entry_ans4, entry_correct]:
        entry.delete(0, tk.END)

    messagebox.showinfo("Успіх", "Тест додано!")

question_label = tk.Label(window, text=quiz_data[0]["question"], font=("Arial", 14))
question_label.pack(pady=10)

option_buttons = []
for i in range(4):
    button = tk.Button(window, text=quiz_data[0]["options"][i], command=lambda v=i: select_answer(v))
    button.pack()
    option_buttons.append(button)

selected_answer_label = tk.Label(window, text="Ваш вибір: Нічого не вибрано", font=("Arial", 12))
selected_answer_label.pack()

submit_button = tk.Button(window, text="Відповісти", command=check_answer)
submit_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack()

next_button = tk.Button(window, text="Наступне питання", command=next_question)

tk.Label(window, text="Додати своє питання").pack(pady=5)

tk.Label(window, text="Питання:").pack()
entry_question = tk.Entry(window, width=50)
entry_question.pack()

tk.Label(window, text="Відповідь 1:").pack()
entry_ans1 = tk.Entry(window, width=50)
entry_ans1.pack()

tk.Label(window, text="Відповідь 2:").pack()
entry_ans2 = tk.Entry(window, width=50)
entry_ans2.pack()

tk.Label(window, text="Відповідь 3:").pack()
entry_ans3 = tk.Entry(window, width=50)
entry_ans3.pack()

tk.Label(window, text="Відповідь 4:").pack()
entry_ans4 = tk.Entry(window, width=50)
entry_ans4.pack()

tk.Label(window, text="Правильна відповідь (1-4):").pack()
entry_correct = tk.Entry(window, width=5)
entry_correct.pack()

button_add = tk.Button(window, text="Додати тест", command=add_custom_test)
button_add.pack(pady=5)

window.mainloop()