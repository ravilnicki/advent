import os

import dotenv

dotenv.load_dotenv()

__version__ = "1.0.0"

URL = "https://adventofcode.com/{}/day/{}/input"
SESSION_ID = os.environ["SESSION_ID"]
HEADERS = {
    "User-Agent": "https://github.com/ravilnicki/advent by ravilnicki@gmail.com",
    "Cookie": "session=" + SESSION_ID,
}
