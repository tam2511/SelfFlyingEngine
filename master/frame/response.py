from .base import BaseFrame


class Response(BaseFrame):
    def __init__(self, feedback):
        super().__init__()
        self.feedback = feedback
        self.pipeline = Pipeline()

    def processing(self):
        while self.is_alive:
            frame = self.frames.get()
            result = self.pipeline(frame)
            action = self.analyze(result)
            self.feedback.put(action)

    def analyze(self, result):
        ...
