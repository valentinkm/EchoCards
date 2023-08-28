from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader


# Recursive splitting to consider different separators in generic text
r_splitter = RecursiveCharacterTextSplitter(
    chunk_size=2000,
    chunk_overlap=200, 
    separators=["\n\n", "\n", " ", "", "."],
    length_function = len
)
transcript_file = "files/transcript.txt"

loader = TextLoader(transcript_file)
data = loader.load()

def load_transcript(transcript_file):
    loader = TextLoader(transcript_file)
    data = loader.load()
    return data

def split_transcript(transcript_file):
    data = load_transcript(transcript_file)
    docs = r_splitter.split_documents(data)
    return docs
docs = split_transcript(transcript_file)

# Initialize an empty string to hold all the content
all_slides = ""

# Loop through each page in the pages list
for i, page in enumerate(pages):
    all_slides += f"Page {i + 1}:\n"
    all_slides += page.page_content
    all_slides += "\n\n"

with open("all_slides.txt", 'w') as f:
    f.write(all_slides)

import nltk
text = all_slides
tokens = nltk.word_tokenize(text)
len(tokens)

