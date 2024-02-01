# Wrapper

## Description

An interface through which we can interact with an open source LLM


## Constructor

config: **kwargs
  Named hyperparameters for the model

model_path: string
  path to the model

## Methods

encode: string->torch.tensor
  return a vector representation of the text

predict: string-string
  return text given a prompt

get_vocabulary: void-->string[]
  list of tokens in model vocabulary




# Head

## Description

Pytorch linear neural network that predicts the next word from a distribution


## Constructor

model_wrapper: Wrapper class
  An instance of the wrapper class defined in the Wrapper section.


## Methods

forward: vector-->vector
  Predict the output token as a vector given a vector input from the wrapper class



# RL Pipeline

## Description

Openai gym environment for the pipeline we have discussed.

Documentation can be found at https://www.gymlibrary.dev/content/environment_creation/






