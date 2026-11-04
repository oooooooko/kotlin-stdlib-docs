# Uuid.Companion.generateV7

`kotlin.uuid` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

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

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("2.3")
        @ExperimentalUuidApi
        public fun generateV7(): Uuid
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L621)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
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

```text title="Output"
true
true
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L248)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
