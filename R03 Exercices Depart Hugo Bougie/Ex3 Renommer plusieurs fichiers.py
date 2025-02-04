# importez os
# # allez dans le dossier Ex3 Videos
# # avec la boucle for, passez à travers chacun des dossiers de os.listdir()
# #     utilisez os.path.splitext pour obtenir le filename et l'extension
# #     utilisez split sur le filename pour obtenir le titre, le cours et le numéro du cours
# #     utilisez strip pour enlever les espaces qui pourraient rester pour le titre et le numéro
# #     en plus utilisez zfill pour remplir le numéro de sorte que 1 deviendra 01
# #     recréez le nouveau nom de fichier#   utliser os.rename pour renommer le fichier
import os

os.chdir(path="R03 Exercices Depart Hugo Bougie\Ex3 Videos")

for file in os.listdir():
   file_Split= os.path.splitext(file)
   filename = file_Split[0]
   filename_split =filename.split("_")
   titre = filename_split[0].strip()
   nom_cours = filename_split[1].strip()
   numero_cours = filename_split[2]
   print(numero_cours)