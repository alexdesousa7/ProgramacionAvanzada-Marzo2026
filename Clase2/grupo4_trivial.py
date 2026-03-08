import requests, html, random

# Alejandro - Incluyo comentarios a lo largo del código, 
# comenzando por # INTERESTING.

class TriviaClient:
    # INTERESTING: Definición + implementación de la clase. Si solo 
    # hacemos esta class TriviaClient y nada más y ejecutamos, eso no haría nada:
    # simplemente definiría la clase y el script termina.
    # Para que algo suceda, debemos (en el script) crear una instancia de la clase y 
    # usarla vía sus métodos (ver más abajo).

    def __init__(self):
        self.base_url = "https://opentdb.com"

    def __get(self, endpoint: str, params: dict = None):
        # INTERESTING: Método auxiliar (privado) que hace la propia request
        # al endpoint que le digas (parámetro endpoint). También puede
        # También puede recibir params como un diccionario, con los query params
        # a usar en la request.
        response = requests.get(f"{self.base_url}/{endpoint}", params=params)
        response.raise_for_status()
        return response.json() # INTERESTING: Devolvemos ya un diccionario, transformamos
        # la variable de tipo respuesta a un tipo diccionario.

    def get_categories(self):
        data = self.__get("api_category.php") # INTERESTING: Hacemos la request
        # (vía el método auxiliar privado) al endpoint que termina por /api_category.php.
        # Debemos tener en cuenta que en la variable data ya se nos queda un diccionario con los 
        # datos de la respuesta, porque dentro del método __get hacemos esa transformación.
        return data["trivia_categories"] # INTERESTING: El método es get_categories, por lo que 
        # devolvemos solamente la parte de la respuesta que nos habla de las categorías, es decir, la parte
        # trivia_categories dentro del diccionario.

    def get_questions(self, amount: int = 1, category: int = None,
                      difficulty: str = None, question_type: str = "multiple"):
        params = {"amount": amount, "type": question_type}
        # INTERESTING: Construimos el diccionario de parámetros para la request posterior:
        if category:
            params["category"] = category
        if difficulty:
            params["difficulty"] = difficulty
        # Petición, request:
        data = self.__get("api.php", params=params)
        # Sobre params:
        # Si le pasamos en params algo como {"amount": 3, "type": "multiple"}, eso se traducirá en la URL de la request a algo como
        # https://opentdb.com/api.php?amount=3&type=multiple. Esto es equivalente a no pasar params pero
        # gestionar nosotros la creación de la url con los query params (añadiendo la ?, y luego nombre_param=valor_param & ...),
        # pero es más cómodo y limpio usar el parámetro params de requests.get, que se encarga de todo eso por nosotros.
        if data["response_code"] != 0:
            # INTERESTING: Es una mala implementación por parte de SU API,
            # indica los problemas vía un dato dentro del diccionario de respuesta, llamado response_code. 
            # Pero, por tanto, nos adaptamos y comprobamos ese caso para saber si ha habido error
            # o no.
            print("No questions found for the given parameters.")
            return []
        # INTERESTING: Si ha ido todo bien, en data ya tenemos un diccionario con los datos de 
        # la respuesta de la API, y sabemos que hay una clave "results" con los datos de la pregunta.
        return data["results"]

    def show_categories(self):
        # Método para mostrar por pantalla las categorías disponibles.
        categories = self.get_categories() # INTERESTING: Aquí llamamos
        # al método get_categories que hemos hecho anteriormente pero en este caso de forma
        # auxiliar, para obtener las categorías, y luego ya las mostramos por pantalla que es 
        # la finalidad de este método en sí mismo.
        print(f"Available categories ({len(categories)}):")
        for cat in categories:
            print(f"  - {cat['id']}: {cat['name']}")

# INTERESTING: Aquí ya ejecuto el código a modo "script", es decir, instancio
# la clase y uso sus métodos según lo que quiera hacer:
trivia_client = TriviaClient() # INTERESTING: Instanciamos la clase, creamos un objeto de tipo TriviaClient.
# Mostrar categorías por pantalla (simplemente mostrarlas, por dentro está haciendo la llamada a la API para obtener los datos, eso sí):
trivia_client.show_categories() # INTERESTING: Usamos el método show_categories para mostrar por pantalla las categorías disponibles.
# Llamar al método get_questions para obtener preguntas, y luego ya podemos procesarlas como queramos (esto ya fuera de la clase):
questions = trivia_client.get_questions(amount=3, category=9) # INTERESTING: Usamos el método get_questions para obtener 3 preguntas de la categoría 9 (General Knowledge).
# Procesarlas ya como queramos, según el caso de uso:
for q in questions:
    print(f"Question: {q['question']}")
