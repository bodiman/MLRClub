import torch.nn as nn
import gymnasium as gym


class Environment(gym.Env):
    def __init__(self, llm, ):
        self.action_space = None
        self.observation_space = None

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
    def step(self):
        ...
    

    """
    Step: predict the next word in the model

    Reset: reset if the end token hits
    """