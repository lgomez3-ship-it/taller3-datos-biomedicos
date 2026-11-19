import os
import csv
import json
import shutil
from pathlib import Path
from datetime import datetime
from validacion import validarRegistro
def registrarLog(accion):
    carpetaData = Path("data")
    if carpetaData.exists():
        pass
    else:
        os.makedirs(carpetaData)
    rutaLog = carpetaData / "log.txt"
    horaActual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    archivoLog = open(rutaLog, "a", encoding="utf-8")
    archivoLog.write(f"[{horaActual}] {accion}\n")
    archivoLog.close()
def crearCarpetas():
    rutas = [Path("data/txt"), Path("data/csv"), Path("data/json")]
    for ruta in rutas:
        if ruta.exists():
            pass
        else:
            os.makedirs(ruta)
    registrarLog("Estructura de carpetas verificada y creada.")
def exportarArchivos(listaRegistros):
    if len(listaRegistros) == 0:
        print("No hay registros para exportar.")
        return "error"
    try:
        crearCarpetas()
        archivoTxt = open("registros.txt", "w", encoding="utf-8")
        for item in listaRegistros:
            lineaTexto = f"{item['id']} | {item['fr']} | {item['fc']} | {item['spo2']}\n"
            archivoTxt.write(lineaTexto)
        archivoTxt.close()
        archivoCsv = open("registros.csv", "w", newline="", encoding="utf-8")
        columnas = ["id", "fr", "fc", "spo2"]
        escritor = csv.DictWriter(archivoCsv, fieldnames=columnas)
        escritor.writeheader()
        escritor.writerows(listaRegistros)
        archivoCsv.close()
        archivoJson = open("registros.json", "w", encoding="utf-8")
        json.dump(listaRegistros, archivoJson, indent=4)
        archivoJson.close()
        shutil.move("registros.txt", "data/txt/registros.txt")
        shutil.move("registros.csv", "data/csv/registros.csv")
        shutil.move("registros.json", "data/json/registros.json")
        registrarLog(f"Se exportaron y organizaron {len(listaRegistros)} registros en TXT, CSV y JSON.")
        print("Archivos guardados y organizados correctamente en la carpeta data.")
        return "exito"
    except Exception as error:
        registrarLog(f"Error al exportar archivos: {error}")
        print(f"Ocurrio un error al exportar: {error}")
        return "error"
def importarJson():
    rutaJson = Path("data/json/registros.json")
    if rutaJson.exists():
        try:
            archivoJson = open(rutaJson, "r", encoding="utf-8")
            datosLeidos = json.load(archivoJson)
            archivoJson.close()
            registrosValidos = []
            for item in datosLeidos:
                if validarRegistro(item) == "valido":
                    registrosValidos.append(item)
            registrarLog(f"Se importaron {len(registrosValidos)} registros validos desde JSON.")
            print(f"Se importaron {len(registrosValidos)} registros correctamente.")
            return registrosValidos
        except Exception as error:
            registrarLog(f"Error al importar JSON: {error}")
            print(f"Error al leer el archivo JSON: {error}")
            return []
    else:
        print("El archivo data/json/registros.json aun no existe.")
        registrarLog("Intento fallido de importar JSON: archivo no encontrado.")
        return []