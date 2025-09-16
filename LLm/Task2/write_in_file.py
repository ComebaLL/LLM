___author___ = "Kuvykin N.D"

import csv

def write_to_csv(data, filename) -> None:
    """
    Функция записывает данные в csv-файлы.
    """
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data)


def write_to_md(func_name: str, run_time: float, filename: str = "time_output.md"):
    """
    Функция записывает данные в md-файл
    """
    with open(filename, "a") as md_file:
        md_file.write(f"Finished {func_name:50s} in {run_time:.4f} seconds\n")
    