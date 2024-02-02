import networkx as nx
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
import random

# Define a sample knowledge graph (you can replace this with your own data)
knowledge_graph = nx.Graph()
knowledge_graph.add_nodes_from(['dog', 'cat', 'animal', 'pet'])
knowledge_graph.add_edges_from([('dog', 'animal'), ('cat', 'animal'), ('dog', 'pet'), ('cat', 'pet')])

# Train Node2Vec model to generate node embeddings
class Node2Vec:
    def __init__(self, graph):
        self.graph = graph

    def train(self, dimensions=64, walk_length=30, num_walks=200, workers=4):
        # Pre-compute transition probabilities
        node2vec = Node2Vec(self.graph)
        model = node2vec.fit(walk_length=walk_length, num_walks=num_walks, workers=workers)
        model.wv.save_word2vec_format('node2vec_embeddings.bin')

    def fit(self, **kwargs):
        # Generate random walks
        walks = self._generate_walks(**kwargs)
        
        # Train Word2Vec model
        model = Word2Vec(walks, size=kwargs['dimensions'], **kwargs)
        return model

    def _generate_walks(self, **kwargs):
        num_walks = kwargs.get('num_walks', 200)
        walk_length = kwargs.get('walk_length', 30)
        
        walks = []
        for _ in range(num_walks):
            for node in self.graph.nodes():
                walk = self._generate_random_walk(node, walk_length)
                walks.append(walk)
        return walks

    def _generate_random_walk(self, start_node, walk_length):
        walk = [start_node]
        for _ in range(walk_length - 1):
            neighbors = list(self.graph.neighbors(walk[-1]))
            if neighbors:
                walk.append(random.choice(neighbors))
            else:
                break
        return walk

# Train Node2Vec model
node2vec = Node2Vec(knowledge_graph)
node2vec.train()

# Load trained embeddings
word_vectors = KeyedVectors.load_word2vec_format('node2vec_embeddings.bin', binary=True)

# Function to generate response to user query
def generate_response(query):
    # Tokenize query and get node embeddings
    tokens = query.split()
    embeddings = [word_vectors[token] for token in tokens if token in word_vectors.vocab]

    # Average node embeddings to represent the query
    if embeddings:
        query_embedding = sum(embeddings) / len(embeddings)
    else:
        return "I'm sorry, I don't understand your query."

    # Find most similar nodes (concepts) in the knowledge graph
    similar_nodes = word_vectors.similar_by_vector(query_embedding, topn=3)

    # Generate response based on similar nodes
    response = "You may be interested in: "
    for node, _ in similar_nodes:
        response += node + ", "

    return response.strip(', ')

# Example usage
query = "dog and cat"
response = generate_response(query)
print("User: ", query)
print("Chatbot: ", response)

