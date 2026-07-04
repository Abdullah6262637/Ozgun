# TİLK Dilinin Resmî Sözdizimi Kuralları (EBNF Spesifikasyonu)

TİLK dilinin dilbilgisel yapısı, derleyici tasarımı standartlarına uygun olarak Extended Backus-Naur Form (EBNF) ile tanımlanmıştır.

## 1. Resmî EBNF Tanımı
```ebnf
Program         ::= Statement*

Statement       ::= VarDecl
                  | Assignment
                  | IfStatement
                  | WhileStatement
                  | ForStatement
                  | FnDeclaration
                  | ReturnStatement
                  | ExprStatement
                  | TamamlanincaStatement

VarDecl         ::= Identifier "=" Expr ";"
Assignment      ::= Identifier "=" Expr ";"
ReturnStatement ::= "döndür" Expr? ";"

IfStatement     ::= Expr ("ise" | "se") Block ( "değilse" Block )?
WhileStatement  ::= Expr "iken" Block
ForStatement    ::= Identifier "," Expr ("dan" | "den" | "tan" | "ten") Expr ("e" | "a" | "ye" | "ya") "dek" ("artarak" | "azalarak")? Block

FnDeclaration   ::= "işlev" Identifier "(" ParamList? ")" Block
Block           ::= "{" Statement* "}"

Expr            ::= LogicalOrExpr
LogicalOrExpr   ::= LogicalAndExpr ( "veya" LogicalAndExpr )*
LogicalAndExpr  ::= EqualityExpr ( "ve" EqualityExpr )*
EqualityExpr    ::= ComparisonExpr ( ( "==" | "!=" ) ComparisonExpr )*
ComparisonExpr  ::= Term ( ( "<" | ">" | "<=" | ">=" ) Term )*
Term            ::= Factor ( ( "+" | "-" ) Factor )*
Factor          ::= Primary ( ( "*" | "/" | "%" ) Primary )*

Primary         ::= Identifier
                  | Number
                  | String
                  | Boolean
                  | "boş"
                  | CallExpr
                  | "(" Expr ")"
                  | HataIseExpr

HataIseExpr     ::= Expr "hata_ise" Block
CallExpr        ::= Identifier "(" ArgList? ")"

ParamList       ::= Identifier ( "," Identifier )*
ArgList         ::= Expr ( "," Expr )*

Boolean         ::= "doğru" | "yanlış"
Number          ::= [0-9]+ ( "." [0-9]+ )?
String          ::= '"' ( [^"\\] | '\\' . )* '"'
Identifier      ::= [a-zA-ZçğıişöüÇĞIİŞÖÜ_] [a-zA-Z0-9çğıişöüÇĞIİŞÖÜ_]*
```

## 2. Öncelik Sıralaması (Precedence)
1. Parantezler `()`, Literaller, Çağrılar
2. Unary Negation `-`, Logical Not `değil`
3. Çarpma `*`, Bölme `/`, Kalan `%`
4. Toplama `+`, Çıkarma `-`
5. Karşılaştırmalar `<`, `>`, `<=`, `>=`
6. Eşitlikler `==`, `!=`
7. Mantıksal VE `ve`
8. Mantıksal VEYA `veya`
