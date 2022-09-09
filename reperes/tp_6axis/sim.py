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

sim = simulation.Simulation('6axis/robot.urdf', fixed=True, panels=True)
parser = argparse.ArgumentParser()
parser.add_argument('--mode', '-m', type=str, default='test')
args = parser.parse_args()
sliders = {}
target = None

if args.mode == 'direct':
    target = p.loadURDF('frame/robot.urdf')
elif args.mode == 'laser':
    target = p.loadURDF('target/robot.urdf')
elif args.mode == 'camera' or args.mode == 'camera2':
    target = p.loadURDF('target2/robot.urdf')
    sliders['target_x'] = p.addUserDebugParameter('target_x', -2, 2, 1)
    sliders['target_y'] = p.addUserDebugParameter('target_y', -2, 2, 0)
    sliders['target_z'] = p.addUserDebugParameter('target_z', -2, 2, 0)
    sliders['aperture'] = p.addUserDebugParameter('aperture', 5, 95, 60)

    imgSize = 200
    pygame.init()
    window = pygame.display.set_mode((imgSize, imgSize))
    pygame.display.set_caption('Camera')

joints = sim.getJoints()
if args.mode == 'inverse':
    sliders['target_x'] = p.addUserDebugParameter('target_x', -2, 2, 1.5)
    sliders['target_y'] = p.addUserDebugParameter('target_y', -2, 2, 0)
    sliders['target_z'] = p.addUserDebugParameter('target_z', 0, 2, 1)
    sliders['target_yaw'] = p.addUserDebugParameter('target_yaw', -math.pi, math.pi, 0)
    sliders['target_pitch'] = p.addUserDebugParameter('target_pitch', -math.pi, math.pi, 0)
    sliders['target_roll'] = p.addUserDebugParameter('target_roll', -math.pi, math.pi, 0)

    target = p.loadURDF('frame/robot.urdf')
else:
    for joint in joints:
        sliders[joint] = p.addUserDebugParameter(joint, -math.pi, math.pi, 0.0)
    
lastLine = time.time()
lastInverse = 0
targets = {'r'+str(k+1): 0 for k in range(6)}

while True:
    if sim.t > 1.0:

        joints = sim.getJoints()
        if args.mode != 'inverse':
            for joint in joints:
                targets[joint] = p.readUserDebugParameter(sliders[joint])

        if args.mode == 'direct':
            m = model.direct(list(targets.values()))
            R = m[0:3,0:3]
            T = m.T[3,:3]
            Q = mat2quat(R)
            p.resetBasePositionAndOrientation(target, list(T), [Q[1], Q[2], Q[3], Q[0]])
            
        elif args.mode == 'laser':
            pos = model.laser(list(targets.values()))
            if pos is not None:
                m = model.direct(list(targets.values()))
                T = m.T[3,:3]
                p.resetBasePositionAndOrientation(target, [pos[0], pos[1], 0.0], [0, 0, 0, 1])

                if time.time() - lastLine > 0.1:
                    lastLine = time.time()
                    p.addUserDebugLine(list(T), [pos[0], pos[1], 0.0], [1.0, 0.0, 0.0], 1, 0.15)

        elif args.mode == 'camera' or args.mode == 'camera2':
            target_x = p.readUserDebugParameter(sliders['target_x'])
            target_y = p.readUserDebugParameter(sliders['target_y'])
            target_z = p.readUserDebugParameter(sliders['target_z'])
            aperture = p.readUserDebugParameter(sliders['aperture'])
            pos = [target_x, target_y, target_z]
            p.resetBasePositionAndOrientation(target, pos, [0, 0, 0, 1])
            view = model.camera(list(targets.values()), pos, imgSize, np.deg2rad(aperture))
            
            window.fill((200, 200, 200))
            pygame.draw.line(window, (150,150,150), (imgSize/2,0), (imgSize/2,imgSize), 1)
            pygame.draw.line(window, (150,150,150), (0,imgSize/2), (imgSize,imgSize/2), 1)
            pygame.draw.circle(window, (150,0,0), (int(view[0]+imgSize/2),int(imgSize/2 - view[1])), int(view[2]))
            pygame.display.flip()

            if args.mode == 'camera2' and time.time() - lastLine > 0.5:
                lastLine = time.time()
                corners = model.camera2(list(targets.values()), np.deg2rad(aperture))
                for corner in corners:
                    if corner is not None:
                        m = model.direct(list(targets.values()))
                        T = m.T[3,:3]
                        p.addUserDebugLine(list(T), list(corner), [0.0, 0.0, 1.0], 1, 0.55)
                attach = ((0,1), (1,2), (2,3), (3,0))
                for entry in attach:
                    if corners[entry[0]] is not None and corners[entry[1]] is not None:
                        p.addUserDebugLine(list(corners[entry[0]]), list(corners[entry[1]]), [0.0, 0.0, 1.0], 1, 0.55)

        elif args.mode == 'inverse':
            x = p.readUserDebugParameter(sliders['target_x'])
            y = p.readUserDebugParameter(sliders['target_y'])
            z = p.readUserDebugParameter(sliders['target_z'])
            yaw = p.readUserDebugParameter(sliders['target_yaw'])
            pitch = p.readUserDebugParameter(sliders['target_pitch'])
            roll = p.readUserDebugParameter(sliders['target_roll'])
            
            m = model.inverseTarget(x, y, z, yaw, pitch, roll)
            R = m[0:3,0:3]
            T = m.T[3,:3]
            Q = mat2quat(R)
            p.resetBasePositionAndOrientation(target, list(T), [Q[1], Q[2], Q[3], Q[0]])

            if (time.time() - lastInverse) > 0.05:
                lastInverse = time.time()
                values = model.inverse(list(targets.values()), x, y, z, yaw, pitch, roll)
                targets = {'r'+str(k+1): values[k] for k in range(6)}

        sim.resetJoints(targets)

    sim.tick()