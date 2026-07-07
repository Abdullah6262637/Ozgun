import re

with open('oz-parser/src/typechecker/inference.rs', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to find all `Err(super::types::TypeError::new(format!( ... ))` and add a closing `)` at the end of the `Err` argument.
# But it's easier to just find `Err(super::types::TypeError::new(format!(...))` and add a closing `)` at the end of the statement or block?
# A better way is to parse the file line by line and balance parentheses, but we can also just revert the file using git checkout, and do it properly.
