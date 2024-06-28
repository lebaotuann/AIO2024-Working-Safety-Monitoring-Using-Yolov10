import os
import uuid

import streamlit as st
from ultralytics import YOLOv10

from constants import DATA_DIRECTORY_PATH

SAFETY_HELMET_WEIGHT_PATH = f"{DATA_DIRECTORY_PATH}/weights/helmet_safety_best.pt"


def generate_name():
    """Generate a name"""
    return str(uuid.uuid4())


def save_upload_file(upload_file, save_folder="images"):
    """Save an image into images folder.

    Args:
        upload_file: The image object.
        save_folder: Name of the folder.

    Returns:
        str: The image path.
    """
    os.makedirs(save_folder, exist_ok=True)
    if upload_file:
        new_filename = generate_name() + "-" + upload_file.name
        save_path = os.path.join(save_folder, new_filename)
        with open(save_path, "wb+") as f:
            data = upload_file.read()
            f.write(data)
        return save_path
    else:
        raise ("Image not found.")


def delete_file(file_path):
    """Remove a image."""
    os.remove(file_path)


def process_and_show_image(image_path):
    """Processes an image for object detection using a custom YOLOv10.
    Show the image result.
    Args:
        image_path (str): The image path to detect.
    """
    model = YOLOv10(SAFETY_HELMET_WEIGHT_PATH)
    image_result = model.predict(source=image_path, imgsz=640, conf=0.3)
    image_predict = image_result[0].save(image_path)
    st.image(image_predict, caption="Processed Image")


def run():
    """Run object detection app"""
    st.set_page_config(page_title="AIO2024 - Module Project 1", layout="wide")
    st.title("Working Safety Monitoring Using YOLOv10")
    upload_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    st.divider()
    if upload_file:
        st.image(upload_file, caption="Uploaded Image")
        new_image_path = save_upload_file(upload_file)
        try:
            process_and_show_image(new_image_path)
        finally:
            delete_file(new_image_path)


if __name__ == "__main__":
    run()
