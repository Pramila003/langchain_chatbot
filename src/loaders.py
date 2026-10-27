"""Load supported source documents."""

from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_split_documnet(folder:str="data/raw"):
    documnet=[]
    
    for path in Path(folder).glob("**/*"):
        if path.suffix.lower()==".pdf":
            documnet.extend(PyPDFLoader(str(path)).load())
            
        elif path.suffix.lower()==".txt":
            documnet.extend(TextLoader(str(path),encoding="utf-8").load())
            
        splitter= RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=200,
        )
        
        return splitter.split_documents(documnet)