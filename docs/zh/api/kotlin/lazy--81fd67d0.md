# lazy

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

创建 `Lazy` 的新实例, 使用指定的初始化功能 `initializer` 和默认的线性安全模式 `LazyThreadSafetyMode.SYNCHRONIZED`。 所使用的锁定既包括平台,也包括执行的细节 。

如果一个值的初始化会丢出一个例外, 它将会试图在下次访问时重新激活该值 。

@sample 样本. lazy. LazySamples.lazySample

??? note "查看英文原文"

    Creates a new instance of the `Lazy` that uses the specified initialization function `initializer`
    and the default thread-safety mode `LazyThreadSafetyMode.SYNCHRONIZED`.
    The lock used is both platform- and implementation- specific detail.
    
    If the initialization of a value throws an exception, it will attempt to reinitialize the value at next access.
    
    @sample samples.lazy.LazySamples.lazySample

## 声明与重载

### 1. Common

```kotlin
public expect fun <T> lazy(initializer: () -> T): Lazy<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/KotlinH.kt#L86)

### 2. Common

```kotlin
public expect fun <T> lazy(mode: LazyThreadSafetyMode, initializer: () -> T): Lazy<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/KotlinH.kt#L97)

创建 `Lazy` 的新实例, 使用指定的初始化功能 `initializer` 和线索安全 `mode` 。

如果一个值的初始化会丢出一个例外, 它将会试图在下次访问时重新激活该值 。

`LazyThreadSafetyMode.SYNCHRONIZED` , 使用的锁既包括平台,也包括执行的具体细节。

@sample 样本.lazySamples.lazySamples.lazySyroncronized 样本 @sample

### 3. Common

```kotlin
@Deprecated("Synchronization on Any? object is supported only in Kotlin/JVM.", ReplaceWith("lazy(initializer)"))
@DeprecatedSinceKotlin(warningSince = "1.9", errorSince = "2.1")
public expect fun <T> lazy(lock: Any?, initializer: () -> T): Lazy<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/KotlinH.kt#L110)

创建 `Lazy` 的新实例, 使用指定的初始化功能 `initializer` 。

`lock` 参数被忽略 。

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
    val answer: Int by lazy {
        println("Computing the answer to the Ultimate Question of Life, the Universe, and Everything")
        42
    }

    println("What is the answer?")
    // Will print 'Computing...' and then 42
    println(answer)
    println("Come again?")
    // Will just print 42
    println(answer)
}
```

```text title="输出"
What is the answer?
Computing the answer to the Ultimate Question of Life, the Universe, and Everything
42
Come again?
42
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/lazy/LazySamples.kt#L14)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
