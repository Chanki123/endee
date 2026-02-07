"""
Perform semantic search on study notes using Endee.
"""

from config import EMBEDDING_DIM


def generate_query_embedding(query):
    """
    Placeholder function for generating query embeddings.
    """
    return [0.0] * EMBEDDING_DIM


def search_endee(query_embedding, top_k=3):
    """
    Placeholder function to represent vector similarity search in Endee.
    """
    # In real usage, this would query Endee
    return [
        "Ohm’s Law states the relationship between voltage and current.",
        "Kirchhoff’s Voltage Law applies to closed electrical circuits."
    ]


if __name__ == "__main__":
    query = input("Enter your search query: ")
    query_embedding = generate_query_embedding(query)

    results = search_endee(query_embedding)

    print("\nTop matching study notes:")
    for result in results:
        print("-", result)

