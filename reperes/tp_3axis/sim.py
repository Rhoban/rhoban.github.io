import math
import time
import numpy as np
from onshape_to_robot import simulation
from colorama import Fore, Back, Style
from transforms3d.quaternions import mat2quat, quat2mat
import pybullet as p
import pygame
import argparse
import model

sim = simulation.Simulation('rrr/robot.urdf', fixed=True, panels=True)
parser = argparse.ArgumentParser()
parser.add_argument('--mode', '-m', type=str, default='direct')
args = parser.parse_args()
sliders = {}
target = None
joints = sim.getJoints()

if args.mode == 'direct':
    target = p.loadURDF('target2/robot.urdf')
    for joint in joints:
        sliders[joint] = p.addUserDebugParameter(joint, -math.pi, math.pi, 0.0)
elif args.mode == 'inverse' or args.mode =='inverse-iterative':
    target = p.loadURDF('target2/robot.urdf')
    sliders['target_x'] = p.addUserDebugParameter('target_x', -1, 1, 0.4)
    sliders['target_y'] = p.addUserDebugParameter('target_y', -1, 1, 0)
    sliders['target_z'] = p.addUserDebugParameter('target_z', -1, 1, 0.25)
elif args.mode == 'triangle' or args.mode == 'triangle-points':
    sliders['triangle_x'] = p.addUserDebugParameter('triangle_x', 0.01, 0.8, 0.4)
    sliders['triangle_z'] = p.addUserDebugParameter('triangle_z', 0.01, 0.3, 0.2)
    sliders['triangle_h'] = p.addUserDebugParameter('triangle_h', 0.01, 0.3, 0.1)
    sliders['triangle_w'] = p.addUserDebugParameter('triangle_w', 0.01, 0.3, 0.2)
elif args.mode == 'circle' or args.mode == 'circle-points':
    sliders['circle_x'] = p.addUserDebugParameter('circle_x', 0.01, 0.8, 0.4)
    sliders['circle_z'] = p.addUserDebugParameter('circle_z', 0.01, 0.3, 0.2)
    sliders['circle_r'] = p.addUserDebugParameter('circle_r', 0.01, 0.3, 0.1)
    sliders['circle_duration'] = p.addUserDebugParameter('circle_duration', 0.01, 10, 3)

lastLine = time.time()
lastInverse = 0
targets = {'motor'+str(k+1): 0 for k in range(3)}

while True:
    if sim.t > 1.0:
        if args.mode == 'direct':
            for joint in joints:
                targets[joint] = p.readUserDebugParameter(sliders[joint])

            T = model.direct(targets)
            p.resetBasePositionAndOrientation(target, T, [0, 0, 0, 1])

        elif args.mode == 'inverse' or args.mode == 'inverse-iterative':
            x = p.readUserDebugParameter(sliders['target_x'])
            y = p.readUserDebugParameter(sliders['target_y'])
            z = p.readUserDebugParameter(sliders['target_z'])
            p.resetBasePositionAndOrientation(target, [x, y, z], [0, 0, 0, 1])

            if args.mode == 'inverse':
                alphas = model.inverse(x, y, z)
                targets = {'motor1': alphas[0], 'motor2': alphas[1], 'motor3': alphas[2]}
            elif args.mode == 'inverse-iterative':
                if (time.time() - lastInverse) > 0.1:
                    alphas = model.inverseIterative(x, y, z)
                    targets = {'motor1': alphas[0], 'motor2': alphas[1], 'motor3': alphas[2]}

        elif args.mode == 'triangle' or args.mode == 'triangle-points':
            x = p.readUserDebugParameter(sliders['triangle_x'])
            z = p.readUserDebugParameter(sliders['triangle_z'])
            h = p.readUserDebugParameter(sliders['triangle_h'])
            w = p.readUserDebugParameter(sliders['triangle_w'])

            if args.mode == 'triangle-points':
                points = model.trianglePoints(x, z, h, w)
                if time.time() - lastLine > 0.1:
                    lastLine = time.time()
                    p.addUserDebugLine(points[0], points[1], [0,0,1], 2, 0.15)
                    p.addUserDebugLine(points[1], points[2], [0,0,1], 2, 0.15)
                    p.addUserDebugLine(points[2], points[0], [0,0,1], 2, 0.15)
            else:
                    alphas = model.triangle(x, z, h, w, sim.t)
                    targets = {'motor1': alphas[0], 'motor2': alphas[1], 'motor3': alphas[2]}
                    sim.addDebugPosition(model.direct(targets), duration=3)
        
        elif args.mode == 'circle' or args.mode == 'circle-points':
            x = p.readUserDebugParameter(sliders['circle_x'])
            z = p.readUserDebugParameter(sliders['circle_z'])
            r = p.readUserDebugParameter(sliders['circle_r'])
            duration = p.readUserDebugParameter(sliders['circle_duration'])

            if args.mode == 'circle-points':
                points = model.circlePoints(x, z, r)
                if (time.time() - lastLine) > 0.2:
                    lastLine = time.time()

                    N = len(points)
                    for k in range(N):
                        p.addUserDebugLine(points[k], points[(k+1)%N], [0,0,1], 2, 0.5)
            else:
                    alphas = model.circle(x, z, r, sim.t, duration)
                    targets = {'motor1': alphas[0], 'motor2': alphas[1], 'motor3': alphas[2]}
                    sim.addDebugPosition(model.direct(targets), duration=3)
            
            
        sim.setJoints(targets)

    sim.tick()
