from lib.issues import *


class Issue:
    def __init__(self, issue_id: int):
        self.id = issue_id
        self.sync()

    def __repr__(self):
        return f'issue_{self.id}'

    def sync(self):
        self.__dict__.update(get_issue_info(self.id))

    def get_comments(self):
        return get_issue_comments(self.id)

    def get_services(self):
        return get_issue_services(self.id)

    def open(self):
        change_issue_status(self.id, 'opened')
        self.sync()

    def complete(self):
        change_issue_status(self.id, 'completed')
        self.sync()

    def change_assignee(self, assignee_id=None, group_id=None):
        change_assignee(self.id, assignee_id, group_id)
        self.sync()

    def add_comment(self, comment: str, author_id: int, public=False):
        add_comment(self.id, comment, author_id, public)
        self.sync()

    def add_service(self, code: str, quantity: float, performer_id=None, **kwargs):
        if not performer_id:
            performer_id = self.assignee['id']
        add_service(self.id, code, quantity, performer_id, **kwargs)

    def add_services(self, performer_id=None, **services):
        if not performer_id:
            performer_id = self.assignee['id']
        add_services(self.id, performer_id, **services)
