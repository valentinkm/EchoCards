import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
load_dotenv()

llm = ChatOpenAI(temperature=0.7, model_name="gpt-4")

chain = load_summarize_chain(llm, chain_type="refine")

prompt_template = """You are an dilligint research student. Your are given a generated transcript of a lecture on {topic}.\n
Transcript:\
{text}\
Step by step extract all information from the transcript and convert it into a clean and complete document with highlighted key concepts, theories, and definitions.\
Use Markdown formatting. Use a question and answer format that can be used to study with active recall for an exam.\
Do not leave anything out and do not add anyting extra.\
Example Format: (use this intendation as well):\
'''- How does Language facilitate cultural learning?\
    - Language allows humans to clearly communicate ideas, especially complicated ones\
    - Human language is unique in having a complex grammar and syntax, as well as a rich vocabulary\
    - It is necessary for successful and precise transmission of cultural ideas\
        - Allows for cumulative cultural learning'''\
Tone: scientific\
Task:\
    - Use a a question and answer format to extract information from the transcript.\
    - Highlight Key Concepts: Emphasize crucial theories, definitions, and concepts using Markdown formatting like bold or italic.\
    - Ensure Completeness: Incorporate all bullet points, sub-points, and other nested lists from the transcript without omitting any content.\
    - Do Not Add Extra Material: Keep the lecture notes faithful to the original transcript, avoiding any addition, removal, or modification of the substance of the content.\
    - Work Step-by-Step: Methodically work through the transcript, slide by slide, to ensure that the final document is both accurate and complete.\
This task is designed to facilitate the creation of complete set of lecture notes that serve as an effective study and reference tool.\
LECTURE NOTES:"""
prompt = PromptTemplate.from_template(prompt_template)

topic = "Methods of Cultural Psychology"

refine_template = (
    """You are a diligent research student. You are given a generated transcript of a lecture on {topic}.\n
    We are given a question answer style notes up to a point of this lecutre\n
    Existing Q&A Notes: {existing_answer}\n
    Your goal is to continue supplementing the existing Q&A notes with additional context from the continued lecture transcript provided below.\n
    ------------\n
    {text}\n
    ------------\n
    Example Format: (use this intendation as well):\
    '''- How does Language facilitate cultural learning?\
        - Language allows humans to clearly communicate ideas, especially complicated ones\
        - Human language is unique in having a complex grammar and syntax, as well as a rich vocabulary\
        - It is necessary for successful and precise transmission of cultural ideas\
            - Allows for cumulative cultural learning'''\
    Task:\
    - Use a Q&A format to extract information from the transcript.\
    - Highlight Key Concepts: Emphasize crucial theories, definitions, and concepts using Markdown formatting like bold or italic.\
    - Ensure Completeness: Incorporate all bullet points, sub-points, and other nested lists from the transcript without omitting any content.\
    - Do Not Add Extra Material: Keep the lecture notes faithful to the original transcript, avoiding any addition, removal, or modification of the substance of the content.\
    - Work Step-by-Step: Methodically work through the transcript, slide by slide, to ensure that the final document is both accurate and complete.\
This task is designed to facilitate the creation of complete set of lecture notes that serve as an effective study and reference tool."""
)

refine_prompt = PromptTemplate.from_template(refine_template)
chain = load_summarize_chain(
    llm=llm,
    chain_type="refine",
    question_prompt=prompt,
    refine_prompt=refine_prompt,
    return_intermediate_steps=True,
    input_key="input_documents",
    output_key="output_text",
)

result = chain({"input_documents":docs, "topic":topic}, return_only_outputs=False)


intermediate_text = "\n".join(result[''])
output_text = result['output_text']
qa_transcript = f"{intermediate_text}\n\n{output_text}"
with open("qa_transcript.md", "w", encoding="utf-8") as f:
    f.write(qa_transcript)


