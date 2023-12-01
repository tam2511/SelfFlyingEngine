from threading import Thread
from queue import Queue
from .video_capture import VideoCapture
from ..frame import Response, VideoStream, DiskWriter


class Core(object):
    def __init__(self, quadcopter, video_stream=False, disk_writer=False):
        self.api = quadcopter.api
        self.__autopilot = False
        self.video_capture = VideoCapture(self.api)
        self.response = None
        self.video_stream = None
        self.disk_writer = None
        self.feedback = None

        if video_stream:
            self.start_video_stream()
        if disk_writer:
            self.start_disk_writer()

    @property
    def autopilot(self):
        return self.__autopilot

    @autopilot.setter
    def autopilot(self, value: bool):
        if self.__autopilot is value:
            return

        if value:
            self.__autopilot = True
            Thread(target=self.processing).start()
        else:
            self.__autopilot = False

    def processing(self):
        self.start_response()

        while self.autopilot:
            action = self.feedback.get()
            self.execute(action)

        self.stop_response()

    def execute(self, method_name, *args):
        getattr(self.api, method_name).__call__(*args)

    def start_response(self):
        self.feedback = Queue()
        self.response = Response(self.feedback)
        self.video_capture.register(self.response)

    def start_video_stream(self):
        self.video_stream = VideoStream(self.api.__class__.__name__)
        self.video_capture.register(self.video_stream)

    def start_disk_writer(self):
        self.disk_writer = DiskWriter(f'{self}.avi')
        self.video_capture.register(self.disk_writer)

    def stop_response(self):
        self.video_capture.unregister(self.response)
        self.response.stop()
        self.response = None
        self.feedback = None

    def stop_video_stream(self):
        if self.video_stream:
            self.video_capture.unregister(self.video_stream)
            self.video_stream.stop()
            self.video_stream = None

    def stop_disk_writer(self):
        if self.disk_writer:
            self.video_capture.unregister(self.disk_writer)
            self.disk_writer.stop()
            self.disk_writer = None

    def kill(self):
        self.autopilot = False
        self.video_capture.stop()
        self.stop_video_stream()
        self.stop_disk_writer()
        self.api.disconnect()
