import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
load_dotenv()

llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo-16k-0613")

chain = load_summarize_chain(llm, chain_type="refine")

prompt_template = """You are an dilligint research student. Your are given slides of a lecture on {topic}.\n
Lecture: {cleaned_slides}\n
Supplement these notes with context from the following transcript of the lecture. Do not leave anything out. 
Identify which slides the speaker giving the lecture is referring to (starting with the first slides, advancing step by step) \
and add all the remarks and points made by the lecturer to the respective slide, if the points are not already explicitly contained in the slide. \
{text}
Format:\
    - *Slide Header and Number*: Clearly mention the slide header along with its number.\
    - *Slide Content*: List the original content of the slide in bullet points. Use Markdown formatting like **bold** or *italic* to emphasize key points.\
    - *Speaker's Remarks*: Include any additional points or elaborations made by the speaker during the lecture, formatted in bullet points.\
Example:\
   Slide 15: **Cumulative Culture?**
    - *Slide Content*:
        - Requires reliable and faithful social transmission.\
        - Requires imitative learning and sophisticated language.\
        - Individual learning through emulative learning does not allow for a ratchet effect across generations.\
- *Speaker's Remarks*:\
        - Cultural fidelity ensures less distortion in passing down beliefs.\
        - Sophisticated language extends beyond mimicry and enables abstract thinking.\
        - The "ratchet effect" signifies incremental cultural growth, which is limited without it.\
Tone: scientific\
Task:\
    - Slide-to-Slide Mapping: Map the content of the transcript to individual slides in a lecture presentation. Identify which points from the transcript correspond to each slide.\
    - Highlight Key Concepts: Emphasize crucial theories, definitions, and concepts using Markdown formatting like bold or italic.\
    - Ensure Completeness: Incorporate all bullet points, sub-points, and other nested lists from the transcript without omitting any content.\
    - Work Step-by-Step: Methodically work through the transcript, slide by slide, to ensure that the final document is both accurate and complete.\
    - Do Not Add Extra Material: Keep the lecture notes faithful to the original transcript, avoiding any addition, removal, or modification of the substance of the content.\
This task is designed to facilitate the creation of an organized set of lecture notes that serve as an effective study and reference tool.\
LECTURE NOTES:"""
prompt = PromptTemplate.from_template(prompt_template)

topic = "Methods of Cultural Psychology"

refine_template = (
    """You are an dilligint research student. Your are given slides of a lecture on {topic}.\n
    Lecture: {cleaned_slides}\n
    Your are provided with a version of the slides that is already supplemented with notes from the speaker transcript of the lecture.\n
    Existing notes with some overlap: {existing_answer}\n
    Additional lecture context is provided below.\n
    Your goal is to continue supplementing the existing slides with the additional lecture transcript provided below in the same manner.\n
    ------------\n
    {text}\n
    ------------\n
    Supplement the existing notes with information from the additional lecture transcript, slide-by-slide. Do NOT omit any details and do NOT make up extra material.\n
    Format:\
        - *Slide Header and Number*: Clearly mention the slide header along with its number.\
        - *Slide Content*: List the original content of the slide in bullet points. Use Markdown formatting like **bold** or *italic* to emphasize key points.\
        - *Speaker's Remarks*: Include any additional points or elaborations made by the speaker during the lecture, formatted in bullet points.\
    Tone: Scientific\
    Task:\
        - Map the new lecture context to existing notes\
        - Emphasize crucial theories, definitions, and concepts\
        - Ensure completeness by incorporating all points from the transcript\
        - Work step-by-step, mapping each part of the lecture to corresponding slides\
    This task is designed to facilitate the creation of an organized set of lecture notes that serve as an effective study and reference tool."""
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

result = chain({"input_documents":docs, "cleaned_slides":cleaned_slides, "topic":topic}, return_only_outputs=False)


intermediate_text = "\n".join(result['intermediate_steps'])
output_text = result['output_text']
combined_text = f"## Intermediate Steps\n{intermediate_text}\n\n## Output Text\n{output_text}"
with open("result_output.md", "w", encoding="utf-8") as f:
    f.write(combined_text)


