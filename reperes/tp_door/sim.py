import numpy as np
import time
from world import World
import utils
import behavior

world = World()
robot = world.load_image("robot.png")
dt = 0.05 # s
door_distance = 2.0 # m
door_size = 1.0 # m
ext_margin = 1.0 # m
max_speed = 1  # m/s
max_rotation = 1  # rad/s

while True:
    behavior.STATE = "init"
    A_world = np.random.uniform(-2, 2, 2)
    A_alpha = np.random.uniform(-np.pi, np.pi)
    T_world_wall = utils.frame(A_alpha, *A_world)
    R_world = utils.transform(T_world_wall, *np.random.uniform([-4, -3], [4, -.2]))
    R_alpha = np.random.uniform(-np.pi, np.pi)
    X_world = utils.transform(T_world_wall, *np.random.uniform([-3, .25], [3, 3]))
    B_world = utils.transform(T_world_wall, 5, 0)
    P_world = utils.transform(T_world_wall, door_distance, 0)
    Pin_world = utils.transform(T_world_wall, door_distance, ext_margin)
    Pext_world = utils.transform(T_world_wall, door_distance, -ext_margin)

    while not world.reset():
        T_world_robot = utils.frame(R_alpha, *R_world)
        A_robot = utils.transform(utils.frame_inv(T_world_robot), *A_world)
        B_robot = utils.transform(utils.frame_inv(T_world_robot), *B_world)

        # Retrieving robot speeds
        speed_x, speed_rot = behavior.robot_tick(A_world, B_world, A_robot, B_robot, X_world)

        R_wall = utils.transform(utils.frame_inv(T_world_wall), *R_world)
        delta_x = np.clip(speed_x, -max_speed, max_speed) * dt
        delta_rot = np.clip(speed_rot, -max_rotation, max_rotation) * dt
        R_world = utils.transform(T_world_robot, delta_x, 0.0)
        R_alpha += delta_rot

        # Draw robot
        world.set_image_pose(robot, *R_world, R_alpha)

        # Draw wall
        world.draw_line(
            *utils.transform(T_world_wall, -100, 0),
            *utils.transform(T_world_wall, door_distance - door_size / 2, 0),
            (255, 128, 0),
            5
        )
        world.draw_line(
            *utils.transform(T_world_wall, door_distance + door_size / 2, 0),
            *utils.transform(T_world_wall, 100, 0),
            (255, 128, 0),
            5
        )

        # Drawing frames
        world.draw_frame("w", np.eye(3))
        world.draw_frame("m", T_world_wall)
        world.draw_frame("r", T_world_robot)
        world.draw_point(*X_world, "X")
        world.draw_point(*A_world, "A")
        world.draw_point(*B_world, "B")
        world.draw_point(*P_world, "P")
        world.draw_point(*Pin_world, "Pin")
        world.draw_point(*Pext_world, "Pext")

        time.sleep(dt)
