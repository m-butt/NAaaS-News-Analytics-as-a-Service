import os
from mlflow import log_metric, log_params
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
from sklearn.decomposition import LatentDirichletAllocation
import nltk
from nltk.corpus import wordnet
from sklearn.preprocessing import MinMaxScaler

nltk.download('wordnet')

def calculate_similarity_score(word, topic_list):
    similarity_scores = []

    # Calculate similarity score for each topic
    for topic in topic_list:
        word_synsets = wordnet.synsets(word)
        topic_synsets = wordnet.synsets(topic)

        if word_synsets and topic_synsets:
            similarity = word_synsets[0].wup_similarity(topic_synsets[0])
        else:
            similarity = 0
        similarity_scores.append(similarity)

    # Perform min-max scaling on the similarity scores
    scaler = MinMaxScaler(feature_range=(0, 1))
    normalized_scores = scaler.fit_transform([[score] for score in similarity_scores])
    normalized_scores = [score[0] for score in normalized_scores]

    return normalized_scores

def preprocess_text(text):
    # Tokenize the text
    tokens = text.lower().split()

    # Remove stopwords
    stopwords = set(['a', 'an', 'the', 'and', 'but', 'to', 'of', 'at', 'in', 'on', 'with', 'for', 'by', 'from', 'said'])
    tokens = [token for token in tokens if token not in stopwords]

    # Join the tokens back into a string
    preprocessed_text = ' '.join(tokens)

    return preprocessed_text

def Lda(articles, num_topics=1, num_words=1, max_df=0.90, min_df=1):
    """Apply Latent Dirichlet Allocation to the articles and return the topics"""
    vectorizer = TfidfVectorizer(max_df=max_df, min_df=min_df, stop_words='english')
    X = vectorizer.fit_transform(articles)
    feature_names = vectorizer.get_feature_names_out()
    lda = LatentDirichletAllocation(n_components=num_topics, max_iter=10, random_state=10).fit(X)
    topics = []
    for topic_idx, topic in enumerate(lda.components_):
        topic_words = [feature_names[i] for i in topic.argsort()[:-num_words - 1:-1]]
        topics.extend(topic_words)
    return topics

def topic_model_nmf(articles, num_topics=1, num_words=1, max_df=0.90, min_df=1):
    """Apply Non-negative Matrix Factorization to the articles and return the topics"""
    vectorizer = TfidfVectorizer(max_df=max_df, min_df=min_df, stop_words='english')
    X = vectorizer.fit_transform(articles)
    feature_names = vectorizer.get_feature_names_out()
    nmf = NMF(n_components=num_topics, max_iter=1000, random_state=10).fit(X)
    topics = []
    for topic_idx, topic in enumerate(nmf.components_):
        topic_words = [feature_names[i] for i in topic.argsort()[:-num_words - 1:-1]]
        topics.extend(topic_words)
    return topics

def extract_topics(details):
    topics_nmf = topic_model_nmf(list(preprocess_text(details).split(" ")), num_topics=3, num_words=3)
    topics_lda = Lda(list(preprocess_text(details).split(" ")), num_topics=3, num_words=3)
    topics = [topic for topic in topics_lda if topic
        topics = [topic for topic in topics_lda if topic in topics_nmf]
    return topics

if __name__ == "__main__":
    file_path = "para.txt"  # Path to the text file
    try:
        with open(file_path, 'r') as file:
            data = file.read()  # Read the contents of the file into a string
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"Error reading the file '{file_path}'.")

    list_ = extract_topics(data)
    score = calculate_similarity_score("terrorism", list_)
    score = sum(score)
    print(score)
    with open("test.txt", "w") as f:
        f.write(str(score))

    log_params({"max_df_topic_model_nmf": 0.90, "max_df_Lda_": 0.90})

    # Log a metric; metrics can be updated throughout the run
    log_metric("accuracy", score)

    with open("test.txt", "w") as f:
        f.write(str(score))
