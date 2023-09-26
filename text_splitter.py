from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredMarkdownLoader


# Recursive splitting to consider different separators in generic text
r_splitter = RecursiveCharacterTextSplitter(
    chunk_size=3000,
    chunk_overlap=200, 
    separators=["\n\n", "\n", " ", ""],
    length_function = len
)

def load_transcript(raw_md):
    loader = UnstructuredMarkdownLoader(raw_md)
    data = loader.load()
    return data

def split_transcript(raw_md):
    data = load_transcript(raw_md)
    docs = r_splitter.split_documents(data)
    return docs


from langchain.prompts import PromptTemplate

prompt_template = """You are an excellent professor in occupational health psychology. Your are given extensive notes on a lecture on occupational health psychology.\n
Transcript:\n
{text}\
Step by step work through the document and create well thought through and very challenging exam questions in a single choice format\n
Example Format: (use this intendation as well):\n
'''- What is true with regard to the Transactional Stress Model? \n
        - A) That stress is inherent in the person \n
        - B) That personal and work resources have only a small influence in the \n
        emergence of well-being.
        - C) That stress arises as a link between motives and beliefs \n
        - D) That the individual cognitive appraisal process is important in the emergence of Stress\n
    - Correct: D)\n\n
    - What is NOT part of burnout? \n
        - A) Physical exhaustion \n
        - B) Distancing from social contacts \n
        - C) Less experience of performance \n
        - D) Low self-esteem\n'''
    - Correct: B)
Task:\n
    - Use a a question and answer format to extract information from the transcript.\n
    - Focus on theories, definitions.\n
    - Ensure Completeness: Incorporate all bullet points, sub-points, and other nested lists from the transcript without omitting any content.\n
    - Do Not Add Extra Material: Keep the lecture notes faithful to the original transcript, avoiding any addition, removal, or modification of the substance of the content.\n
    - Work Step-by-Step: Methodically work through the transcript, to ensure that the final document is both accurate and complete.\n
This task is designed to facilitate the creation of complete set exam questions of the whole lecture and literature notes.\n
LECTURE NOTES:"""
prompt = PromptTemplate.from_template(prompt_template)

refine_template = (
    """You are an excellent porfessor in occupational health pychology. You are given a generated transcript of a lecture on occupational health psychology.\n
    We are given a set of exam questions up to a point based on a lecture and literature notes\n
    Existing Q&A Notes: {existing_answer}\n
    Your goal is to continue creating the existing challenging exam questions in single choice format with additional context from the continued lecture transcript provided below.\n
    ------------\n
    {text}\n
    ------------\n
    Example Format: (use this intendation as well):\n
    '''- What is true with regard to the Transactional Stress Model? \n
            - A) That stress is inherent in the person \n
            - B) That personal and work resources have only a small influence in the \n
            emergence of well-being.
            - C) That stress arises as a link between motives and beliefs \n
            - D) That the individual cognitive appraisal process is important in the emergence of Stress\n
        - Correct: D)\n\n
        - What is NOT part of burnout? \n
            - A) Physical exhaustion \n
            - B) Distancing from social contacts \n
            - C) Less experience of performance \n
            - D) Low self-esteem\n'''
        - Correct: B)
    Task:\n
        - Use a a question and answer format to extract information from the transcript.\n
        - Focus on theories, definitions.\n
        - Ensure Completeness: Incorporate all bullet points, sub-points, and other nested lists from the transcript without omitting any content.\n
        - Do Not Add Extra Material: Keep the lecture notes faithful to the original transcript, avoiding any addition, removal, or modification of the substance of the content.\n
        - Work Step-by-Step: Methodically work through the transcript, to ensure that the final document is both accurate and complete.\n
    This task is designed to facilitate the creation of complete set exam questions of the whole lecture and literature notes."""
)

refine_prompt = PromptTemplate.from_template(refine_template)


from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain

_ = load_dotenv()

llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")

chain = load_summarize_chain(
    llm=llm,
    chain_type="refine",
    question_prompt=prompt,
    refine_prompt=refine_prompt,
    return_intermediate_steps=True,
    input_key="input_documents",
    output_key="output_text",
)

# generate transcript
def generate_qa_transcript(docs):
    result = chain({"input_documents":docs}, return_only_outputs=False)
    output_text = result['output_text']
    return output_text



raw_md = "files/work2.md"
docs = split_transcript(raw_md)

# Generate the QA transcript
qa_transcript = generate_qa_transcript(docs)


with open("output_qa_transcript1.txt", "w") as f:
        f.write(qa_transcript)


