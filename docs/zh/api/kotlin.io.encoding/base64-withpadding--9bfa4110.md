# Base64.withPadding

`kotlin.io.encoding` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一个新的`Base64`例,该实例相当于此实例,但以指定的`option`页挂牌配置。

此方法不修改此实例。 如果指定的 `option` 与当前此实例的贴贴选项相同, 则返回此实例本身。 否则, 将使用相同的字母创建新实例, 但配置为新贴贴贴选项 。

@sample 样本.i.e.encoding.Base64Samples,附有PatedSample

??? note "查看英文原文"

    Returns a new `Base64` instance that is equivalent to this instance
    but configured with the specified padding `option`.
    
    This method does not modify this instance. If the specified `option` is the same as the current
    padding option of this instance, this instance itself is returned. Otherwise, a new instance is created
    using the same alphabet but configured with the new padding option.
    
    @sample samples.io.encoding.Base64Samples.withPaddingSample

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.0")
    public fun withPadding(option: PaddingOption): Base64
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/io/encoding/Base64.kt#L139)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*



fun main() {
    // The predefined Base64.UrlSafe instance uses PaddingOption.PRESENT.
    // Create a new instance with PaddingOption.ABSENT_OPTIONAL from the Base64.UrlSafe instance.
    val base64UrlSafeCustomPadding = Base64.UrlSafe.withPadding(Base64.PaddingOption.ABSENT_OPTIONAL)

    // The new instance continues using the same UrlSafe alphabet but omits padding when encoding
    println(base64UrlSafeCustomPadding.encode(byteArrayOf(-1, 0, -2, 0)))
    // It allows decoding both padded and unpadded inputs
    println(base64UrlSafeCustomPadding.decode("_wD-AA").contentToString())
    println(base64UrlSafeCustomPadding.decode("_wD-AA==").contentToString())
}
```

```text title="输出"
_wD-AA
[-1, 0, -2, 0]
[-1, 0, -2, 0]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L102)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
