# mlops/steps/run_conversations.py
from zenml import step
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
import os
os.environ["GROQ_API_KEY"] = "" 


@step
def run_conversations(
    queries: list[dict],
    index_path: str
) -> None:

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.load_local(
        index_path,
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever()

    llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
    )


    prompt = PromptTemplate.from_template(
        """Use the context to answer the question.

        Context:
        {context}

        Question:
        {question}
        """
    )

    rag_chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
    )

    for turn in queries:
        response = rag_chain.invoke(turn["user"])
        print("USER:", turn["user"])
        print("BOT:", response.content)
