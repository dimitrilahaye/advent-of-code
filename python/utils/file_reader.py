import os

def read_input(day: int, year: int) -> list[str]:
    """
    Lit l'entrée pour un jour et une année donnés.
    Le fichier d'entrée doit être nommé 'input.txt' et se trouver dans 
    'YYYY/XX/input.txt'.
    """
    day_str = f"{day:02d}"
    file_path = os.path.join(str(year), day_str, "input.txt")
    
    try:
        with open(file_path, 'r') as f:
            lines = [line.rstrip('\n') for line in f]
            return lines
    except FileNotFoundError:
        print(f"Erreur: Le fichier d'entrée n'a pas été trouvé à {file_path}")
        return []