import numpy as np



def generate_car_data(filename, initial_pose, velocities_and_angles):

    """

    Generates a text file with the car's initial pose and subsequent velocities and angles.

    

    :param filename: Name of the file to be generated.

    :param initial_pose: Tuple (x, y, heading_angle) representing the car's initial pose.

    :param velocities_and_angles: List of tuples [(forward_velocity, steering_angle), ...].

    """

    with open(filename, 'w') as file:

        # Write the initial pose

        file.write(f"{initial_pose[0]},{initial_pose[1]},{initial_pose[2]}\n")

        

        # Write the velocities and angles

        for velocity, angle in velocities_and_angles:

            file.write(f"{velocity},{angle}\n")



# Different paths

paths = [

    {

        'filename': 'path1.txt',

        'initial_pose': (0, 0, 0.0),

        'velocities_and_angles': [

            (1.0, 0.0), (1.0, 0.1), (1.0, 0.2), (1.0, 0.3),

            (1.0, 0.4), (1.0, 0.5), (1.0, 0.6), (1.0, 0.7),

            (1.0, 0.8), (1.0, 0.9), (1.0, 1.0), (1.0, 1.1)

        ]

    },

    {

        'filename': 'path2.txt',

        'initial_pose': (2, 2, 0.785),

        'velocities_and_angles': [

            (0.5, -0.2), (0.6, -0.1), (0.7, 0.0), (0.8, 0.1),

            (0.9, 0.2), (1.0, 0.3), (1.1, 0.4), (1.2, 0.5),

            (1.3, 0.6), (1.4, 0.7), (1.5, 0.8), (1.6, 0.9)

        ]

    },

    {

        'filename': 'path3.txt',

        'initial_pose': (-1, 1, -0.785),

        'velocities_and_angles': [

            (1.2, -0.1), (1.1, 0.0), (1.0, 0.1), (0.9, 0.2),

            (0.8, 0.3), (0.7, 0.4), (0.6, 0.5), (0.5, 0.6),

            (0.4, 0.7), (0.3, 0.8), (0.2, 0.9), (0.1, 1.0)

        ]

    },

    {

        'filename': 'path4.txt',

        'initial_pose': (3, -3, 1.5708),

        'velocities_and_angles': [

            (0.8, -0.3), (0.7, -0.2), (0.6, -0.1), (0.5, 0.0),

            (0.4, 0.1), (0.3, 0.2), (0.2, 0.3), (0.1, 0.4),

            (0.2, -0.1), (0.3, -0.2), (0.4, -0.3), (0.5, -0.4)

        ]

    }

]



# Generate files for each path

for path in paths:

    generate_car_data(path['filename'], path['initial_pose'], path['velocities_and_angles'])

