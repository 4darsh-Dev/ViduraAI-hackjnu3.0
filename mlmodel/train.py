import pandas as pd
import numpy as np

import json

train_file = "F:/backup-kali/Hackathons/ViduraAI/datasets/train.json"

with open(train_file) as f:
    train = json.load(f)

test_file = "F:/backup-kali/Hackathons/ViduraAI/datasets/test.json"

with open(test_file) as f:
    test = json.load(f)



import logging 

from simpletransformers.question_answering import QuestionAnsweringModel, QuestionAnsweringArgs

# selecting the model type
model_type = "bert"
model_name = "bert-base-cased"

if model_type == "bert":
    model_name = "bert-base-cased"

# Configure the model
model_args = QuestionAnsweringArgs()

model_args.train_batch_size = 32
model_args.evaluate_during_training = True
model_args.n_best_size = 3
model_args.num_train_epochs = 5
model_args.learning_rate = 1e-5


# Advanced methodology

train_args = {
    'learning_rate': 1e-5,
    'overwrite_output_dir': True,
    'reprocess_input_data': True,
    'use_cached_eval_features': True,
    'output_dir': f'outputs/{model_type}',
    'best_model_dir': f'outputs/{model_type}/best_model',
    'evaluate_during_training': True,
    'max_seq_length': 128,
    'num_train_epochs': 5,
    'train_batch_size': 32,
    'evaluate_during_training_steps': 1000,
    'wandb_project': 'Question Answering using BERT',
    'wandb_kwargs': {"name" : model_name},

    'save_model_every_epoch': False,
    'save_eval_checkpoints': False,
    'n_best_size': 3,

    'train_batch_size': 128,
    'eval_batch_size': 64,



    
}

# Initialize the model

model = QuestionAnsweringModel(model_type, model_name, args=train_args)

model.train_model(train, eval_data=test)







    



