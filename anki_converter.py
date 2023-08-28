def reformat_for_anki_multiple(input_text):
    qa_pairs = input_text.strip().split("\n\n")
    anki_formatted_list = []

    for qa_pair in qa_pairs:
        lines = qa_pair.split("\n")
        question = lines[0].strip("**")
        answers = lines[1:]
        formatted_answers = "<ul>"

        for answer in answers:
            formatted_answers += f"<li>{answer.strip('- ').strip()}</li>"
        formatted_answers += "</ul>"

        anki_text = f"{question};{formatted_answers}"
        anki_formatted_list.append(anki_text)
    
    return anki_formatted_list

anki_formatted_list = reformat_for_anki_multiple(qa_transcript)

with open('anki_import.txt', 'w', encoding='utf-8') as f:
    for item in anki_formatted_list:
        f.write(f"{item}\n")

