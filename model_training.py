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


# Splitting dataset into training and validation sets

# Training set
x_training = data[:training_set]
y_training = labels[:training_set]

# Validation set
x_validation = data[training_set: training_set + validation_set]
y_validation = labels[training_set: training_set + validation_set]


# Defining callbacks for Keras
callbacks = [
    keras.callbacks.EarlyStopping(
        monitor='val_loss',
        patience=2,
        min_delta=0,
        mode='auto',
        baseline=None,
    ),
    keras.callbacks.ModelCheckpoint(
        filepath='phishing_urls_model.h5',
        monitor='val_loss',
        save_best_only=True,
    )
]

num_chars = len(tokenizer.word_index) + 1
embedding_dim = 128


# Creating the model to train

ml_model = Sequential()

def modelSetup(): # adding model setup inside function for testing
    ml_model.add(Embedding(num_chars, embedding_dim, input_length=max_len))
    ml_model.add(Bidirectional(LSTM(256, dropout=0.3, recurrent_dropout=0.3, return_sequences=True)))
    ml_model.add(Bidirectional(LSTM(256, dropout=0.3, recurrent_dropout=0.3, return_sequences=True)))
    ml_model.add(Bidirectional(LSTM(128, dropout=0.3, recurrent_dropout=0.3)))
    ml_model.add(Dense(1, activation='sigmoid'))
    
modelSetup()
ml_model.summary()

ml_model.compile(
    optimizer='adam', 
    loss='binary_crossentropy', 
    metrics=['accuracy']
)

# Training the model
ml_model.fit(x_training, y_training, epochs=10, batch_size=1200, callbacks=callbacks, validation_split=0.20, shuffle=True)

# Validating the model
val_score, val_acc = ml_model.evaluate(x_validation, y_validation, verbose=1, batch_size=1024)

print(f"Validation Score: {val_score:.2f}")
print(f"Accuracy of the Model: {val_acc * 100:.2f}%")
