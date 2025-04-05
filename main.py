import customtkinter as ct
from tkinter import StringVar, messagebox
from constants import category_ids
import random
from api import show_data

def game():
    import game.main

def start_quiz(selected_category, selected_difficulty):
    quiz_data = show_data(selected_category, selected_difficulty, "multiple", 15)
    if isinstance(quiz_data, str):
        print(quiz_data)
        return
    question_index = 0
    question(quiz_data, question_index)

def question(quiz_data, question_index):
    current_question = quiz_data[question_index]
    question_text = current_question['question']
    correct_answer = current_question['correct_answer']
    wrong_answers = current_question['incorrect_answers']
    for widget in app.winfo_children():
        widget.destroy()
    quiz_frame = ct.CTkFrame(app, corner_radius=15, fg_color="#1e1e1e")
    quiz_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
    quiz_frame.grid_rowconfigure(0, weight=1)
    quiz_frame.grid_columnconfigure(0, weight=1)
    question_label = ct.CTkLabel(quiz_frame, text=question_text, font=("Impact", 24), text_color="white")
    question_label.grid(row=0, column=0, padx=10, pady=20)
    options = [correct_answer] + wrong_answers
    random.shuffle(options)
    option_var = StringVar(value=options[0])
    for i, option in enumerate(options):
        radio_button = ct.CTkRadioButton(quiz_frame, text=option, variable=option_var, value=option, font=("Impact", 18))
        radio_button.grid(row=i+1, column=0, padx=10, pady=10)
    def submit_answer():
        selected_answer = option_var.get()
        if selected_answer == correct_answer:
            show_result_screen("Correct", correct_answer, quiz_data, question_index)
        else:
            show_result_screen("Wrong", correct_answer, quiz_data, question_index)
    submit_button = ct.CTkButton(quiz_frame, text="Submit", font=("Impact", 18, "bold"), width=200, command=submit_answer)
    submit_button.grid(row=5, column=0, pady=20)

def show_result_screen(result, correct_answer, quiz_data, question_index):
    for widget in app.winfo_children():
        widget.destroy()
    result_frame = ct.CTkFrame(app, corner_radius=15, fg_color="#1e1e1e")
    result_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
    result_frame.grid_rowconfigure(0, weight=1)
    result_frame.grid_columnconfigure(0, weight=1)
    result_text = ct.CTkLabel(result_frame, text=result, font=("Impact", 48, "bold"), text_color="white")
    result_text.grid(row=0, column=0, padx=10, pady=50)
    correct_answer_label = ct.CTkLabel(result_frame, text=f"The correct answer is: {correct_answer}", font=("Impact", 24), text_color="white")
    correct_answer_label.grid(row=1, column=0, padx=10, pady=20)
    def continue_button():
        next_question_index = question_index + 1
        if next_question_index < len(quiz_data):
            question(quiz_data, next_question_index)
        else:
            for widget in app.winfo_children():
                widget.destroy()
            end_label = ct.CTkLabel(app, text="Quiz Completed!", font=("Impact", 48, "bold"), text_color="white")
            end_label.pack(pady=50)
            close_button = ct.CTkButton(app, text="Close and Go to Game", font=("Impact", 18, "bold"), width=300, command=game)
            close_button.pack(pady=30)
    continue_button = ct.CTkButton(result_frame, text="Continue", font=("Impact", 18, "bold"), width=200, command=continue_button)
    continue_button.grid(row=2, column=0, pady=30)

app = ct.CTk()
app.title("Quiz App")
app.geometry('1000x700')
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
main_frame = ct.CTkFrame(app, corner_radius=15, fg_color="#1e1e1e")
main_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
main_frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
main_frame.grid_columnconfigure(0, weight=1)
header_frame = ct.CTkFrame(main_frame, fg_color="#2e2e2e", corner_radius=15)
header_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
header_label = ct.CTkLabel(header_frame, text="Quiz App", font=("Impact", 45, "bold"), text_color="white")
header_label.pack(pady=20)
content_frame = ct.CTkFrame(main_frame, fg_color="#2e2e2e", corner_radius=15)
content_frame.grid(row=1, column=0, sticky="nsew", padx=30, pady=30)
content_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
content_frame.grid_columnconfigure(0, weight=1)
options = list(category_ids.keys())
category_var = StringVar(value=options[0])
category_menu = ct.CTkOptionMenu(content_frame, values=options, variable=category_var, width=300, font=("Impact", 20))
category_menu.grid(row=0, column=0, padx=10, pady=30)
difficulty_options = ["Easy", "Medium", "Hard"]
difficulty_var = StringVar(value=difficulty_options[0])
difficulty_menu = ct.CTkOptionMenu(content_frame, values=difficulty_options, variable=difficulty_var, width=300, font=("Impact", 20))
difficulty_menu.grid(row=1, column=0, padx=10, pady=30)
start_button = ct.CTkButton(main_frame, text="Start Quiz", font=("Impact", 18, "bold"), width=300, command=lambda: start_quiz(category_var.get(), difficulty_var.get()))
start_button.grid(row=4, column=0, pady=30)
app.mainloop()
