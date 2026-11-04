# Uuid.equals

`kotlin.uuid` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

检查此uid 是否等于指定的 `other` 对象。

其它 @param 个 对象 与此值比较的值为 @return `true`, 如果 `other` 是 `Uuid` 的例子, 由与此值相同的序列位数组成; 其它值为 `false` 。

@sample 样本.uuuid.uuuds.uuidEquals

??? note "查看英文原文"

    Checks whether this uuid is equal to the specified `other` object.
    
    @param other The object to compare with this uuid.
    @return `true` if `other` is an instance of `Uuid`, and consists of the same sequence
      of bits as this uuid; `false` otherwise.
    
    @sample samples.uuid.Uuids.uuidEquals

## 声明与重载

### 1. Common

```kotlin
override fun equals(other: Any?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L235)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.Instant
import kotlin.uuid.*



fun main() {
    val uuid1 = Uuid.fromULongs(0x550E8400E29B41D4uL, 0xA716446655440000uL)
    val uuid2 = Uuid.parse("550e8400-e29b-41d4-a716-446655440000")
    val uuid3 = Uuid.parse("550e8400-e29b-41d4-a716-446655440001") // the last bit is one

    println(uuid1 == uuid2)
    println(uuid1 == uuid3)
}
```

```text title="输出"
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L124)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
