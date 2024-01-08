import os
import sys

from utils import Log

from utils_file_movie import ImageFile, MovieFile

log = Log('images_to_movie')


def main(dir_path: str):
    image_list = ImageFile.list_from_dir(dir_path)
    movie_file_name = os.path.join(dir_path, 'movie.mp4')
    movie_file = MovieFile.from_image_list(
        image_list,
        movie_file_name,
        dict(
            image_duration=5,
            cross_fade_in_duration=0.5,
            cross_fade_out_duration=0.5,
        ),
    )
    log.info(f'Converting images in "{dir_path}" to {movie_file.name}.')


if __name__ == '__main__':
    dir_path = sys.argv[1]
    main(dir_path)
