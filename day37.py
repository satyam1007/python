#day37 - Virtual Environment in Python


'''
1. Why Virtual Environments Matter

Think of a virtual environment (venv) as your own little sandbox.
Without it, Python packages you install are global — which can cause conflicts between projects.
Without it, Python packages you install are global — which can cause conflicts between projects.

With venv:

    Each project can have its own package versions

    You won't break other projects when upgrading dependencies

    Your setup is cleaner and more reproducible

2. Check Python on Your Mac

Open Terminal and check your Python version:

python3 --version
and
pip3 --version
macOS ships with an old Python 2.x sometimes, so always use python3 and pip3.

3. Create a Virtual Environment

In the folder where your project will live:

python3 -m venv myenv
python3 -m venv → creates the environment
myenv → name of the folder (you can choose anything)

4. Activate the Virtual Environment

Run:
source myenv/bin/activate
If successful, your terminal prompt changes, e.g.:

(myenv) yourname@MacBook project-folder %
Now any pip install ... goes into this environment only.

5. Installing Packages

Inside the activated environment:
pip install requests

To see installed packages:
pip list

6. Deactivating

When you're done working:
deactivate

7. Saving and Reusing

If you want to share your dependencies:

pip freeze > requirements.txt

And later (or on another machine):

pip install -r requirements.txt

Quick Cheatsheet
Command	                  Purpose
python3 -m venv myenv ==>	Create virtual environment
source myenv/bin/activate ==>	Activate on macOS/Linux
deactivate ==> Exit virtual environment
pip freeze > requirements.txt	==> Save dependencies
pip install -r requirements.txt	==> Install from file
'''
