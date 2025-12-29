def markdown_to_blocks(markdown):
    lines = markdown.split("\n\n")
    new_list = []
    for line in lines:
        if line == "":
            continue
        new_list.append(line.strip())
    return new_list
