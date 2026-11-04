# ContractBuilder.implies

`kotlin.contracts` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

指定在条件作为接收器参数维持时通过时要观察到的效果。

目前只支持 `ReturnsNotNull` 效果。

注:接收者只能接受一个布林表达式子集,其中函数参数或接收者( `this` )经过无效检查(`== null`, `!= null` ); - 实例检查( `is` , `!is` );

??? note "查看英文原文"

    Specifies the effect that will be observed if the condition passed as a receiver argument holds.
    
    Only `ReturnsNotNull` effect is supported for now.
    
    Note: the receiver can accept only a subset of boolean expressions,
    where a function parameter or receiver (`this`) undergoes
    - null-checks (`== null`, `!= null`);
    - instance-checks (`is`, `!is`);

## 声明与重载

### 1. Common

```kotlin
@ExperimentalExtendedContracts
    @ContractsDsl
    @SinceKotlin("2.2") // Technically 2.2.20
    public infix fun Boolean.implies(value: ReturnsNotNull)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/contracts/ContractBuilder.kt#L99)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


import kotlin.contracts.*
fun textOrNull(value: Any?): String? {
    contract { (value is String) implies returnsNotNull() }
    return value as? String
}
fun main() { println(textOrNull("Kotlin")); println(textOrNull(42)) }
```

```text title="输出"
Kotlin
null
```

编译选项：`-Xallow-condition-implies-returns-contracts`

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
