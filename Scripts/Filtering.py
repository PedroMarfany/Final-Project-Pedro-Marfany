"""
Scripts to make filters
"""

import pandas as pd 
import click


def load_dataset(NBADataset):
    """
    Función para cargar el dataset
    """
    extension = NBADataset.rsplit('.', 1)[-1]
    if extension == "csv":
        return pd.read_csv(NBADataset)
    else:
        raise TypeError(f"La extension es {extension} y no csv. Prueba otra vez")

class NBADataFilter:
    def __init__(self, filepath):
        self.dataset = pd.read_csv(filepath)
    
    def filter_by_height(self, min_height_cm):
        """
        Filtra jugadores por altura mínima.
        """
        return self.dataset[self.dataset['player_height'] > min_height_cm]
    
    def filter_by_points(self, min_points):
        """
        Filtra jugadores que anotan más de un número mínimo de puntos por juego.
        """
        return self.dataset[self.dataset['pts'] > min_points]
    
    def filter_by_team(self, team_abbreviation):
        """
        Filtra jugadores por equipo
        """
        return self.dataset[self.dataset['team_abbreviation'] == team_abbreviation]
    def filter_by_country(self, country_name):
        try:
            return self.dataframe[self.dataframe['country'] == country_name]
        except KeyError:
            print("La columna 'country' no existe en el dataset.")
        except TypeError:
            print("El tipo de dato para 'country_name' no es válido.")

@click.command(short_help='Parser to import datset')
@click.option('-f', '--file_name', required=True, help='File to import')
def main(bundeslig_player):
    """
    Main function
    """
    df = load_dataset(bundeslig_player)
    
    
    result = FilteringClass(df).filter_price(12)
    
    print(result.shape)

if _name_ == "_main_":
    main()





