from threading import Thread, Event


class VideoCapture(object):
    def __init__(self, api):
        self.api = api
        self.video_capture = api.get_frame_read()
        self.observers = []
        self.is_alive = True

        self.event = Event()
        Thread(target=self.notify_observers).start()

    def notify_observers(self):
        self.api.streamon()

        while self.is_alive:
            self.event.wait()
            frame = self.video_capture.frame
            for observer in self.observers:
                observer.put(frame)

        self.api.streamoff()

    def register(self, observer):
        self.observers.append(observer)
        self.event.set()

    def unregister(self, observer):
        self.observers.remove(observer)

        if not len(self.observers):
            self.event.clear()

    def stop(self):
        self.is_alive = False
        self.event.set()
