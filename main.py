"""One-line review of the most boring everyday object."""

import os

REVIEW = "This rubber band held my papers together for three years, then snapped the morning I actually needed it \u2014 loyal right up to the exact wrong second."


def validate(text):
    if not isinstance(text, str):
        raise ValueError("review must be text")
    if not text.strip():
        raise ValueError("review must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("review must be 1 to 200 characters")
    return text


def self_test():
    validate(REVIEW)
    print(f"character count: {len(REVIEW)}")
    assert 1 <= len(REVIEW) <= 200
    assert "\n" not in REVIEW
    print("self-test passed")


def main():
    self_test()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(validate(REVIEW))


if __name__ == "__main__":
    main()
