import hashlib
import time

# Contraseñas simples (débiles)
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

# Agregar algunas contraseñas más complejas
contrasenas_complejas = [
    "Segur0!", "P@ssw0rd!", "M1Contrasena", "Python2024!", "Codigo123$",
    "A1b2c3d4!", "Qwerty!123", "Winter2024@", "Summer!2024", "Spring#2024",
    "Autumn$2024", "January!1", "February@2", "March#2023", "April$2024",
    "May%2024", "June&2024", "July*2024", "August(24", "September)24",
    "October+24", "November=24", "December_24", "Monday!1", "Tuesday@2",
    "Wednesday#3", "Thursday$4", "Friday%5", "Saturday&6", "Sunday*7"
]

# Combinar todas las contraseñas
contrasenas = contrasenas_simples + contrasenas_complejas

# Función para calcular hash SHA-256
def calcular_hash(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

# Función para guardar usuarios y hashes
def guardar_usuarios_hashes(contrasenas):
    with open("usuarios_hashes.txt", "w") as archivo:
        for i, contrasena in enumerate(contrasenas):
            usuario = f"usuario{i+1:03d}"
            hash_contrasena = calcular_hash(contrasena)
            archivo.write(f"{usuario}:{hash_contrasena}\n")
    print("Archivo 'usuarios_hashes.txt' creado con éxito!")

# Función para crear diccionario de prueba
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

    print("Archivo 'diccionario_prueba.txt' creado con éxito!")

# Función para agregar contraseñas al sistema
def agregar_contrasenas():
    print("\nAGREGAR CONTRASEÑAS AL SISTEMA")
    print("=" * 40)
    
    nuevas_contrasenas = []
    
    while True:
        print("\nOpciones:")
        print("1. Agregar contraseña manualmente")
        print("2. Volver al menú principal")
        
        opcion = input("Seleccione una opción (1-2): ").strip()
        
        if opcion == "1":
            contrasena = input("Ingrese la contraseña a agregar: ").strip()
            if contrasena:
                nuevas_contrasenas.append(contrasena)
                print(f"Contraseña '{contrasena}' agregada exitosamente.")
                
                # Preguntar si quiere agregar al diccionario también
                agregar_al_diccionario = input("¿Desea agregar esta contraseña al diccionario de prueba también? (s/n): ").strip().lower()
                if agregar_al_diccionario == 's':
                    with open("diccionario_prueba.txt", "a") as archivo:
                        archivo.write(contrasena + "\n")
                    print("Contraseña agregada al diccionario de prueba.")
            else:
                print("Error: La contraseña no puede estar vacía.")
                       
        elif opcion == "2":
            break
        else:
            print("Opción no válida. Por favor, seleccione 1 o 2.")
    
    # Agregar las nuevas contraseñas a la lista principal
    if nuevas_contrasenas:
        global contrasenas
        contrasenas.extend(nuevas_contrasenas)
        
        # Actualizar el archivo de usuarios y hashes
        guardar_usuarios_hashes(contrasenas)
        print(f"\nSe agregaron {len(nuevas_contrasenas)} contraseñas al sistema.")
        print(f"Total de contraseñas en el sistema: {len(contrasenas)}")
    
    return nuevas_contrasenas

def leer_diccionario_prueba(archivo_diccionario="diccionario_prueba.txt"):
    try:
        with open(archivo_diccionario, "r") as archivo:
            palabras = [linea.strip() for linea in archivo.readlines()]
        print(f"Se leyeron {len(palabras)} palabras del diccionario de prueba")
        return palabras
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo_diccionario}")
        return []

# Función para leer los usuarios y hashes
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

# Función para analizar fortaleza de contraseñas y generar recomendaciones
def analizar_fortaleza_contrasenas(coincidencias):
    recomendaciones = []
    contrasenas_debiles = []
    
    for coincidencia in coincidencias:
        contrasena = coincidencia['contrasena']
        usuario = coincidencia['usuario']
        
        # Verificar longitud
        if len(contrasena) < 8:
            recomendacion = f"Usuario {usuario}: La contraseña '{contrasena}' es demasiado corta (solo {len(contrasena)} caracteres). Recomendación: Use al menos 8 caracteres."
            recomendaciones.append(recomendacion)
            contrasenas_debiles.append({
                'usuario': usuario,
                'contrasena': contrasena,
                'longitud': len(contrasena),
                'problema': 'contraseña corta'
            })
        
        # Verificar si es solo numérica
        elif contrasena.isdigit():
            recomendacion = f"Usuario {usuario}: La contraseña '{contrasena}' contiene solo números. Recomendación: Combine letras, números y símbolos."
            recomendaciones.append(recomendacion)
            contrasenas_debiles.append({
                'usuario': usuario,
                'contrasena': contrasena,
                'longitud': len(contrasena),
                'problema': 'solo números'
            })
        
        # Verificar si es una palabra común
        elif contrasena.lower() in [p.lower() for p in contrasenas_simples[:20]]:
            recomendacion = f"Usuario {usuario}: La contraseña '{contrasena}' es muy común. Recomendación: Evite palabras comunes del diccionario."
            recomendaciones.append(recomendacion)
            contrasenas_debiles.append({
                'usuario': usuario,
                'contrasena': contrasena,
                'longitud': len(contrasena),
                'problema': 'palabra común'
            })
    
    return recomendaciones, contrasenas_debiles

# Función principal para comparar hashes con medición de tiempo
def comparar_hashes_con_diccionario():
    print("COMPARADOR DE HASHES CON DICCIONARIO DE PRUEBA \n")
    
    # Medir tiempo de inicio
    tiempo_inicio = time.time()
    
    # Leer el diccionario de prueba
    palabras_diccionario = leer_diccionario_prueba()
    if not palabras_diccionario:
        print("No se pudo leer el diccionario de prueba. Saliendo...")
        return [], 0
    
    # Leer usuarios y hashes
    usuarios_hashes = leer_usuarios_hashes()
    if not usuarios_hashes:
        print("No se pudieron leer los usuarios y hashes. Saliendo...")
        return [], 0
    
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
    
    # Medir tiempo de finalización
    tiempo_fin = time.time()
    tiempo_total = tiempo_fin - tiempo_inicio
    
    # Mostrar resultados
    print(f"\nRESULTADOS ")
    print(f"Coincidencias encontradas: {len(coincidencias)}")
    print(f"Total de usuarios en el sistema: {len(usuarios_hashes)}")
    print(f"Porcentaje de éxito: {(len(coincidencias)/len(usuarios_hashes))*100:.2f}%")
    print(f"Tiempo total del proceso: {tiempo_total:.4f} segundos")
    
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
        
        # Analizar fortaleza y mostrar recomendaciones
        print(f"\nANÁLISIS DE FORTALEZA DE CONTRASEÑAS")
        print("=" * 60)
        recomendaciones, contrasenas_debiles = analizar_fortaleza_contrasenas(coincidencias)
        
        if recomendaciones:
            print(f"\nSe encontraron {len(contrasenas_debiles)} contraseñas débiles:")
            print("-" * 60)
            for debil in contrasenas_debiles:
                print(f"Usuario: {debil['usuario']}, Contraseña: '{debil['contrasena']}' ({debil['longitud']} chars) - Problema: {debil['problema']}")
            
            print(f"\nRECOMENDACIONES DE SEGURIDAD:")
            print("-" * 60)
            for recomendacion in recomendaciones:
                print(f"• {recomendacion}")
            
            # Guardar recomendaciones en archivo
            with open("recomendaciones_seguridad.txt", "w") as archivo:
                archivo.write("RECOMENDACIONES DE SEGURIDAD PARA CONTRASEÑAS DÉBILES\n")
                archivo.write("=" * 50 + "\n\n")
                for recomendacion in recomendaciones:
                    archivo.write(recomendacion + "\n")
                archivo.write(f"\nResumen: {len(contrasenas_debiles)} contraseñas necesitan mejorarse.\n")
            print(f"\nRecomendaciones guardadas en 'recomendaciones_seguridad.txt'")
        else:
            print("¡Todas las contraseñas recuperadas cumplen con los criterios básicos de seguridad!")
    else:
        print("\nNo se encontraron coincidencias.")
    
    return coincidencias, tiempo_total

# Función para ejecutar todo el proceso
def ejecutar_proceso_completo():
    print("INICIANDO PROCESO COMPLETO \n")
    
    # Crear archivos necesarios si no existen
    print("1. Creando archivos necesarios...")
    guardar_usuarios_hashes(contrasenas)
    crear_diccionario_prueba()
    
    print("\n2. Realizando comparación de hashes...")
    coincidencias, tiempo = comparar_hashes_con_diccionario()
    
    return coincidencias, tiempo

# Función para mostrar estadísticas del sistema
def mostrar_estadisticas():
    try:
        # Leer usuarios y hashes
        usuarios_hashes = leer_usuarios_hashes()
        palabras_diccionario = leer_diccionario_prueba()
        
        print(f"\nESTADÍSTICAS DEL SISTEMA:")
        print("=" * 40)
        print(f"Total de usuarios en el sistema: {len(usuarios_hashes)}")
        print(f"Total de palabras en el diccionario: {len(palabras_diccionario)}")
        print(f"Contraseñas predefinidas: {len(contrasenas)}")
        
        # Contar contraseñas cortas en el diccionario
        contrasenas_cortas = sum(1 for p in palabras_diccionario if len(p) < 8)
        print(f"Contraseñas cortas (<8 chars) en diccionario: {contrasenas_cortas}")
        
    except Exception as e:
        print(f"Error al leer estadísticas: {e}")

# Función para mostrar el menú principal
def mostrar_menu():
    print("         SISTEMA DE ANÁLISIS DE CONTRASEÑAS")
    print("1. Ejecutar proceso completo")
    print("2. Comparar contraseñas (solo comparación)")
    print("3. Crear archivos necesarios")
    print("4. Agregar contraseñas al sistema")
    print("5. Mostrar estadísticas del sistema")
    print("6. Salir")
    print("=" * 50)

# Función principal con menú interactivo
def main():
    resultados = None
    tiempo_ejecucion = 0
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ").strip()
        
        if opcion == "1":
            print("\nEjecutando proceso completo...")
            resultados, tiempo_ejecucion = ejecutar_proceso_completo()
            
        elif opcion == "2":
            print("\nIniciando comparación de contraseñas...")
            resultados, tiempo_ejecucion = comparar_hashes_con_diccionario()
            
        elif opcion == "3":
            print("\nCreando archivos necesarios...")
            guardar_usuarios_hashes(contrasenas)
            crear_diccionario_prueba()
            print("Archivos creados exitosamente!")
            
        elif opcion == "4":
            agregar_contrasenas()
            
        elif opcion == "5":
            mostrar_estadisticas()
            
        elif opcion == "6":
            print("\n¡Gracias por usar el sistema! ¡Hasta pronto!")
            break
            
        else:
            print("\nOpción no válida. Por favor, seleccione una opción del 1 al 6.")

# Ejecutar el script principal
if __name__ == "__main__":
    main()