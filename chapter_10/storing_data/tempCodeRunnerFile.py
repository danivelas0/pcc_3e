from pathlib import Path
import json

path = Path('numbers.json')
numbers = json.loads(path.read_text())
print(numbers)