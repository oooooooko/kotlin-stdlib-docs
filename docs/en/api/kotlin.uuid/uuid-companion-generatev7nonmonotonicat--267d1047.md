# Uuid.Companion.generateV7NonMonotonicAt

`kotlin.uuid` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

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

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("2.3")
        @ExperimentalUuidApi
        public fun generateV7NonMonotonicAt(timestamp: Instant): Uuid
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L672)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
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

```text title="Output"
true
01992f9f-2558-7b4f-a490-14de08079208
true
01992f9f-2558-7407-a6d0-b19b6598df26
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L260)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
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

```text title="Output"

```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L278)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
