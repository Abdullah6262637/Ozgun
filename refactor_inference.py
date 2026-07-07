import re

with open('oz-parser/src/typechecker/inference.rs', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Result<..., String> with Result<..., super::types::TypeError>
content = content.replace('Result<Type, String>', 'Result<Type, super::types::TypeError>')
content = content.replace('Result<(), String>', 'Result<(), super::types::TypeError>')

# Replace Err("...") with Err(super::types::TypeError::new("..."))
# Be careful with already converted ones.
content = re.sub(r'Err\(\s*format!\(', r'Err(super::types::TypeError::new(format!(', content)
content = re.sub(r'Err\(\s*"([^"]+)"\s*\)', r'Err(super::types::TypeError::new("\1"))', content)

# Map unify errors to include spans
# self.unify(&t1, &t2)? -> self.unify(&t1, &t2).map_err(|e| e.with_span(expr.span.clone()))?
content = re.sub(r'(self\.unify\([^)]+\))\?', r'\1.map_err(|e| e.with_span(expr.span.clone()))?', content)

with open('oz-parser/src/typechecker/inference.rs', 'w', encoding='utf-8') as f:
    f.write(content)
