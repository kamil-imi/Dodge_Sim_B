import pygame
import os

GLOBAL_PATH = f"{os.getcwd()}\\assets\\"


def get_image_by_relative_path(relative_path):
    path = GLOBAL_PATH+relative_path
    return pygame.image.load(path).convert_alpha()


def get_images_by_relative_path(relative_path):
    image_surfaces = []

    # Get the full path to the folder
    folder_path = os.path.join(os.getcwd(), relative_path)

    # Check if the folder exists
    if os.path.exists(folder_path):
        # Iterate through files in the folder
        for filename in os.listdir(folder_path):
            filepath = os.path.join(folder_path, filename)

            # Check if the file is an image
            if os.path.isfile(filepath) and any(filepath.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg']):
                # Load the image using Pygame and apply convert_alpha()
                image_surface = pygame.image.load(filepath).convert_alpha()
                image_surfaces.append(image_surface)
    else:
        raise ValueError("function get_images_by_relative_path get wrong argument,"
                         " the path to the dictionary doesn't exist")

    return tuple(image_surfaces)

