import re

with open('oz-parser/src/typechecker/inference.rs', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace any `.to_string()` inside `Err(...)` that was missed.
# Specifically, we have strings followed by `.to_string()` inside `Err(...)`.
# Let's just find `Err(` followed by string and `.to_string()` possibly with newlines.
content = re.sub(
    r'Err\(\s*"([^"]+)"\s*\.\s*to_string\(\)\s*\)',
    r'Err(type_err!("\1"))',
    content,
    flags=re.DOTALL
)

# Also check for any remaining `Err("...".to_string())` where the string might have quotes inside it. (none reported)

with open('oz-parser/src/typechecker/inference.rs', 'w', encoding='utf-8') as f:
    f.write(content)
