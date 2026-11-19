import random
from validacion import validarCampo, validarRegistro
def generarRegistros(cantidad=50):
    if cantidad < 50:
        cantidad = 50
    listaRegistros = []
    for numero in range(1, cantidad + 1):
        if numero < 10:
            textoId = "ID-00" + str(numero)
        elif numero < 100:
            textoId = "ID-0" + str(numero)
        else:
            textoId = "ID-" + str(numero)
        edad = random.randint(18, 90)
        textoFr = str(edad) + " Años"
        frecuenciaCardiaca = random.randint(55, 140)
        if frecuenciaCardiaca < 100:
            textoFc = "0" + str(frecuenciaCardiaca) + "ppm"
        else:
            textoFc = str(frecuenciaCardiaca) + "ppm"
        saturacionOxigeno = random.randint(88, 100)
        textoSpo2 = str(saturacionOxigeno) + "%"
        registro = {
            "id": textoId,
            "fr": textoFr,
            "fc": textoFc,
            "spo2": textoSpo2
        }
        if validarRegistro(registro) == "valido":
            listaRegistros.append(registro)
    return listaRegistros
def ordenarPorFrecuencia(listaRegistros):
    registrosOrdenados = listaRegistros.copy()
    total = len(registrosOrdenados)
    for i in range(total):
        for j in range(0, total - i - 1):
            frecuenciaActual = int(registrosOrdenados[j]["fc"].replace("ppm", ""))
            frecuenciaSiguiente = int(registrosOrdenados[j + 1]["fc"].replace("ppm", ""))
            if frecuenciaActual > frecuenciaSiguiente:
                temporal = registrosOrdenados[j]
                registrosOrdenados[j] = registrosOrdenados[j + 1]
                registrosOrdenados[j + 1] = temporal
    return registrosOrdenados
def ingresarRegistroManual():
    print("--- Ingreso manual de registro ---")
    identificacion = input("id (ejemplo ID-001): ").strip()
    if validarCampo("id", identificacion) == "invalido":
        print("Error: Formato de id incorrecto.")
        return None
    edad = input("Edad (ejemplo 18 Años): ").strip()
    if validarCampo("fr", edad) == "invalido":
        print("Error: Formato de edad incorrecto.")
        return None
    frecuenciaCardiaca = input("Frecuencia cardiaca (ejemplo 090ppm): ").strip()
    if validarCampo("fc", frecuenciaCardiaca) == "invalido":
        print("Error: Formato de frecuencia incorrecto.")
        return None
    saturacionOxigeno = input("Saturacion spo2 (ejemplo 95%): ").strip()
    if validarCampo("spo2", saturacionOxigeno) == "invalido":
        print("Error: Formato de saturacion incorrecto.")
        return None
    registro = {
        "id": identificacion,
        "fr": edad,
        "fc": frecuenciaCardiaca,
        "spo2": saturacionOxigeno
    }
    return registro