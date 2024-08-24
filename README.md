# 🕵️ Malicious URL Detection System

![python](https://img.shields.io/badge/Python-3.6.7-blue.svg)

A binary classification model to detect malicious URLs using a Bidirectional LSTM network. In response to the prevalent cyber-threat of phishing attacks, this project applies deep learning to natural language processing (NLP) to effectively detect potential phishing attacks.

<!--
<p align="center">
  <img width="400" src="https://mermaid.ink/img/pako:eNqFk01v2zAMhv8KoXMyrCk2DB4wILHTryVAMbs9zM6BtRhbiCx5khwgK_rfq0jevEswnSSK70OKpF5ZrTmxhDUG-xaK7GulwK9lmaFDSLWUVDuhVQJPPzYWUHHY4AtJC3ujO3hshW0LVIcdzOffYFUW-kBK_MaoSbU6knFR6zTk9GsgVZPdxTCroErLR-RcqCaBtbKDIVhKOfkCekuOHcGGVOPaUZsGbVYWBoWaP6MUPESFvJfCjU5ZcFqX6-6FQgif_YnMlNkUxaeXkbIEz_7F2vxJcR0IN-VKcGFiLVDCJi-2EQVXCSw-fYYnJZydQWZ0rwcHHz9cj4CbALi9DFj8B3AbAHeXAdcJXC2-XAbcBcB9GZ83FiAXTacFh6UHHmPh9trASig0J0glWiv2og43I-c-cB5ixWO70MgT5E73_bm25-nY-nmSkLZUH3otlPP2Uf4Q5N_LqVUecEQ5oCPw4f9tIbkdm7GOTIeC-_F8PSMq5lrqqGKJ33I0h4pV6s374eB0flI1S5wZaMaMHpqWJXuU1p-G3lMpE-hnvPtr7VH91Ho6Exe-69v4G8KneHsH3WwEIA?type=png">
</p>
-->

![nlp_maliciousurldetect_diagram_rawsab](https://github.com/user-attachments/assets/a9d181e7-3498-4fba-9cfe-524390ddad8a)


## ⚙️ Requirements

[Install python](https://www.python.org/downloads/) and the required libraries (must have [pip](https://packaging.python.org/en/latest/tutorials/installing-packages/) installed). Ensure that the repository is downloaded and the command is run in the appropriate directory:

```
$ pip install -r install-libraries.txt
```

## 🖥️ Running the System

Once the model is downloaded (updated .h5 model will be uploaded soon), run the following:
```
$ python flask_rest_api.py
```

Next, open a new tab or window and run the following, replacing https://www.https://phishtank.org/faq.php with a URL (non-base URL) of your choice:
```
$ python3 flask_request.py -u https://www.https://phishtank.org/faq.php
```

Expected Output:
```
$ [{'Prediction Result': 3.228831036385466, 'Malicious URL Probability': 'The URL provided is not likely to be malicious.', 'url': ' https://www.https://phishtank.org/faq.php'}]

```
