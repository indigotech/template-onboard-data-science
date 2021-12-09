# Onboarding Data Science

Hi! Welcome to the Data Science onboarding. To help you become more familiar withour current stack, we are proposing a simple project. It is composed by a series of Jupyter Notebooks with instructions and exercises.

## Initial setup
Firstly, you may install some tools:
* [Python (Python3, preferably)](https://www.python.org/)
* [Jupyter Notebook or JupyterLab](https://jupyter.org/) or [Anaconda](https://www.anaconda.com/products/individual)

Before installing, check if you already have them in your computer.
Now, let's go to our next step: cloning this repository.

In order to update and manipulate the files in this repository in your personal computer, you should clone it.
At the top of the page, you will find a green button `code`, where you will see the https link of the repo. Copy the link, go to your terminal, find a place to put your repo and type:

> git clone <repo link>

Great! Now, you can access the local repository.

## Task 1
As your first task, we invite you to do your first commit in GitHub.
So open your repository through the terminal by typing

> code .

It will open a VSCode window. Now, find the README file and update it (for example, change the title of the page by adding your name to it).
To add your changes to the remote repository (on GitHub), save the updated file (cmd + s), go to the terminal and type:

> git checkout -b feature/onboard-issues
> git add .
> git commit -m "short message explaining the update you did"
> git push origin feature/onboard-issues

The first line creates a new branch in your repository. This means that your changes will be added to this new branch instead of the main one. This is a pattern we follow so we do not mess things up. We only add our changes to the main branch when we are sure that our code works fine and we can put it on production. To name a branch, we also follow some rules: before the slash (/), we indicate what type of issue we are going to solve in the branch (add a new `feature`, `fix` a problem, correct some `bug`,...). After the slash, we indicate what we are actually doing (which feature we are creating, or which problem we are fixing).

The second line adds the changes we made in the README file to a "staging area". The third line actually saves your changes. the `-m` allows you to add a message to your commit. It is useful and important to indicate what you have done in the commit and helps you to "know where you are" when you are doing more complicated operations.

The last line pushes your changes to the remote repository, to the branch indicated at the end of the command.

## Task 2
Now that you know how to commit your changes, open your notebook locally and let's start coding :)

Spoiler: at this onboarding version, we will be using the Palmer Penguins dataset

Horst AM, Hill AP, Gorman KB (2020). palmerpenguins: Palmer
   Archipelago (Antarctica) penguin data. R package version 0.1.0.
   https://allisonhorst.github.io/palmerpenguins/. doi:
   10.5281/zenodo.3960218.