import html, random
from grupo4_trivial import TriviaClient


class SportsTrivial:

    SPORTS_CATEGORY = 21  # ID de la categoría "Sports" en Open Trivia DB

    def __init__(self):
        self.client = TriviaClient()

    def play(self, n: int = 5):
        questions = self.client.get_questions(amount=n, category=self.SPORTS_CATEGORY)
        if not questions:
            print("No se pudieron obtener preguntas. Inténtalo de nuevo.")
            return

        score = 0
        for i, q in enumerate(questions, start=1):
            # Decodificar HTML entities (&amp;, &#039;, etc.)
            question_text = html.unescape(q["question"])
            correct = html.unescape(q["correct_answer"])
            options = [html.unescape(a) for a in q["incorrect_answers"]] + [correct]
            random.shuffle(options)

            print(f"\n--- Pregunta {i}/{len(questions)} ---")
            print(question_text)
            for idx, option in enumerate(options, start=1):
                print(f"  {idx}. {option}")

            answer = input("Tu respuesta (número): ").strip()

            # Validar que la respuesta sea un número válido
            if not answer.isdigit() or not (1 <= int(answer) <= len(options)):
                print(f"Respuesta no válida. La respuesta correcta era: {correct}")
                continue

            chosen = options[int(answer) - 1]
            if chosen == correct:
                print("¡Correcto!")
                score += 1
            else:
                print(f"Incorrecto. La respuesta correcta era: {correct}")

        print(f"\n=== Resultado final: {score}/{len(questions)} ===")


if __name__ == "__main__":
    game = SportsTrivial()
    game.play(5) # Jugamos a responder 5 preguntas de la categoría "Sports". Puedes cambiar el número para jugar con más o menos preguntas.
