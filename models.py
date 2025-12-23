class Task:
    def init(self, task_id, title, is_completed=False):
        self.id = task_id
        self.title = title
        [span_0](start_span)self.is_completed = is_completed[span_0](end_span)

    def to_dict(self):
        """Serialization: Convert Object to JSON-ready Dictionary"""
        [span_1](start_span)return {"id": self.id, "title": self.title, "is_completed": self.is_completed}[span_1](end_span)

    @staticmethod
    def from_dict(data):
        """Deserialization: Convert Dictionary back to Task Object"""
         (start_span)return Task(data['id'], data['title'], data['is_completed'])
