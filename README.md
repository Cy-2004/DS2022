# DS2022

Course material for **DS2022 Systems I: Introduction to Computing**

## Fall 2026

Instructors: 
[**Daniel Graham**](https://datascience.virginia.edu/people/daniel-graham)
[**Karsten Siller**](https://datascience.virginia.edu/people/karsten-siller)

Syllabi and course details are in Canvas (single page for all sections):

- [**DS2022 Sections 001 - 003**](https://canvas.its.virginia.edu/)

## Setup

Please read and complete all [setup instructions](setup/GENERAL.md) by the end of week 1.

## Content

<<<<<<< HEAD
[Weekly modules](CONTENT.md)

## Forks

Once you have forked this repository, you have two options for keeping your fork current with new changes added to the original repository:

### Update your fork with the GitHub UI

1. Find the "Sync Fork" button on the main page of your fork in GitHub.
2. Within the drop-down menu, click on "Update Branch" to incorporate all upstream changes.

![Sync Fork with Upstream](https://s3.amazonaws.com/ds2002-resources/images/sync-fork-upstream.png)

### Update your fork with the CLI

To stay current with new releases into the course repository, follow these steps:

1. Add an upstream source
```
git remote add upstream https://github.com/uvasds-systems/ds2002.git
```
2. Fetch from the upstream branch:
```
git fetch upstream
```
3. Merge your branch with the upstream branch.
```
git merge upstream/main main
```

This can be run in a single block:
```
git remote add upstream https://github.com/uvasds-systems/ds2002.git
git fetch upstream
git merge upstream/main main
```

This will pull all upstream changes in and merge them with your fork. Note that the first line is a one-time configuration, whereas lines 2 and 3 can be used repeatedly to catch up with the upstream source.
=======
- [Schedule](CONTENT.md): Overview of weekly topics
- [Class materials](class/): Hands-on exercises
- [In-class demos](demos/): Documentation of instructor-led live coding demos

## Staying up to date

Course materials change during the semester. Work from **your fork**, and periodically pull new content from the course repository (**upstream**).

- **First time only:** [Initial setup](#initial-setup-do-this-once)
- **Each week (or whenever we update materials):** [Weekly sync](#weekly-sync)
- **When you want to save your own notes or work:** [Push your work to GitHub](#push-your-work-to-github)

### Initial setup (do this once)

1. Log in to GitHub and **fork** this course repository (`ksiller/DS2022`).

2. Clone **your fork** (replace `YOUR_USERNAME`):

```bash
git clone https://github.com/YOUR_USERNAME/DS2022.git
cd DS2022
```

3. Check remotes:

```bash
git remote -v
```

After a fresh clone you should only see `origin` (your fork):

```
origin    https://github.com/YOUR_USERNAME/DS2022.git (fetch)
origin    https://github.com/YOUR_USERNAME/DS2022.git (push)
```

If `upstream` is already listed and points to `https://github.com/ksiller/DS2022.git`, skip to [Weekly sync](#weekly-sync).

4. Add the course repository as **upstream**:

```bash
git remote add upstream https://github.com/ksiller/DS2022.git
```

5. Confirm both remotes:

```bash
git remote -v
```

```
origin    https://github.com/YOUR_USERNAME/DS2022.git (fetch)
origin    https://github.com/YOUR_USERNAME/DS2022.git (push)
upstream  https://github.com/ksiller/DS2022.git (fetch)
upstream  https://github.com/ksiller/DS2022.git (push)
```

- **origin**: your fork on GitHub (you push here)
- **upstream**: the course repository (you pull updates from here)

### Weekly sync

Run these steps in your local `DS2022` folder whenever you want the latest course materials.

1. Save any local work you care about (or confirm there is nothing to save):

```bash
git status
```

If you have changes to keep:

```bash
git add .
git commit -m "Save my local work"
```

If the working tree is clean, skip the commit.

2. Update `main` from the course repository:

```bash
git switch main
git fetch upstream
git merge upstream/main
```

3. (Optional) Update your fork on GitHub so it matches what you just synced:

```bash
git push origin main
```

If Git reports a merge conflict, ask in class or office hours before forcing anything.

### Push your work to GitHub

When you add your own notes or files and want them on your fork:

```bash
git add .
git commit -m "Describe your change"
git push origin main
```

Push to **origin** (your fork), not upstream. You do not have write access to the course repository.
>>>>>>> upstream/main
