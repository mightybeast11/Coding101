[TOC]

# C知识补充

In [C](https://en.wikipedia.org/wiki/C_(programming_language)) and [C++](https://en.wikipedia.org/wiki/C%2B%2B) ==pointers== are variables that ==store addresses== and can be `null`.

-   In the [C++](https://en.wikipedia.org/wiki/C%2B%2B), a ==reference== is a simple [reference](https://en.wikipedia.org/wiki/Reference_(computer_science)) datatype that is less powerful but safer than the [pointer](https://en.wikipedia.org/wiki/Pointer_(computer_programming)) type inherited from [C](https://en.wikipedia.org/wiki/C_(programming_language)). 
-   [What's the difference between * and & in C?](https://stackoverflow.com/questions/28778625/whats-the-difference-between-and-in-c)
-   [C++ 指针和引用 吐血整理 Pointer&Reference](https://www.cnblogs.com/tangxiaobo199181/p/7989464.html)
-   `int a; // declare variable`
-   `int *b; // declare pointer, b is the pointer, *b is the actual object`
-   dereference 间接引用: `*b`就是一个间接引用

---

# Tips

- On mac, always run `xcode-select --install` after a system update to install the latest version of **Xcode Command Line Tools**.
- trait有点类似interface, 需要被implement
- mod是代码组织的基本单位, 类似class文件 (注意, 这里是说一个文件, 不是一个类, Java的每个类都正好是个文件, 但别的语言不一定)
- struct很像Java class, 类似一个对象的定义
- [main.rs or lib.rs](https://stackoverflow.com/questions/57756927/rust-modules-confusion-when-there-is-main-rs-and-lib-rs): `main.rs` is the entry point of a binary, **can run**. `lib.rs` is a library(库) for functionality sharing, **cannot run**.
- `impl`块中没有`&self`参数的`fn`叫函数(类似Java的static method, 调用必须声明impl块)
- `impl`块中有`&self`参数的`fn`叫方法(类似Java的instance method)
- `&'static str` is equivalent to `&str`

---

# 资源

- run `rustup doc`
- [The Rust Programming Language](https://doc.rust-lang.org/book/title-page.html)
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/print.html)

---

# 变量

- **Variables are immutable by default.** 

    Rust是强类型语言, 但是可以不给变量定义类型, compiler也能infer.

    ```rust
    let x = 1;
    let mut x = 5; 
    // type can be infered by compiler
    ```

    **Shadowing** **重影**: edits an immutable or mutable variable using `let`. The purpose is to **recycle variable name**. 

    -   **重影**可以修改变量的类型, 可变性(mutability), 赋值. 
    -   **重新赋值**则只能改变赋值, 别的都不能变.
    -   **常量**(constant)什么都不能改.

    ```rust
    let x = "yes";
    let x = x.len();// type of x changes from string to int
    ```

- **Constants are always immutable.** 

    常量必须定义类型. Constant value must be pre-computed, cannot be computed at runtime.

    ```rust
    const MAX_POINTS: u32 = 100_000; // u32 is the type
    ```

---

# 基本数据类型

- scalar类型

    1. Integer

        - 有符号signed: i8, i16, **i32**, i64, i128
        - 无符号unsigned: u8, u16, u32, u64, u128
        - 不同进制前缀: `0b`, `0o`, `0x`

    2. Float: f32, **f64**

    3. Boolean: `true`, `false`

    4. Character: char

         

- 复合类型

    1. Tuple: fixed length

        ```rust
        // 不必同类型
        let tup: (i32, f64, u8) = (500, 6.4, 1); 
        // destructure a tuple
        let (x, y, z) = tup;
        // access tuple element
        let five_hundred = tup.0;
        ```

    2. Array: fixed length, on stack instead of heap

        ```rust
        // 必须同类型
        let arr: [i32; 5]  = [1, 2, 3, 4, 5];
        // 快速声明array
        let arr_all_three = [3; 5]; // [3, 3, 3, 3, 3]
        // access array element
        let first = arr[0];
        ```

    

- 运算符

    -   有`+=`
    -   没有`++`和`--`, 因为降低代码可读性

---

# Function

- 可以以任何顺序定义函数

- 必须定义参数类型

- **Statement**没有返回值

- **Expression**有返回值

    expression没有分号结尾

    给expression加分号就会把它变成statement

    ```rust
    fn trial_function(x: i32, y: i64) {
    	let x = 5; // statement, this line returns nothing
    	
    	let y = {
    		let x = 3; // shadowing the variable x
    		x + 1 // an expression
    	}; // this block is a statement, contents inside the block is an expression
    }
    // function definition itself is a statement (no ending semicolon though)
    ```

- 返回值就是function中最后一个expression, 但是也可以直接用`return`强行返回

- 函数必须声明返回类型, 不声明的视作不返回值, 也就不能返回任何值

    ```rust
    fn main() {
        let x = five();
        println!("print {}", x);
    }
    
    fn five() -> i32 {
        5 // no semicolon, need to keep it as an expression
    } // seems weird, but this is a valid function in Rust
    
    // run: print 5
    ```

---

# Control flow

- `if`

    - `if` is an **expression** (see above), so can be used inside a statement.
    - 判断条件必须是`bool`, Rust不支持非0即`true`
    - 所有branch(`if`, `else if`, `else`)必须是相同的返回类型

    ```rust
    let condition = true;
    let x = if condition {5} else {6}; // 三元判断
    ```

    

- 循环

1. `loop`有点像python的`while True:`, 本身不会停止, 需要手动`break`

        `break`后的值会被返回

       ```rust
       let mut counter = 0;
       // result is assigned the value returned by loop
       let result = loop {
       	counter += 1;
       	if counter == 10 {
       		break counter * 2; // counter * 2 is returned
        	}
       };
       ```

    2. `while`: can be replaced with `loop`, `if`, `else`, `break`, but `while` is neater.

    3. `for`: 没有`for (i=0; i<10; i++) {}`这个用法, 只能`while i<10 {}`

        ```rust
        let a = [10, 20, 30, 40, 50];
        // avoid index errors
        for element in a.iter() {
        	println!("the value is: {}", element);
        }
        
        // loop over a range, prints 3, 2, 1
        for number in (1..4).rev() { 
        	println!("{}", number); 
        }
        ```

---

# Ownership

所有权有以下三条规则：

-   Rust 中的每个值都有一个变量，称为其所有者。
-   一次只能有一个所有者。
-   当所有者不在程序运行范围时，该值将被删除。



**变量 variable**

**移动**: 当第二个变量被创建时, 第一个自动无效

```rust
let s1 = String::from("hello");
let s2 = s1;
// s2 is valid, s1 is invalid now, there are only 1 copy in the heap
```

**克隆**: 当第二个变量被克隆了一份, 第一个仍然有效

```rust
let s1 = String::from("hello");
let s2 = s1.clone();
// both are valid, there are 2 copies in the heap
```

**如果将变量当作参数传入函数，那么它和移动的效果是一样的。(也就是说, 变量在当前scope中已经无效了)**

**被当作函数返回值的变量所有权将会被移动出函数并返回到调用函数的地方，而不会直接被无效释放。**



**引用 reference**

上面说的都是变量, 还有引用(reference)可以间接访问变量. 引用不获得ownership.

使用&声明一个引用:

```rust
let s1 = String::from("hello");
let s2 = &s1;
// s2 is a reference pointing to s1 in stack, s1 points to the actual value in heap
// ownership rule is not violated, only s1 owns the value
```

一个变量可以有多个引用, 但是只能有一个可变引用(mutable reference)

```rust
let mut s = String::from("hello");
let r1 = &mut s;
let r2 = &mut s; // this line is invalid, cannot declare a second mutable reference
```

如果一个引用不能指向任何可以访问的值 (空指针/值已被删除), 那这个引用invalid. 

---

