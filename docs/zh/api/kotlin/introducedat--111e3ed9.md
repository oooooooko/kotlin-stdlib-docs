# IntroducedAt

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

版本号表示库自己的发布版本，并非 Kotlin 版本。注解参数必须带默认值，编译器生成旧签名以维持二进制兼容。

??? note "查看英文原文"

    Instructs the Kotlin compiler to generate overloads by specifying the versions in which _optional_ parameters were
    introduced, after the initial publication of the library.
    Generated overloads are hidden and aimed to maintain binary compatibility,
    they let users of your library upgrade to the newer version without having to recompile their code.
    
    Value parameters with the same version are assumed to have been introduced at the same time.
    For example, given the signature,
    
    ```kotlin
    fun example(a: A, @IntroducedAt("1.1") b: B = defaultB, @IntroducedAt("1.1") c: C = defaultC, @IntroducedAt("1.4") d: D = defaultD)
    ```
    
    the compiler generates overloads corresponding to the following,
    
    ```kotlin
    fun example(a: A) // hidden, initial version
    fun example(a: A, @IntroducedAt("1.1") b: B = defaultB, @IntroducedAt("1.1") c: C = defaultC) // hidden, version 1.1
    
    // non-hidden overload, version 1.4
    fun example(a: A, @IntroducedAt("1.1") b: B = defaultB, @IntroducedAt("1.1") c: C = defaultC, @IntroducedAt("1.4") d: D = defaultD)
    ```
    
    Note that once a user of the library compiles against the new version, the most recent overload
    (the one with all the optional parameters) is chosen for code generation. That means that from that
    point on the older version of the library may no longer be used as a dependency.
    
    ### Restrictions on `IntroducedAt`
    
    The version string must follow the [Apache Maven version format](https://maven.apache.org/ref/3-LATEST/maven-artifact/apidocs/org/apache/maven/artifact/versioning/ComparableVersion.html).
    Versions in a signature must appear in **ascending** order.
    
    - Parameters without this annotation are assumed to correspond to the "initial version".
    - If the last parameter has a function type, this rule may be disregarded.
      This makes it possible to introduce optional parameters before the **trailing lambda** position.
    
    It is not allowed to use this annotation on extension receivers or context parameters,
    only in value parameters.
    
    Value parameters marked with the annotation must have a **default value**.
    Default values for optional arguments may not depend on values from a newer version.
    
    It is not allowed to use this annotation on non-final methods, including abstract methods and interfaces.
    These restrictions are similar to those of `kotlin.jvm.JvmName`.
    
    It is not allowed to use this annotation in combination with `kotlin.jvm.JvmOverloads`.
    
    If a data class constructor has parameters annotated with the annotation,
    the compiler also generates the corresponding overloads of its `copy` method in addition to the constructor overloads.
    
    > For more information you can check the [full design (KEEP) document](https://github.com/Kotlin/KEEP/blob/main/proposals/KEEP-0431-version-overloading.md).
    
    @property version version string following the [Apache Maven version format](https://maven.apache.org/ref/3-LATEST/maven-artifact/apidocs/org/apache/maven/artifact/versioning/ComparableVersion.html).

## 声明与重载

### 1. Common

```kotlin
@Target(AnnotationTarget.VALUE_PARAMETER)
@MustBeDocumented
@SinceKotlin("2.3")
@ExperimentalVersionOverloading
public annotation class IntroducedAt(val version: String)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/annotations/VersionOverloads.kt#L24)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


fun greeting(name: String, @IntroducedAt("1.1") punctuation: String = "!"): String = "Hello, $name$punctuation"
fun main() { println(greeting("Kotlin")); println(greeting("Kotlin", "?")) }
```

```text title="输出"
Hello, Kotlin!
Hello, Kotlin?
```

## 版本与来源

本页用途说明和示例已单独整理。声明取自官方源码固定标签 `v2.4.21`，示例在 JVM 上使用 Kotlin / stdlib 2.4.21 校验。
