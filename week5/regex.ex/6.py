import re

txt = "Hello, world. How are you?"
res = re.sub(r"[ ,.]", ":", txt)

print("Modified text:", res)