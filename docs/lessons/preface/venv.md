---
title: Virtual Environments
chapter: Preface
---
# Virtual Environments
Virtual environments are a crucial tool in software development that allow you to 
create isolated spaces for your projects. This isolation helps manage dependencies and 
avoid conflicts between different projects. For example, you might have two projects
that require different versions of the same library. You might even have two projects
that have different functions with identical names! By using virtual environments, 
you can ensure that each project stays self-contained and doesn't interfere with others.

Most virtual environments are paired with a package manager, which helps you install, 
update, and manage the libraries your project depends on.

## Python
Popular tools for managing virtual environments in Python include:
- **venv**: A built-in module that comes with Python 3. It allows you to create 
    lightweight virtual environments. It is usually paired with the `pip` package 
    manager that comes bundled with Python.
- **pipx**: A tool to help you install and run Python applications in isolated 
  environments. Usually paired with `poetry` package manager.
- **conda**: A cross-platform package manager that also manages virtual environments.
  It is popular in data science and scientific computing communities, and for the 
  sudden changes to the academic and non-profit licensing of their user interface 
  *Anaconda* in 2024 (alongside unexpected legal threats to institutions that 
  continued  to use it). A command-line only implementation *miniconda* remains 
  free. Conda manages both packages and environments for multiple programming languages.
- **uv**: An extremely fast, modern tool made by Astral. It is designed to be simple 
  to be simple to use and easy to integrate into existing workflows.

!!! note

    I heavily recommend using `uv` for beginners and experienced developers alike.

## MATLAB
MATLAB achieves similar functionality to virtual environments by using a "path" system.
You can create separate folders for different projects and add or remove these folders
from the MATLAB path as needed. This way, you can manage different sets of functions
and scripts for each project without conflicts. Unfortunately, this is quite cumbersome
and not conducive to good development practices.