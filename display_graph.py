from pyvis.network import Network
import pandas as pd

# Création du réseau
g = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")

# Lecture du fichier CSV
csv_file = pd.read_csv("links.csv")

sources = csv_file['src']
targets = csv_file['dest']

edge_data = zip(sources, targets)

# Dictionnaire pour stocker le degré de chaque nœud
degree_count = {}

# Calcul du degré des nœuds
for src, dst in zip(sources, targets):
    if src in degree_count:
        degree_count[src] += 1
    else:
        degree_count[src] = 1

    if dst in degree_count:
        degree_count[dst] += 1
    else:
        degree_count[dst] = 1

# Ajouter les nœuds avec une taille proportionnelle à leur degré
for node, degree in degree_count.items():
    g.add_node(node, title=node, size=10 + degree * 2)  # Taille minimale 10, augmente avec le degré

# Ajouter les arêtes
for src, dst in zip(sources, targets):
    g.add_edge(src, dst)

# Affichage
g.show('mygraph.html', notebook=False)

