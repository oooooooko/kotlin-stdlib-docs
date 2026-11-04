# ExposedCopyVisibility

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

在先前版本的科特林中,生成的数据类“复制”方法总是能引起公众的注意,即使主建商是非公共的。 这暴露了数据类的非公共构建商。

在未来版本的科特林中,生成的数据类“复制”方法与主建构人具有同样的可见度。

当您对数据类别应用 `ExposedCopyVisibility` 注释时: 1. 您选择让公众继续 ** 双进制 显示生成的“ 副本” 方法。 但“ 副本” 方法的非法使用将无法进入 。 2. 您只是在声明上抑制关于行为变化的警告/ 警告/ 警告 / 警告 / 警告 / 非法 ** 复制 方法的 / 使用** 将持续, 即使您使用 `ExposedCopyVisibility` 方法 ! **

□ 折旧时间表

- ** 第1阶段** Kotlin 2. 20. 20。 汇编者警告数据类申报和非法“ 副本” 方法使用的行为变化( 非法使用是迁移结束时将隐形的)。 有可能用 `ConsistentCopyVisibility` / `ExposedCopyVisibility` 注释或“ Xconversity data- slas- opbility- visible” 标记来抑制申报的警告。 非法使用应该开始迁移。 ** 第2阶段** (supposedly Kotlin 2. 1 或 Kotlin 2. 2) 。 警告变成错误。 提醒会变成错误。 记住, 编译者仍然在引擎盖下生成公开的“ 副本 ” 。 二元签名会保存。 有可能用 `ConsistentCopyVisibility` / `ExposedCopyVisibility` 说明或“ Xconsent- data- licopli- visibilable- visibility” 旗帜来抑制申报的错误。 无法抑制非法“ 副本” 方法上的错误。 非法使用应该迁移。 - ** 第3阶段** (Vuperedly Kotlin 2.2 或 Kotlin 2.3)。默认更改。 除非使用 `ExposedCopyVisibility` , 生成的“ 复制” 方法与主建构器具有相同的可见度。 二进制签名更改。 声明上的错误不再报告 。 “- Xconferent data- class- option- visibility” 编译器旗帜和 `ConsistentCopyVisibility` 批注现在没有必要 。

** 注:** - 精确绘制折旧阶段和 Kotlin 版本的地图,请在 [KT-11914] (https://youtrack.jetbrains.com/issue/KT-11914).)之后(通过使用“ 递进” /“ 错误” 编译器的标记,您可将警告变成错误。

□ **** 建议和替代物

- 如果你写新代码或不关心二元兼容性,建议使用 `ConsistentCopyVisibility` (或“Xconversent data-lis-option-visible” )而不是 `ExposedCopyVisibility` 的编译器。 - 当你使用`ExposedCopyVisibility`时, 还建议在同一模块中使用“- Xconversent data- class-visible-visibility” 。 这样, 老类不会改变他们的行为, 但新类将拥有“ opy” 方法的正确可见度 。 - 一旦所有非法的“ opy” 方法都迁移了, 请放弃 `ExposedCopyVisibility` annologation 。 - 您可以在生成的“ opy” 的同时引入自己的“ opypy” 类似方法, 并将所有使用方式迁移到引入的方法 。 - 您可以将您的数据类重写为常规 Kotlin 类 类 。 您需要手动执行所有数据类生成的方法 。

@see `ConsistentCopyVisibility` @see [KT-11914] (https://youtrack.jetbrains.com/issue/KT-11914))

??? note "查看英文原文"

    In previous versions of Kotlin, the generated 'copy' method of a data class always had public visibility,
    even if the primary constructor was non-public. That exposed the non-public constructor of the data class.
    
    In future versions of Kotlin,
    the generated 'copy' method of a data class will have the same visibility as the primary constructor.
    
    When you apply `ExposedCopyVisibility` annotation to your data class:
    1. You choose to keep the public **binary** visibility of the generated 'copy' method.
       But illegal usages of the 'copy' method will become inaccessible anyway.
    2. You suppress the warning/error about the behavior change only on the declaration.
       **Please note** that the warning/error on all the illegal **usages** of the 'copy' method **stays even if you use `ExposedCopyVisibility`!**
    
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
    
    @see `ConsistentCopyVisibility`
    @see [KT-11914](https://youtrack.jetbrains.com/issue/KT-11914)

## 声明与重载

### 1. Common

```kotlin
@Target(AnnotationTarget.CLASS)
@Retention(AnnotationRetention.BINARY)
@SinceKotlin("2.0")
public annotation class ExposedCopyVisibility
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/annotations/ConsistentCopyVisibility.kt#L63)

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
    val value = kotlin.ExposedCopyVisibility()
    println(value)
}
```

```text title="输出"
@kotlin.ExposedCopyVisibility()
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
