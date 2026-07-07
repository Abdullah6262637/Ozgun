import re

def process_file():
    with open('oz-parser/src/typechecker/inference.rs', 'r', encoding='utf-8') as f:
        content = f.read()

    # Signatures
    content = content.replace('Result<Type, String>', 'Result<Type, super::types::TypeError>')
    content = content.replace('Result<(), String>', 'Result<(), super::types::TypeError>')
    content = content.replace('Result<TypeEnv, String>', 'Result<TypeEnv, super::types::TypeError>')

    # We want to replace Err(...) with Err((...).into())
    # A simple token parser in Python to balance parens
    def replace_err(text):
        out = ""
        i = 0
        while i < len(text):
            if text[i:i+4] == "Err(":
                out += "Err(("
                i += 4
                parens = 1
                start = i
                while i < len(text) and parens > 0:
                    if text[i] == '(':
                        parens += 1
                    elif text[i] == ')':
                        parens -= 1
                    if parens > 0:
                        out += text[i]
                    i += 1
                out += ").into())"
            else:
                out += text[i]
                i += 1
        return out

    content = replace_err(content)
    
    # We want to map unify errors: `self.unify(&t1, &t2)?` -> `self.unify(&t1, &t2).map_err(|e| e.with_span(expr.span.clone()))?`
    # Also `self.unify(a, b)?`
    content = re.sub(r'(self\.unify\([^)]+\))\?', r'\1.map_err(|e| e.with_span(expr.span.clone()))?', content)
    
    with open('oz-parser/src/typechecker/inference.rs', 'w', encoding='utf-8') as f:
        f.write(content)

process_file()
