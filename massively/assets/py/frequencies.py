from collections import Counter
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

# Download NLTK stopwords (if not already downloaded)
nltk.download('stopwords')
nltk.download('punkt')

# Define a set of stop words
stop_words = set(stopwords.words('english'))

# Add custom stop words
custom_stop_words = {'said', 'minneapolis', 'get', 'make', 'first', 'adams', 'need', 'help', 'last', 'use', 'times', 'former', 'angeles', 'photograph', 'including', 'among', 'states', 'could', 'mr', 'back', 'los', 'department', 'york', 'la', 'que', 'en', 'many', 'el', 'enlarge', 'de', 'image', 'like', 'may', 'think', 'state', 'going', 'dont', 'years', 'way', 'writer', 'know', 'staff', 'time', 'st', 'new', 'us', 'minnesota', 'twin', 'paul', 'cities', 'company', 'one', 'street', 'publication', 'document', 'star', 'tribune', 'minn', 'news', 'is', 'people', 'since', 'thursday', 'wednesday', 'even', 'also', 'say', 'ago', 'day', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'monday', 'tuesday', 'friday', 'saturday', 'sunday', 'week', 'month', 'year', 'today', 'tomorrow', 'would', 'city', 'george', 'floyd', 'floyds'}
stop_words.update(custom_stop_words)

# Read the corpora from external file
corpora_file = 'massively/assets/py/txt/ST052021.txt'

with open(corpora_file, 'r') as file:
    file_contents = file.read()

# Use regex to extract text between "Full text:" and "Subject:"
matches = re.findall(r'Full text:(.*?)Subject:', file_contents, re.DOTALL)
full_text = ' '.join(matches)

# Replace occurrences of "officer" with "police"
full_text = full_text.replace("officer", "police")
full_text = full_text.replace("polices", "police")
full_text = full_text.replace("trumps", "trump")
full_text = full_text.replace("protest", "protests")
full_text = full_text.replace("protestss", "protests")

# Remove all punctuationb
full_text = re.sub(r'[^\w\s]', '', full_text)

# Tokenize the text into words
words = word_tokenize(full_text)

# Remove stop words and convert to lowercase
filtered_words = [word.lower() for word in words if word.lower() not in stop_words]

# Count word frequencies
word_counts = Counter(filtered_words)

# Count the frequency of "murder" in the text
appeals_count = word_counts.get("appeals", 0)
attorney_count = word_counts.get("attorney", 0)
binns_count = word_counts.get("binns", 0)
black_count = word_counts.get("black", 0)
building_count = word_counts.get("building", 0)
cahill_count = word_counts.get("cahill", 0)
case_count = word_counts.get("case", 0)
change_count = word_counts.get("change", 0)
chauvin_count = word_counts.get("chauvin", 0)
community_count = word_counts.get("community", 0)
council_count = word_counts.get("council", 0)
court_count = word_counts.get("court", 0)
crime_count = word_counts.get("crime", 0)
death_count = word_counts.get("death", 0)
evidence_count = word_counts.get("evidence", 0)
family_count = word_counts.get("family", 0)
federal_count = word_counts.get("federal", 0)
fonteno_count = word_counts.get("fonteno", 0)
freeman_count = word_counts.get("freeman", 0)
houston_count = word_counts.get("houston", 0)
jurors_count = word_counts.get("jurors", 0)
justice_count = word_counts.get("justice", 0)
killing_count = word_counts.get("killing", 0)
lake_count = word_counts.get("lake", 0)
lane_count = word_counts.get("lane", 0)
law_count = word_counts.get("law", 0)
man_count = word_counts.get("man", 0)
march_count = word_counts.get("march", 0)
murder_count = word_counts.get("murder", 0)
nelson_count = word_counts.get("nelson", 0)
night_count = word_counts.get("night", 0)
park_count = word_counts.get("park", 0)
police_count = word_counts.get("police", 0)
prosecutors_count = word_counts.get("prosecutors", 0)
protests_count = word_counts.get("protests", 0)
public_count = word_counts.get("public", 0)
racial_count = word_counts.get("racial", 0)
rhodes_count = word_counts.get("rhodes", 0)
center_count = word_counts.get("center", 0)
thao_count = word_counts.get("thao", 0)
trial_count = word_counts.get("trial", 0)
trump_count = word_counts.get("trump", 0)
video_count = word_counts.get("video", 0)
walz_count = word_counts.get("walz", 0)
white_count = word_counts.get("white", 0)
work_count = word_counts.get("work", 0)



# Get top 20 most common words
top_20_words = word_counts.most_common(20)

# Print the top 20 most common words
print("Top 20 words most used in connection to 'George Floyd':")
for word, count in top_20_words:
    print(f"{word}: {count}")



