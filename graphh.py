import networkx as nx
import matplotlib.pyplot as plt

# new graph erstellen
graph = nx.DiGraph()

# tables as nodes in the graph definieren
tables = ['album', 'artist', 'playlist', 'track', 'track_artist1', 'track_playlist1']
graph.add_nodes_from(tables)

# attributes for each table definieren
table_attributes = {
    'album': ['id', 'name', 'uri', 'followers', 'total_tracks'],
    'artist': ['id', 'name', 'uri', 'followers', 'total_tracks'],
    'playlist': ['id', 'name', 'uri', 'followers', 'total_tracks'],
    'track': ['id', 'name', 'uri', 'album_id', 'artist_id'],
    'track_artist1': ['id', 'name', 'uri', 'track_id', 'artist_id'],
    'track_playlist1': ['id', 'name', 'uri', 'track_id', 'playlist_id']
}

# attributes fuer jede knote addieren
for table in tables:
    attributes = table_attributes[table]
    for attribute in attributes:
        graph.nodes[table][attribute] = None

# fremdschluessel als kanten definieren
foreign_keys = [
    ('album', 'album', 'album'),
    ('album', 'album', 'artist'),
    ('album', 'album', 'track'),
    ('album', 'album', 'playlist'),
    ('artist', 'artist', 'album'),
    ('artist', 'artist', 'artist'),
    ('artist', 'artist', 'track'),
    ('artist', 'artist', 'playlist'),
    ('playlist', 'playlist', 'album'),
    ('playlist', 'playlist', 'artist'),
    ('playlist', 'playlist', 'track'),
    ('playlist', 'playlist', 'playlist'),
    ('track', 'track', 'album'),
    ('track', 'track', 'artist'),
    ('track', 'track', 'track'),
    ('track', 'track', 'playlist'),
    ('track_artist1', 'track_artist1', 'album'),
    ('track_artist1', 'track_artist1', 'artist'),
    ('track_artist1', 'track_artist1', 'track'),
    ('track_artist1', 'track_artist1', 'playlist'),
    ('track_playlist1', 'track_playlist1', 'album'),
    ('track_playlist1', 'track_playlist1', 'artist'),
    ('track_playlist1', 'track_playlist1', 'track'),
    ('track_playlist1', 'track_playlist1', 'playlist')
]

# kanten erzeugen
for foreign_key in foreign_keys:
    from_table, from_column, to_table = foreign_key
    graph.add_edge(from_table, to_table, label=from_column)

# graph basteln
pos = nx.spring_layout(graph)  # layout algorithm
nx.draw_networkx(graph, pos, with_labels=True, node_size=500, node_color='lightblue', edge_color='gray')
edge_labels = nx.get_edge_attributes(graph, 'label')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
plt.show()
print("As you have already seen, the knowledge Graph ist created :)")