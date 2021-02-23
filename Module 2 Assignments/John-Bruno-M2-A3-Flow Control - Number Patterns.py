{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# M2-A3 Flow Control - Number Patterns\n",
    "\n",
    "# Instructions:\n",
    "Write a Python script that accepts three numbers from the user, then outputs one of three results: \n",
    "- Numbers are increasing\n",
    "- Numbers are decreasing\n",
    "- Numbers are neither increasing nor decreasing\n",
    "\n",
    "**Bold** indicates input from the console.<br>\n",
    "Your code design should be reasonably efficient. \n",
    "\n",
    "### Expected sample output:\n",
    "Please input number one:<br>\n",
    "**11**<br>\n",
    "Please input number two:<br>\n",
    "**27**<br>\n",
    "Please input number three:<br>\n",
    "**99**<br>\n",
    "Numbers are increasing\n",
    "\n",
    "### Expected sample output:\n",
    "Please input number one:<br>\n",
    "**1020**<br>\n",
    "Please input number two:<br>\n",
    "**512**<br>\n",
    "Please input number three:<br>\n",
    "**0**<br>\n",
    "Numbers are decreasing\n",
    "\n",
    "### Expected sample output:\n",
    "Please input number one:<br>\n",
    "**55**<br>\n",
    "Please input number two:<br>\n",
    "**67**<br>\n",
    "Please input number three:<br>\n",
    "**1**<br>\n",
    "Numbers are neither increasing nor decreasing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please input number one: 5\n",
      "Please input number two: 6\n",
      "Please input number three: 3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Numbers are neither increasing nor decreasing\n"
     ]
    }
   ],
   "source": [
    "num1 = int (input(('Please input number one:')))\n",
    "num2 = int (input(('Please input number two:')))\n",
    "num3 = int (input(('Please input number three:')))\n",
    "if num1 < num2 and num2 < num3:\n",
    "    print('Numbers are increasing')\n",
    "elif num1 > num2 and num2 > num3:\n",
    "    print('Numbers are decreasing')\n",
    "else:\n",
    "    print('Numbers are neither increasing nor decreasing')"
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
