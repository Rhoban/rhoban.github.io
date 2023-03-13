import matplotlib.pyplot as plt
import model_correction as model
import numpy as np
import torch as th
from mlp import MLP

net = MLP(1, 1)

optimizer = th.optim.Adam(net.parameters(), 1e-3)
xs = np.linspace(0, 5, 1000)
ys = np.sin(xs)*2.5 + 1.5

xs = th.tensor(xs, dtype=th.float).view(-1, 1)
ys = th.tensor(ys, dtype=th.float).view(-1, 1)
step = 0

while True:
    # Showing
    plt.clf()
    plt.plot(xs.numpy(), ys.numpy(), label="sin(x)*2.5 + 1.5")
    with th.no_grad():
        plt.scatter(xs, net(xs).numpy(), label="Neural network", color="orange")
    plt.legend()
    plt.grid()
    plt.title(f"Iteration #{step}")
    plt.pause(1e-3)

    # Training
    loss = th.nn.functional.mse_loss(net(xs), ys)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    print(loss)
    step += 1


        
