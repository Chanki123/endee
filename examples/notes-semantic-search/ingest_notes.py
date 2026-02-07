"""
Ingest study notes and prepare them for storage
in the Endee vector database.
"""

from config import EMBEDDING_DIM


def load_notes(file_path):
    """
    Load study notes from a text file and split them into chunks.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        notes = file.read().split("\n\n")
    return notes


def generate_embedding(text):
    """
    Placeholder function for generating embeddings.
    In real usage, this would call an embedding model.
    """
    return [0.0] * EMBEDDING_DIM


def store_in_endee(note_chunks):
    """
    Placeholder function to represent storing embeddings in Endee.
    """
    for index, chunk in enumerate(note_chunks):
        embedding = generate_embedding(chunk)

        # Here we would send the embedding to Endee
        print(f"Prepared chunk {index + 1} for storage in Endee")


if __name__ == "__main__":
    notes = load_notes("data/notes.txt")
    store_in_endee(notes)

