# 📂 GH-repo

![Python](https://shieldcn.dev/badge/Python.svg?variant=branded&brand=python) ![VS Code Installs](https://shieldcn.dev/vscode/installs/esbenp/prettier-vscode.svg?variant=branded) ![Built by a Human](<https://shieldcn.dev/badge/built%20by-a%20human.svg?logo=%F0%9F%91%A8%E2%80%8D%F0%9F%92%BB>) ![On Fire](<https://shieldcn.dev/badge/status-on%20fire.svg?logo=twemoji%3A1f525&variant=destructive>)

### 🔎 GitHub Repository Extractor

A Python-based utility to **fetch, organize, and document GitHub profiles and repositories** with ease. This project combines filesystem organization with GitHub API integration to give you a complete snapshot of any public GitHub profile.

---

## 🚀 Features

- **Profile Data Extraction**Fetches detailed information about any GitHub profile (ID, username, bio, followers, etc.).
- **Markdown Bio Generation**Converts the profile bio into a clean Markdown file for easy readability.
- **Repository Data Collection**Extracts metadata of all repositories (name, forks, issues, languages, etc.).
- **Automatic Repo Cloning**Clones all repositories locally using GitPython for offline access.
- **File Structure Organizer**
  Generates a neat `structure.txt` file showing the directory tree of your project.

---

## 📂 Project Structure

```plaintext
GH-repo/
│
├── git-data-extract.py     # Fetches GitHub profile & repos
├── OSFoldersList.py        # Generates directory structure
├── requirement.txt         # Dependencies
├── README.md               # Documentation
└── output/                 # Extracted profile & repo data
```

---

## ⚙️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/GH-repo.git
cd GH-repo
pip install -r requirement.txt
```

---

## 🖥️ Usage

---

### **Run the Extractor**

Fetch GitHub profile and repository data:

```bash
python git-data-extract.py
```

- Prompts for a GitHub username.
- Creates a folder `github-<username>-<id>` with:
  - `profile.txt` → Profile details
  - `profile_bio.md` → Markdown bio
  - `repos_data.txt` → Repository metadata
  - Cloned repositories in subfolders

---

## 📊 Example Output

**Profile Data (`profile.txt`)**

```plaintext
id - 123456
login - tux_106
name - John Doe
followers - 42
following - 10
created_at - 2020-01-01
```

**Repository Data (`repos_data.txt`)**

```plaintext
Total repo on this profile: 5
-------------------------
Project 1, sample-repo
id - 987654
full_name - tux_106/sample-repo
forks_count - 12
default_branch - main
```

---

## 🛠️ Dependencies

- **requests** – For API calls
- **markdown** – For bio conversion
- **GitPython** – For cloning repositories

Install them via:

```bash
pip install -r requirement.txt
```

---

## 📌 Notes

- Works only with **public GitHub profiles**.
- Ensure you have **Git installed** for cloning repositories.
- Excludes unnecessary files/folders like `.git`, `__pycache__`, `.venv`, etc.

---

## 🌟 Why Use GH-repo?

- **Fast & Simple** – Minimal setup, quick results.
- **Comprehensive** – Profile + repo data + local clones.
- **Professional Output** – Markdown and text files for easy documentation.
- **Extensible** – Customize excluded paths, patterns, or attributes.

---

## 📜 License

This project is licensed under the MIT License – feel free to use, modify, and share.
