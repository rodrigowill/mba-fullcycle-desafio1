import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_postgres import PGVector

class Search:

    def search_query(self:str) -> list: 

        load_dotenv()
        for k in ("GOOGLE_API_KEY", "PGVECTOR_URL", "PGVECTOR_COLLECTION"):
            if not os.getenv(k):
                raise RuntimeError(f"Environment variable {k} is not set")

        embeddings = GoogleGenerativeAIEmbeddings(model=os.getenv("GEMINI_MODEL", "gemini-embedding-004"))

        store = PGVector(
            embeddings=embeddings,
            collection_name=os.getenv("PGVECTOR_COLLECTION"),
            connection=os.getenv("PGVECTOR_URL"),
            use_jsonb=True,
        )

        return store.similarity_search_with_score(self, k=10)