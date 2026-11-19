from datos import generarRegistros, ordenarPorFrecuencia, ingresarRegistroManual
from archivos import exportarArchivos, importarJson, registrarLog
from base import (
    subirRegistrosMongo,
    consultarPromedioFc,
    consultarSpo2Bajo,
    buscarPorIdMongo,
    exportarResultadosMongo
)

listaRegistros = []
ejecutando = "si"
registrarLog("Inicio de ejecucion del programa.")

while ejecutando == "si":
    print("""
==========================================
   GESTION DE DATOS BIOMEDICOS - TALLER 3
==========================================
1. Generar 50 registros aleatorios
2. Ingresar registro manualmente
3. Mostrar registros actuales
4. Ordenar registros por frecuencia cardiaca (FC)
5. Exportar archivos (TXT, CSV y JSON)
6. Importar registros desde JSON
7. Subir registros a MongoDB Atlas
8. Consultar promedio de FC en MongoDB
9. Consultar registros con SpO2 menor a 94
10. Buscar registro por ID en MongoDB
11. Exportar consultas de MongoDB a JSON
0. Salir""")
    opcion = input("Seleccione una opcion: ").strip()
    if opcion == "1":
        listaRegistros = generarRegistros(50)
        registrarLog(f"Se generaron {len(listaRegistros)} registros aleatorios.")
        print(f"Se generaron {len(listaRegistros)} registros validos correctamente.")
    elif opcion == "2":
        nuevoRegistro = ingresarRegistroManual()
        if nuevoRegistro != None:
            listaRegistros.append(nuevoRegistro)
            registrarLog(f"Se agrego manualmente el registro {nuevoRegistro['id']}.")
            print("Registro agregado correctamente.")
    elif opcion == "3":
        if len(listaRegistros) == 0:
            print("No hay registros cargados en memoria.")
        else:
            print()
            print(f"--- LISTADO DE REGISTROS ({len(listaRegistros)}) ---")
            for item in listaRegistros:
                print(f"ID: {item['id']} | FR: {item['fr']} | FC: {item['fc']} | SpO2: {item['spo2']}")
    elif opcion == "4":
        if len(listaRegistros) == 0:
            print("No hay registros para ordenar.")
        else:
            listaRegistros = ordenarPorFrecuencia(listaRegistros)
            registrarLog("Registros ordenados por frecuencia cardiaca.")
            print("Registros ordenados por frecuencia cardiaca de menor a mayor.")
    elif opcion == "5":
        exportarArchivos(listaRegistros)
    elif opcion == "6":
        datosImportados = importarJson()
        if len(datosImportados) > 0:
            listaRegistros = datosImportados
    elif opcion == "7":
        subirRegistrosMongo(listaRegistros)
    elif opcion == "8":
        promedio = consultarPromedioFc()
        if promedio > 0:
            print(f"El promedio de frecuencia cardiaca en MongoDB es: {promedio} ppm")
    elif opcion == "9":
        bajos = consultarSpo2Bajo()
        print(f"Registros con SpO2 menor a 94%: {len(bajos)}")
        if len(bajos) == 0:
            print("No hay registros con SpO2 menor a 94%.")
        else:
            print()
            print(f"--- REGISTROS CON SPO2 MENOR A 94% ({len(bajos)}) ---")
            for item in bajos:
                print(f"ID: {item['id']} | FR: {item['fr']} | FC: {item['fc']} | SpO2: {item['spo2']}")
    elif opcion == "10":
        idBuscar = input("Ingrese el ID del paciente a buscar (ej. ID-001): ").strip()
        encontrado = buscarPorIdMongo(idBuscar)
        if encontrado != None:
            print(f"Registro encontrado -> ID: {encontrado['id']} | FR: {encontrado['fr']} | FC: {encontrado['fc']} | SpO2: {encontrado['spo2']}")
        else:
            print("No se encontro ningun registro con ese ID en MongoDB.")
    elif opcion == "11":
        exportarResultadosMongo()
    elif opcion == "0":
        registrarLog("Cierre del programa.")
        print("Programa finalizado.")
        ejecutando = "no"
    else:
        print("Opcion no valida. Intente de nuevo.")