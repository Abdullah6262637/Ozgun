use wasm_bindgen::prelude::*;
use std::rc::Rc;
use std::cell::RefCell;
use oz_vm::{compiler::Compiler, vm::VM};
use oz_lexer::Token;
use logos::Logos;

#[wasm_bindgen]
pub fn run_tilk_code(code: &str) -> String {
    let lexer = Token::lexer(code);
    let mut tokens = Vec::new();
    for (token_res, span) in lexer.spanned() {
        match token_res {
            Ok(token) => tokens.push((token, span)),
            Err(_) => return format!("HATA: Sözcüksel analiz hatası {:?}", span),
        }
    }
    
    let ast = match oz_parser::parse_tokens(tokens, code.len()) {
        Ok(ast) => ast,
        Err(e) => return format!("HATA: Sözdizimi hatası: {:?}", e),
    };
    
    let compiler = Compiler::new();
    let instructions = match compiler.compile_program(&ast) {
        Ok(insts) => insts,
        Err(e) => return format!("HATA: Derleme hatası: {:?}", e),
    };
    
    let stdout_buf = Rc::new(RefCell::new(Vec::new()));
    
    let mut vm = VM::new(instructions);
    vm.stdout = Some(stdout_buf.clone());
    
    if let Err(e) = vm.run() {
        let err_str = format!("ÇALIŞMA ZAMANI HATASI: {:?}", e);
        let partial_output = {
            let b = stdout_buf.borrow();
            String::from_utf8_lossy(&b).to_string()
        };
        if partial_output.is_empty() {
            return err_str;
        } else {
            return format!("{}\n{}", partial_output, err_str);
        }
    }
    
    let final_output = {
        let b = stdout_buf.borrow();
        String::from_utf8_lossy(&b).to_string()
    };
    final_output
}
