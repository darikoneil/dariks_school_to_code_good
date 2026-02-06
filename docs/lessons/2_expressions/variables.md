---
title: variables
chapter: Expressions
chapter_number: 2
lesson_number: 1
---

# Variables
Variables are names that refer to values. Assigning a variable binds a name to a 
value; later references to the name use the bound value. Variables make programs 
readable and let us reuse computed results. Variables can be reassigned to new 
values,  and in both Python & Matlab, they can refer to values of different types 
over time (dynamic typing).


??? abstract "Variables vs. Values"

    Let's return to our cooking analogy: variables are like labels on bowls, and  
    values are the dough inside.

    - Putting dough into a bowl = assigning a value to a variable.
    - Moving the label to a different bowl = rebinding the variable to a new value.
    - Scooping dough into a new bowl = copying a value (shallow or deep copy).
    - Two labels on the same bowl = two variables referencing the same mutable object;  
    changing the dough through one label affects the other.


=== "Python"

    ```python
    # Simple assignment
    x = 10
    
    # Rebinding and dynamic typing
    x = "now a string"

    # Multiple assignment / unpacking
    a, b = 1, 2
    a, b = b, a  # swap without a temp variable

    # Type hints (optional)
    y: int = 5
    ```

=== "Matlab"

    ```matlab
    % Assignment
    x = 10;

    % Rebinding and dynamic typing
    x = 'now a string';

    % Multiple assignment is usually done element-wise or via arrays
    a = 1; b = 2;
    ```


## Gotchas

1. **Case-Sensitivity**: Variables names are case-sensitive and must start with 
    a letter or underscore
2. **Reserved keywords**: Special reserved words (e.g., `if`, `for`, `while`) cannot be 
   used as variable names.
3. **Shadowing**: Don't use names that shadow other things (e.g., `list`, `str`, 
   `sum`). You may no longer be able to access them!
4. **Mutability**: Always assume variables are mutable by default; unexpected sharing 
   happens when multiple variables refer to the same object!
