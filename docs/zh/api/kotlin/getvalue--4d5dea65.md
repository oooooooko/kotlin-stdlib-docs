# getValue

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

扩展操作员,允许将`V`型只读财产委托给提及`V`型财产或其子类型的财产。

@receiver 财产是指`V`类型或其子类型的只读或可变财产,该财产是指没有接收器,即它指的是顶级财产,或是接收者受该财产的约束。

示例:

```
class Login(val username: String)
val defaultLogin = Login("Admin")
val defaultUsername by defaultLogin::username
// equivalent to
val defaultUserName get() = defaultLogin.username
```

??? note "查看英文原文"

    An extension operator that allows delegating a read-only property of type `V`
    to a property reference to a property of type `V` or its subtype.
    
    @receiver A property reference to a read-only or mutable property of type `V` or its subtype.
    The reference is without a receiver, i.e. it either references a top-level property or
    has the receiver bound to it.
    
    Example:
    
    ```
    class Login(val username: String)
    val defaultLogin = Login("Admin")
    val defaultUsername by defaultLogin::username
    // equivalent to
    val defaultUserName get() = defaultLogin.username
    ```

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
public inline operator fun <V> KProperty0<V>.getValue(thisRef: Any?, property: KProperty<*>): V
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/properties/PropertyReferenceDelegates.kt#L11)

### 2. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
public inline operator fun <T, V> KProperty1<T, V>.getValue(thisRef: T, property: KProperty<*>): V
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/properties/PropertyReferenceDelegates.kt#L62)

扩展经营人,允许将`V`型只读成员或扩展财产委托给提及成员或扩展财产的`V`型或其亚型的财产。

@receiver 财产是指`V`型或其亚型的只读或可变财产,该财产是指`T`型无约束接收器。

示例:

```
class Login(val username: String)
val Login.user by Login::username
// equivalent to
val Login.user get() = this.username
```

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun <T> Lazy<T>.getValue(thisRef: Any?, property: KProperty<*>): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Lazy.kt#L43)

将 `T` 型只读财产授予 `Lazy` 的延伸。

允许使用Lazy(Lazy)来进行财产授权: `val property: String by lazy { initializer }`

@sample 样本. lazy. LazySamples.lazySample

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
