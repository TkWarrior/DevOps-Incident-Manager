# Find the method in the source code given a line number
def find_method(source, line_no):
    lines = source.split("\n")
    
    if line_no is None:
        raise Exception("Unable to extract line number from logs.\n")
    
    start = line_no - 1

    while start >= 0 and "public" not in lines[start]:
        start -= 1

    brace = 0
    end = start
    for i in range(start, len(lines)):
        if "{" in lines[i]:
            brace += 1
        if "}" in lines[i]:
            brace -= 1
        if brace == 0 and i > start:
            end = i
            break

    return start, end
