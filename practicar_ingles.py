import tkinter as tk
from tkinter import messagebox
import csv
from operator import itemgetter

class TestInglesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Test de Inglés")

        # Preguntas y respuestas
        self.preguntas = [
            "1. What is the capital of France?",
            "2. How many days are there in a leap year?",
            "3. Who wrote 'Romeo and Juliet'?",
            "4. What is the opposite of 'old'?",
            "5. What is the past tense of 'go'?",
            "6. What is the largest planet in our solar system?",
            "7. How many continents are there in the world?",
            "8. What is the chemical symbol for gold?",
            "9. Which country is famous for kangaroos?",
            "10. Who painted the Mona Lisa?",
            "11. What is the largest mammal in the world?",
            "12. How many colors are there in a rainbow?",
            "13. What is the longest river in the world?",
            "14. What is the square root of 144?",
            "15. Who is known as the 'Father of Computers'?",
            "16. What is the currency of Japan?",
            "17. What is the largest ocean on Earth?",
            "18. Which is the world's tallest mountain?",
            "19. What is the main language spoken in Brazil?",
            "20. Who wrote 'Hamlet'?"
        ]

        self.respuestas = [
            "Paris",
            "366",
            "William Shakespeare",
            "young",
            "went",
            "Jupiter",
            "7",
            "Au",
            "Australia",
            "Leonardo da Vinci",
            "Blue whale",
            "7",
            "Nile",
            "12",
            "Charles Babbage",
            "Yen",
            "Pacific Ocean",
            "Mount Everest",
            "Portuguese",
            "William Shakespeare"
        ]

        # Variables para seguimiento
        self.pregunta_actual = 0
        self.puntuacion = 0

        # Elementos de la GUI
        self.label_pregunta = tk.Label(root, text=self.preguntas[self.pregunta_actual])
        self.label_pregunta.pack(pady=20)

        self.entry_respuesta = tk.Entry(root)
        self.entry_respuesta.pack(pady=10)

        self.btn_siguiente = tk.Button(root, text="Siguiente", command=self.verificar_respuesta)
        self.btn_siguiente.pack(pady=10)

    def verificar_respuesta(self):
        respuesta_usuario = self.entry_respuesta.get().strip().lower()
        respuesta_correcta = self.respuestas[self.pregunta_actual].lower()

        if respuesta_usuario == respuesta_correcta:
            self.puntuacion += 1

        self.pregunta_actual += 1

        if self.pregunta_actual < len(self.preguntas):
            # Mostrar la siguiente pregunta
            self.label_pregunta.config(text=self.preguntas[self.pregunta_actual])
            self.entry_respuesta.delete(0, tk.END)
        else:
            # Se acabaron las preguntas, mostrar la puntuación
            self.mostrar_resultados()

    def mostrar_resultados(self):
        mensaje = f"¡Test completado!\nTu puntuación es: {self.puntuacion}/{len(self.preguntas)}"
        messagebox.showinfo("Resultados", mensaje)
        self.guardar_puntuacion()
        self.mostrar_puntajes()

    def guardar_puntuacion(self):
        with open('puntajes.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.puntuacion])

    def mostrar_puntajes(self):
        # Leer puntajes desde el archivo
        puntajes = []
        with open('puntajes.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                puntajes.append(int(row[0]))

        # Ordenar puntajes de mayor a menor
        puntajes.sort(reverse=True)

        # Crear mensaje de puntajes
        mensaje = "Puntajes más altos:\n"
        for i, puntaje in enumerate(puntajes[:10], 1):
            mensaje += f"{i}. {puntaje}/{len(self.preguntas)}\n"

        messagebox.showinfo("Puntajes Altos", mensaje)
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TestInglesApp(root)
    root.mainloop()
