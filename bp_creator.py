from pathlib import Path
import os

class BPCreator:
    TMP_DIR = '/tmp/bp_creator'

    def __init__(self, image_path):
        self._image_path = image_path

    def get_image_path(self):
        return self._image_path

    @staticmethod
    def process_text(text):
        arr = [i.strip() for i in text.split('\n')]
        for ind, i in enumerate(arr):
            if len(i) > 0:
                arr[ind] = '>' + arr[ind]
        return '\n'.join(arr)

    def create_bp(self, text):
        if Path(self.TMP_DIR).is_file():
            os.remove(self.TMP_DIR)
        if not Path(self.TMP_DIR).is_dir():
            os.mkdir(self.TMP_DIR)
        return self.get_image_path()

    def set_image_path(self, image_path):
        self._image_path = image_path
