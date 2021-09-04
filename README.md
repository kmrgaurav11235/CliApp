# CliApp

## Installations
* Install Python3: `brew install python3`
* Pip3 is installed with Python3
* To install virtualenv via pip run: `pip3 install virtualenv`

## Using virtalenv
If you have a project in a directory called my-project you can set up virtualenv for that project by running:

```cd my-project/```

```virtualenv venv```

These commands create a venv/ directory in your project where all dependencies are installed. You need to activate it first though (in every terminal instance where you are working on your project):

```source venv/bin/activate```

You should see a (venv) appear at the beginning of your terminal prompt indicating that you are working inside the virtualenv. Now when you install something like this:

```pip install .```

or

```pip install --editable .```

It will get installed in the venv/ folder, and not conflict with other projects.

Now, you can run your python script, e.g. `my_script.py`:

```my_script```

To leave the virtual environment run:

```deactivate```
