"""Configure the Sentence Transformer embeddings."""


from langchain_huggingface import HuggingFaceEmbeddings
from src.config import settings

embbedings = HuggingFaceEmbeddings(
    model = settings.embedding_model,
    encode_kwargs={"normalize_embeddings":  True},
)