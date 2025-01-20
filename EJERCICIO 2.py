import csv
import cProfile

def process_csv(file_path):
    """Lee un fichero CSV, capitaliza nombres y calcula letras de DNI."""
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Saltar el encabezado
        return [
            {'name': row[0].strip().title(), 'dni_letter': "TRWAGMYFPDXBNJZSQVHLCKE"[int(row[1]) % 23]}
            for row in reader
        ]

def main():
    """Procesa dos ficheros CSV y mide su rendimiento."""
    for file in ['small_dataset.csv', 'large_dataset.csv']:
        data = process_csv(file)
        print(f"{file}: {len(data)} registros procesados.")

if __name__ == "__main__":
    cProfile.run('main()')
