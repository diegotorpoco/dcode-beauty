from nltk.corpus import stopwords
import spacy
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from dcodebeauty.datos import read_file
from gensim.models import CoherenceModel


products,data,chori_data = read_file()
data = data['description']

stopwords = stopwords.words("english")
ignore_words = ['skin','oil','also','water','ingredient','used','property','work','antioxidant','product','products','formula']



def gen_words(texts):
    final = []
    for text in texts:
        new = gensim.utils.simple_preprocess(text, deacc=True)
        final_words = [word for word in new if not word in ignore_words]
        final.append(final_words)
    return (final)


def lemmatization(texts, allowed_postags=["NOUN"]):
    nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])
    texts_out = []
    for text in texts:
        doc = nlp(text)
        new_text = []
        for token in doc:
            if token.pos_ in allowed_postags:
                new_text.append(token.lemma_)
        final = " ".join(new_text)
        texts_out.append(final)
    return (texts_out)

lemmatized_texts = lemmatization(data)
data_words = gen_words(lemmatized_texts)
id2word = corpora.Dictionary(data_words)


def get_corpus(data_words):
    corpus = []
    for text in data_words:
        new = id2word.doc2bow(text)
        corpus.append(new)
    return corpus
corpus= get_corpus(data_words)