# Fix sys path thing
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.absolute()))

from .pixray import run

