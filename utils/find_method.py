# # Find the method in the source code given a line number
# def find_method(source, line_no):
#     lines = source.split("\n")
 
#     if line_no is None:
#         raise Exception("Unable to extract line number from logs.\n")
    
#     start = line_no - 1

#     while start >= 0 and "public" not in lines[start]:
#         start -= 1

#     brace = 0
#     end = start
#     for i in range(start, len(lines)):
#         if "{" in lines[i]:
#             brace += 1
#         if "}" in lines[i]:
#             brace -= 1
#         if brace == 0 and i > start:
#             end = i
#             break

#     return start, end

def find_method(source, line_no):
    lines = source.split("\n")

    # If line number is missing or invalid
    if not line_no:
        return None, None

    # Clamp line number to file size
    line_no = max(1, min(line_no, len(lines)))

    start = line_no - 1

    # Walk upwards until we hit a method signature
    while start >= 0:
        if "public" in lines[start] and "(" in lines[start]:
            break
        start -= 1

    if start < 0:
        return None, None

    # Find the end of the method using brace matching
    brace = 0
    end = start
    found_body = False

    for i in range(start, len(lines)):
        brace += lines[i].count("{")
        brace -= lines[i].count("}")

        if "{" in lines[i]:
            found_body = True

        if found_body and brace == 0 and i > start:
            end = i
            break

    return start, end
