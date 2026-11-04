# Uuid.Companion.random

`kotlin.uuid` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

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

## Declarations and overloads

### 1. Common

```kotlin
public fun random(): Uuid
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L544)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
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

```text title="Output"
false
false
false
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L224)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
