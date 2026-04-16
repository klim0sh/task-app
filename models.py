class Task:
    def __init__(self, name, priority, deadline, done=False):
        self.name = name
        self.priority = priority
        self.deadline = deadline
        self.done = done
    def mark_done(self):
        self.done = not self.done
    def __str__(self):
        symbols = {True:'✅', False: '❌'}
        return f"{symbols[self.done]} | {self.name} | {self.priority} | {self.deadline}"
    def to_dict(self):
        return {
            "name": self.name,
            "priority": self.priority,
            "deadline": self.deadline,
            "done": self.done
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['priority'], data['deadline'], data['done'])
    
class RecurringTask(Task):
    def __init__(self, name, priority, deadline, interval_days, done=False):
        super().__init__(name, priority, deadline, done)
        self.interval_days = interval_days
    
    def __str__(self):
        base = super().__str__()
        return f"{base} | каждые {self.interval_days} дн."