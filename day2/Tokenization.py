import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt', quiet=True)

def select_creativity_level(text):
    tokens = word_tokenize(text)
    token_length = len(tokens)

    if token_length <= 5:
        creativity_level = 0.2
        style = "factual"
    elif token_length <= 15:
        creativity_level = 0.6
        style = "balanced"
    else:
        creativity_level = 0.9
        style = "creative"

    return creativity_level, style, token_length


text = "Tokenization using GenAI by control parameters is important for generating different types of responses."

creativity_level, style, token_length = select_creativity_level(text)

print("Token count:", token_length)
print("Creativity level:", creativity_level)
print("Response style:", style)
