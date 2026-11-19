import json
from pymongo import MongoClient
from validacion import validarRegistro
from archivos import registrarLog
def obtenerColeccion():
    enlace = "mongodb+srv://lgomez3_db_user:7GC9oHzDwR0MugUj@cluster0.1rnc1oa.mongodb.net/"
    cliente = MongoClient(enlace)
    baseDatos = cliente["biomedica"]
    coleccion = baseDatos["signos_vitales"]
    return coleccion
def subirRegistrosMongo(listaRegistros):
    if len(listaRegistros) == 0:
        print("No hay registros para subir a MongoDB.")
        return "error"
    try:
        coleccion = obtenerColeccion()
        registrosParaSubir = []
        for item in listaRegistros:
            if validarRegistro(item) == "valido":
                registrosParaSubir.append(item.copy())
        if len(registrosParaSubir) == 0:
            print("Ningun registro paso la validacion.")
            return "error"
        coleccion.delete_many({})
        coleccion.insert_many(registrosParaSubir)
        registrarLog(f"Se subieron {len(registrosParaSubir)} registros a MongoDB Atlas.")
        print(f"Se subieron {len(registrosParaSubir)} registros a MongoDB correctamente.")
        return "exito"
    except Exception as error:
        registrarLog(f"Error al subir registros a MongoDB: {error}")
        print(f"Error al conectar o subir datos a MongoDB: {error}")
        return "error"
def consultarPromedioFc():
    try:
        coleccion = obtenerColeccion()
        documentos = list(coleccion.find({}, {"_id": 0}))
        if len(documentos) == 0:
            print("No hay datos en MongoDB para calcular el promedio.")
            return 0
        sumaFc = 0
        for doc in documentos:
            valorFc = int(doc["fc"].replace("ppm", ""))
            sumaFc += valorFc
        promedio = round(sumaFc / len(documentos), 2)
        registrarLog(f"Consulta MongoDB: promedio de frecuencia cardiaca = {promedio} ppm.")
        return promedio
    except Exception as error:
        registrarLog(f"Error al consultar promedio en MongoDB: {error}")
        print(f"Error en la consulta: {error}")
        return 0
def consultarSpo2Bajo():
    try:
        coleccion = obtenerColeccion()
        documentos = list(coleccion.find({}, {"_id": 0}))
        listaBajos = []
        for doc in documentos:
            valorSpo2 = int(doc["spo2"].replace("%", ""))
            if valorSpo2 < 94:
                listaBajos.append(doc)
        registrarLog(f"Consulta MongoDB: se encontraron {len(listaBajos)} registros con spo2 menor a 94.")
        return listaBajos
    except Exception as error:
        registrarLog(f"Error al consultar spo2 bajo en MongoDB: {error}")
        print(f"Error en la consulta: {error}")
        return []
def buscarPorIdMongo(idBuscar):
    try:
        coleccion = obtenerColeccion()
        documento = coleccion.find_one({"id": idBuscar.strip()}, {"_id": 0})
        if documento:
            registrarLog(f"Consulta MongoDB: se encontro el registro con id {idBuscar}.")
            return documento
        else:
            registrarLog(f"Consulta MongoDB: no se encontro el registro con id {idBuscar}.")
            return None
    except Exception as error:
        registrarLog(f"Error al buscar por id en MongoDB: {error}")
        print(f"Error en la busqueda: {error}")
        return None
def exportarResultadosMongo():
    try:
        promedioFc = consultarPromedioFc()
        spo2Bajos = consultarSpo2Bajo()
        resultados = {
            "promedio_fc_ppm": promedioFc,
            "total_spo2_menor_94": len(spo2Bajos),
            "registros_spo2_menor_94": spo2Bajos
        }
        archivoSalida = open("resultados_mongo.json", "w", encoding="utf-8")
        json.dump(resultados, archivoSalida, indent=4)
        archivoSalida.close()
        registrarLog("Se exportaron las consultas de MongoDB a resultados_mongo.json.")
        print("Resultados exportados correctamente a resultados_mongo.json.")
        return "exito"
    except Exception as error:
        registrarLog(f"Error al exportar resultados_mongo.json: {error}")
        print(f"Error al exportar resultados: {error}")
        return "error"