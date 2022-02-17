import io
import os
import torch
import pandas as pd
from tqdm.notebook import tqdm
from torch.utils.data import Dataset, DataLoader
from ml_things import plot_dict, plot_confusion_matrix, fix_text
from sklearn.metrics import classification_report, accuracy_score
from transformers import (set_seed,
                          TrainingArguments,
                          Trainer,
                          GPT2Config,
                          GPT2Tokenizer,
                          AdamW, 
                          get_linear_schedule_with_warmup,
                          GPT2ForSequenceClassification,
                          pipeline)

import random
import time

pipelina=pipeline("text-classification",model="modeltestvec_huggingface",)
print("model nacten, api ready")


# import main Flask class and request object
from flask import Flask, request

# create the Flask app
app = Flask(__name__)



@app.route('/classify', methods=[ 'POST'])
def classify():
    tic = time.perf_counter()
    data=request.form.get('text')
    print(data)
    try:
        test=str(pipelina(data))
        toc = time.perf_counter()
        print(f"cas{toc - tic:0.4f} seconds")
        return test
    except:
        return "oof"

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
