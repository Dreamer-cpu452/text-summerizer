import nltk
import networkx as nx

from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('punkt_tab')

def generate_summary(text, ratio=0.6):
    sentences = sent_tokenize(text)

    total_sentences = len(sentences)

    if total_sentences <= 5:
        return text

    summary_count = max(
    3,
    int(total_sentences * ratio)
)
    vectorizer = TfidfVectorizer(stop_words='english')

    tfidf_matrix = vectorizer.fit_transform(sentences)

    similarity_matrix = cosine_similarity(tfidf_matrix)

    graph = nx.from_numpy_array(similarity_matrix)

    scores = nx.pagerank(graph)

    ranked = []

    for i, sentence in enumerate(sentences):
        ranked.append((scores[i], i, sentence))

    top_sentences = sorted(
        ranked,
        reverse=True
    )[:summary_count]

    top_sentences = sorted(
        top_sentences,
        key=lambda x: x[1]
    )

    first_sentence = sentences[0]
    last_sentence = sentences[-1]

    selected_sentences = [s[2] for s in top_sentences]

    if first_sentence not in selected_sentences:
        selected_sentences.insert(0, first_sentence)

    if last_sentence not in selected_sentences:
        selected_sentences.append(last_sentence)

    summary = "\n\n".join(selected_sentences)

    return summary