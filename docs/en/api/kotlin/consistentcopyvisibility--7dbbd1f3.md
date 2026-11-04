# ConsistentCopyVisibility

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

In previous versions of Kotlin, the generated 'copy' method of a data class always had public visibility,
even if the primary constructor was non-public. That exposed the non-public constructor of the data class.

In future versions of Kotlin,
the generated 'copy' method of a data class will have the same visibility as the primary constructor.

When you apply the `ConsistentCopyVisibility` annotation to a data class with non-public constructor:
1. The generated 'copy' method will have the same visibility as the primary constructor.
   You enroll into the new behavior right away.
2. You disable all the warnings/errors about the behavior change because they become unnecessary.

The effect of '-Xconsistent-data-class-copy-visibility' flag is the same as applying `ConsistentCopyVisibility` to all data classes in the module.

## Deprecation timeline

- **Phase 1.** Kotlin 2.0.20.
  The compiler warns about the behavior change on the data class declaration and on illegal 'copy' method usages (illegal usages are those that will become invisible by the end of the migration).
  It's possible to suppress the warning on the declaration with `ConsistentCopyVisibility`/`ExposedCopyVisibility` annotations or the '-Xconsistent-data-class-copy-visibility' flag.
  Illegal usages should start the migration.
- **Phase 2.** (Supposedly Kotlin 2.1 or Kotlin 2.2). The warnings turn into errors.
  Keep in mind that the compiler still generates public 'copy' under the hood. The binary signature is preserved.
  It's possible to suppress the error on the declaration with `ConsistentCopyVisibility`/`ExposedCopyVisibility` annotations or the '-Xconsistent-data-class-copy-visibility' flag.
  It's impossible to suppress the error on illegal 'copy' method usages.
  Illegal usages should migrate.
- **Phase 3.** (Supposedly Kotlin 2.2 or Kotlin 2.3). The default changes.
  Unless `ExposedCopyVisibility` is used, the generated 'copy' method has the same visibility as the primary constructor.
  The binary signature changes.
  The error on the declaration is no longer reported.
  '-Xconsistent-data-class-copy-visibility' compiler flag and `ConsistentCopyVisibility` annotation are now unnecessary.

**Notes:**
- For the exact mapping of deprecation phases and Kotlin versions follow [KT-11914](https://youtrack.jetbrains.com/issue/KT-11914).
- You can turn the warning into an error by using the '-progressive'/'-Werror' compiler flag.

## Recommendation and alternatives

- If you write new code or don't care about binary compatibility,
  it's recommended to use `ConsistentCopyVisibility` (or '-Xconsistent-data-class-copy-visibility' compiler flag) instead of the `ExposedCopyVisibility`.
- When you use `ExposedCopyVisibility`, it's also recommended to use '-Xconsistent-data-class-copy-visibility' in the same module.
  This way, old classes won't change their behavior, but new classes will have the correct visibility of the 'copy' method.
- Once all the illegal 'copy' method usages are migrated, please drop the `ExposedCopyVisibility` annotation.
- You can introduce your own 'copy'-like method alongside the generated 'copy',
  and migrate all the usages to the introduced method.
- You can rewrite your data class to regular Kotlin class.
  You need to manually implement all the data class generated methods.

@see `ExposedCopyVisibility`
@see [KT-11914](https://youtrack.jetbrains.com/issue/KT-11914)

## Declarations and overloads

### 1. Common

```kotlin
@Target(AnnotationTarget.CLASS)
@Retention(AnnotationRetention.BINARY)
@SinceKotlin("2.0")
public annotation class ConsistentCopyVisibility
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/annotations/ConsistentCopyVisibility.kt#L8)

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
    val value = kotlin.ConsistentCopyVisibility()
    println(value)
}
```

```text title="Output"
@kotlin.ConsistentCopyVisibility()
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
