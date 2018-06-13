import os
import sys

import cv2
import fire
import numpy as np

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from deepface import get_detector, get_recognizer, save_features
from deepface.utils.visualization import draw_bboxs


def show_with_face(npimg, faces, visualize=False):
    if visualize:
        img = draw_bboxs(np.copy(npimg), faces)
        cv2.imshow('DeepFace', img)
        cv2.waitKey(0)


class DeepFace:
    def __init__(self):
        pass

    def run(self, source_path=None,
            db_path=None,
            img_path=None,
            visualize=True):
        if source_path:
            save_features(img_folder_path=source_path,
                          output_path=db_path)

        npimg = cv2.imread(img_path, cv2.IMREAD_COLOR)

        # detect
        detector = get_detector()
        faces = detector.detect(npimg=npimg)

        # recognize
        recognizer = get_recognizer(db=db_path)
        result = recognizer.detect(faces=faces, npimg=npimg)
        tagged_faces = recognizer.tag_faces(faces=faces, result=result)

        show_with_face(npimg, tagged_faces, visualize=visualize)


if __name__ == '__main__':
    fire.Fire(DeepFace)