from utils.utils import preproc, vis
from utils.utils import BaseEngine
import numpy as np
import cv2
import time
import os
import argparse

class Predictor(BaseEngine):
    def __init__(self, engine_path):
        super(Predictor, self).__init__(engine_path)
        self.n_classes = 80  # your model classes

if __name__ == '__main__':

    engine = ""
    pred = Predictor(engine_path=engine)
    pred.get_fps()
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        pred.detect(frame)