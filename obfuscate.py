import hashlib
import sys
for line in sys.stdin:
    subcommunities = line.split(" ")
    subcommunities.sort()
    hashed = map(lambda subcommunity:
        hashlib.sha256(subcommunity.encode('utf-8')).hexdigest(),
        subcommunities)
    print(":".join(hashed))
