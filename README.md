# 🤖 Petrus AI Assistant (RAG)

A private, secure AI assistant that uses Retrieval-Augmented Generation (RAG) to answer questions based on internal company policy documents. Powered by Amazon Bedrock (Claude 3 & Titan) and LangChain.

## 🛠️ Tech Stack

- **LLM**: Anthropic Claude 3 Sonnet (via AWS Bedrock)
- **Embeddings**: Amazon Titan Text Embeddings
- **Vector Store**: FAISS (Facebook AI Similarity Search)
- **Orchestration**: LangChain
- **Frontend**: Streamlit

## 📂 Project Structure
```
├── data/
│   └── documents/          # Place your company PDFs here
├── vectorstore/            # Local storage for the FAISS index
├── app.py                  # Streamlit frontend UI
├── rag.py                  # PDF processing and retrieval logic
├── llm.py                  # AWS Bedrock configuration
├── agent.py                # Logic connecting LLM and Retrieval
└── requirements.txt        # Python dependencies
```

## 🚀 Getting Started

### 1. Prerequisites

- Python **3.9+**
- An **AWS Account** with access to:
  - Amazon Bedrock
  - Claude 3 Sonnet
  - Titan Embeddings G1 – Text
- AWS CLI configured locally:

```bash
aws configure
```
### 2. Installation

Clone this repository and install the dependencies:

```bash
pip install -r requirements.txt
```

### 3. Initializing Vector DB

```bash
python3 rag.py
```

### 4. Running the Application

Launch the Streamlit interface:

```bash
streamlit run app.py
```

## 💡 How It Works
    - **Ingestion**: The system reads PDFs from data/documents/, splits them into 500-character chunks, and converts them into vectors using Amazon Titan.

    - **Retrieval**: When you ask a question, the system searches the FAISS index for the top 3 most relevant document snippets.

    - **Generation**: The relevant snippets and your question are sent to Claude 3 Sonnet, which generates a precise answer based only on the provided context.

## ⚠️ Important Notes
**🌍 AWS Regions**

LLM: **ap-south-1** (Mumbai)

Embeddings: **us-east-1** (N. Virginia)

Ensure your IAM user has permissions in both regions,
or update llm.py and rag.py to use a single region.