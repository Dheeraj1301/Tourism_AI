from langchain.document_loaders import PyPDFLoader, CSVLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer, InputExample, losses
from torch.utils.data import DataLoader
import os
from config import DATA_DIR, VECTOR_STORE_DIR

loaders = []
for file in os.listdir(DATA_DIR):
    path = os.path.join(DATA_DIR, file)
    if file.endswith('.pdf'):
        loaders.append(PyPDFLoader(path))
    elif file.endswith('.csv'):
        loaders.append(CSVLoader(path))
    elif file.endswith('.txt') or file.endswith('.md'):
        loaders.append(TextLoader(path))

docs = []
for loader in loaders:
    docs.extend(loader.load())

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
split_docs = splitter.split_documents(docs)

# Fine-tune the sentence transformer model using document pairs
base_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
train_examples = []
for i in range(0, len(split_docs) - 1, 2):
    text_a = split_docs[i].page_content
    text_b = split_docs[i + 1].page_content
    train_examples.append(InputExample(texts=[text_a, text_b]))
if len(split_docs) % 2 == 1:
    last_text = split_docs[-1].page_content
    train_examples.append(InputExample(texts=[last_text, last_text]))

train_loader = DataLoader(train_examples, shuffle=True, batch_size=16)
train_loss = losses.MultipleNegativesRankingLoss(base_model)
base_model.fit(train_objectives=[(train_loader, train_loss)], epochs=1, show_progress_bar=True)

base_model.save('fine_tuned_model')
embeddings = HuggingFaceEmbeddings(model_name='fine_tuned_model')

vectordb = FAISS.from_documents(split_docs, embeddings)
vectordb.save_local(VECTOR_STORE_DIR)

print('✅ Vector index built and saved with fine-tuned model.')
