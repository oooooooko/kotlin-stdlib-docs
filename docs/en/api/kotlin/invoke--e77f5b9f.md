# invoke

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Initiates a call to this deep recursive function, forming a root of the call tree.

This operator should not be used from inside of `DeepRecursiveScope` as it uses the call stack slot for
initial recursive invocation. From inside of `DeepRecursiveScope` use
`callRecursive``DeepRecursiveScope.callRecursive`.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.7")
public operator fun <T, R> DeepRecursiveFunction<T, R>.invoke(value: T): R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/DeepRecursive.kt#L74)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
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

```text title="Output"
15
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

This example requires `kotlin-reflect:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/utils/DeepRecursiveTest.kt#L24)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
