# Final-Project-Pedro-Marfany
Este repositorio contiene scripts avanzados de Python diseñados para cargar, filtrar, y analizar un dataset de la NBA. Incluye funcionalidades para aplicar filtros específicos a los datos, realizar debugging básico, y ejecutar pruebas unitarias para validar la lógica de filtrado.

## Installation

   pip install -r requirements.txt

## Usage
    python scripts/repo_first_script.py -i dataset/NBADataset.csv

Explain the command
 Carga el dataset de la NBA desde la ubicación especificada y aplica una serie de filtros basados en los argumentos adicionales proporcionados, por otra parte  por altura, puntos, equipo, y país, dependiendo de las opciones que se agreguen al comando. 
Explain additional arguments
Voy a proporcionar diferentes argumentos como por ejemplo
--height 200: Filtra jugadores con una altura superior a 200 cm.
--points 20: Filtra jugadores que han anotado más de 20 puntos por juego.
--team LAL: Filtra jugadores que pertenecen al equipo Los Angeles Lakers (LAL).



## Test

    pytest

