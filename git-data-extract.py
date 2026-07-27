import os
import git
import markdown
import requests
from OSFoldersList import files_list

Github_Username = str(input("enter Profile name:"))
Github_Profiles = f"https://api.github.com/users/{Github_Username}"
Github_Repo_urls = f"https://api.github.com/users/{Github_Username}/repos"
All_Public_Repos_list = []
Response_user_profile = requests.get(Github_Profiles)
Response_user_repo = requests.get(Github_Repo_urls)


profile_fields = [
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
if Response_user_profile.status_code == 200:
    data_profile = Response_user_profile.json()

    if not os.path.exists(f"github-{Github_Username}-{data_profile['id']}"):
        os.mkdir(f"github-{Github_Username}-{data_profile['id']}")
    try:
        with open(
            f"github-{Github_Username}-{data_profile['id']}/profile.txt", "w"
        ) as file_profile:
            for profile_field in profile_fields:
                if profile_field in data_profile:
                    file_profile.write(
                        f"{profile_field} - {data_profile[profile_field]} \n"
                    )
                else:
                    continue
        if data_profile["avatar_url"]:
            response = requests.get(data_profile["avatar_url"]).content
            with open(
                f"github-{Github_Username}-{data_profile['id']}/avatar.jepg", "wb"
            ) as file_image:
                file_image.write(response)

    except Exception as e:
        print(str(e))
    try:
        with open(
            f"github-{Github_Username}-{data_profile['id']}/profile_bio.md", "w"
        ) as file_profile_bio:
            if data_profile["bio"]:
                profile_bio_str = markdown.markdown(data_profile["bio"])
                file_profile_bio.write("\n" + profile_bio_str)
    except Exception as e:
        print(str(e))
else:
    print(f"Unable to get data {Response_user_profile.status_code}")
print("\n", "-" * 151, "\n")
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
if Response_user_repo.status_code == 200:
    data_repos = Response_user_repo.json()
    try:
        with open(
            f"github-{Github_Username}-{data_profile['id']}/repos_data.txt", "w"
        ) as file_repo:
            file_repo.write(f"Total repo on this profile {len(data_repos)}")
            for no, repo in enumerate(data_repos):
                file_repo.write("-------------------------\n\n")
                file_repo.write(f"Project {no+1}, {repo['name']}")
                file_repo.writelines(
                    f"{profile_repo_Attribute} - {repo[profile_repo_Attribute]}\n"
                    for profile_repo_Attribute in profile_repo_Attributes
                )
            print(f"{repo['name']} created successfully! ")
    except Exception as e:
        print(str(e))
else:
    print(f"Unable to get data {Response_user_repo.status_code}")
if Response_user_profile.status_code == 200 and Response_user_repo.status_code == 200:
    base_dir = f"github-{Github_Username}-{data_profile['id']}"
    os.makedirs(base_dir, exist_ok=True)

    try:
        for repo in data_repos:
            repo_name = repo.get("name")
            if not repo_name:
                continue

            repo_dir = os.path.join(base_dir, repo_name)
            all_repo = f"https://github.com/{Github_Username}/{repo_name}.git"

            if os.path.exists(repo_dir):
                print(f"{repo_name} already exists locally, skipping clone.")
                continue

            print(f"{repo_name} Repo is cloning currently")
            git.Repo.clone_from(all_repo, repo_dir)

            structure_file = os.path.join(repo_dir, f"{repo_name}-Structure.txt")
            with open(structure_file, "w", encoding="utf-8") as file_structure:
                files_list(repo_dir, file_structure=file_structure)

            print(f"{repo_name} created successfully!")
    except Exception as e:
        print(e)
