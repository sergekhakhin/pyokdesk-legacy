from lib.issues import get_opened_issues, get_issue_comments, leave_comment

for issue_id in get_opened_issues():
    if not get_issue_comments(issue_id):
        leave_comment(issue_id, 'В работе.', author_id=6)
