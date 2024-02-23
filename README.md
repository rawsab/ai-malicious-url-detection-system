# 🕵️ Malicious URL Detection System

![python](https://img.shields.io/badge/Python-3.6.7-blue.svg)

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
