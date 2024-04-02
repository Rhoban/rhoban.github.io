import math
import time
from onshape_to_robot import simulation
import pybullet as p
import model as model
import argparse

sim = simulation.Simulation("pantilt/robot.urdf", fixed=True, panels=True)
parser = argparse.ArgumentParser()
parser.add_argument("--mode", "-m", type=str, default="test")
args = parser.parse_args()
sliders = {}
target = None


def resetBasePositionWithMatrix(target, T):
    t, q = sim.matrixToPose(T)
    p.resetBasePositionAndOrientation(target, t, q)

if args.mode == "direct":
    target = p.loadURDF("frame/robot.urdf")
elif args.mode == "laser":
    target = p.loadURDF("target/robot.urdf")
elif args.mode == "inverse" or args.mode == "inverse_nn":
    target = p.loadURDF("target/robot.urdf")

joints = sim.getJoints()
if args.mode == "board":
    pass
elif args.mode in ["inverse", "inverse_nn"]:
    sliders["target_x"] = p.addUserDebugParameter("target_x", -2, 2, 1.5)
    sliders["target_y"] = p.addUserDebugParameter("target_y", -2, 2, 0)
else:
    for joint in joints:
        sliders[joint] = p.addUserDebugParameter(joint, -math.pi, math.pi, 0.0)

lastLine = time.time()
lastInverse = 0
targets = {"motor1": 0, "motor2": 0}

while True:
    if sim.t > 1.0:

        joints = sim.getJoints()
        if args.mode not in ["inverse", "inverse_nn"]:
            for joint in joints:
                targets[joint] = p.readUserDebugParameter(sliders[joint])

        if args.mode == "direct":
            T = model.direct(*list(targets.values()))
            resetBasePositionWithMatrix(target, T)

        elif args.mode == "laser":
            pos = model.laser(*list(targets.values()))
            if pos is not None:
                m = model.direct(*list(targets.values()))
                T = m.T[3, :3]
                p.resetBasePositionAndOrientation(target, [pos[0], pos[1], 0.0], [0, 0, 0, 1])

                if time.time() - lastLine > 0.1:
                    lastLine = time.time()
                    p.addUserDebugLine(list(T), [pos[0], pos[1], 0.0], [1.0, 0.0, 0.0], 1, 0.15)

        elif args.mode == "inverse" or args.mode == "inverse_nn":
            x = p.readUserDebugParameter(sliders["target_x"])
            y = p.readUserDebugParameter(sliders["target_y"])
            p.resetBasePositionAndOrientation(target, [x, y, 0.0], [0, 0, 0, 1])

            if args.mode == "inverse":
                angles = model.inverse(x, y)
            else:
                angles = model.inverse_nn(x, y)
            targets = {"motor1": angles[0], "motor2": angles[1]}

        sim.resetJoints(targets)

    sim.tick()
