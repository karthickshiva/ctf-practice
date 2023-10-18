import requests

# Set your GitHub username and repository details
username = 'MrSecretiveCoder'
repository = 'Secret'
commit_sha = '5931fd4bf469a43c632d427b9c26d34260161b5a'
token = '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'

# Define the API URL for browsing contents at a specific commit
base_url = f'https://api.github.com/repos/{username}/{repository}/contents'
commit_url = f'{base_url}?ref={commit_sha}'

# Make a GET request to list the contents at the specified commit
response = requests.get(commit_url, headers={'Authorization': f'token {token}'})

if response.status_code == 200:
    contents = response.json()
    for content in contents:
        print(content['name'])
else:
    print(f"Failed to list contents. Status code: {response.status_code}")
