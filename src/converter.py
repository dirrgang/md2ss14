# filepath: /md2ss14/md2ss14/src/converter.py
import re


def md_to_ss14(md: str) -> str:
    # Headings: #, ##, ###, ####
    def heading_repl(match):
        level = len(match.group(1))
        text = match.group(2).strip()
        return f"[head={level}]{text}[/head]"

    md = re.sub(r"^(#{1,4})\s+(.*)$", heading_repl, md, flags=re.MULTILINE)

    # Bold-italic: ***text*** or ___text___
    md = re.sub(r"(\*\*\*|___)(.*?)\1", r"[bolditalic]\2[/bolditalic]", md)

    # Bold: **text** or __text__
    md = re.sub(r"(\*\*|__)(.*?)\1", r"[bold]\2[/bold]", md)

    # Italic: *text* or _text_
    md = re.sub(r"(\*|_)(.*?)\1", r"[italic]\2[/italic]", md)

    # Inline code: `text` (optional, not in SS14 spec, so ignore or remove)
    md = re.sub(r"`(.*?)`", r"\1", md)

    # Bulleted lists: - item, * item, + item
    def bullet_repl(match):
        text = match.group(1).strip()
        return f"[bullet/]{text}"

    md = re.sub(r"^\s*[-*+]\s+(.*)$", bullet_repl, md, flags=re.MULTILINE)

    # Color: <span style="color:red">text</span> or <font color="red">text</font>
    md = re.sub(
        r'<(?:span|font)[^>]*color\s*=\s*["\']?([#\w]+)["\']?[^>]*>(.*?)</(?:span|font)>',
        r"[color=\1]\2[/color]",
        md,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # Markdown color extension: [color=red]text[/color]
    md = re.sub(
        r"\[color=([#\w]+)\](.*?)\[/color\]",
        r"[color=\1]\2[/color]",
        md,
        flags=re.DOTALL,
    )

    # Remove any remaining HTML tags
    md = re.sub(r"<[^>]+>", "", md)

    return md
