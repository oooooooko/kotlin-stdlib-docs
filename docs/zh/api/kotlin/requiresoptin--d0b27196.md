# RequiresOptIn

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

信号说明附加说明的批注类别是需要明确选择加入的API的标记。

任何附加此种标记的公告的呼唤网站,或在签字时提及任何其他需要选择加入的声明,都应选择加入API, 使用`OptIn`, 或加注该标记本身, 从而有效地进一步推广选择加入要求。

选择进入标记的预期用途包括但不限于以下用途:- 实验性API供公众预览,可能改变其语义或影响二进制兼容性;- 内部声明,由于技术原因,不应在申报图书馆外使用,但为`public`。 - 脆弱或微妙的API, 需要大量专门知识使用,因此需要明确的选择进入。

□ 纠纷

当声明带有选择适用要求时,即被视为具有传染性,意味着其所有使用或在其他声明中提及都将要求明确选择适用。 宣传的一条大指则如下:如果标记适用声明不复存在,只有明确选择适用(或相应的警告)的地方才会打破。 这一规则并不意味着过渡性,例如,传播不通过插入传播选择适用,使`inline`功能作者有责任正确标记。

类型范围

一种类型的选择进入,如果带有选择进入标记,或外部声明(类别或接口)要求选择进入,则被视为需要选择进入。 任何使用任何在签字中提及这类类型的声明,即使其不是直接在呼叫站点上使用,即使此类声明并不直接要求选择进入,也要求明确选择进入。

例如,考虑以下以非宣传选入为标志的声明:```
@UnstableApi
class Unstable

@OptIn(UnstableApi::class)
fun foo(): Unstable = Unstable()

@OptIn(UnstableApi::class)
fun bar(arg: Unstable = Unstable()) {}

@OptIn(UnstableApi::class)
fun Unstable?.baz() {}
```以及各自的呼叫地点:```
fun outerFun() {
    val s = foo()
    bar()
    null.baz()
}
```尽管呼叫站点并不直接提到 `Unstable` 型,但由于传染性,每个呼叫站点将触发相应的选择进入警告或错误。 请注意,传播不是过渡性的,即拨打`outerFun`不会引发任何进一步的选择进入要求。

· 词汇范围

如果某一类型需要选择适用,则这种要求将传播到其词汇范围和所有嵌套声明。```
@UnstableApi
class Unstable {
    fun memberFun() = ...

    class NestedClass {
        fun nestedFun() = ...
    }
}
```

任何使用 `Unstable` 、 `NestedClass` 或其成员职能都需要明确选择加入。

推翻声明

选择适用标记也通过继承和接口实施来传播,如果基本声明要求选择适用,则压倒它要求明确选择适用或宣传选择适用要求。

另见[科特林语文件](https://kotlinlang.org/docs/opt-in-requirements.html)) 详情。

@property 信息, 需要报告在没有明确选择使用或空字符串的情况下使用 API 的习惯上。 默认信息是 : “ 此声明是实验性的, 其使用应该标记为“ marker ” 或 “ @OptIn( Mark: class) ” , 其`Marker` 是 选择输入要求标记 。 @property 级别指定了没有明确选择使用 的 API 的使用在代码中是如何报告的 。

??? note "查看英文原文"

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

## 声明与重载

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

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/annotations/OptIn.kt#L14)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
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

```text title="输出"
@kotlin.RequiresOptIn(message=, level=ERROR)
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
