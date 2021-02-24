# hc2021

Pour utiliser le repo :

- creer un dossier en copiant example
- copier main_template.py dans main.py (gitignore, pour travailler en parallèle)
- lancer main.py `python main.py`

Le script:
- lit les lignes en isolant la premiere avec la fonction `prepare_file`
- permet d'ecrire un fichier en renvoyant une liste de listes en entrée à la fonction `write_output`


Exemple de `run.py` qui utilise ça :

```python
from shared.file_management import prepare_file, write_output


#config est la premiere ligne, data les uivantes

[config, data] = prepare_file("./input/a_example")



print("-----config------")
print(config)

print("-----data------")
print(data)



def myAlgo(config, data):
    # ici ecriture de l'algo lui meme
    return  [[1], [2, 2, 2], [3, 3, 3]]

lines = myAlgo(config, data)

print("------output------")
print(lines)

write_output(lines)
```