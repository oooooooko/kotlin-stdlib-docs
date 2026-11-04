# DeepRecursiveScope.callRecursive

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

重复呼叫此 `DeepRecursiveFunction` 函数, 将调用激活框架置于电堆上, 而不是常规调用回拨时使用的实际调用堆。

??? note "查看英文原文"

    Makes recursive call to this `DeepRecursiveFunction` function putting the call activation frame on the heap,
    as opposed to the actual call stack that is used by a regular recursive call.

## 声明与重载

### 1. Common

```kotlin
public abstract suspend fun callRecursive(value: T): R
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/DeepRecursive.kt#L96)

### 2. Common

```kotlin
public abstract suspend fun <U, S> DeepRecursiveFunction<U, S>.callRecursive(value: U): S
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/DeepRecursive.kt#L102)

调用指定`DeepRecursiveFunction`函数,将调用激活框架置于电压堆上,而不是常规调用的实际调用堆叠。

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
