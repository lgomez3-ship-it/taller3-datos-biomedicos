import re
def validarCampo(campo, valor):
    texto = str(valor).strip()
    if campo== "id":
        patron = r"^ID-\d{3}$"
    elif campo == "fr":
        patron = r"^\d{1,3} Años$"
    elif campo=="fc":
        patron = r"^\d{3}ppm$"
    elif campo == "spo2":
        patron= r"^\d{2,3}%$"
    else:
        return "invalido"
    coincidencia = re.match(patron, texto)
    if coincidencia:
        return "valido"
    else:
        return "invalido"
def validarRegistro(registro):
    if "id" in registro and "fr" in registro and "fc" in registro and "spo2" in registro:
        estadoId = validarCampo("id", registro["id"])
        estadoFr = validarCampo("fr", registro["fr"])
        estadoFc= validarCampo("fc", registro["fc"])
        estadoSpo2 = validarCampo("spo2", registro["spo2"])
        if estadoId == "valido" and estadoFr == "valido" and estadoFc == "valido" and estadoSpo2 == "valido":
            return "valido"
        else:
            return "invalido"
    else:
        return "invalido"