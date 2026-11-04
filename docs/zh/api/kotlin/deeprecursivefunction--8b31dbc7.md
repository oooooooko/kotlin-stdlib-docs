# DeepRecursiveFunction

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

定义深递归函数, 以将其堆叠放在堆叠上, 从而允许非常深的递归函数不使用实际调用堆叠。 要启动对这个深递归函数的呼叫, 请使用其 `invoke` 函数。 作为大拇指规则, 如果循环的深度超过千次, 则使用它 。

`DeepRecursiveFunction` 需要一个 `T` 的参数, 返回 `R` 型的结果。 `block` 代码定义了循环函数的体。 在这个区块中, `callRecursive` 0005`DeepRecursiveScope.callRecursive` 函数可用于对声明函数进行循环调用。 其它的 `DeepRecursiveFunction` 也可以在此范围内调用 `callRecursive` 扩展 。

例如,请看看以下的递归树类和这个树的深度递归例子,上面有100K节点:

```
class Tree(val left: Tree? = null, val right: Tree? = null)
val deepTree = generateSequence(Tree()) { Tree(it) }.take(100_000).last()
```

常规递归函数可以定义以计算树的深度:

```
fun depth(t: Tree?): Int =
    if (t == null) 0 else max(depth(t.left), depth(t.right)) + 1
println(depth(deepTree)) // StackOverflowError
```

如果此 `depth` 函数被调用为 `deepTree`, 则由于深重循环而产生 `StackOverflowError`。
然而,`depth`函数可以用`DeepRecursiveFunction`以下列方式重新写入,然后
它成功地计算了“ 深度( 深度) ” (EptTree)```DeepRecursiveFunction.invoke` expression:

```val 深度 = 深递流流流 < teet?, Int> { t - > 如果 (t = null) , 则 最大 0 其它 (call recursive (t. left, call Recursive (t. right) + 1 } 打印 / OK (深度( 深滴) / Ok```

Deep recursive functions can also mutually call each other using a heap for the stack via
`callRecursive``DeepRecursiveScope.callRecursive` extension. For example, the
following pair of mutually recursive functions computes the number of tree nodes at even depth in the tree.

```val 共递=对象 {val even: 深递增功能 < 线索? , Int> = 深递增功能 {t - > 如果( t = null) 0 其它奇数。 调回递减( t. left) + 奇数。 调回回溯( t. right) + 1} 等值奇数: 深递增功能 < tree? , 内特 > = 深递增功能 { t - > 如果( t =null) 0 其它偶数。 调回溯( t. left) + 偶数。 调回溯( t. right) }

@param `T` 函数参数类型。 @param `R` 函数结果类型。 8,0000005 阻断函数体 。

??? note "查看英文原文"

    Defines deep recursive function that keeps its stack on the heap,
    which allows very deep recursive computations that do not use the actual call stack.
    To initiate a call to this deep recursive function use its `invoke` function.
    As a rule of thumb, it should be used if recursion goes deeper than a thousand calls.
    
    The `DeepRecursiveFunction` takes one parameter of type `T` and returns a result of type `R`.
    The `block` of code defines the body of a recursive function. In this block
    `callRecursive``DeepRecursiveScope.callRecursive` function can be used to make a recursive call
    to the declared function. Other instances of `DeepRecursiveFunction` can be called
    in this scope with `callRecursive` extension, too.
    
    For example, take a look at the following recursive tree class and a deeply
    recursive instance of this tree with 100K nodes:
    
    ```
    class Tree(val left: Tree? = null, val right: Tree? = null)
    val deepTree = generateSequence(Tree()) { Tree(it) }.take(100_000).last()
    ```
    
    A regular recursive function can be defined to compute a depth of a tree:
    
    ```
    fun depth(t: Tree?): Int =
        if (t == null) 0 else max(depth(t.left), depth(t.right)) + 1
    println(depth(deepTree)) // StackOverflowError
    ```
    
    If this `depth` function is called for a `deepTree` it produces `StackOverflowError` because of deep recursion.
    However, the `depth` function can be rewritten using `DeepRecursiveFunction` in the following way, and then
    it successfully computes ``depth(deepTree)```DeepRecursiveFunction.invoke` expression:
    
    ```
    val depth = DeepRecursiveFunction<Tree?, Int> { t ->
        if (t == null) 0 else max(callRecursive(t.left), callRecursive(t.right)) + 1
    }
    println(depth(deepTree)) // Ok
    ```
    
    Deep recursive functions can also mutually call each other using a heap for the stack via
    `callRecursive``DeepRecursiveScope.callRecursive` extension. For example, the
    following pair of mutually recursive functions computes the number of tree nodes at even depth in the tree.
    
    ```
    val mutualRecursion = object {
        val even: DeepRecursiveFunction<Tree?, Int> = DeepRecursiveFunction { t ->
            if (t == null) 0 else odd.callRecursive(t.left) + odd.callRecursive(t.right) + 1
        }
        val odd: DeepRecursiveFunction<Tree?, Int> = DeepRecursiveFunction { t ->
            if (t == null) 0 else even.callRecursive(t.left) + even.callRecursive(t.right)
        }
    }
    ```
    
    @param `T` the function parameter type.
    @param `R` the function result type.
    @param block the function body.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.7")
public class DeepRecursiveFunction<T, R>(
    internal val block: suspend DeepRecursiveScope<T, R>.(T) -> R
)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/DeepRecursive.kt#L11)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.test.*

private class MutualRec {
        val even: DeepRecursiveFunction<Tree?, Int> = DeepRecursiveFunction { t ->
            if (t == null) 0 else odd.callRecursive(t.left) + odd.callRecursive(t.right) + 1
        }

        val odd: DeepRecursiveFunction<Tree?, Int> = DeepRecursiveFunction { t ->
            if (t == null) 0 else even.callRecursive(t.left) + even.callRecursive(t.right)
        }
    }

private class MutualAndDirectMixRec {
        val b: DeepRecursiveFunction<Int, String> = DeepRecursiveFunction { i -> "b$i" }

        val a: DeepRecursiveFunction<Int, String> = DeepRecursiveFunction { i ->
            when (i) {
                // mix callRecursive calls to other function and in this context
                0 -> b.callRecursive(1) + callRecursive(2) + aa().callRecursive(3)
                else -> "a$i"
            }
        }

        fun aa() = a
    }

private class EqualToAnythingClassRec {
        var nullCount = 0

        val a: DeepRecursiveFunction<Tree?, EqualToAnything> = DeepRecursiveFunction { t ->
            if (t == null) EqualToAnything(nullCount++) else b.callRecursive(t.left)
        }

        val b: DeepRecursiveFunction<Tree?, EqualToAnything> = DeepRecursiveFunction { t ->
            if (t == null) EqualToAnything(nullCount++) else a.callRecursive(t.left)
        }
    }

private class Tree(val left: Tree? = null, val right: Tree? = null)

private fun deepTree(n: Int) = generateSequence(Tree()) { Tree(it) }.take(n).last()

private fun binaryTree(k: Int): Tree? =
        if (k == 0) null else Tree(binaryTree(k - 1), binaryTree(k - 1))

private val depth = DeepRecursiveFunction<Tree?, Int> { t ->
        if (t == null) 0 else maxOf(
            callRecursive(t.left),
            callRecursive(t.right)
        ) + 1
    }

// It is equals to any other class
    private class EqualToAnything(val i: Int) {
        override fun equals(other: Any?): Boolean = true
        override fun toString(): String = "OK"
    }

// Throws exception on all object methods
    private class Bad(val i: Int) {
        override fun equals(other: Any?): Boolean = error("BAD")
        override fun hashCode(): Int = error("BAD")
        override fun toString(): String = error("BAD")
    }

fun main() {

        val k = 15
        println(depth(binaryTree(k)))
    
}
```

```text title="输出"
15
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/utils/DeepRecursiveTest.kt#L24)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
