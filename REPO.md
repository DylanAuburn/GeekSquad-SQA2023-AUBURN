Dylan Moglowsky:
  I created the Git Hook that completes a static analysis pass of the repo for every commit. For this I utilized bandit
to automate the analysis of the python files recursively through the repo and put the results in a csv file named
banditReport.csv. I learned that attempting to create a .git/hooks directory in the main repo will cause an error, and
instead I simply put the pre-commit file directly into the main to allow users to manually add it to their local git.
