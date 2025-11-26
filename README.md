# Password-Lab

Equipo Abbyshaelyn
Programación 1
noviembre 2025
PasswordLab
Sistema de Análisis de Contraseñas
Este proyecto es una herramienta de análisis de seguridad de contraseñas que permite evaluar la fortaleza de contraseñas mediante técnicas de comparación de hashes y diccionarios.

 Características
- Generación de hashes SHA-256 para contraseñas
- Comparación con diccionarios de prueba para detectar contraseñas débiles
- Análisis de fortaleza con recomendaciones de seguridad
- Sistema interactivo con menú de opciones
- Gestión de usuarios y contraseñas
- Estadísticas del sistema
- Generación de reportes de seguridad


Ejecución
Opciones del menú principal
Desglose Detallado del Sistema de Análisis de Contraseñas

OPCIÓN 1: Ejecutar Proceso Completo
Descripción: realiza todo el flujo de trabajo automáticamente en una sola ejecución.
Proceso paso a paso:
1. Creación de archivos base
   - Genera usuarios_hashes.txt con todos los usuarios y sus hashes
   - Crea diccionario_prueba.txt con contraseñas comunes

2. Comparación de hashes
   - Lee ambos archivos generados
   - Calcula hashes de todas las palabras del diccionario
   - Compara con los hashes de usuarios
   - Identifica coincidencias

3. Análisis y reporte
   - Evalúa fortaleza de contraseñas encontradas
   - Genera recomendaciones de seguridad
   - Muestra estadísticas completas
   - Guarda reporte en recomendaciones_seguridad.txt

Casos de uso ideal:
- Primera ejecución del sistema
- Evaluación completa del estado de seguridad
- Demostración del funcionamiento completo


OPCIÓN 2: Comparar Contraseñas (Solo Comparación)
Descripción: ejecuta únicamente la fase de comparación sin recrear archivos.
Funciones principales involucradas:
comparar_hashes_con_diccionario()
python
def comparar_hashes_con_diccionario():
     1. Lectura de archivos existentes
    palabras_diccionario = leer_diccionario_prueba()
    usuarios_hashes = leer_usuarios_hashes()
     2. Cálculo de hashes del diccionario
    hashes_diccionario = {}
    for palabra in palabras_diccionario:
        hash_palabra = calcular_hash(palabra)
        hashes_diccionario[hash_palabra] = palabra
    3. Búsqueda de coincidencias
    coincidencias = []
    for usuario, hash_usuario in usuarios_hashes.items():
        if hash_usuario in hashes_diccionario:
          Contraseña encontrada.

analizar_fortaleza_contrasenas()`
python
def analizar_fortaleza_contrasenas(coincidencias):
    Análisis de cada contraseña encontrada
    for coincidencia in coincidencias:
        contrasena = coincidencia['contrasena']
        
   Verificar longitud
        if len(contrasena) < 8:
             Recomendación: contraseña muy corta
        
  Verificar si es solo numérica
        elif contrasena.isdigit():
             Recomendación: usar combinación de caracteres
Salida típica:
Coincidencias encontradas: 15
Total de usuarios: 70
Porcentaje de éxito: 21.43%
Tiempo total: 0.0456 segundos

CONTRASEÑAS DÉBILES ENCONTRADAS:
• usuario001: 123456 (6 chars) - Problema: contraseña corta
• usuario002: password (8 chars) - Problema: palabra com

Casos de uso ideal:
- Re-evaluación después de agregar nuevas contraseñas
- Pruebas rápidas de seguridad
- Monitoreo continuo


OPCIÓN 3: Crear Archivos Necesarios
Descripción: genera o regenera los archivos base del sistema.
Funciones principales:
guardar_usuarios_hashes()
def guardar_usuarios_hashes(contrasenas):
    with open(usuarios_hashes.txt, w) as archivo:
        for i, contrasena in enumerate(contrasenas):
            usuario = f"usuario{i+1:03d}"  # Formato: usuario001, usuario002...
            hash_contrasena = calcular_hash(contrasena)
            archivo.write(f"{usuario}:{hash_contrasena}\n")
Ejemplo de archivo generado:
usuario001:8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92
usuario002:5e884898da28047151d0e56f8dc6292773603d0d6aabbddadf2903f7b6b166a
crear_diccionario_prueba()
def crear_diccionario_prueba():
    diccionario = [
        "123456", "password", "12345678", "qwerty", "abc123",
        # ... 25 palabras comunes más
    ]
    with open(diccionario_prueba.txt, w) as archivo:
        for palabra in diccionario:
            archivo.write(palabra + "\n")
Casos de uso ideal:
- Configuración inicial del sistema
- Resetear archivos corruptos
- Preparar entorno para demostraciones

OPCIÓN 4: Agregar Contraseñas al Sistema
Descripción: Interfaz interactiva para añadir nuevas contraseñas al sistema.
Flujo de trabajo:
1. Entrada de contras
def agregar_contrasenas():
    nuevas_contrasenas = []
    while True:
        contrasena = input("Ingrese la contraseña a agregar: ").strip()
        if contrasena:
            nuevas_contrasenas.append(contrasena)
2. Opción de agregar al diccionario
python
agregar_al_diccionario = input(
    "¿Desea agregar esta contraseña al diccionario de prueba también? (s/n): "
).strip().lower()
if agregar_al_diccionario == 's':
    with open("diccionario_prueba.txt", "a") as archivo:
        archivo.write(contrasena + "\n")
3. Actualización del sistema
Agregar a la lista global
contrasenas.extend(nuevas_contrasenas)
Regenerar archivo de usuarios con nuevas contraseñas
guardar_usuarios_hashes(contrasenas)
Características:
- Validación: No permite contraseñas vacías
- Flexibilidad: Decide si agregar al diccionario de prueba
- Persistencia: Actualiza automáticamente todos los archivos
- Feedback: Muestra confirmaciones y estadísticas actualizadas
Casos de uso ideal:
- Expansión del conjunto de prueba
- Simulación de nuevos usuarios
- Pruebas con contraseñas específicas

OPCIÓN 5: Mostrar Estadísticas del Sistema
Descripción: proporciona una visión general del estado actual del sistema.
Métricas mostradas:
mostrar_estadisticas
def mostrar_estadisticas():
    usuarios_hashes = leer_usuarios_hashes()
    palabras_diccionario = leer_diccionario_prueba() 
    print(f"Total de usuarios en el sistema: {len(usuarios_hashes)}")
    print(f"Total de palabras en el diccionario: {len(palabras_diccionario)}")
    print(f"Contraseñas predefinidas: {len(contrasenas)}")
    
   Análisis de calidad
    contrasenas_cortas = sum(1 for p in palabras_diccionario if len(p) < 8)
    print(f"Contraseñas cortas (<8 chars) en diccionario: {contrasenas_cortas}")


Ejemplo de salida:
ESTADÍSTICAS DEL SISTEMA:
========================================
Total de usuarios en el sistema: 70
Total de palabras en el diccionario: 25
Contraseñas predefinidas: 70
Contraseñas cortas (<8 chars) en diccionario: 12

Casos de uso ideal:
- Monitoreo del tamaño del sistema
- Planificación de expansión
- Análisis de cobertura del diccionario

OPCIÓN 6: Salir
Descripción: cierra la aplicación de manera controlada.
Funcionamiento:
- Termina el bucle principal del menú
- Muestra mensaje de despedida
- Libera recursos (archivos abiertos)
- Retorna control al sistema operativo

FUNCIONES PRINCIPALES DEL SISTEMA
1. calcular_hash(contrasñas)
def calcular_hash(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()
Propósito: Convertir texto plano a hash SHA-256
Uso: Seguridad, no reversible

2. leer_diccionario_prueba()
def leer_diccionario_prueba(archivo_diccionario="diccionario_prueba.txt"):
    with open(archivo_diccionario, "r") as archivo:
        return [linea.strip() for linea in archivo.readlines()]
Propósito: Cargar palabras del diccionario de prueba

3. leer_usuarios_hashes()
def leer_usuarios_hashes(archivo_usuarios="usuarios_hashes.txt"):
    usuarios_hashes = {}
    with open(archivo_usuarios, "r") as archivo:
        for linea in archivo:
            usuario, hash_valor = linea.strip().split(":")
            usuarios_hashes[usuario] = hash_valor
    return usuarios_hashes
Propósito: Cargar usuarios y sus hashes almacenados

4. main() - Función principal
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ").strip()
        Manejo de todas las opciones del menú
Propósito: Controlar el flujo principal de la aplicación

Flujos de Trabajo Típicos
Para nuevos usuarios:
1. Opción 3 → Crear archivos base
2. Opción 2 → Ejecutar primera comparación
3. Opción 5 → Ver estadísticas
Para pruebas continuas:
1. Opción 4 → Agregar nuevas contraseñas
2. Opción 2 → Ejecutar comparación
3. Revisar recomendaciones generadas
Para demostración:
1. Opción 1 → Proceso completo automático
2. Revisar todos los archivos generados

Este desglose muestra cómo cada opción del menú se integra en un sistema cohesivo para el análisis de seguridad de contraseñas.

Archivos generados
- `usuarios_hashes.txt`: Lista de usuarios con sus hashes SHA-256
- `diccionario_prueba.txt`: Diccionario de contraseñas comunes para pruebas
- `recomendaciones_seguridad.txt`: Reporte con recomendaciones de seguridad

Conjuntos de datos incluidos
Contraseñas simples (débiles)
Incluye contraseñas comunes como "123456", "password", "qwerty", etc.

Contraseñas complejas
Ejemplos de contraseñas más seguras como "Segur0!", "P@ssw0rd!", "Python2024!"

Métricas y estadísticas
El sistema proporciona:
- Tiempo de ejecución de procesos
- Porcentaje de éxito en recuperación
- Número de contraseñas débiles detectadas
- Estadísticas de longitud y complejidad

 Recomendaciones de seguridad
El sistema genera recomendaciones basadas en:
- Longitud mínima: Al menos 8 caracteres
- Complejidad: Combinación de letras, números y símbolos
- Evitar patrones comunes: No usar palabras del diccionario
- Unicidad: No reutilizar contraseñas

Notas importantes
- Las contraseñas se almacenan como hashes, pero el diccionario contiene texto plano

Propósito educativo
Este proyecto está diseñado para:
- Entender cómo funcionan los ataques por diccionario
- Aprender sobre hashing de contraseñas
- Comprender los criterios de contraseñas seguras
- Practicar análisis de seguridad básico


