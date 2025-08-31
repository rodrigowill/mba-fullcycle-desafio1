from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory
from search import Search
from dotenv import load_dotenv

load_dotenv()

def main():
    """Função principal do chat"""
    print("🤖 Chat sobre Teste de Performance")
    print("=" * 40)
    print("Digite 'sair' para encerrar o chat")
    print("=" * 40)
    
    try:
        
        print()
        
        # Loop principal do chat
        while True:
            try:
                # Receber input do usuário
                user_question = input("Faça uma pergunta: ").strip()
                
                # Verificar se quer sair
                if user_question.lower() in ['sair', 'exit', 'quit', 'q']:
                    print("👋 Até logo!")
                    break
                
                # Verificar se a entrada não está vazia
                if not user_question:
                    print("❌ Por favor, digite uma pergunta.")
                    continue
                
                # Gerar resposta usando LangChain
                context = (Search.search_query(user_question))
                system = ("""
                    CONTEXTO:{context}
                            
                    REGRAS:
                    - Responda somente com base no CONTEXTO.
                    - Se a informação não estiver explicitamente no CONTEXTO, responda:
                    "Não tenho informações necessárias para responder sua pergunta."
                    - Nunca invente ou use conhecimento externo.
                    - Nunca produza opiniões ou interpretações além do que está escrito.

                    EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
                    Pergunta: "Qual é a capital da França?"
                    Resposta: "Não tenho informações necessárias para responder sua pergunta."

                    Pergunta: "Quantos clientes temos em 2024?"
                    Resposta: "Não tenho informações necessárias para responder sua pergunta."

                    Pergunta: "Você acha isso bom ou ruim?"
                    Resposta: "Não tenho informações necessárias para responder sua pergunta."

                    PERGUNTA DO USUÁRIO: {question}

                    RESPONDA A {question}
                            
                    """)
                user = ("user", "{question}")
                chat_prompt = ChatPromptTemplate([system, user])
                messages = chat_prompt.format_messages(context=context, question=user_question)
                model = init_chat_model(model="gemini-2.5-flash", model_provider="google_genai", temperature=0.5)
                result = model.invoke(messages)
                print()
                print("Resposta: ", result.content)
                print()
                
            except KeyboardInterrupt:
                print("\n👋 Chat interrompido pelo usuário. Até logo!")
                break
            except Exception as e:
                print(f"❌ Erro: {e}")
                print("Tente novamente ou digite 'sair' para encerrar.")
                print()
                
    except Exception as e:
        print(f"❌ Erro ao inicializar o chat: {e}")
        print("Verifique sua conexão com a internet e a validade da API key.")

if __name__ == "__main__":
    main()






"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system),
    MessagesPlaceholder(variable_name="history"), #histórico de mensagens
    ("human", "{user_question}")
])

chat_model = init_chat_model(model="gemini-2.5-flash", model_provider="google_genai")

chain = context | prompt | chat_model

session_store: dict[str, InMemoryChatMessageHistory] = {}

# Pega o histótico da sessao
def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]

conversational_chain = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

# simular criacao de novas sessoes
config = {"configurable": {"session_id": "demo-session"}}

# Interactions
response1 = conversational_chain.invoke({"input": input("Faça uma pergunta sobre teste de performance: ").strip()}, config=config)
print("Assistant: ", response1.content)
print("-"*30)


"""