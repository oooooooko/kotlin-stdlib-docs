# toUByteArray

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回包含此通用数组全部元素的UByte数组。

??? note "查看英文原文"

    Returns an array of UByte containing all of the elements of this generic array.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun Array<out UByte>.toUByteArray(): UByteArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4939)

### 2. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ByteArray.toUByteArray(): UByteArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4948)

返回`UByteArray`类型的一个数组,这是此数组的复制件,其中每个元素都是对本数组相应元素的未指派重新解释。

### 3. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun Collection<UByte>.toUByteArray(): UByteArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UCollections.kt#L22)

返回包含此收藏全部元素的 UByte 数列。

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val data = byteArrayOf(0xDE.toByte(), 0x2D, 0x02, 0xC0.toByte(), 0x5C, 0x0E)

    // Using the default format
    println(data.toHexString())

    // Using a custom format
    val format = HexFormat {
        upperCase = true
        bytes {
            bytesPerLine = 4
            byteSeparator = " " // One space
            bytePrefix = "0x"
        }
    }
    println(data.toHexString(format))

    // Formatting a segment of the byte array
    println(data.toHexString(startIndex = 2, endIndex = 5, format))

    // Formatting unsigned bytes with the same binary representations yields the same string
    val unsignedData = data.toUByteArray()
    println(unsignedData.toHexString(format))
}
```

```text title="输出"
de2d02c05c0e
0xDE 0x2D 0x02 0xC0
0x5C 0x0E
0x02 0xC0 0x5C
0xDE 0x2D 0x02 0xC0
0x5C 0x0E
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L365)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
