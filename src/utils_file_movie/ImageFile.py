import os

from utils import File, Log

log = Log('ImageFile')


class ImageFile(File):
    @staticmethod
    def is_image_ext(ext: str) -> bool:
        return ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

    @staticmethod
    def list_from_dir(dir_path: str) -> list['ImageFile']:
        image_file_list = []
        for file_name in os.listdir(dir_path):
            ext = os.path.splitext(file_name)[1]
            if not ImageFile.is_image_ext(ext):
                continue
            image_path = os.path.join(dir_path, file_name)
            image_file = ImageFile(image_path)
            image_file_list.append(image_file)
        log.info(f'Found {len(image_file_list)} images in "{dir_path}".')
        return image_file_list
