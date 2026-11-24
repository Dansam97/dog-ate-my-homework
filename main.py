import os

TEXT = "You said 'eat your homework' was a figure of speech. I am a dog. I do not do figures of speech."

def validated_text():
    encoded = TEXT.encode("utf-8")
    decoded = encoded.decode("utf-8")
    if not (1 <= len(decoded) <= 200):
        raise ValueError("entry must be 1-200 characters")
    if not decoded.strip():
        raise ValueError("entry must not be only whitespace")
    if decoded.count("\n") != 0:
        raise ValueError("entry must be exactly one line")
    return decoded

def main():
    text = validated_text()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write((text + "\n").encode("utf-8"))
    with open(path, "rb") as f:
        written = f.read().decode("utf-8")
    if written != text + "\n":
        raise ValueError("written bytes do not match entry text")

if __name__ == "__main__":
    main()
