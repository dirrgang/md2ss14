# Markdown to SS14 Converter

This project provides a command-line tool to convert Markdown files into a formatted string suitable for SS14. The tool processes various Markdown elements such as headings, bold, italic, inline code, bulleted lists, and color formatting.

## Features

- Converts Markdown headings to SS14 formatted headings.
- Supports bold and italic text formatting.
- Handles inline code (removes it as it's not in SS14 spec).
- Converts bulleted lists into SS14 bullet format.
- Supports color formatting from HTML and Markdown color extensions.

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

To use the converter, run the following command in your terminal:

```
python -m src <input_file.md> [output_file.txt]
```

- `<input_file.md>`: The path to the input Markdown file.
- `[output_file.txt]`: (Optional) The path to the output text file. If not provided, the output will be printed to the console.

## Example

Given an input Markdown file `example.md`:

```
# Heading 1
This is **bold** text and this is *italic* text.
- Item 1
- Item 2
```

You can convert it by running:

```
python -m src example.md output.txt
```

The output will be written to `output.txt` in the SS14 format.

## Testing

To run the tests for the converter, navigate to the `tests` directory and run:

```
pytest test_converter.py
```

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.