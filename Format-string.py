def format_string(string, formatter=None):
    '''Format a string using the formatter object, which
      is expected to have a format() method that accepts
      a string.'''

    class DefaultFormatter:
        '''Format a string in title case.'''

        def format(self, string):
            return str(string).title()
        # End format.

    # End Class.

    if not formatter:
        formatter = DefaultFormatter()
    # Endif;

    return formatter.format(string)

# End format_string.

hello_string = "hello world, how are you today?"
print(" input: " + hello_string)
print("output: " + format_string(hello_string))
