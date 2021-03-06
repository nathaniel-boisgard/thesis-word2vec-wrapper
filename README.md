# Word2Vec Wrapper

A simple, Python-based and dockerized wrapper to access word2vec vectors from pretrained models.

## Usage

1. Build Docker image (e.g. `$ docker build -t "word2vec-wrapper" .`) 
2. Run Docker image and map ports (Docker image uses 5000) and mount a volume containing pretrained word2vec models (e.g. `docker run -p 5000:5000 -v ~/w2cmodels:/app/model word2vec-wrapper`)
3. Load model by navigating to `[HOST]:[PORT]/model/set?model=[model filename]` (e.g. http://localhost:5000/model/set?model=GoogleNews-vectors-negative300.bin). If the model is NOT in binary format, please use the "not_binary" GET paramter (any value will suffice, e.g. &not_binary=1)
4. Get word vectors by GETting `[HOST]:[PORT]/?word=[your word]` (e.g. `$ curl -XGET http://localhost:5000/?word=president`). If word is not amongst vocabulary, an empty vector is returned
