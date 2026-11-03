"""Download the Inside Airbnb Paris data (snapshot of 16 September 2026) into data/ and check the MD5.

Usage: python data.py
"""
import hashlib
import urllib.request
from pathlib import Path

BASE_URL = "https://data.insideairbnb.com/france/ile-de-france/paris/2026-09-16"

FILES = {
    "listings.csv.gz": (f"{BASE_URL}/data/listings.csv.gz", "141d5a6ee3fdd003a305ac10e16f72e6"),
    "neighbourhoods.geojson": (f"{BASE_URL}/visualisations/neighbourhoods.geojson", None),
}

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(exist_ok=True)

for name, (url, expected_md5) in FILES.items():
    path = DATA_DIR / name

    if not path.exists():
        print(f"Downloading {name}...")
        urllib.request.urlretrieve(url, path)

    if expected_md5 is not None:
        md5 = hashlib.md5(path.read_bytes()).hexdigest()
        if md5 != expected_md5:
            raise ValueError(f"{name}: MD5 mismatch ({md5} instead of {expected_md5}). "
                             "Delete the file and download it again.")
        print(f"{name}: OK (MD5 verified)")
    else:
        print(f"{name}: OK")
