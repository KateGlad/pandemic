import re
import numpy as np

def extract_text(text):
    try:
        text = re.sub(r"(?:<.*?>|[^А-я\s])", " ", text).strip()
        return re.sub(r"\s+", " ", text)
    except TypeError:
        return np.nan

data["responsibilities"].apply(lambda x: extract_text(x))
data["achievements"].apply(lambda x: extract_text(x))
