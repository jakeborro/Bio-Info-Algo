# Input single strand DNA, output reverse complement

def rvrsr(strand):
    complement = {"A":"T", "T":"A", "C":"G", "G":"C"}
    output = [complement[x] for x in strand[::-1]]
    return "".join(output)

# Multiple quotes to accommodate large output on multiple lines
# bash script tr -d '\n' if a single line is needed

print rvrsr("""strand""")
