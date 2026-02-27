import json
import sys

source = json.loads(sys.stdin.readline())
patch = json.loads(sys.stdin.readline())

def merge_patch(src, pat):
    result = dict(src)
    for key, val in pat.items():
        if val is None:
            if key in result:
                del result[key]
        elif key in result and isinstance(result[key], dict) and isinstance(val, dict):
            result[key] = merge_patch(result[key], val)
        else:
            result[key] = val
    return result

patched = merge_patch(source, patch)
print(json.dumps(patched, separators=(',', ':'), sort_keys=True))