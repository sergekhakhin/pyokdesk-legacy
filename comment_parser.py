from lib.issues import get_issue_list_by_status, get_issue_comments, add_comment

comment = "В работе."

for issue_id in get_issue_list_by_status(['opened', 'repair']):
    if not get_issue_comments(issue_id):
        add_comment(issue_id, comment, author_id=6, public=True)
