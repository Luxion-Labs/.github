import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from contributors import pick_people

cfg = {"limit": 2, "ignore": ["bot"], "thanks": {"Zed": ["Docs"]}}
people, total = pick_people({"a": 5, "b": 3, "c": 1, "bot": 9}, cfg)
assert [p[0] for p in people] == ["a", "zed"], people  # credited user kept despite 0 commits, case-insensitive
assert total == 4
