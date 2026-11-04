# Uuid.Companion.generateV7

`kotlin.uuid` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

生成一个新的随机`Uuid`版本7实例。

返回的 uuid 是符合 [IETF 变量(变式) 2 ( https://www.rfc-editor.org/rfc/rfc9562.html#section-4.1) ) 和 [版本 7] (https://www.rfc-editor.org/rfc/rfc9562.html#section-4.2), 使用 UNIX 时间戳作为前缀和随机生成的后缀, 使连续生成的若干 Uuid 能够单调顺序, 同时又保持未来的 uid 值可以互换 。

当前实施保障了在应用寿命范围内返回的铀铀的严格单一度; 同一主机在单独程序中生成的两种铀以及不同主机生成的铀的单一度保障没有。 如果在同一时间的同一时间要求多个铀, 目前的实施将使用[ RFC-9562, 第6.2. 单调和对称] (https://www.rfc-editor.org/rfc/rfc9562.html#section-6.2)) 所涵盖的“固定比特点专用反制”方法, 实现严格的单调。

随机部分的uuid 使用平台上可用的加密安全伪随机编号生成器(CSPRNG) 生成。 如果基础系统收集的 entropy 不够, 这个功能可能会阻断, 直到收集到足够的 entropy , CSPRNG 完全初始化。 值得一提的是, Kotlin/ WasmWassi 目标中使用的 PPRNG 无法保证加密安全。 有关每个支持目标中用于随机生成 uid 的 API 详情, 请参见下面的列表 。

请注意, 返回的 uud 不推荐用于加密目的。 因为版本 7 uud 具有部分可预期的位图, 并且使用最多74 位的 entropy, 不论平台如何 。

每种支助目标的随机生成都使用下列APIs: - Kotlin/JVM-[java.security-securerandom](https://docs.oracle.com/javase/8/docs/api/java/security/SecureRandom.html) - Kotlin/JS) -- -- [Crypto.getRandomValues (](https://developer.mozilla.org/en-US/docs/Web/API/Crypto/getRandomValues) - Kotlin/WasmJsmJs) -- -- [Crypto.getRandomValues ()](https://developer.mozilla.org/en-US/docs/Web/API/Crypto/getRandomValues) - Kotlin/WasmWasi -- -- [random_get](https://github.com/WebAssembly/WASI/blob/main/legacy/preview1/docs.md#random_get) - Kotlin/Native: -- Linux目标 -- -- [植物](https://www.man7.org/linux/man-pages/man2/getrandom.2.html)) -- -- 苹果和本地机器人目标 -- -- [arc4random_buf](https://man7.org/linux/man-pages/man3/arc4random_buf.3.html) - Windows 目标 -- -- 视窗目标 -- [https://man7.org/linux/man-pages/man3/arc4random_buf.3.html)] -- 目标 [BCryptGenRandom] ( https://learn.microsoft.com/en-us/windows/win32/api/bcrypt/nf-bcrypt-bcryptgenrandom) )

请注意,用于生产随机uid的原始API今后可能发生变化。

@return A 随机生成 uuid @throws 如果 API 失败, 运行时间例外。 参考相应的 API 基础文件, 原因可能是失败, 以及如何处理 的指导 。

@sample 样本.uuid.Uuuds.v7

??? note "查看英文原文"

    Generates a new random `Uuid` Version 7 instance.
    
    The returned uuid is a time-based sortable UUID that conforms to the
    [IETF variant (variant 2)](https://www.rfc-editor.org/rfc/rfc9562.html#section-4.1)
    and [version 7](https://www.rfc-editor.org/rfc/rfc9562.html#section-4.2),
    uses UNIX timestamp in milliseconds as a prefix and a randomly generated suffix,
    allowing several consecutively generated uuids to be monotonically ordered and yet keep future uuid values unguessable.
    
    The current implementation guarantees strict monotonicity of returned uuids within the scope of an application lifetime.
    There are no monotonicity guarantees for two uuids generated in separate processes on the same host,
    as well as for uudis generated on different hosts.
    If multiple uuids were requested at the exact same instant of time, the current implementation will use
    the "Fixed Bit-Length Dedicated Counter" method covered by the
    [RFC-9562, §6.2. Monotonicity and Counters](https://www.rfc-editor.org/rfc/rfc9562.html#section-6.2)
    to achieve strict monotonicity.
    
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
    
    @sample samples.uuid.Uuids.v7

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.3")
        @ExperimentalUuidApi
        public fun generateV7(): Uuid
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L621)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.Instant
import kotlin.uuid.*



fun main() {
    // Generates a random, unique and strictly ordered uuids each time
    val uuid1 = Uuid.generateV7()
    val uuid2 = Uuid.generateV7()
    val uuid3 = Uuid.generateV7()

    println(uuid1 < uuid2)
    println(uuid1 < uuid3)
    println(uuid2 < uuid3)
}
```

```text title="输出"
true
true
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L248)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
