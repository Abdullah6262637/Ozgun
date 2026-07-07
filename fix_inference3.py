import re

with open('oz-parser/src/typechecker/inference.rs', 'r', encoding='utf-8') as f:
    content = f.read()

# Add macro definition at the top
macro_def = """
macro_rules! type_err {
    ($($arg:tt)*) => {
        super::types::TypeError::new(format!($($arg)*))
    }
}
"""

# Insert macro after imports
import_end = content.find('\n\n', content.find('use std::path::PathBuf;'))
content = content[:import_end] + "\n" + macro_def + content[import_end:]

# Replace signatures
content = content.replace('Result<Type, String>', 'Result<Type, super::types::TypeError>')
content = content.replace('Result<(), String>', 'Result<(), super::types::TypeError>')
content = content.replace('Result<TypeEnv, String>', 'Result<TypeEnv, super::types::TypeError>')
content = content.replace('Result<Vec<Spanned<Statement>>, String>', 'Result<Vec<Spanned<Statement>>, super::types::TypeError>')

# Replace Err(format!(...)) with Err(type_err!(...))
content = content.replace('Err(format!(', 'Err(type_err!(')

# Replace Err("...") with Err(type_err!("..."))
content = re.sub(r'Err\(\s*"([^"]+)"\s*\)', r'Err(type_err!("\1"))', content)

# But there is also `Err(e)` where `e` is an error from another function, though most use `?`.
# In inference.rs, there is `Err(format!("Sözcüksel analiz hatası at {:?}", span))` - this is handled by `Err(format!(`

with open('oz-parser/src/typechecker/inference.rs', 'w', encoding='utf-8') as f:
    f.write(content)
