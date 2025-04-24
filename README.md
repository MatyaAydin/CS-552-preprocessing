# CS-552-preprocessing


Preprocessing functions for the course CS-552 - Modern natural language processing taught at EPFL.


### Getting started

To get all necessary packages, run the following command
```bash
pip install -r requirements.txt
```

To load `Llama-3.2-1B`, you must agree with the EULA on https://huggingface.co/meta-llama/Llama-3.2-1B. Once this is done, you must create a token on hugging face to authentify when loading the model. The key must be in the file `./keys/HF_KEY.py` with the variable
```python
api_key = "YOURKEY"
```

_Note_: Create a write key, otherwise it does not work ![alt text](image.png)


Similarly, you can do the same with Mistral key.

### Repo structure

* `WS_wikipedia.py`: extract short descriptions about subjects using wikipedia and wikidata. Will be used for the external knowledge of the RAG model.

* `preprocess_mcq.py`: turns an EPFL MCQ exam into a csv with questions-solutions pairs.
**TODO**: extract choices from questions and correct answer from solution, hangle images

* `tryOllama.ipynb`: Attempt to load Llama, you can ignore this