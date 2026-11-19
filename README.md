# Gestión de Datos Biomédicos y Base de Datos NoSQL

Proyecto desarrollado para la asignatura **Informática 1 (Unidad 3 y 4)** de la Facultad de Ingeniería de la Universidad de Antioquia. El sistema permite generar, validar, ordenar, almacenar localmente y gestionar en la nube registros de signos vitales simulados.

## Estructura del proyecto

* `main.py`: Menú interactivo principal que integra todos los módulos del sistema.
* `validacion.py`: Validación de formatos y rangos biomédicos mediante expresiones regulares (`id`, `fr`, `fc`, `spo2`).
* `datos.py`: Generación aleatoria de registros, ingreso manual y ordenamiento por frecuencia cardiaca.
* `archivos.py`: Exportación e importación en formatos `.txt`, `.csv` y `.json`, organización automática de directorios y registro de actividad en `log.txt`.
* `base.py`: Conexión con MongoDB Atlas (`biomedica.signos_vitales`), carga de datos validados y consultas estadísticas.
* `data/`: Carpeta generada automáticamente con subdirectorios `/txt`, `/csv`, `/json` y el archivo `log.txt`.
* `resultados_mongo.json`: Archivo generado con el promedio de frecuencia cardiaca y los registros con $\text{SpO}_2 < 94\%$.

## Formato de los datos validados

* **ID (`id`):** `ID-001`
* **Edad (`fr`):** `18 Años`
* **Frecuencia cardiaca (`fc`):** `090ppm`
* **Saturación de oxígeno (`spo2`):** `95%`

## Requisitos e instalación

1. Tener instalado Python 3.10 o superior.
2. Instalar el controlador de MongoDB:
   ```bash
   pip install pymongo
   ```

## Ejecución

Ejecutar el archivo principal desde la terminal en la raíz del proyecto:

```bash
python main.py
```