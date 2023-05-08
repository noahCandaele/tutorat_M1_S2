# tutorat_M1_S2

### Re-structuration intelligente d'un jeu de donnée de debats politiques pour l'extraction de structures argumentaires

L'objectif du travail à réaliser est de structurer des données nécessaires à l'étude des composantes et des relations au sein des débats politiques qui ont eu lieu lors des élections du président des États-Unis de 1960 à 2016. Les débats se présentent sous la forme d'un dialogue entre un candidat et l'autre, qui répondent aux questions posées par un orateur sur divers sujets tels que l'économie, la sécurité, l'éducation, la guerre, les soins de santé, etc. Chaque débat a été divisé en sections en tenant compte des différents sujets abordés.

### Code Source

Le code source est divisé en plusieurs parties:
* source_code/propre.ipynb est un python notebook contenant tout le code nécessaire à la génération du context1 et context2
* source_code/ctx3.ipynb contient le code nécessaire pour le context3
* source_code/classification/ regroupe les différents tests liés à la classification de component en utilisant principalement le modèle BERT
