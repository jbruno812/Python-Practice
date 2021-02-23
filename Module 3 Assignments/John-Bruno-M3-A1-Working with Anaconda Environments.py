{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Assignment: Creating, Using, and Deleting Conda Environments\n",
    "\n",
    "A *conda enviornment* is a virtual environment implemented as a folder that contains conda packages you have installed. A primary motivation to use virtual environments is to manage dependencies. For example, you may have a legacy project that requires an earlier version of ```numpy``` or ```pandas``` and a separate project for which you prefer to use the most recent versions. To accomplish this, you create virtual environments and specify the version of packages needed for that environment. Additionally, having unnecessary packages in your environment leads to inefficiencies and a higher probability of conflict.\n",
    "\n",
    "For this reason, if you are doing specialized work (e.g., a project that requires modules that you don't typically use), you may want to create an environment specifically for that project.\n",
    "\n",
    "If you have used pip and virtualenv in the past, you can use conda to perform all of the same operations. Pip is a package manager and virtualenv is an environment manager. Conda is both.\n",
    "\n",
    "This tutorial is only an overview. For a much more detailed understanding of conda, see the docs (https://docs.conda.io/projects/conda/en/latest/user-guide/index.html)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "To work with conda *within* this notebook, we'll use magic commands.\n",
    "\n",
    "Magics are specific to and provided by the IPython kernel. Whether Magics are available on a kernel is a decision that is made by the kernel developer on a per-kernel basis. To work properly, Magics must use a syntax element which is not valid in the underlying language. For example, the IPython kernel uses the % syntax element for Magics as % is not a valid unary operator in Python. (see https://ipython.readthedocs.io/en/stable/interactive/magics.html for more info)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# List the folders and files in the current directory. This can be useful for determining where an output file was written when using a relative path.\n",
    "%ls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# List the packages in the current environment.\n",
    "%conda list"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "List the environments on your system. You should at least have the ```base``` enviornment."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%conda env list"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Create a new environment named 'temp'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "To create a conda virtual environment, **Using an Anaconda prompt (NOT a magic command)**, type the following:\n",
    "```conda create -n temp```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "# type the magic command to list environments: (your list will look different than mine, but should at least include base and temp)\n",
    "%conda env list"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Using the Conda Cheat sheet, remove the temp environment. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Type the magic command to list environments\n",
    "%conda list env"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Create a new environment called msba by cloning the base environment. Again, do this at the Anaconda prompt, not in Jupyter Lab."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# List the environments\n",
    "conda list env"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# List the packages in the msba environment (refer to the cheat sheet)\n",
    "conda list --name msba"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using the command prompt, install the Beautiful Soup module (bs4) into the msba enviornment."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# List the packages in the msba environment\n",
    "conda list --name msba"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "### When running any magic commands, my Visual Studio Code starts up and gives me the terminal, so I did everything in this notebook in that and wasn't sure how to show it in the notebook.\n",
    "### I now have another environment called msba with beautiful soup installed on my pc, seperate from my base. Again, wasn't sure how to show in notebook if that was what was suppose to be done."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
