#primer ejercicio del taller 
#funcion que cuenta los menores de edad en una lista de edades
def ejercicio1(lista_edades:[int])->int:
    c=0
    for i in lista_edades:
        if i <18:
            c+=1
    return(c)

# Pruebas de la función anterior
assert ejercicio1([23, 31, 16, 11, 21, 18, 34, 45, 17, 16, 32, 43, 20, 19, 18, 16, 14, 33]) == 6
print("Prueba superada ￿￿")

# Función que cuenta las vocales en una palabra
def ejercicio09(palabra: str) -> int:
  vocales="aeiou"
  return [c for c in palabra if c in vocales]



# Pruebas de la función anterior
assert (ejercicio09("Lorem ipsum dolor sit Amet, consectetur adipiscing elit"))==19
assert (ejercicio09("Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis"))==25
print("Prueba superada ￿￿")

# Función que cuenta los múltiplos
def ejercicio10(numeros: [int]) -> int:
    
  for i in numeros:
    if (numeros % 3 ==0 and numeros % 5 ==0 and numeros % 2 ==0):

 # Pruebas para la función anterior

        assert(ejercicio10([5, 10, 30, 25, 24, 60, 12, 100, 120, 15, 90, 95, 36, 35, 72, 180])) == 5
print("Prueba superada ￿￿")   

# Función que cuenta el número de perros
def ejercicio11(perros: [str]) -> (int, int):
 nombres=("fifi", "mateo")

 return [nombres for nombres in perros if nombres in perros]



  # Prueba de la función anterior
 assert (ejercicio11(["lila", "firulais", "romeo", "fifi", "neron", "milagro", "fifi", "lila", "cariño", "rosa", "fifi", "mateo", "rex"])) ==(3,1)
print("Prueba superada ￿￿")

# Función para contar partidos
def resultados_partidos(partidos:[(int, int)]) -> (int, int, int):
  int=int
  int<int
  int>int

  for i in partidos:
    if resultados_partidos (int=int) and (int<int) and (int>int):




 #prueba de la función anterior
      assert (resultados_partidos([(1, 3), (0, 0), (4, 0), (5, 3), (2, 2), (4, 3), (1, 0), (1, 2), (0, 0), (3, 2), (3, 1), (7, 0), (0, 2), (3, 3),(4, 2), (3, 4)])) == (8, 4, 4)
#print("Prueba superada ￿￿")


