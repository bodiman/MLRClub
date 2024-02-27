import torch.nn as nn
import gymnasium as gym

from openai_gym import spaces

import numpy as np

from model import LinearModel


class TransformerFinetuneEnv(gym.Env):
    def __init__(self, llm, ):
        self.observation_shape = spaces.Discrete(4096)    
        self.action_space = spaces.Discrete(32000)

        self.network = LinearModel()
        

    def step(self, action):
        ...

    """
    Parameters
    ----------

    action: ?
        token to append to the output.

    Returns
    -------

    observation: str
        The updated predicted string.

    reward: float
        The reward for a particular action

    terminated: boolean
        Weather the terminal state has been reached (an end-token is predicted)

    truncated: boolean
        Weather the token limit has been reached (this can be adjusted)

    info: dict
        not sure if this is required


    """
    

    """
    Step: predict the next word in the model

    Reset: reset if the end token hits
    """