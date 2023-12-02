Dylan Moglowsky:
  I created the Git Hook that completes a static analysis pass of the repo for every commit. For this I utilized bandit
to automate the analysis of the python files recursively through the repo and put the results in a csv file named
banditReport.csv. I learned that attempting to create a .git/hooks directory in the main repo will cause an error, and
instead I simply put the pre-commit file directly into the main to allow users to manually add it to their local git.

Wilson Sinclair:
    For my contribution, I created a logging module that is responsible for creating a logging object. This logging object is used to log anything that is deemed important or interesting during runtime. This can range from variables, return values and so forth. 5 methods have logging impemented in them. These include getCountFromAnalysis(), main(), getYAMLFiles(), scanUserName() and scanPasswords(). Logging and software forensics in general have taught us that these techniques are able to catch errors and weaknesses that would otherwise be difficult to catch by just looking at the code. If something goes wrong during runtime, then you are able to see it immediatley or even much later by looking at the logs.
