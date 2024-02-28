import tkinter as tk
from tkinter import messagebox
import csv
import time
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
        self.inicio_tiempo = 0
        self.tiempo_transcurrido = 0

        # Elementos de la GUI
        self.label_pregunta = tk.Label(root, text=self.preguntas[self.pregunta_actual])
        self.label_pregunta.pack(pady=20)

        self.entry_respuesta = tk.Entry(root)
        self.entry_respuesta.pack(pady=10)

        self.btn_siguiente = tk.Button(root, text="Siguiente", command=self.verificar_respuesta)
        self.btn_siguiente.pack(pady=10)

        self.btn_reiniciar = tk.Button(root, text="Reiniciar Test", command=self.reiniciar_test)
        self.btn_reiniciar.pack(pady=10)

        self.btn_borrar_puntajes = tk.Button(root, text="Borrar Puntajes", command=self.borrar_puntajes)
        self.btn_borrar_puntajes.pack(pady=10)

        self.label_tiempo = tk.Label(root, text="")
        self.label_tiempo.pack(pady=10)

        self.label_resultados = tk.Label(root, text="")
        self.label_resultados.pack(pady=20)

        self.cronometro()

    def cronometro(self):
        self.inicio_tiempo = time.time()
        self.actualizar_tiempo()

    def actualizar_tiempo(self):
        tiempo_actual = time.time()
        self.tiempo_transcurrido = int(tiempo_actual - self.inicio_tiempo)
        tiempo_formateado = time.strftime("%H:%M:%S", time.gmtime(self.tiempo_transcurrido))
        self.label_tiempo.config(text="Tiempo transcurrido: " + tiempo_formateado)
        self.root.after(1000, self.actualizar_tiempo)

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
            # Se acabaron las preguntas, mostrar la puntuación y resultados
            self.mostrar_resultados()

    def mostrar_resultados(self):
        mensaje = f"¡Test completado!\nTu puntuación es: {self.puntuacion}/{len(self.preguntas)}\nTiempo: {self.tiempo_transcurrido} segundos\n\n"
        mensaje += "Resumen de respuestas:\n"
        for i in range(len(self.preguntas)):
            mensaje += f"{self.preguntas[i]}\n"
            respuesta_usuario = self.entry_respuesta.get().strip().lower()
            respuesta_correcta = self.respuestas[i].lower()
            if respuesta_usuario == respuesta_correcta:
                mensaje += "Respuesta: Correcta\n\n"
            else:
                mensaje += f"Respuesta incorrecta. La respuesta correcta es: {respuesta_correcta}\n\n"

        self.label_resultados.config(text=mensaje)
        self.guardar_puntuacion()
        self.mostrar_puntajes()

    def guardar_puntuacion(self):
        with open('puntajes.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.puntuacion, self.tiempo_transcurrido])

    def mostrar_puntajes(self):
        # Leer puntajes desde el archivo
        puntajes = []
        with open('puntajes.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                puntajes.append([int(row[0]), int(row[1])])

        # Ordenar puntajes de mayor a menor
        puntajes.sort(key=itemgetter(0), reverse=True)

        # Crear mensaje de puntajes
        mensaje = "Puntajes más altos:\n"
        for i, puntaje in enumerate(puntajes[:10], 1):
            mensaje += f"{i}. Puntuación: {puntaje[0]}/{len(self.preguntas)} - Tiempo: {puntaje[1]} segundos\n"

        messagebox.showinfo("Puntajes Altos", mensaje)

    def reiniciar_test(self):
        self.pregunta_actual = 0
        self.puntuacion = 0
        self.inicio_tiempo = time.time()
        self.tiempo_transcurrido = 0
        self.label_pregunta.config(text=self.preguntas[self.pregunta_actual])
        self.entry_respuesta.delete(0, tk.END)

    def borrar_puntajes(self):
        if messagebox.askyesno("Borrar Puntajes", "¿Estás seguro de borrar todos los puntajes?"):
            with open('puntajes.csv', mode='w', newline='') as file:
                pass  # Borrar el contenido del archivo
            messagebox.showinfo("Puntajes Borrados", "Puntajes borrados correctamente.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TestInglesApp(root)
    root.mainloop()
 