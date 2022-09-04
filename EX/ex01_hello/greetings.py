"""EX01 Greetings."""
"""
3. GreetingsGreetingsGreetings
Example output:

Enter a greeting: Hello
Enter a recipient: world
How many times to repeat: 3
Hello world! Hello world! Hello world!

"""
greeting = f"{input('Enter a greeting: ')} "
recipient = f"{input('Enter a recipient: ')}! "
repeat = input("How many times to repeat: ")
print((greeting + recipient) * repeat)
