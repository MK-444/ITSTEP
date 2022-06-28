import re
regex_compile = re.compile(r"\w{7,}")

with open("input.txt","r") as reader, open("First_task__ready.txt","w") as output:
    for line in reader:
        regex_search = regex_compile.findall(line)
        if len(regex_search) > 0:
            words = " ".join(regex_search)
            output.write(words)
            output.write("\n")