---
title: numerics
chapter: Data Types
chapter_number: 1
lesson_number: 1
---

# Numeric Data Types
Numeric data types are used to represent numbers in programming. They can be broadly 
categorized into two main types: integers and floating-point numbers.

## Integer Types
Integer types represent whole numbers without any fractional or decimal component.

They can be further divided into two categories:

 
### Signed Integers: 
Signed integers can represent both positive and negative values.

  - `int8`: 8-bit signed integer (-128 to 127)
  - `int16`: 16-bit signed integer (-32,768 to 32,767)
  - `int32`: 32-bit signed integer (-2,147,483,648 to 2,147,483,647)
  - `int64`: 64-bit signed integer (-large number to large number)

=== "Python"

    ```python
    # Standard Library
    python_integer = 10          # signed int

    # Numpy
    import numpy as np

    a = np.int8(15)  # 8-bit signed integer
    b = np.int16(15) # 16-bit signed integer
    c = np.int32(15) # 32-bit signed integer
    d = np.int64(15) # 64-bit signed integer
    e = np.intp(15) # platform-dependent signed integer
    ```

=== "Matlab"

    ```matlab
    a = int8(15);    % 8-bit signed integer
    b = int16(15);   % 16-bit signed integer
    c = int32(15);   % 32-bit signed integer
    d = int64(15);   % 64-bit signed integer
    ```

### Unsigned Integers
Unsigned integers can only represent non-negative values. Examples include:

  - `uint8`: 8-bit unsigned integer (0 to 255)
  - `uint16`: 16-bit unsigned integer (0 to 65,535)
  - `uint32`: 32-bit unsigned integer (0 to 4,294,967,295)
  - `uint64`: 64-bit unsigned integer (0 to large number)

=== "Python"

    ```python
    # Numpy
    import numpy as np

    f = np.uint8(15)  # 8-bit unsigned integer
    g = np.uint16(15) # 16-bit unsigned integer
    h = np.uint32(15) # 32-bit unsigned integer
    i = np.uint64(15) # 64-bit unsigned integer
    ```

=== "Matlab"

    ```matlab
    e = uint8(15);   % 8-bit unsigned integer
    f = uint16(15);  % 16-bit unsigned integer
    g = uint32(15);  % 32-bit unsigned integer
    h = uint64(15);  % 64-bit unsigned integer
    ```

## Floating-Point Types
Floating-point types are used to represent real numbers that have a fractional component.

  - float16: 16-bit floating-point number (half precision)
  - float32: 32-bit floating-point number (single precision)
  - float64: 64-bit floating-point number (double precision)

=== "Python"

    ```python
    python_float = 3.14        # float

    # Numpy
    import numpy as np

    j = np.float16(3.14) # 16-bit floating-point number
    k = np.float32(3.14) # 32-bit floating-point number
    l = np.float64(3.14) # 64-bit floating-point number
    ```

=== "Matlab"

    ```matlab
    i = single(3.14); % 32-bit floating-point number
    j = double(3.14); % 64-bit floating-point number
    ```

## Casting Between Numeric Types
Casting refers to the conversion of one numeric type to another. This is often necessary
when performing operations that involve different numeric types. Most programming  
languages provide built-in functions to facilitate type casting. It is important to 
be aware of potential data loss when casting from a higher precision type to a  
lower precision type.

=== "Python"

    ```python
    import numpy as np

    # Casting from float to int
    float_num = 9.99
    int_num = int(float_num)  # Standard Library

    # Numpy casting
    a = np.float32(9.99)
    b = a.astype(np.int32)  # Cast to 32-bit integer
    ```
=== "Matlab"

    ```matlab
    float_num = 9.99;
    int_num = int32(float_num); % Cast to 32-bit integer
    ```

## Choosing the Right Numeric Type
When choosing a numeric type, consider the following factors:
- **Range**: Ensure the type can accommodate the expected range of values.
- **Precision**: Choose a type that provides sufficient precision for calculations.
- **Memory Usage**: Consider the memory constraints of your application.
- **Performance**: Some operations may be faster with certain numeric types.

## Gotcha's
- Be cautious of overflow and underflow when working with fixed-size integer types.
- Floating-point arithmetic can introduce rounding errors; be mindful when comparing
  floating-point numbers to determine if they are identical.
- When casting a float to an int, not all langauge will follow the same rounding rules.
  Always check the documentation for the specific behavior in your programming language.
