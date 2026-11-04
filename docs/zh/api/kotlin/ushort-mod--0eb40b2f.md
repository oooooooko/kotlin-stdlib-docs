# UShort.mod

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将此值( divided) 的下层分割的剩余值乘以其他值( diovisor) 。

结果总是比断层小。

对于未指定类型,地面和短距分区的剩余部分相同。 @sample 样本. misc. ilutins.modUnign

??? note "查看英文原文"

    Calculates the remainder of flooring division of this value (dividend) by the other value (divisor).
    
    The result is always less than the divisor.
    
    For unsigned types, the remainders of flooring division and truncating division are the same.
    @sample samples.misc.Builtins.modUnsigned

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
    @kotlin.internal.IntrinsicConstEvaluation
    public inline fun mod(other: UByte): UByte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UShort.kt#L215)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
    @kotlin.internal.IntrinsicConstEvaluation
    public inline fun mod(other: UShort): UShort
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UShort.kt#L226)

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
    @kotlin.internal.IntrinsicConstEvaluation
    public inline fun mod(other: UInt): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UShort.kt#L237)

### 4. Common

```kotlin
@kotlin.internal.InlineOnly
    @kotlin.internal.IntrinsicConstEvaluation
    public inline fun mod(other: ULong): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UShort.kt#L248)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.assertFailsWith



fun main() {
    // Unsigned types have no negative values, so mod produces the
    // same result as the % operator
    println(7u.mod(3u))
    println(7u % 3u)

    // A zero divisor throws
    assertFailsWith<ArithmeticException> { 1u.mod(0u) }
}
```

```text title="输出"
1
1
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/misc/builtins.kt#L109)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
