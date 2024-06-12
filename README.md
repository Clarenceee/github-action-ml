#### GitHub Actions
A workflow is a configurable automated process that will run one or more jobs. Workflows are defined by a YAML file checked in to your repository and will run when triggered by an event in your repository, or they can be triggered manually, or at a defined schedule.

Workflows are defined in the .github/workflows directory in a repository, and a repository can have multiple workflows, each of which can perform a different set of tasks. For example, you can have one workflow to build and test pull requests, another workflow to deploy your application every time a release is created, and still another workflow that adds a label every time someone opens a new issue.

A workflow must contain the following basic components:
1. One or more events that will trigger the workflow.
2. One or more jobs, each of which will execute on a runner machine and run a series of one or more steps.
3. Each step can either run a script that you define or run an action, which is a reusable extension that can simplify your workflow.

---

#### DVC
Data Version Control [(DVC)](https://dvc.org/doc/start?tab=Windows-Cmd-) is enabled in this repository as well to track large datasets and machine learning models alongside the code, sidestepping all the limitations of storing it in Git.
- It can be connected to cloud storages / Google drive / local storage systems referred as "remotes"
- In this repository it is connected to local temp storage

mkdir %TEMP%/dvcstore
dvc remote add -d myremote %TEMP%\dvcstore