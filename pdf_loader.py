all_slides = ""

for i, page in enumerate(pages):
    all_slides += f"Page {i + 1}:\n"
    all_slides += page.page_content
    all_slides += "\n\n"

with open("all_slides.txt", 'w') as f:
    f.write(all_slides)