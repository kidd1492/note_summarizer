import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.probability import FreqDist

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
#Create object lemmatizer
lemmatizer = WordNetLemmatizer()

processed_data = []
for line in data:
    words = word_tokenize(line)
    words = [lemmatizer.lemmatize(word.lower()) for word in words if word.isalnum() and word.lower() not in stop_words]
    processed_data.append(' '.join(words))


# Example: Frequency-based summarization
all_words = ' '.join(processed_data).split()
freq_dist = FreqDist(all_words)
summary = freq_dist.most_common(10)  # Top 10 most common words
print("Summary:", summary)
