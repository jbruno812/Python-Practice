{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# M1-A4 Variables, Expressions, and Types (A)\n",
    "\n",
    "# Instructions: \n",
    "\n",
    "Write code that asks the user for two numbers and then returns the two numbers added, the two numbers multiplied, the first number raised to the power of the second number, the first number divided by the second number and the variable type of the first number divided by the second. <br>\n",
    "\n",
    "**Bold** indicates input from the console.<br>\n",
    "Do not hard code; different numbers will be tested.\n",
    "\n",
    "### Expected sample output:\n",
    "Enter the first number:<br>\n",
    "**9**<br>\n",
    "Enter the second number:<br>\n",
    "**4**<br>\n",
    "13<br>\n",
    "36<br>\n",
    "6561<br>\n",
    "2.25<br>\n",
    "<class 'float'>\n",
    "\n",
    "### Expected sample output:\n",
    "Enter the first number:<br>\n",
    "**6**<br>\n",
    "Enter the second number:<br>\n",
    "**2**<br>\n",
    "8<br>\n",
    "12<br>\n",
    "36<br>\n",
    "3.0<br>\n",
    "<class 'float'>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the first number 9\n",
      "Enter the second number 4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "13\n",
      "36\n",
      "6561\n",
      "2.25\n",
      "<class 'float'>\n"
     ]
    }
   ],
   "source": [
    "num1 = int (input(('Enter the first number')))\n",
    "num2 = int (input(('Enter the second number')))\n",
    "num3 = int (num1+num2)\n",
    "print (num3)\n",
    "num4 = int (num1*num2)\n",
    "print (num4)\n",
    "num5 = int (num1**num2)\n",
    "print (num5)\n",
    "num6 = float (num1/num2)\n",
    "print (num6)\n",
    "print (type(num6))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
