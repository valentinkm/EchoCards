from langchain.prompts import PromptTemplate

prompt_template = """You are an dilligint research student. Your are given a generated transcript of a lecture on {topic}.\n
Transcript:\n
{text}\
Step by step extract all information from the transcript and convert it into a clean and complete document with highlighted key concepts, theories, and definitions.\
Use Markdown formatting. Use a question and answer format that can be used to study with active recall for an exam.\
Do not leave anything out and do not add anyting extra.\n
Example Format: (use this intendation as well):\n
'''- How does Language facilitate cultural learning?\n
    - Language allows humans to clearly communicate ideas, especially complicated ones\n
    - Human language is unique in having a complex grammar and syntax, as well as a rich vocabulary\n
    - It is necessary for successful and precise transmission of cultural ideas\n
        - Allows for cumulative cultural learning\n\n'''
Tone: scientific\n
Task:\n
    - Use a a question and answer format to extract information from the transcript.\n
    - Highlight Key Concepts: Emphasize crucial theories, definitions, and concepts using Markdown formatting like bold or italic.\
    - Ensure Completeness: Incorporate all bullet points, sub-points, and other nested lists from the transcript without omitting any content.\
    - Do Not Add Extra Material: Keep the lecture notes faithful to the original transcript, avoiding any addition, removal, or modification of the substance of the content.\
    - Work Step-by-Step: Methodically work through the transcript, slide by slide, to ensure that the final document is both accurate and complete.\
This task is designed to facilitate the creation of complete set of lecture notes that serve as an effective study and reference tool.\
LECTURE NOTES:"""
prompt = PromptTemplate.from_template(prompt_template)

refine_template = (
    """You are a diligent research student. You are given a generated transcript of a lecture on {topic}.\n
    We are given a question answer style notes up to a point of this lecutre\n
    Existing Q&A Notes: {existing_answer}\n
    Your goal is to continue supplementing the existing Q&A notes with additional context from the continued lecture transcript provided below.\n
    ------------\n
    {text}\n
    ------------\n
    Example Format: (use this intendation as well):\n
    '''- How does Language facilitate cultural learning?\n
        - Language allows humans to clearly communicate ideas, especially complicated ones\n
        - Human language is unique in having a complex grammar and syntax, as well as a rich vocabulary\n
        - It is necessary for successful and precise transmission of cultural ideas\n
            - Allows for cumulative cultural learning'''\n
    Task:\n
    - Use a Q&A format to extract information from the transcript.\n
    - Highlight Key Concepts: Emphasize crucial theories, definitions, and concepts using Markdown formatting like bold or italic.\
    - Ensure Completeness: Incorporate all bullet points, sub-points, and other nested lists from the transcript without omitting any content.\
    - Do Not Add Extra Material: Keep the lecture notes faithful to the original transcript, avoiding any addition, removal, or modification of the substance of the content.\
    - Work Step-by-Step: Methodically work through the transcript, slide by slide, to ensure that the final document is both accurate and complete.\
This task is designed to facilitate the creation of complete set of lecture notes that serve as an effective study and reference tool."""
)

refine_prompt = PromptTemplate.from_template(refine_template)