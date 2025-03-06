# playground: toy projects, coding challenges, & practice problems

Setup and troubleshooting notes:
- In current config, I had to perform some manual steps in Cursor / VSCode after building the devcontainer:
-- `chown` all project folder files and subdirectories to the `appuser` user
-- Command palette "Developer: Reload Window" to not get "no registered task type: 'docker-build'" error
-- Change my selected Python interpreter to the same Python3.13 interpreter that is set as the preferred path: Command Palette and "Python: Select Interpreter"
-- Open new bash Terminal window to get proper interpreter to which pip -m had installed Python packages