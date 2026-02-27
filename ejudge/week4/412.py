import json
import sys

obj1 = json.loads(sys.stdin.readline())
obj2 = json.loads(sys.stdin.readline())

diffs = []

def deep_diff(a, b, path=""):
    keys = set(a.keys()) | set(b.keys())
    for key in keys:
        subpath = f"{path}.{key}" if path else key
        va = a.get(key, "<missing>")
        vb = b.get(key, "<missing>")
        if isinstance(va, dict) and isinstance(vb, dict):
            deep_diff(va, vb, subpath)
        elif va != vb:
            va_str = json.dumps(va, separators=(',', ':')) if va != "<missing>" else "<missing>"
            vb_str = json.dumps(vb, separators=(',', ':')) if vb != "<missing>" else "<missing>"
            diffs.append(f"{subpath} : {va_str} -> {vb_str}")

deep_diff(obj1, obj2)

if diffs:
    for line in sorted(diffs):
        print(line)
else:
    print("No differences")