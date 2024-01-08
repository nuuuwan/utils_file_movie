from moviepy.editor import ImageClip, concatenate_videoclips
from utils import File

from utils_file_movie.ImageFile import ImageFile


class MovieFile(File):
    @staticmethod
    def from_image_list(
        image_file_list: list[ImageFile],
        movie_file_name: str,
        options: dict = {},
    ):
        image_duration = options.get("image_duration", 1)
        cross_fade_in_duration = options.get("cross_fade_in_duration")
        cross_fade_out_duration = options.get("cross_fade_out_duration")

        clips = []
        for image_file in image_file_list:
            clip = ImageClip(image_file.path)
            clip = clip.set_duration(image_duration)
            if cross_fade_in_duration:
                clip = clip.crossfadein(cross_fade_in_duration)
            if cross_fade_out_duration:
                clip = clip.crossfadeout(cross_fade_out_duration)
            clips.append(clip)

        concat_clip = concatenate_videoclips(clips, method="compose")
        concat_clip.write_videofile(movie_file_name, fps=24)
        movie_file = MovieFile(movie_file_name)
        return movie_file
