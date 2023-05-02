import sys, subprocess

input = sys.stdin.read()

p = subprocess.Popen(
    ["python3", "simple-sat/src/sat.py", "-a"],
    stdout=subprocess.PIPE,
    stdin=subprocess.PIPE,
    stderr=subprocess.STDOUT,
)
output = p.communicate(input=str.encode(input))[0].decode("utf-8").strip()

print(
    "\n".join(
        [
            "".join(
                ["0" if "~" in x else "1" for x in [v for v in l.split() if "I" in v]]
            )
            for l in output.split("\n")
        ]
    )
)
