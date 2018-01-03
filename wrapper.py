#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
import numpy as np

import gensim

app = Flask(__name__)

model = None


@app.route('/')
def getWordVector():
    word = request.args.get('word')
    
    if model is None:
        return "No model initialized"
        
    else:    
        if word is not None:
            try:
                nparr = model.wv[word]

                return np.array2string(nparr)
            except:
                return "[]"
        else:
            return "No argument given"


@app.route('/model-size')
def getVocabularySize():
    if model is None:
            return "No model initialized"
        
    else:    
        size = len(model.wv.vocab)

        return str(size)

@app.route('/model/set')    
def setModel():

    global model

    modelSource = request.args.get('model')
    modelIsBinary = request.args.get('not_binary')
    
    if modelIsBinary is not None:
        modelIsBinary = False
    
    else:
        modelIsBinary = True
        
    
    if modelSource is not None:    
        model = gensim.models.KeyedVectors.load_word2vec_format("./model/"+modelSource, binary=modelIsBinary)
        
        return "Model changed to "+modelSource
    
    else:
        return "No argument given"


@app.route('/model/list')    
def listModels():
    return "'german.model' (small german model)\n'GoogleNews-vectors-negative300.bin' (big english model)\n'wiki.de.vec' (big german model - ATTENTION: THIS MODEL IS NOT! IN BINARY FORMAT)"
        

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
