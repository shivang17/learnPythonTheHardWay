# Define empty braces to format various other texts
formatter = "{} {} {}"

# Add various number into the formatter using FORMAT method
print(formatter.format(1,2,3,4))

# Add various strings into the formatter using FORMAT method
print(formatter.format("one","two","three","four"))

# Add boolean into the formatter using FORMAT method
print(formatter.format(True,False, False, True))

# Insert the variable itself again in own variable using FORMAT method
print(formatter.format(formatter,formatter,formatter,formatter))

print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear")
    )