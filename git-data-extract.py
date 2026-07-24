
# * Modules
import requests
import markdown
import base64
import git
import os

# * Urls

github_Uname = input("enter Profile name:")
github_profile = f"https://api.github.com/users/{github_Uname}"
github_repos_url = f"https://api.github.com/users/{github_Uname}/repos"
AllPublic_Repos = []
response_profile = requests.get(github_profile)  # ! Convert profile data to json
response_repo = requests.get(github_repos_url)  # ! Convert repository data to json
data_profile = response_profile.json()
data_repos = response_repo.json()

if not os.path.exists(f"github-{github_Uname}-{data_profile["id"]}"):
    os.mkdir(f"github-{github_Uname}-{data_profile["id"]}")
# * Extract Profiles data
profile_name_Attributes = [
    "id",
    "login",
    "name",
    "email",
    "avatar_url",
    "url",
    "html_url",
    "public_repos",
    "location",
    "followers",
    "following",
    "created_at",
    "updated_at",
]
if response_profile.status_code == 200:
    try:
        with open(
            f"github-{github_Uname}-{data_profile["id"]}/profile.txt", "w"
        ) as file_profile:
            print(f"{file_profile} created successfully! ")
            for profile_name_Attribute in profile_name_Attributes:
                if (
                    profile_name_Attribute is not None
                    or profile_name_Attribute in data_profile
                ):
                    file_profile.write(
                        f"{profile_name_Attribute} - {data_profile[profile_name_Attribute]} \n"
                    )
            print(f"{file_profile} data added successfull! ")
    except Exception as e:
        print(str(e))

    try:
        with open(
            f"github-{github_Uname}-{data_profile["id"]}/profile_bio.md", "w"
        ) as file_profile_bio:
            if data_profile["bio"] and data_profile["bio"] is not None:
                profile_bio_str = markdown.markdown(f"""{data_profile["bio"]}""")
                file_profile_bio.write("\n" + profile_bio_str)
            print(f"{file_profile_bio} created successfully! ")
    except Exception as e:
        print(str(e))

else:
    print(f"Unable to get data {response_profile.status_code}")

print("\n\n\n")


profile_repo_Attributes = [
    "id",
    "full_name",
    "url",
    "created_at",
    "updated_at",
    "allow_forking",
    "forks_count",
    "languages_url",
    "has_issues",
    "is_template",
    "fork",
    "default_branch",
]
if response_repo.status_code == 200:
    try:
        with open(
            f"github-{github_Uname}-{data_profile["id"]}/repos_data.txt", "w"
        ) as file_repo:
            file_repo.write(f"Total repo on this profile {len(data_repos)}")
            for no, repo in enumerate(data_repos):
                file_repo.write("-------------------------\n\n")
                file_repo.write(f"Project {no+1}, {repo["name"]}")
                for profile_repo_Attribute in profile_repo_Attributes:
                    file_repo.write(
                        f"{profile_repo_Attribute} - {repo[profile_repo_Attribute]}\n"
                    )
            print(f"{file_repo} created successfully! ")
    except Exception as e:
        print(str(e))
else:
    print(f"Unable to get data {response_repo.status_code}")

if response_profile.status_code == 200 and response_repo.status_code == 200:
    try:
        for repo in data_repos:
            if not os.path.exists(f"github-{github_Uname}-{data_profile["id"]}/{repo["name"]}"):
                os.mkdir(f"github-{github_Uname}-{data_profile["id"]}/{repo["name"]}")
            all_repo = f"https://github.com/{github_Uname}/{repo["name"]}.git"
            local_dir = (
                f"github-{github_Uname}-{data_profile["id"]}/{repo["name"]}"
            )
            git.Repo.clone_from(all_repo, local_dir)
    except Exception as e:
        print(str(e))
