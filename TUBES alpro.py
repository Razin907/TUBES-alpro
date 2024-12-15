import tkinter as tk
from tkinter import messagebox, simpledialog

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Aplikasi Kuis")
        
        self.username = ""
        self.score = 0
        self.questions = []
        self.answers = []

        self.login_frame = tk.Frame(self.master)
        self.login_frame.pack(pady=10)

        self.label = tk.Label(self.login_frame, text="Masukkan Nama:")
        self.label.pack(pady=5)

        self.entry = tk.Entry(self.login_frame)
        self.entry.pack(pady=5)

        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.pack(pady=5)

    def login(self):
        self.username = self.entry.get()
        if self.username:
            self.login_frame.pack_forget()
            self.main_frame()
        else:
            messagebox.showwarning("Warning", "Nama tidak boleh kosong!")

    def main_frame(self):
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack(pady=10)

        self.add_question_button = tk.Button(self.main_frame, text="Tambah Soal", command=self.add_question)
        self.add_question_button.pack(pady=5)

        self.show_score_button = tk.Button(self.main_frame, text="Tampilkan Skor", command=self.show_score)
        self.show_score_button.pack(pady=5)

        self.show_questions_button = tk.Button(self.main_frame, text="Tampilkan Semua Soal", command=self.show_questions)
        self.show_questions_button.pack(pady=5)

        self.edit_question_button = tk.Button(self.main_frame, text="Edit Soal", command=self.edit_question)
        self.edit_question_button.pack(pady=5)

        self.delete_question_button = tk.Button(self.main_frame, text="Hapus Soal", command=self.delete_question)
        self.delete_question_button.pack(pady=5)

    def add_question(self):
        question = simpledialog.askstring("Input", "Masukkan soal:")
        answer = simpledialog.askstring("Input", "Masukkan jawaban:")
        if question and answer:
            self.questions.append(question)
            self.answers.append(answer)
            messagebox.showinfo("Info", "Soal dan jawaban berhasil ditambahkan!")

    def show_score(self):
        messagebox.showinfo("Skor", f"Skor Anda: {self.score}")

    def show_questions(self):
        if self.questions:
            self.display_questions(0)
        else:
            messagebox.showinfo("Soal", "Tidak ada soal yang ditambahkan.")

    def display_questions(self, index):
        if index < len(self.questions):
            user_answer = simpledialog.askstring("Input", self.questions[index])
            if user_answer == self.answers[index]:
                self.score += 1
                messagebox.showinfo("Correct", "Jawaban Anda benar!")
            else:
                messagebox.showinfo("Incorrect", f"Jawaban Anda salah. Jawaban yang benar adalah: {self.answers[index]}")
            self.display_questions(index + 1)  # Rekursif untuk menampilkan soal berikutnya

    def edit_question(self):
        if self.questions:
            index = simpledialog.askinteger("Input", "Masukkan indeks soal yang ingin diedit:")
            if index is not None and 0 <= index < len(self.questions):
                new_question = simpledialog.askstring("Input", "Masukkan soal baru:")
                new_answer = simpledialog.askstring("Input", "Masukkan jawaban baru:")
                if new_question and new_answer:
                    self.questions[index] = new_question
                    self.answers[index] = new_answer
                    messagebox.showinfo("Info", "Soal dan jawaban berhasil diedit!")
            else:
                messagebox.showerror("Error", "Indeks soal tidak valid.")
        else:
            messagebox.showinfo("Soal", "Tidak ada soal yang ditambahkan.")

    def delete_question(self):
        if self.questions:
            index = simpledialog.askinteger("Input", "Masukkan indeks soal yang ingin dihapus:")
            if index is not None and 0 <= index < len(self.questions):
                self.questions.pop(index)
                self.answers.pop(index)
                messagebox.showinfo("Info", "Soal dan jawaban berhasil dihapus!")
            else:
                messagebox.showerror("Error", "Indeks soal tidak valid.")
        else:
            messagebox.showinfo("Soal", "Tidak ada soal yang ditambahkan.")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
