import os
import click
import requests

@click.command()
@click.argument('nombre_proyecto')
def crear_proyecto(nombre_proyecto):
    # Crear la estructura de carpetas
    os.makedirs(nombre_proyecto)
    os.chdir(nombre_proyecto)

    os.makedirs('App')
    os.makedirs('Back_Django')
    os.makedirs('Front_Angular')
    os.makedirs('Datos')
    os.makedirs('Iniciales')
    os.makedirs('Prediciones')
    os.makedirs('Transformaciones')
    os.makedirs(os.path.join('Transformaciones', 'EDA'))
    os.makedirs('Modelos')
    os.makedirs(os.path.join('Modelos', 'LogisticRegression'))
    os.makedirs(os.path.join('Modelos', 'RandomForest'))
    os.makedirs('Recursos')
    os.makedirs('_pycache__')

    # Crear archivos dentro de las carpetas
    with open(os.path.join('Datos', 'heart_disease_dataset.csv'), 'w') as f:
        f.write("Contenido de heart_disease_dataset.csv")

    with open(os.path.join('Prediciones', 'prueba_masiva.csv'), 'w') as f:
        f.write("Contenido de prueba_masiva.csv")

    with open(os.path.join('Prediciones', 'prueba_prediccion.csv'), 'w') as f:
        f.write("Contenido de prueba_prediccion.csv")

    with open(os.path.join('Transformaciones', 'heart_disease_dataset_all_columns.csv'), 'w') as f:
        f.write("Contenido de heart_disease_dataset_all_columns.csv")

    with open(os.path.join('Transformaciones', 'heart_disease_dataset_no_num.csv'), 'w') as f:
        f.write("Contenido de heart_disease_dataset_no_num.csv")

    with open(os.path.join('Transformaciones', 'heart_disease_dataset_no_target.csv'), 'w') as f:
        f.write("Contenido de heart_disease_dataset_no_target.csv")

    # Crear archivos de notebooks
    notebooks = {
        'LogisticRegression_binaryCase.ipynb': 'Modelos/LogisticRegression',
        'LogisticRegression_multivariateCase.ipynb': 'Modelos/LogisticRegression',
        'RandomForest_binaryCase.ipynb': 'Modelos/RandomForest'
    }

    for notebook, folder in notebooks.items():
        with open(os.path.join(folder, notebook), 'w') as f:
            f.write("# Notebook para {}\n".format(notebook))

    # Descargar el contenido de toolbook.py desde GitHub
    toolbook_url = 'https://raw.githubusercontent.com/Alfiie1203/crear_proyecto.py/main/Recursos/toolbook.py'
    response = requests.get(toolbook_url)
    if response.status_code == 200:
        with open(os.path.join('Recursos', 'toolbook.py'), 'w') as f:
            f.write(response.text)
    else:
        click.echo("Error al descargar el archivo toolbook.py.")

    click.echo("Proyecto {} creado exitosamente.".format(nombre_proyecto))

if __name__ == '__main__':
    crear_proyecto()
