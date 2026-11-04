# setValue

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

An extension operator that allows delegating a mutable property of type `V`
to a property reference to a mutable property of the same type `V`.

@receiver A property reference to a mutable property of type `V`.
The reference is without a receiver, i.e. it either references a top-level property or
has the receiver bound to it.

Example:

```
class Login(val username: String, var incorrectAttemptCounter: Int = 0)
val defaultLogin = Login("Admin")
var defaultLoginAttempts by defaultLogin::incorrectAttemptCounter
// equivalent to
var defaultLoginAttempts: Int
    get() = defaultLogin.incorrectAttemptCounter
    set(value) { defaultLogin.incorrectAttemptCounter = value }
```

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
public inline operator fun <V> KMutableProperty0<V>.setValue(thisRef: Any?, property: KProperty<*>, value: V)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/properties/PropertyReferenceDelegates.kt#L35)

### 2. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
public inline operator fun <T, V> KMutableProperty1<T, V>.setValue(thisRef: T, property: KProperty<*>, value: V)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/properties/PropertyReferenceDelegates.kt#L84)

An extension operator that allows delegating a mutable member or extension property of type `V`
to a property reference to a member or extension mutable property of the same type `V`.

@receiver A property reference to a read-only or mutable property of type `V` or its subtype.
The reference has an unbound receiver of type `T`.

Example:

```
class Login(val username: String, var incorrectAttemptCounter: Int)
var Login.attempts by Login::incorrectAttemptCounter
// equivalent to
var Login.attempts: Int
    get() = this.incorrectAttemptCounter
    set(value) { this.incorrectAttemptCounter = value }
```

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class)

import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.math.*
import kotlin.random.*
import kotlin.ranges.*
import kotlin.reflect.*
import kotlin.sequences.*
import kotlin.text.*
import kotlin.time.*
import kotlin.time.Duration.Companion.seconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.uuid.*
import kotlin.io.encoding.*
import java.io.File
import kotlin.*

val demoProperty = 42
var demoMutable = 42
fun demoFunction(value: Int): Int = value + 1

fun main() {
    val source = ::demoMutable
    val result = source.`setValue`(1, ::demoProperty, 1)
    println(result)
}
```

```text title="Output"
kotlin.Unit
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
