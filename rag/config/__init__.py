"""
Configuration settings for the RAG application
"""
import os

# Load configuration from environment variables
PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
LOCATION = os.environ.get("GOOGLE_CLOUD_LOCATION")

# Common resource paths
def get_corpus_path(corpus_id: str) -> str:
    """
    Constructs a full corpus resource path from a corpus ID.
    
    Args:
        corpus_id: The numeric ID of the corpus
        
    Returns:
        Full resource path for the corpus
    """
    return f"projects/{PROJECT_ID}/locations/{LOCATION}/ragCorpora/{corpus_id}" 