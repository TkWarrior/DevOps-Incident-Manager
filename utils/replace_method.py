# Replace the method in the source code with the new method
def replace_method(source, start, end, new_method):
    
    lines = source.split("\n")
    return "\n".join(
        lines[:start] +
        [new_method] +
        lines[end+1:]
    )
