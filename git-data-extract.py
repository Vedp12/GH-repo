import requests
import json
import markdown
import base64
try:
	github_uname = input("Enter Github UserName: ")
	github_profile = f"https://api.github.com/users/{github_uname}"
	github_repos_url = f"https://api.github.com/users/{github_uname}/repos"
	response = requests.get(github_profile)  #! Get Profile data
	response1 = requests.get(github_repos_url)
	data = response1.json()
	markdowns_list = []
	try:
		if response.status_code == 200:
			data = response.json()  # ! Format that data
			attributes = [
				"id",
				"login",
				"name",
				"email",
				"avatar_url",
				"url",
				"html_url",
				"bio",
				"public_repos",
				"location",
				"followers",
				"following",
				"created_at",
				"updated_at",
			]
			for attribute in attributes:
				if attribute in data:
					print(f"{attribute}: {data[attribute]}")
				else:
					print(f"{attribute}: Not found:")
					continue
		else:
			print(f"{response.status_code}: {response.text}")
	except Exception as e:
		print(f"Unable to fetch This profile data! error occurred At: {e}")

	print("\n\n\n")
	try:
		if response1.status_code == 200:
			print(f"{response.json()["name"]}'s All public repos: ")
			data = response1.json()
			print(f"Total repos: {len(data)}")
			attributes = [
				"id",
				"fullname",
				"url",
				"created_at",
				"updated_at",
				"starred_url",
				"allow_forking",
				"forks_count",
				"languages_url",
				"has_pull_requests",
				"is_template",
				"default_branch"
			]
		for no, datas in enumerate(data):
				print(f"\nNo {no+1}: {datas['name']}")
				for attribute in attributes:
					markdowns_list.append(attribute)

					if attribute not in datas:
						continue
					print(f"{attribute}: {datas[attribute]}")
	except Exception as e:
		print(f"Unable to fetch this repos data! error occurred At: {e}")

	print("\n\n\n")
	print("DO you want to check the content of these repos?")
	choice = input("Enter Yes or No: ")
	if choice == "yes" or "y" or "Yes" or "yeah" or "YES" :
		for no, datas in enumerate(data):
			print(f"\nNo {no + 1}: {datas['name']}")
			data = requests.get(github_repos_url).json()
			repos_markdown = base64.b64decode(data["content"]).decode("utf-8")
			print(repos_markdown)
except Exception as e:
	print(f"Error: {e}")
	exit()
