import requests
from datetime import datetime, timedelta

class GitHubIngestionBot:
    def __init__(self, repo_owner, repo_name, token):
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.token = token
        self.headers = {
            'Authorization': f'token {self.token}',
            'Accept': 'application/vnd.github.v3+json'
        }

    def fetch_commits(self, since_days=7):
        since = (datetime.utcnow() - timedelta(days=since_days)).isoformat() + 'Z'
        url = f'https://api.github.com/repos/{self.repo_owner}/{self.repo_name}/commits'
        params = {'since': since}
        response = requests.get(url, headers=self.headers, params=params)
        return response.json() if response.status_code == 200 else []

    def fetch_pull_requests(self, state='all'):
        url = f'https://api.github.com/repos/{self.repo_owner}/{self.repo_name}/pulls'
        params = {'state': state}
        response = requests.get(url, headers=self.headers, params=params)
        return response.json() if response.status_code == 200 else []

    def fetch_issues(self, state='all'):
        url = f'https://api.github.com/repos/{self.repo_owner}/{self.repo_name}/issues'
        params = {'state': state}
        response = requests.get(url, headers=self.headers, params=params)
        return response.json() if response.status_code == 200 else []

    def summarize(self):
        commits = self.fetch_commits()
        prs = self.fetch_pull_requests()
        issues = self.fetch_issues()

        summary = {
            'commit_count': len(commits),
            'pull_request_count': len(prs),
            'issue_count': len(issues),
            'latest_commit': commits[0] if commits else None,
            'latest_pr': prs[0] if prs else None,
            'latest_issue': issues[0] if issues else None
        }

        return summary


bot = GitHubIngestionBot('ChirayuXD', 'AES_PASSWORD_MANAGER', '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')
summary = bot.summarize()
print(summary)
