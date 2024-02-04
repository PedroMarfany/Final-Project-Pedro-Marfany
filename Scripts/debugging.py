"""
Script to create the debugging 
"""


from scripts.Filtering import NBADataFilter 
import pandas as pd

def main():
    # Creando un DataFrame de ejemplo para poder forzar errrores 
    data = {
        'player_name': ['John Doe', 'Jane Smith'],
        'pts': [10, 'Veinticinco'],
        'player_height': [200, 180],
        'age': [25, 'Treinta'],
        'team_abbreviation': ['LAL', 'BOS'],
        'country': ['USA', 'Canada'],
        'ast': [5, 7]
    }
    df = pd.DataFrame(data)

    nba_filter = NBADataFilter(df)

    # Intentamos filtrar por puntos, pero hay un error debido al tipo de dato incorrecto en 'pts'
    try:
        players_with_more_than_20pts = nba_filter.filter_by_points(20)
        print(players_with_more_than_20pts)
    except Exception as e:
        print(f"Error al filtrar por puntos: {e}")

    # Debugging: Verificar el tipo de datos de la columna 'pts'
    print("Tipos de datos en el DataFrame:")
    print(df.dtypes)

    # Intentamos corregir el error manualmente (esto es solo para propósitos de este ejemplo)
    df['pts'] = pd.to_numeric(df['pts'], errors='coerce')  # Convertir a numérico, 'coerce' convierte errores en NaN

    # Intentamos filtrar nuevamente
    try:
        players_with_more_than_20pts = nba_filter.filter_by_points(20)
        print(players_with_more_than_20pts)
    except Exception as e:
        print(f"Error después de la corrección: {e}")

if __name__ == "__main__":
    main()
