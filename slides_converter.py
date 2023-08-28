import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import ChatPromptTemplate
from langchain.chains.llm import LLMChain

load_dotenv()

################################################### Preprocess #################################################
llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo-16k-0613")


preprocess_prompt = ChatPromptTemplate.from_template(
    """You are an excellent executive assistant.\
        You are given a raw text file containing the lecture notes from a lecture on {topic}.\
        Lecture: {all_slides}\
        Objective:
        Clean up and reformat raw text from lecture slides into a Markdown file. The aim is to produce a well-structured document with slide headers, numbers, and highlighted key concepts, theories, and definitions.\
        Instructions:\
        - Identify Artifacts: Look through the raw text to identify any artifacts that have resulted from the copying process (e.g., unusual characters, repeated sections, etc.) and remove them.\
        - Segment Slides: Divide the cleaned-up text into individual slides, as they were originally presented.\
        - Add Slide Headers and Numbers: Begin each segment with a Markdown-formatted header that includes the slide number and any available slide titles (e.g., ## Slide 1: Introduction).\
        - Highlight Key Concepts: Emphasize important concepts, theories, and definitions. You can make use of Markdown formatting like bold or italic for this purpose.\
        - Ensure Completeness: Do not omit any content from the original raw text. Include all bullet points, sub-points, and other forms of nested lists.\
        - Work Step-by-Step: It is crucial to proceed methodically, slide by slide, to ensure accuracy and completeness.\
        - Do Not Add Extra Material: The conversion should be faithful to the original content. Do not add, remove, or modify the substance of the content.
        CLEAN MARKDOWN: """
)

preprocess_chain = LLMChain(llm=llm, prompt=preprocess_prompt, 
                     output_key="cleaned-slides"
                    )

cleaned_slides = preprocess_chain.run(
    topic="Methods of Cultural Psychology",
    all_slides=all_slides)

with open("cleaned_slides.txt", "w") as f:
    f.write(cleaned_slides)