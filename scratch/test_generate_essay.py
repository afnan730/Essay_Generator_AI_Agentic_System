import os
import sys
from dotenv import load_dotenv
load_dotenv()

from generate_essay import generate_essay

print("Testing generate_essay with topic 'Palestine'...")
try:
    result = generate_essay("Palestine")
    print("SUCCESS!")
    print("Title:", result["title"])
    print("Number of sections:", len(result["sections"]))
    for i, section in enumerate(result["sections"]):
        print(f"Section {i+1}:")
        print("  Heading:", section["heading"])
        print("  Image URL:", section["image_url"])
        print("  Content preview:", section["content"][:100] + "...")
except Exception as e:
    print("FAILED with exception:")
    import traceback
    traceback.print_exc(file=sys.stdout)
