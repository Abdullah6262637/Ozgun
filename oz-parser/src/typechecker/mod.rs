pub mod types;
pub mod unify;
pub mod inference;

pub use types::{Type, Scheme, TypeEnv};
pub use inference::{TypeChecker, create_default_type_env, check_program};
