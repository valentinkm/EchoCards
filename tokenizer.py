import tiktoken
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
encoding.encode(cleaned_slides)
def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens
num_tokens_from_string(cleaned_slides, "gpt-3.5-turbo")