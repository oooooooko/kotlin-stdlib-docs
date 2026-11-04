# Uuid.Companion.random

`kotlin.uuid` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

生成一个新的随机 `Uuid` 实例。

此函数与 `Uuid.generateV4` 等同。

返回的 uuid 符合 [IETF 变量(变体 2) ( https://www.rfc-editor.org/rfc/rfc9562.html#section-4.1) 和 [版本 4) ( https://www.rfc-editor.org/rfc/rfc9562.html#section-4.2), ) , 设计为独一, 概率很高, 不论产生时间或地点。 用户使用平台上可用的加密安全伪兰编号生成器( CSPRNG) 。 如果基础系统收集的加密加密无效, 此功能可能会阻塞, 直到收集足够的 entropy , 并且 CSPRNG 完全初始化。 值得一提的是 Kotlin/ WasmWassi 目标中使用的 PRON 保证不会加密安全 。 请参看下面关于每个支持目标中随机生成 uiduidard 的 API 详情列表 。

请注意, 返回的 uud 不推荐用于加密目的。 因为版本 4 uud 具有部分可预期的位图, 最多使用122 位的 entropy, 不论平台如何 。

每种支助目标的随机生成都使用下列APIs: - Kotlin/JVM-[java.security-securerandom](https://docs.oracle.com/javase/8/docs/api/java/security/SecureRandom.html) - Kotlin/JS) -- -- [Crypto.getRandomValues (](https://developer.mozilla.org/en-US/docs/Web/API/Crypto/getRandomValues) - Kotlin/WasmJsmJs) -- -- [Crypto.getRandomValues ()](https://developer.mozilla.org/en-US/docs/Web/API/Crypto/getRandomValues) - Kotlin/WasmWasi -- -- [random_get](https://github.com/WebAssembly/WASI/blob/main/legacy/preview1/docs.md#random_get) - Kotlin/Native: -- Linux目标 -- -- [植物](https://www.man7.org/linux/man-pages/man2/getrandom.2.html)) -- -- 苹果和本地机器人目标 -- -- [arc4random_buf](https://man7.org/linux/man-pages/man3/arc4random_buf.3.html) - Windows 目标 -- -- 视窗目标 -- [https://man7.org/linux/man-pages/man3/arc4random_buf.3.html)] -- 目标 [BCryptGenRandom] ( https://learn.microsoft.com/en-us/windows/win32/api/bcrypt/nf-bcrypt-bcryptgenrandom) )

请注意,用于生产随机uid的原始API今后可能发生变化。

@return A 随机生成 uuid @throws 如果 API 失败, 运行时间例外。 参考相应的 API 基础文件, 原因可能是失败, 以及如何处理 的指导 。

@see Uuid.generate V4 @sample 样本.uuid.Uuids.random

??? note "查看英文原文"

    Generates a new random `Uuid` instance.
    
    This function is synonymous to `Uuid.generateV4`.
    
    The returned uuid conforms to the [IETF variant (variant 2)](https://www.rfc-editor.org/rfc/rfc9562.html#section-4.1)
    and [version 4](https://www.rfc-editor.org/rfc/rfc9562.html#section-4.2),
    designed to be unique with a very high probability, regardless of when or where it is generated.
    The uuid is produced using a cryptographically secure pseudorandom number generator (CSPRNG)
    available on the platform. If the underlying system has not collected enough entropy, this function
    may block until sufficient entropy is collected, and the CSPRNG is fully initialized. It is worth mentioning
    that the PRNG used in the Kotlin/WasmWasi target is not guaranteed to be cryptographically secure.
    See the list below for details about the API used for producing the random uuid in each supported target.
    
    Note that the returned uuid is not recommended for use for cryptographic purposes.
    Because version 4 uuid has a partially predictable bit pattern, and utilizes at most
    122 bits of entropy, regardless of platform.
    
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
    
    @see Uuid.generateV4
    @sample samples.uuid.Uuids.random

## 声明与重载

### 1. Common

```kotlin
public fun random(): Uuid
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L544)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.Instant
import kotlin.uuid.*



fun main() {
    // Generates a random and unique uuid each time
    val uuid1 = Uuid.random()
    val uuid2 = Uuid.random()
    val uuid3 = Uuid.random()

    println(uuid1 == uuid2)
    println(uuid1 == uuid3)
    println(uuid2 == uuid3)
}
```

```text title="输出"
false
false
false
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L224)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
