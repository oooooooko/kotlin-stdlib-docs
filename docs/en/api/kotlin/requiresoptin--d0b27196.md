# RequiresOptIn

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Signals that the annotated annotation class is a marker of an API that requires an explicit opt-in.

Call sites of any declaration that is either annotated with such a marker or mentions in its signature any
other declaration that requires opt-in should opt in to the API either by using `OptIn`,
or by being annotated with that marker themselves, effectively causing further propagation of the opt-in requirement.

The intended uses of opt-in markers include, but are not limited to the following:
- Experimental API for public preview that might change its semantics or affect binary compatibility.
- Internal declarations that should not be used outside the declaring library, but are `public` for technical reasons.
- Fragile or delicate API that needs a lot of expertise to use and thus require an explicit opt-in.

## Contagiousness

When a declaration is marked with an opt-in requirement, it is considered to be contagious, meaning that all its uses
or mentions in other declarations will require an explicit opt-in.
A rule of thumb for propagating is the following: if the marked declaration ceases to exist, only
the places with explicit opt-in (or the corresponding warning) will break. This rule does not imply transitivity,
e.g. the propagation does not propagate opt-in through inlining, making it the responsibility `inline` function author
to mark it properly.

### Type scopes

A type is considered requiring opt-in if it is marked with an opt-in marker, or the outer declaration (class or interface) requires opt-in.
Any use of any declaration that mentions such type in its signature will require an explicit opt-in, even if it is not used
directly on the call site, and even if such declarations do not require opt-in directly.

For example, consider the following declarations that are marked with non-propagating opt-in:
```
@UnstableApi
class Unstable

@OptIn(UnstableApi::class)
fun foo(): Unstable = Unstable()

@OptIn(UnstableApi::class)
fun bar(arg: Unstable = Unstable()) {}

@OptIn(UnstableApi::class)
fun Unstable?.baz() {}
```
and their respective call sites:
```
fun outerFun() {
    val s = foo()
    bar()
    null.baz()
}
```
Even though call sites do not mention `Unstable` type directly, the corresponding opt-in warning or error will be triggered
in each call site due to propagation contagiousness. Note that the propagation is not transitive, i.e. calls to `outerFun`
itself would not trigger any further opt-in requirements.

### Lexical scopes

If a type requires an opt-in, such requirement is propagated to its lexical scope and all its nested declarations.
For example, for the following scope:
```
@UnstableApi
class Unstable {
    fun memberFun() = ...

    class NestedClass {
        fun nestedFun() = ...
    }
}
```

Any use of `Unstable`, `NestedClass`, or their member functions will require an explicit opt-in.

### Overridden declarations

Opt-in markers are also propagated through the inheritance and interface implementation.
If the base declaration requires an opt-in, overriding it requires either an explicit opt-in or
propagating the opt-in requirement.

See also [Kotlin language documentation](https://kotlinlang.org/docs/opt-in-requirements.html) for more information.

@property message message to be reported on usages of API without an explicit opt-in, or empty string for the default message.
                  The default message is: "This declaration is experimental and its usage should be marked with 'Marker'
                  or '@OptIn(Marker::class)'", where `Marker` is the opt-in requirement marker.
@property level specifies how usages of API without an explicit opt-in are reported in code.

## Declarations and overloads

### 1. Common

```kotlin
@Target(ANNOTATION_CLASS)
@Retention(BINARY)
@MustBeDocumented
@SinceKotlin("1.3")
public annotation class RequiresOptIn(
    val message: String = "",
    val level: Level = Level.ERROR
)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/annotations/OptIn.kt#L14)

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

fun main() {
    val value = kotlin.RequiresOptIn()
    println(value)
}
```

```text title="Output"
@kotlin.RequiresOptIn(message=, level=ERROR)
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
