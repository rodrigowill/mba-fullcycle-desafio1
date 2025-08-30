import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_postgres import PGVector
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model

load_dotenv()
for k in ("GOOGLE_API_KEY", "PGVECTOR_URL", "PGVECTOR_COLLECTION"):
    if not os.getenv(k):
        raise RuntimeError(f"Environment variable {k} is not set")

query = input("Me faça uma pergunta sobre agile testing, performance testing ou team topology: ").strip()
embeddings = GoogleGenerativeAIEmbeddings(model=os.getenv("GEMINI_MODEL", "gemini-embedding-004"))
store = PGVector(
    embeddings=embeddings,
    collection_name=os.getenv("PGVECTOR_COLLECTION"),
    connection=os.getenv("PGVECTOR_URL"),
    use_jsonb=True,
)
results = store.similarity_search_with_score(query, k=3)

system = ("system", "You are an expert in software development, software testing and technology teamse")
user = ("user", "{question}")

chat_prompt = ChatPromptTemplate([system, user])

messages = chat_prompt.format_messages(question=query)

for msg in messages:
    print(f"{msg.type}: {msg.content}")

gemini = init_chat_model(model="gemini-2.5-flash", model_provider="google_genai")
result = gemini.invoke(messages)
print(result.content)


for i, (doc, score) in enumerate(results, start=1):
    print("="*50)
    print(f"Resultado {i} (score: {score:.2f}):")
    print("="*50)

    print("\nTexto:\n")
    print(doc.page_content.strip())

    print("\nMetadados:\n")
    for k, v in doc.metadata.items():
        print(f"{k}: {v}")