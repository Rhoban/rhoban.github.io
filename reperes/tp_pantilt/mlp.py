import torch as th


class MLP(th.nn.Module):
    def __init__(self, input_dimension: int, output_dimension: int):
        super().__init__()

        self.net = th.nn.Sequential(
            th.nn.Linear(input_dimension, 3),
            th.nn.ReLU(),
            th.nn.Linear(3, 3),
            th.nn.ReLU(),
            th.nn.Linear(3, output_dimension),
        )

    def forward(self, x):
        return self.net(x)

    def load(self):
        self.load_state_dict(th.load("weights"))

    def save(self):
        th.save(self.state_dict(), "weights")
