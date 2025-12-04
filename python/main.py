import sys
import importlib

def run_day(year: int, day: int):
    """Importe et exécute le script de solution pour un jour donné."""
    day_str = f"{day:02d}"
    
    try:
        # Importe le module dynamiquement (ex: 2023.01.solution)
        module_path = f"{year}.{day_str}.solution"
        module = importlib.import_module(module_path)

        module.solve()
        
    except ModuleNotFoundError:
        print(f"Erreur: Solution non trouvée pour l'année {year}, Jour {day}.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'exécution du Jour {day}: {e}")

if __name__ == "__main__":
    
    if len(sys.argv) < 3:
        print("Erreur : Veuillez spécifier l'année et le jour.")
        print("Usage: python main.py <ANNÉE> <JOUR>")
        sys.exit(1) 

    try:
        year = int(sys.argv[1])
        day = int(sys.argv[2])
    except ValueError:
        raise ValueError("L'année et le jour doivent être des nombres entiers.")

    run_day(year, day)