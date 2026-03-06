import requests
import re

# Alejandro - Incluyo comentarios de mejora a lo largo del código, comenzando por # SUGGESTION.
# En general, está bastante bien, solamente os comento un tema de estilo a lo largo de todo 
# el código que habéis hecho y también una observación sobre los métodos que estáis usando para
# solo conectar a la API, que veo que son cosas auxiliares para vosotros para dentro de la clase.

class APIClient:
    def __init__(self):
        self.base_url = "https://catfact.ninja/"
    
    def only1Fact(self, maxlenght): # SUGGESTION: En Python se suele ir a snake_case para nombres
        # de funciones / métodos para variables, es decir: def only_one_fact(self, max_length) ...
        # (esto en todo el código)
        try:
            url = f"{self.base_url}fact"
            params = {"max_length":maxlenght}
            response = requests.get(url, params= params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud: {e}")
            return None
        
    def moreThan1Fact(self, factNumber, maxlenght):
        try:
            url = f"{self.base_url}facts"
            params = {"max_length":maxlenght, "limit":factNumber}
            response = requests.get(url, params= params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud: {e}")
            return None
        
    def trollJson(self, json):
        return [elem["fact"].replace("cats", "you").replace(" cat ", " you ").replace("Cats", "You").replace("Cat ", "You ") for elem in json["data"]]
        ###return re.sub("Cats", "People", [elem["fact"] for elem in json["data"]])


        
    
        
    def factCats(self, factNumber = 9999, maxLength = 9999, isTroll = False):
        # SUGGESTION: Viendo que vuestro método principal es este y que es el que se ocupa de
        # "limpiar" o seleccionar los datos desde el json y devolver simplemente las frases 
        # (bien hecho, así debe ser), yo dejaría los métodos only1Fact y moreThan1Fact como métodos
        # privados, ya que son auxiliares para dentro de vuestra clase, ningún cliente debería
        # llamarlos desde fuera si solo queréis proporcionar la utilidad de obtener frases, no necesitan 
        # llamar a esos otros.
        if factNumber == 1:
            json = self.only1Fact(maxLength)
        else:
            json = self.moreThan1Fact(factNumber, maxLength)

        if isTroll:
            return self.trollJson(json)
        else:
            return [elem["fact"] for elem in json["data"]]
    
