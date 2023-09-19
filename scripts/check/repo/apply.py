import argparse
import os
import git

parser = argparse.ArgumentParser(description="Check SyncraftCore's Git Repos")
parser.add_argument("--software", required=True, help="Software Name")

args = parser.parse_args()

path = os.path.join('/home', 'pi', 'SyncraftCore', 'softwares', args.software)

if os.path.exists(path):
    
    def repo_status(repo_path: str):
        try:
            repo = git.Repo(repo_path)
            remote_branch = repo.remote().refs[0]
            local_branch = repo.active_branch
            if local_branch.commit != remote_branch.commit:
                print('outdated')
            else:
                print('up-to-date')
        except Exception as e:
            print('error')

    repo_status(repo_path=path)

else:
    print ('error')