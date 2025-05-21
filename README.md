# CS-552-preprocessing


Preprocessing functions for the course CS-552 - Modern natural language processing taught at EPFL.


### Getting started

To get all necessary packages, run the following command
```bash
pip install -r requirements.txt
```


Similarly, you can do the same with Mistral key.

### Repo structure

* `WS_wikipedia.py`: extract short descriptions about subjects using wikipedia and wikidata. Will be used for the external knowledge of the RAG model.

* `preprocess_mcq.py`: turns an EPFL MCQ exam into a csv with questions-solutions pairs.
**TODO**: extract choices from questions and correct answer from solution, hangle images
