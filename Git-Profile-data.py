# # import requests
# # import markdown
# #
# # github_uname = input("Enter Github UserName: ")
# # github_profile_url = f"https://api.github.com/users/{github_uname}"
# # git_repo_url = f"https://api.github.com/repos/Vedp12/GH-repo"
# # response = requests.get(github_profile_url)
# #
# # response1 = requests.get(git_repo_url)
# # data = response1.json()
# # for datas in data:
# #     print(f"{datas}:{data[datas]}")
# #
# #
# # data1 = response.json()
# #
# # try:
# #     if response.status_code == 200:
# #         print(data1[git_repo_url])
# #         git_attribute_data1s = [
# #             "name",
# #             "email",
# #             "url",
# #             "bio",
# #             "public_repos",
# #             "blog",
# #             "repo",
# #             "avatar_url",
# #             # "open_issues_count",
# #             "followers",
# #             # "stars",
# #             "following",
# #             # "forks_count",
# #         ]
# #
# #         for git_attribute_data1 in git_attribute_data1s:
# #             if not data1[git_attribute_data1]:
# #                 print(f'{git_attribute_data1}: Not found')
# #                 continue
# #             else:
# #                 print(f"{git_attribute_data1}: {data1[git_attribute_data1]}")
# #         git_repo_data1s = [
# #
# #         ]
# #
# #     else:
# #         print("Error: " + response)
# # except Exception as e:
# #     print(f"Error: {e}")
#
#
# # import requests
# # import base64
# # url = "https://api.github.com/repos/torvalds/linux/readme"
# # data = requests.get(url).json()
# # readme = base64.b64decode(data["content"]).decode("utf-8")
# # print(readme)
# # files = requests.get(url).json()
# #
# # for file in files:
# #     print(file["name"], file["type"])
#
#
# import requests
#
# repos = requests.get(
#     "https://api.github.com/users/torvalds/repos"
# ).json()
#
# for repo in repos:
#     print(repo["name"])
