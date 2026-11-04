# toUShortArray

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns an array of UShort containing all of the elements of this generic array.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun Array<out UShort>.toUShortArray(): UShortArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4999)

### 2. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ShortArray.toUShortArray(): UShortArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5008)

Returns an array of type `UShortArray`, which is a copy of this array where each element is an unsigned reinterpretation
of the corresponding element of this array.

### 3. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun Collection<UShort>.toUShortArray(): UShortArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UCollections.kt#L61)

Returns an array of UShort containing all of the elements of this collection.

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


fun main() { println(listOf(1.toUShort(), 2.toUShort()).toUShortArray().contentToString()) }
```

```text title="Output"
[1, 2]
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
