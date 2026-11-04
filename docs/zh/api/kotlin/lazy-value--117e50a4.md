# Lazy.value

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

获取当前 `Lazy` 例的迷性初始值。 一旦初始化了该值, 则在 `Lazy` 例的余生中不得改变 。

@sample 样本.lazy.LazySamples.lazyExplicationSample

??? note "查看英文原文"

    Gets the lazily initialized value of the current `Lazy` instance.
    Once the value was initialized it must not change during the rest of lifetime of this `Lazy` instance.
    
    @sample samples.lazy.LazySamples.lazyExplicitSample

## 声明与重载

### 1. Common

```kotlin
public val value: T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Lazy.kt#L23)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.thread

fun lazySynchronizedSample() {
        val answer: Int by lazy(LazyThreadSafetyMode.SYNCHRONIZED) {
            println("Computing the answer to the Ultimate Question of Life, the Universe, and Everything")
            42
        }

        val t1 = thread {
            println("Thread 1: $answer")
        }

        val t2 = thread {
            println("Thread 2: $answer")
        }

        // It is guaranteed that 'Computing' message will be printed once, and both threads will see 42 as an answer
        t1.join()
        t2.join()
    }

fun lazySafePublicationSample() {
        class Answer(val value: Int, val computedBy: Thread = Thread.currentThread()) {
            override fun toString() = "Answer: $value, computed by: $computedBy"
        }

        val answer: Answer by lazy(LazyThreadSafetyMode.PUBLICATION) {
            println("Computing the answer to the Ultimate Question of Life, the Universe, and Everything")
            Answer(42)
        }

        val t1 = thread(name = "#1") {
            println("Thread 1: $answer")
        }

        val t2 = thread(name = "#2") {
            println("Thread 2: $answer")
        }

        // It is **not** guaranteed that 'Computing' message will be printed once,
        // but guaranteed that both threads will see 42 computed by *the same* thread as an answer
        t1.join()
        t2.join()
    }

fun explicitLockLazySample() {
        val lock = Any()
        val answer: Int by lazy(lock) {
            println("Computing the answer to the Ultimate Question of Life, the Universe, and Everything")
            42
        }

        // Lock is acquired first, so thread cannot compute the answer
        val thread: Thread
        synchronized(lock) {
            thread = thread(name = "#1") {
                println("Thread is asking for an answer")
                println("$answer")
            }
            println("Let's hold the thread #1 for a while with a lock")
            Thread.sleep(100) // Let it wait
        }
        // Lock is unlocked, the thread will print an answer
        thread.join()
    }

fun main() {
    val answer: Lazy<Int> = lazy {
        println("Computing the answer to the Ultimate Question of Life, the Universe, and Everything")
        42
    }

    println("What is the answer?")
    println(answer)
    println("Oh, now compute it please")
    // Will print 'Computing...' and then 42
    println(answer.value)
    println("Come again?")
    // Will print 42
    println(answer.value)
}
```

```text title="输出"
What is the answer?
Lazy value not initialized yet.
Oh, now compute it please
Computing the answer to the Ultimate Question of Life, the Universe, and Everything
42
Come again?
42
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/lazy/LazySamples.kt#L29)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
