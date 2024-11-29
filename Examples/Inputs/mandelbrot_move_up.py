# Fractal Toolbox is a series of python scripts for generating images
# and videos based on Julia and Mandelbrot sets.
# Copyright (C) 2024  Vivien ELIE
#
# This file is part of Fractal Toolbox.
#
# Fractal Toolbox is free software: you can redistribute it and/or modify it under the terms
# of the GNU General Public License as published by the Free Software Foundation,
# either version 3 of the License, or (at your option) any later version.
#
# Fractal Toolbox is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with Fractal Toolbox.
# If not, see <https://www.gnu.org/licenses/>.


import sys
import os
import csv



# Classes
class ClassParameters:
    def __init__(self):
        self.images_number = 0
        self.type_fractal = ""
        self.max_iterations = 0
        self.start_xmin = 0
        self.start_xmax = 0
        self.start_ymin = 0
        self.start_ymax = 0
        self.R = 0
        self.G = 0
        self.B = 0
        self.opt_next_image = ""
        self.zoom_amount = 0
        self.centering_sigma = 0
        self.centering_up = 0
        self.centering_down = 0
        self.centering_left = 0
        self.centering_right = 0
        self.move_x = 0.0
        self.move_y = 0.0

        self.output_folder_pathname = ""
        self.output_filename = ""






# Globales
parameters = ClassParameters()





# Main
if __name__ == '__main__':

    # Configuration
    parameters.images_number = 1440
    parameters.type_fractal = "mandelbrot"
    parameters.max_iterations = 1000
    parameters.start_xmin = -0.75
    parameters.start_xmax = -0.747
    parameters.start_ymin = 0.06
    parameters.start_ymax = 0.063
    parameters.R = 60
    parameters.G = 25
    parameters.B = 15
    parameters.opt_next_image = "CENTERING+MOVE"
    parameters.zoom_amount = 0.0
    parameters.centering_sigma = 2.0
    parameters.centering_up = 0
    parameters.centering_down = 0
    parameters.centering_left = 1
    parameters.centering_right = 1
    parameters.move_x = 0.0
    parameters.move_y = 0.00001

    parameters.output_folder_pathname = "Outputs"
    parameters.output_filename = "mandelbrot_move_up.csv"

    # Prepare output folder
    if not os.path.exists(parameters.output_folder_pathname):
        os.makedirs(parameters.output_folder_pathname)

    # Prepare csv header and first data line
    data = []
    data.append(["type_fractal", "max_iterations", "julia_a", "julia_b", "xmin", "xmax", "ymin", "ymax", "r", "g", "b",
                 "opt_next_image", "zoom_amount", "centering_sigma",
                 "centering_up", "centering_down", "centering_left", "centering_right",
                 "move_x", "move_y"])
    data.append([parameters.type_fractal,
                 str(parameters.max_iterations),
                 "",
                 "",
                 str(parameters.start_xmin),
                 str(parameters.start_xmax),
                 str(parameters.start_ymin),
                 str(parameters.start_ymax),
                 str(parameters.R),
                 str(parameters.G),
                 str(parameters.B),
                 parameters.opt_next_image,
                 str(parameters.zoom_amount),
                 str(parameters.centering_sigma),
                 str(parameters.centering_up),
                 str(parameters.centering_down),
                 str(parameters.centering_left),
                 str(parameters.centering_right),
                 str(parameters.move_x),
                 str(parameters.move_y)])

    # Adds data
    for cnt in range(1, parameters.images_number):
        data.append([parameters.type_fractal,
                     str(parameters.max_iterations),
                     "",
                     "",
                     "",
                     "",
                     "",
                     "",
                     str(parameters.R),
                     str(parameters.G),
                     str(parameters.B),
                     parameters.opt_next_image,
                     str(parameters.zoom_amount),
                     str(parameters.centering_sigma),
                     str(parameters.centering_up),
                     str(parameters.centering_down),
                     str(parameters.centering_left),
                     str(parameters.centering_right),
                     str(parameters.move_x),
                     str(parameters.move_y)])

    # Write output csv file
    with open(os.path.join(parameters.output_folder_pathname, parameters.output_filename),
              mode="w",
              newline="",
              encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(data)

    # End
    sys.exit(0)
