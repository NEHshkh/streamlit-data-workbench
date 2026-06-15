# GitHub Workflow for Streamlit Data Workbench

This workflow is based on the professor's class documents:

- `Command Line Git.docx`
- `CollaborativeGitHubLab.docx`

The workflow uses command line Git, GitHub branches, pull requests, review, merge, and GitHub Actions. The goal is to keep the `main` branch stable while practicing a professional collaboration process.

## Workflow Steps

1. Make sure GitHub access is configured.

```bash
gh auth status
```

This checks that the GitHub CLI and Git can access the remote repository.

2. Update the local `main` branch.

```bash
git checkout main
git pull origin main
```

3. Create a feature branch for the change.

```bash
git checkout -b improve-data-workbench
```

4. Make changes in the `streamlit_data_workbench` folder and test the Streamlit app.

```bash
cd streamlit_data_workbench
pip install -r requirements.txt
streamlit run app.py
```

5. Review changed files.

```bash
git status
```

6. Stage and commit the work with a clear message.

```bash
git add .
git commit -m "Improve Streamlit data workbench"
```

7. Push the branch to GitHub.

```bash
git push -u origin improve-data-workbench
```

8. Open a pull request on GitHub from the feature branch into `main`.

9. Review the pull request, check that the app runs, and confirm the GitHub Actions workflow passes.

10. Merge the pull request into `main`.

11. Delete the completed branch after it has been merged.

## Collaboration Requirement

The professor's collaborative lab asks students to practice a real GitHub collaboration process.

For this repository, the collaboration workflow is:

1. Invite the instructor or reviewer to the GitHub repository if required.
2. Let the reviewer submit a pull request with suggested changes.
3. Review the suggested changes in the pull request.
4. Merge the reviewer pull request if the changes are correct.
5. Make at least one improvement to the Streamlit app or documentation.
6. Push the improvement on a feature branch.
7. Open a pull request back into `main`.

This matches the class goal: the project should be simple, but the GitHub workflow should be professional.

## GitHub Actions

This repository also has an automated workflow file:

```text
.github/workflows/streamlit-workflow.yml
```

The Actions workflow installs dependencies, checks Python syntax, and smoke-tests the included CSV and SQLite data repositories whenever code is pushed or a pull request is opened.

## Summary

The project workflow is:

```text
authenticate -> pull main -> create branch -> edit and test -> commit -> push -> pull request -> review -> merge
```

This keeps `main` stable and supports the collaboration process required for the class.
