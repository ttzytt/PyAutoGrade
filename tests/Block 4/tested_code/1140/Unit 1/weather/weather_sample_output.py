Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.




"""
Sample output for T5, v2:

What is the temperature today (in °F)? 95
Wow that's hot.
That's 35 °C.

What is the temperature today (in °F)? 60
That's 15.56 °C.

What is the temperature today (in °F)? 40
That's so cold.
That's 4.44 °C.

What is the temperature today (in °F)? 20
That's freezing!
That's - 6.67 °C.

"""






"""
Sample output for T6, v2:

# good temperature, rain, no jacket
What is the temperature today (in °F)? 60
Is it raining? Yes
Do you have a jacket? No
You shouldn’t play outside today.

# good temperature, rain, jacket
What is the temperature today (in °F)? 60
Is it raining? Yes
Do you have a jacket? Yes
You should play outside today.

# good temperature, no rain
What is the temperature today (in °F)? 60
Is it raining? No
You should play outside today.

# bad temperature, jacket
What is the temperature today (in °F)? 40
Do you have a jacket? Yes
You should play outside today.

# bad temperature, no jacket
What is the temperature today (in °F)? 40
Do you have a jacket? No
You shouldn't play outside today.

# too cold
What is the temperature today (in °F)? 20
You shouldn’t play outside today.

# too hot
What is the temperature today (in °F)? 300
You shouldn’t play outside today.

"""
