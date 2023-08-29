def qa2anki(input_text):
    anki_formatted_list = []
    
    buffer = []
    
    for line in input_text.strip().split("\n"):
        if line.startswith("**"):  # This line is a new question
            if buffer:  # If the buffer is not empty, save the previous question-answer pair
                question = buffer[0]
                answers = buffer[1:]
                formatted_answers = "<ul>"  # Start the list
                for answer in answers:
                    stripped_answer = answer.strip('- ').strip()
                    if stripped_answer:  # Only append if not empty or whitespace
                        formatted_answers += f"<li>{stripped_answer}</li>"
                formatted_answers += "</ul>"  # End the list
                anki_text = f"{question};{formatted_answers}"
                anki_formatted_list.append(anki_text)
                buffer = []  # Clear the buffer
            buffer.append(line.strip("**"))  # Add the new question to the buffer
        else:
            buffer.append(line.strip())  # Add the answer line to the buffer
    
    # save the last question-answer pair
    if buffer:
        question = buffer[0]
        answers = buffer[1:]
        formatted_answers = "<ul>"  # Start the list
        for answer in answers:
            stripped_answer = answer.strip('- ').strip()
            if stripped_answer:  # Only append if not empty or whitespace
                formatted_answers += f"<li>{stripped_answer}</li>"
        formatted_answers += "</ul>"  # End the list
        anki_text = f"{question};{formatted_answers}"
        anki_formatted_list.append(anki_text)

    # Join the list into a single string with each card on a new line
    anki_formatted_text = '\n'.join(anki_formatted_list)
    
    return anki_formatted_text