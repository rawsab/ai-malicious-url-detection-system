# Train the model on the dataset from PhishTank

import data_preprocessed
import numpy as np
import keras
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense, Embedding, Flatten, Bidirectional, Activation, Dropout, BatchNormalization, GRU, LSTM
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

