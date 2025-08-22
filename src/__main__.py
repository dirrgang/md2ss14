import sys
from converter import md_to_ss14

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m md2ss14 input.md [output.txt]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    with open(input_file, encoding="utf-8") as f:
        md = f.read()

    ss14_doc = md_to_ss14(md)

    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(ss14_doc)
    else:
        print(ss14_doc)

if __name__ == "__main__":
    main()