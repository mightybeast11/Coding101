# 数字中间可以加下划线

Java7开始，数字可以使用下划线**提高可读性**，compiler会无视这些下划线。

`System.out.println(100_000);`

> 100000



# 特殊浮点数

- 非数字：`Double.NaN`，`Float.NaN`
- 正无穷： `Double.POSITIVE_INFINITY`，`Float.POSITIVE_INFINITY`
- 负无穷：`Double.NEGATIVE_INFINITY`，`Float.NEGATIVE_INFINITY`

其中`NaN`比较特殊，判断是否为特殊值时应该使用`if (Double.isNaN(x))`，而不是`if (x == Double.NaN)`，因为每一个`NaN`都被认为不相等。



# 常量

使用`final`来定义常量。虽然Java预留了`const`作为keyword，但是并没有启用。



# `strictfp`

strict floating point

可以用来修饰**类，接口，方法**。使用严格浮点计算，使Java计算实现全**硬件**平台统一。（有可能造成溢出）



# 求非负余数

负数%正数有时候会得到负余数，使用`Math.floorMod(-1, 2)`来稳定得到非负余数。

（除数是负数时，依然会得到负余数）

```java
System.out.println(-1 % -2);
System.out.println(Math.floorMod(-1, 2));
System.out.println(Math.floorMod(-1, -2));
```

> -1
>
> 1
>
> -1



# 全平台数学运算

使用`StrictMath`类来代替`Math`类

