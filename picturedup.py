import os
from PIL import Image
from PIL import ImageChops

def is_same_image(path_to_image_1, path_to_image_2):
    print(f"Comparing {path_to_image_1} to {path_to_image_2}")

    if (not path_to_image_1.endswith(".jpg")) or (not path_to_image_2.endswith(".jpg")):
        return False

    image_1 = Image.open(path_to_image_1)
    image_2 = Image.open(path_to_image_2)

    try:
        difference = ImageChops.difference(image_1, image_2)
    except ValueError:
        return False

    nonzero_boundary = difference.getbbox()

    if nonzero_boundary is not None:
        print("The images are different.")
        return False
    else:
        print("The images are the same.")
        return True

def keep_image(path_to_image):
    keep_folder = r"C:\Users\richard\Pictures\Keep"
    keep_filename = path_to_image.replace(image_base_path, keep_folder)
    print("Keeping image: moving image to: ", keep_filename)
    try:
        os.rename(path_to_image, keep_filename)
    except FileExistsError:
        os.remove(path_to_image)

def remove_image(path_to_image):
    pending_deletion_folder = r"C:\Users\richard\PendingDeletion"
    disposal_filename = path_to_image.replace(image_base_path, pending_deletion_folder)
    print("Disposing image: moving image to: ", disposal_filename)
    try:
        os.rename(path_to_image, disposal_filename)
    except FileExistsError:
        os.remove(path_to_image)


picture_directory = r"C:\Users\richard\Pictures"
contents = os.listdir(picture_directory)

for folder in contents:
    print(f"FOLDER: {folder}")
    folder_path = os.path.join(picture_directory, folder)
    folder_contents = os.listdir(folder_path)

    # Ignore empty folders
    if len(folder_contents) > 0:

        image_base_path = os.path.join(picture_directory, folder)

        end_of_list = False
        index = 0

        while not end_of_list:

            folder_contents = os.listdir(folder_path)

            if len(folder_contents) == 1:
                # Only one image left, move it to Keep
                image_path = os.path.join(image_base_path, folder_contents[0])
                keep_image(image_path)
                end_of_list = True
            else:
                print(f"\n\nRead images {folder_contents[index]} and {folder_contents[index+1]}")
                image_1_path = os.path.join(image_base_path, folder_contents[index])
                image_2_path = os.path.join(image_base_path, folder_contents[index+1])

                if is_same_image(image_1_path, image_2_path):
                    remove_image(image_1_path)
                else:
                    keep_image(image_1_path)

    else:
        #Folder is empty. Delete it.
        print("Folder is empty. Deleting folder.")
        os.rmdir(folder_path)
