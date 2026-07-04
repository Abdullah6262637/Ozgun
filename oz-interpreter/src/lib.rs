pub mod val;
pub mod builtins;
pub mod eval;

#[cfg(test)]
mod tests;

pub use val::{Val, Env, TaskState};
pub use builtins::create_global_env;
pub use eval::{eval_expr, eval_stmt, eval_program};
