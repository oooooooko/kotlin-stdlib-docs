# DeepRecursiveFunction

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

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

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.7")
public class DeepRecursiveFunction<T, R>(
    internal val block: suspend DeepRecursiveScope<T, R>.(T) -> R
)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/DeepRecursive.kt#L11)

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
