# Uuid.Companion.generateV7NonMonotonicAt

`kotlin.uuid` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

生成一个新的 `Uuid` 版本7例,用于指定 `moment in time` `timestamp`。

返回的 uuid 是符合 [IETF 变量(变式) 2 ( https://www.rfc-editor.org/rfc/rfc9562.html#section-4.1) ) 和 [版本 7] (https://www.rfc-editor.org/rfc/rfc9562.html#section-4.2), 使用从 `timestamp` 中提取的 UNIX 时间戳的毫秒作为前缀和随机生成的后缀 。

与`generateV7`不同,该函数不提供任何单音保证,也就是说,没有保证订单
将此函数调用两次或多次, 与 `timestamp` 完全相同, 从而创建的用户名。
如果需要多个与同一时间戳对应的词汇,请考虑使用此函数生成这些词汇,
然后对结果进行排序,然后使用它来达到单音。

此函数旨在生成与过去( 或未来) 相对应的 v7 uuid。 如果一个 `generateV7` 与当前需要的时间时间相对应, 则总是考虑使用 `generateV7` 。

此函数不影响 `generateV7` 的状态和单一度保障, 因此即使它被从遥远的未来用一个时间戳来引用, `generateV7` 将继续返回 uids, 并给时间上一个时刻相应的时间戳。

随机部分的uuid 使用平台上可用的加密安全伪随机编号生成器(CSPRNG) 生成。 如果基础系统收集的 entropy 不够, 这个功能可能会阻断, 直到收集到足够的 entropy , CSPRNG 完全初始化。 值得一提的是, Kotlin/ WasmWassi 目标中使用的 PPRNG 无法保证加密安全。 有关每个支持目标中用于随机生成 uid 的 API 详情, 请参见下面的列表 。

请注意, 返回的 uud 不推荐用于加密目的。 因为版本 7 uud 具有部分可预期的位图, 并且使用最多74 位的 entropy, 不论平台如何 。

每种支助目标的随机生成都使用下列APIs: - Kotlin/JVM-[java.security-securerandom](https://docs.oracle.com/javase/8/docs/api/java/security/SecureRandom.html) - Kotlin/JS) -- -- [Crypto.getRandomValues (](https://developer.mozilla.org/en-US/docs/Web/API/Crypto/getRandomValues) - Kotlin/WasmJsmJs) -- -- [Crypto.getRandomValues ()](https://developer.mozilla.org/en-US/docs/Web/API/Crypto/getRandomValues) - Kotlin/WasmWasi -- -- [random_get](https://github.com/WebAssembly/WASI/blob/main/legacy/preview1/docs.md#random_get) - Kotlin/Native: -- Linux目标 -- -- [植物](https://www.man7.org/linux/man-pages/man2/getrandom.2.html)) -- -- 苹果和本地机器人目标 -- -- [arc4random_buf](https://man7.org/linux/man-pages/man3/arc4random_buf.3.html) - Windows 目标 -- -- 视窗目标 -- [https://man7.org/linux/man-pages/man3/arc4random_buf.3.html)] -- 目标 [BCryptGenRandom] ( https://learn.microsoft.com/en-us/windows/win32/api/bcrypt/nf-bcrypt-bcryptgenrandom) )

请注意,用于生产随机uid的原始API今后可能发生变化。

@return A 随机生成 uuid @throws 如果 API 失败, 运行时间例外。 参考相应的 API 基础文件, 原因可能是失败, 以及如何处理 的指导 。

@sample 样本.uuuid.Uuids.v7 非海洋- @sample

??? note "查看英文原文"

    Generates a new random `Uuid` Version 7 instance for a specified `moment in time``timestamp`.
    
    The returned uuid is a time-based sortable UUID that conforms to the
    [IETF variant (variant 2)](https://www.rfc-editor.org/rfc/rfc9562.html#section-4.1)
    and [version 7](https://www.rfc-editor.org/rfc/rfc9562.html#section-4.2),
    uses UNIX timestamp in milliseconds extracted from `timestamp` as a prefix and a randomly generated suffix.
    
    Unlike `generateV7`, this function does not provide any monotonicity guarantees, meaning that there will be no guaranteed order
    for uuids created by calling this function two or more times with exactly the same `timestamp`.
    If multiple uuids corresponding to the same timestamp are needed, consider generating them using this function,
    then sorting the result before using it to achieve the monotonicity.
    
    This function is aimed for generating v7 uuids corresponding to the past (or the future).
    Always consider using `generateV7` if an uuid corresponding to a current moment in time in needed.
    
    This function does not affect the state and monotonicity guarantees of `generateV7` in any way,
    so even if it is invoked with a timestamp from a distant future,
    `generateV7` will continue returning uuids with a timestamp corresponding to a current moment in time.
    
    The random part of the uuid is produced using a cryptographically secure pseudorandom number generator (CSPRNG)
    available on the platform.
    If the underlying system has not collected enough entropy, this function
    may block until sufficient entropy is collected, and the CSPRNG is fully initialized.
    It is worth mentioning
    that the PRNG used in the Kotlin/WasmWasi target is not guaranteed to be cryptographically secure.
    See the list below for details about the API used for producing the random uuid in each supported target.
    
    Note that the returned uuid is not recommended for use for cryptographic purposes.
    Because version 7 uuid has a partially predictable bit pattern, and utilizes at most
    74 bits of entropy, regardless of platform.
    
    The following APIs are used for producing the random uuid in each of the supported targets:
      - Kotlin/JVM - [java.security.SecureRandom](https://docs.oracle.com/javase/8/docs/api/java/security/SecureRandom.html)
      - Kotlin/JS - [Crypto.getRandomValues()](https://developer.mozilla.org/en-US/docs/Web/API/Crypto/getRandomValues)
      - Kotlin/WasmJs - [Crypto.getRandomValues()](https://developer.mozilla.org/en-US/docs/Web/API/Crypto/getRandomValues)
      - Kotlin/WasmWasi - [random_get](https://github.com/WebAssembly/WASI/blob/main/legacy/preview1/docs.md#random_get)
      - Kotlin/Native:
          - Linux targets - [getrandom](https://www.man7.org/linux/man-pages/man2/getrandom.2.html)
          - Apple and Android Native targets - [arc4random_buf](https://man7.org/linux/man-pages/man3/arc4random_buf.3.html)
          - Windows targets - [BCryptGenRandom](https://learn.microsoft.com/en-us/windows/win32/api/bcrypt/nf-bcrypt-bcryptgenrandom)
    
    Note that the underlying API used to produce random uuids may change in the future.
    
    @return A randomly generated uuid.
    @throws RuntimeException if the underlying API fails. Refer to the corresponding underlying API
      documentation for possible reasons for failure and guidance on how to handle them.
    
    @sample samples.uuid.Uuids.v7NonMonotonicAt
    @sample samples.uuid.Uuids.v7ForTimestampSorted

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.3")
        @ExperimentalUuidApi
        public fun generateV7NonMonotonicAt(timestamp: Instant): Uuid
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L672)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*
import kotlin.time.Instant
import kotlin.uuid.*



fun main() {
    val timestamp = Instant.fromEpochMilliseconds(1757440583000L)

    val uuid1 = Uuid.generateV7NonMonotonicAt(timestamp)
    val uuid2 = Uuid.generateV7NonMonotonicAt(timestamp)

    // Uuids have the same timestamp prefix (01992f9f-2558-, which corresponds to 1757440583000 in hex),
    // but other bytes are different.
    println(uuid1.toHexDashString().startsWith("01992f9f-2558-"))
    println(uuid1.toHexDashString())

    println(uuid2.toHexDashString().startsWith("01992f9f-2558-"))
    println(uuid2.toHexDashString())

    assertNotEquals(uuid1, uuid2)
}
```

```text title="输出"
true
01992f9f-2558-7b4f-a490-14de08079208
true
01992f9f-2558-7407-a6d0-b19b6598df26
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L260)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.Instant
import kotlin.uuid.*



fun main() {
    val timestamp = Instant.fromEpochMilliseconds(1757440583000L)

    // Generate 5 uuids for the same timestamp, and them explicitly sort them to ensure monotonicity
    val uuids = sequence<Uuid> { Uuid.generateV7NonMonotonicAt(timestamp) }.take(5).sorted().toList()

    for (idx in 1..<uuids.size) {
        println(uuids[idx - 1] < uuids[idx])
    }
}
```

```text title="输出"

```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L278)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
