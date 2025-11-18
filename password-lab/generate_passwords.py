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

ef leer_diccionario_prueba(archivo_diccionario="diccionario_prueba.txt"):
    try:
        with open(archivo_diccionario, "r") as archivo:
            palabras = [linea.strip() for linea in archivo.readlines()]
        print(f"Se leyeron {len(palabras)} palabras del diccionario de prueba")
        return palabras
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo_diccionario}")
        return []

# Funcion para leer los usuarios y hashes
def leer_usuarios_hashes(archivo_usuarios="usuarios_hashes.txt"):
    try:
        usuarios_hashes = {}
        with open(archivo_usuarios, "r") as archivo:
            for linea in archivo:
                partes = linea.strip().split(":")
                if len(partes) == 2:
                    usuario, hash_valor = partes
                    usuarios_hashes[usuario] = hash_valor
        print(f"Se leyeron {len(usuarios_hashes)} usuarios con sus hashes")
        return usuarios_hashes
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo_usuarios}")
        return {}

# Funcion principal para comparar hashes
def comparar_hashes_con_diccionario():
    print("=== COMPARADOR DE HASHES CON DICCIONARIO DE PRUEBA ===\n")
    
    # Leer el diccionario de prueba
    palabras_diccionario = leer_diccionario_prueba()
    if not palabras_diccionario:
        print("No se pudo leer el diccionario de prueba. Saliendo...")
        return
    
    # Leer usuarios y hashes
    usuarios_hashes = leer_usuarios_hashes()
    if not usuarios_hashes:
        print("No se pudieron leer los usuarios y hashes. Saliendo...")
        return
    
    # Calcular hashes para cada palabra del diccionario
    hashes_diccionario = {}
    for palabra in palabras_diccionario:
        hash_palabra = calcular_hash(palabra)
        hashes_diccionario[hash_palabra] = palabra
    
    print(f"\nSe calcularon hashes para {len(hashes_diccionario)} palabras del diccionario")
    
    # Buscar coincidencias
    coincidencias = []
    for usuario, hash_usuario in usuarios_hashes.items():
        if hash_usuario in hashes_diccionario:
            contrasena_descifrada = hashes_diccionario[hash_usuario]
            coincidencias.append({
                'usuario': usuario,
                'hash': hash_usuario,
                'contrasena': contrasena_descifrada
            })
    
    # Mostrar resultados
    print(f"\n=== RESULTADOS ===")
    print(f"Coincidencias encontradas: {len(coincidencias)}")
    print(f"Total de usuarios en el sistema: {len(usuarios_hashes)}")
    print(f"Porcentaje de éxito: {(len(coincidencias)/len(usuarios_hashes))*100:.2f}%")
    
    if coincidencias:
        print("\nCoincidencias encontradas:")
        print("-" * 80)
        print(f"{'USUARIO':<15} {'CONTRASEÑA':<20} {'HASH':<20}")
        print("-" * 80)
        for coincidencia in coincidencias:
            usuario = coincidencia['usuario']
            contrasena = coincidencia['contrasena']
            hash_valor = coincidencia['hash'][:20] + "..."  # Mostrar solo parte del hash
            print(f"{usuario:<15} {contrasena:<20} {hash_valor:<20}")
    else:
        print("\nNo se encontraron coincidencias.")
    
    return coincidencias

# Funcion para ejecutar todo el proceso
def ejecutar_proceso_completo():
    print("=== INICIANDO PROCESO COMPLETO ===\n")
    
    # Crear archivos necesarios si no existen
    print("1. Creando archivos necesarios...")
    guardar_usuarios_hashes(contrasenas)
    crear_diccionario_prueba()
    
    print("\n2. Realizando comparación de hashes...")
    coincidencias = comparar_hashes_con_diccionario()
    
    return coincidencias

# Ejecutar el script principal
if __name__ == "__main__":
    ejecutar_proceso_completo()
        
#Medir el tiempo o y contar cuántas se recuperaron; presentar recomendaciones para fortalecer contraseñas encontradas
