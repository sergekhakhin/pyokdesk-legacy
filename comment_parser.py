from lib.issues import get_issue_list_by_status, get_issue_comments, add_comment

for issue_id in get_issue_list_by_status('opened'):
    if not get_issue_comments(issue_id):
        add_comment(issue_id, 'В работе.', author_id=6, public=True)
