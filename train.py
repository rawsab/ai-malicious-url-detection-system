# Train the model on the dataset from PhishTank

import numpy as np
import keras

from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense, Embedding, Flatten, Bidirectional, Activation, Dropout, BatchNormalization, GRU, LSTM
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

import data_preprocessed

# Processing URL data and labels for training
url_set = data_preprocessed.main()

sample_set = []
label_set = []

for key, value in url_set.items():
    sample_set.append(key)
    label_set.append(value)


# Printing the number of non-malicious and malicious URLs
print(label_set.count(0))
print(label_set.count(1))


# Tokenizing the URL data

max_chars = 20000
max_len = 128

tokenizer = Tokenizer(num_words=max_chars, char_level=True)
tokenizer.fit_on_texts(sample_set)
sequences = tokenizer.texts_to_sequences(sample_set)
word_index = tokenizer.word_index

data = pad_sequences(sequences, maxlen=max_len) # Padding the sequences
labels = np.array(label_set) # Converting the labels to a numpy array

print('Number of unique tokens found: %s' % len(word_index))
print('Shape of data tensor:', data.shape)
print('Shape of label tensor:', labels.shape)


# Dividing the data into training and validation sets

training_set = int(len(sample_set) * 0.95)
validation_set = int(len(sample_set) * 0.05)

print(f"Training set: {training_set}, Validation set: {validation_set}")

indices = np.arange(data.shape[0])
np.random.shuffle(indices) # Shuffling the data

# Rearranging the data and labels to match shuffled indices
data = data[indices]
labels = labels[indices]