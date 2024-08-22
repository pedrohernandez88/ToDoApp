class todo:
  def __init__(self, code_id: int, title: str, description: str):
        self.code_id = code_id
        self.title = title
        self.description = description
        self.completed = False
        self.tags = []

def mark_completed(self):
    self.completed=True

def add_tag(self, tag:str):
    if tag not in self.tags:
        self.tags.append(tag)

def _str_(self):
    return f"{self.code_id} - {self.title}"

class TodoBook:
    def _init_(self):
        self.todos = Dict[int, todo] = {}

def add_todo(self, title: str, description: str) -> int:
    code_id = len(self.todos) + 1
    self.todo [code_id] = todo(code_id, title, description, False)
    return code_id


    