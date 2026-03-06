# Tenemos que crear una clase para el cliente
# Evaluar la documentacion de la api y evaluar que podemos utilizar en nuestra clase cliente.abs

# Alejandro - Incluyo comentarios de mejora a lo largo del código, comenzando por # SUGGESTION.
# Es solo un punto, y es una recomendación de estilo que, de hecho, es opinable, pero personalmente
# lo vería más elegante como os indico a continuación. En general, está bastante guay lo que
# hicisteis.
import requests

class DogClient:
    def __init__(self):
        self.base_url = "https://dog.ceo/api/breeds/"

    def __get(self, url: str):
        # SUGGESTION: Hubiese quedado más elegante y más útil a largo plazo definir
        # este método como def __get(self, url:str, endpoint:str) y hacer aquí 
        # la concatenación de strings urls + endpoint.
        response = requests.get(url)
        return response.json()
    
    def get_list(self):
        # SUGGESTION: Con el cambio anterior, se llamaría con 
        # self.__get(self.base_url, "list/all")
        return self.__get(self.base_url + "list/all")
        
    def get_random_dogs(self, number_of_dogs: int = 1):
        # SUGGESTION: Con el cambio anterior, se llamaría con 
        # self.__get(self.base_url, f"image/random/{number_of_dogs}") --> Ver funcionamiento
        # de los f-strings en Python.
        return self.__get(self.base_url + "image/random/" + str(number_of_dogs))
    
    def find_breeds_by_letter(self, letter: str):
        breeds = self.get_list()
        return [breed.lower() for breed in breeds["message"] if breed.startswith(letter.lower())]
    
    def find_breeds_with_subbreeds(self):
       breeds = self.get_list()
       return [breed.lower() for breed in breeds["message"] if len(breeds["message"][breed]) > 0] 
       
    def show(self, dogs, show_subbreeds=False):
        print(f'Se han encontrado {len(dogs)} razas:')
        for index, dog in enumerate(dogs):
            print(f" - {index + 1}. {dog}")
            if show_subbreeds:
                for index2, subbreed in enumerate(self.get_list()["message"][dog]):
                    print(f" -- {index + 1}.{index2 + 1}.{subbreed}")

def test_class():
    dog_client = DogClient()
    print(dog_client.get_list())
    print(dog_client.get_random_dogs(4))
    print(dog_client.find_breeds_by_letter("VIZSLA")) #vizsla
    dog_client.show(dog_client.find_breeds_by_letter("A"))
    dog_client.show(dog_client.find_breeds_with_subbreeds(), show_subbreeds=True)

test_class()
