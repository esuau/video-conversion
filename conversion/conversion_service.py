import ffmpy


class ConversionService(object):

    def __init__(self, _config_):
        self.configuration = _config_

    def convert_video(self, _origin_, _target_):
        ff = ffmpy.FFmpeg(
            inputs={_origin_: None},
            outputs={_target_: '-y -vcodec mpeg4 -b 4000k -acodec mp2 -ab 320k'}
        )
        ff.run()
