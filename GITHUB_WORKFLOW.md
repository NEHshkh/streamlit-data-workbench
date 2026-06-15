# GitHub Workflow for Streamlit Data Workbench

This repository follows the GitHub workflow from the class examples: use command line Git, work on a branch, push to GitHub, open a pull request, review the change, then merge into `main`.

## Workflow Steps

1. Update the local `main` branch.

```bash
git checkout main
git pull origin main
```

2. Create a feature branch for the change.

```bash
git checkout -b improve-data-workbench
```

3. Make changes in the `streamlit_data_workbench` folder and test the Streamlit app.

```bash
cd streamlit_data_workbench
pip install -r requirements.txt
streamlit run app.py
```

4. Review changed files.

```bash
git status
```

5. Stage and commit the work with a clear message.

```bash
git add .
git commit -m "Improve Streamlit data workbench"
```

6. Push the branch to GitHub.

```bash
git push -u origin improve-data-workbench
```

7. Open a pull request on GitHub from the feature branch into `main`.

8. Review the pull request, check that the app runs, and confirm the GitHub Actions workflow passes.

9. Merge the pull request into `main`.

10. Delete the completed branch after it has been merged.

## GitHub Actions

This repository also has an automated workflow file:

```text
.github/workflows/streamlit-workflow.yml
```

The Actions workflow installs dependencies, checks Python syntax, and smoke-tests the included CSV and SQLite data repositories whenever code is pushed or a pull request is opened.

## Summary

The project workflow is:

```text
pull main -> create branch -> edit and test -> commit -> push -> pull request -> review -> merge
```

This keeps `main` stable and supports the collaboration process required for the class.
