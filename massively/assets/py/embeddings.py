import re
from gensim.models import Word2Vec
from nltk.corpus import stopwords

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    return text

def preprocess_text(text):
    # Regular expression to find words
    words = re.findall(r'\b\w+\b', text)
    
    # Load stopwords
    stop_words = set(stopwords.words('english')) | {"said", "one", "would", "also", "ive", "unfolded", "time"}
    
    # Filter stopwords and digits
    filtered_words = [word for word in words if word not in stop_words and not word.isdigit()]
    return filtered_words

def train_word2vec(tokens):
    # Word2Vec parameters
    params = {
        'vector_size': 100,
        'window': 5,
        'min_count': 2,
        'workers': 4,
        'sg': 0,
        'seed': 42
    }
    # Training the model
    model = Word2Vec([tokens], **params)
    return model

def main():
    file_path = 'massively/assets/py/txt/NYT012021.txt'  # Update this path
    text = load_data(file_path)
    tokens = preprocess_text(text)
    model = train_word2vec(tokens)
    
    # Displaying the vocabulary size and some similar words examples
    print("Vocabulary Size:", len(model.wv.key_to_index))
    if 'floyd' in model.wv.key_to_index:
        print("Words similar to 'floyd':", model.wv.most_similar('floyd', topn=10))

if __name__ == "__main__":
    main()
