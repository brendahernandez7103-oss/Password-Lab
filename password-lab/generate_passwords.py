import hashlib

# Contrasenas simples (debiles)
contrasenas_simples = [
        "123456", "password", "12345678", "qwerty", "abc123",
        "password1", "12345", "123456789", "letmein", "welcome",
        "monkey", "dragon", "master", "hello", "freedom",
        "whatever", "qazwsx", "trustno1", "admin", "login",
        "passw0rd", "shadow", "ashley", "sunshine", "princess",
        "michael", "charlie", "jessica", "password123", "123123",
        "football", "baseball", "superman", "iloveyou", "starwars",
        "batman", "test", "pass", "1234", "1234567"
    ]
    
    # Agregar algunas contrasenas mas complejas
contrasenas_complejas = [
        "Segur0!", "P@ssw0rd!", "M1Contrasena", "Python2024!", "Codigo123$",
        "A1b2c3d4!", "Qwerty!123", "Winter2024@", "Summer!2024", "Spring#2024",
        "Autumn$2024", "January!1", "February@2", "March#2023", "April$2024",
        "May%2024", "June&2024", "July*2024", "August(24", "September)24",
        "October+24", "November=24", "December_24", "Monday!1", "Tuesday@2",
        "Wednesday#3", "Thursday$4", "Friday%5", "Saturday&6", "Sunday*7"
    ]
  # Combinar todas las contrasenas
contrasenas = contrasenas_simples + contrasenas_complejas
# Funcion para calcular hash SHA-256
def calcular_hash(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

# Funcion para guardar usuarios y hashes
def guardar_usuarios_hashes(contrasenas):
    with open("usuarios_hashes.txt", "w") as archivo:
        for i, contrasena in enumerate(contrasenas):
            usuario = f"usuario{i+1:03d}"
            hash_contrasena = calcular_hash(contrasena)
            archivo.write(f"{usuario}:{hash_contrasena}\n")
    print("Archivo 'usuarios_hashes.txt' creado con exito!")

# Funcion para crear diccionario de prueba
def crear_diccionario_prueba():
    diccionario = [
        "123456", "password", "12345678", "qwerty", "abc123",
        "password1", "12345", "123456789", "letmein", "welcome",
        "monkey", "dragon", "master", "hello", "freedom",
        "user0", "user1", "user2", "test0", "test1",
        "admin", "login", "passw0rd", "shadow", "sunshine"
    ]
    
    with open("diccionario_prueba.txt", "w") as archivo:
        for palabra in diccionario:
            archivo.write(palabra + "\n")
    print("Archivo 'diccionario_prueba.txt' creado con exito!")