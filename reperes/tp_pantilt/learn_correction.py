import model_correction as model
import numpy as np
import torch as th
from torchinfo import summary
import time
from mlp import MLP

net = MLP(2, 2)
# summary(net)
# exit()

batch_size = 256
optimizer = th.optim.Adam(net.parameters(), 1e-3)

for k in range(1024):
    angles = np.random.uniform([-np.pi, 0.2], [np.pi, 1.7], size=(batch_size, 2))
    laser_pos = [model.laser(*angle) for angle in angles]

    angles = th.tensor(angles, dtype=th.float)
    laser_pos = th.tensor(laser_pos, dtype=th.float)

    loss = th.nn.functional.smooth_l1_loss(net(laser_pos), angles)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    print(loss)

net.save() 