# [100 Days of Python by Angela Yu](https://www.udemy.com/course/100-days-of-code/)
## Day 17: The quiz project and the benefits of OOP

I learned about object oriented programming in college. 
But I haven't done any project since. 
It's a good refresher how the OOP concept works and how to call variables from different files using Python.

Some key lessons I learned today:

1. How to declare a class in Python. The syntax seemed different and new to me.
```
 # Create a class
 class Question:
  # Create a constructor. This holds default values. It's like DNA.
  def__init__(self,answer,text):
  self.text=text
  self.answer=answer 
```		
2. I kept getting this `TypeError`and found this helpful: ["TypeError: list indices must be integers, not dict"](https://stackoverflow.com/questions/26266425/typeerror-list-indices-must-be-integers-not-dict) 
3. In order to loop through the dictionary value, use the value directly.
4. Go back to the first challenge to understand: classes, objects, attributes, and methods.
