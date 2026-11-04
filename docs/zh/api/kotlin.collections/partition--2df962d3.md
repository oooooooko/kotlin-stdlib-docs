# partition

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将原始阵列分割成一对列表,其中* 第一批* 列表包含 `predicate` 生成 `true` 的元素,而* 第二组* 列表包含 `predicate` 生成 `false` 的元素。

@sample 样本、采集资料、阵列、变形、部门原始资料

??? note "查看英文原文"

    Splits the original array into a pair of lists,
    where *first* list contains elements for which `predicate` yielded `true`,
    while *second* list contains elements for which `predicate` yielded `false`.
    
    @sample samples.collections.Arrays.Transformations.partitionArrayOfPrimitives

## 声明与重载

### 1. Common

```kotlin
public inline fun <T> Array<out T>.partition(predicate: (T) -> Boolean): Pair<List<T>, List<T>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26273)

### 2. Common

```kotlin
public inline fun ByteArray.partition(predicate: (Byte) -> Boolean): Pair<List<Byte>, List<Byte>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26293)

### 3. Common

```kotlin
public inline fun ShortArray.partition(predicate: (Short) -> Boolean): Pair<List<Short>, List<Short>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26313)

### 4. Common

```kotlin
public inline fun IntArray.partition(predicate: (Int) -> Boolean): Pair<List<Int>, List<Int>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26333)

### 5. Common

```kotlin
public inline fun LongArray.partition(predicate: (Long) -> Boolean): Pair<List<Long>, List<Long>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26353)

### 6. Common

```kotlin
public inline fun FloatArray.partition(predicate: (Float) -> Boolean): Pair<List<Float>, List<Float>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26373)

### 7. Common

```kotlin
public inline fun DoubleArray.partition(predicate: (Double) -> Boolean): Pair<List<Double>, List<Double>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26393)

### 8. Common

```kotlin
public inline fun BooleanArray.partition(predicate: (Boolean) -> Boolean): Pair<List<Boolean>, List<Boolean>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26413)

### 9. Common

```kotlin
public inline fun CharArray.partition(predicate: (Char) -> Boolean): Pair<List<Char>, List<Char>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26433)

### 10. Common

```kotlin
public inline fun <T> Iterable<T>.partition(predicate: (T) -> Boolean): Pair<List<T>, List<T>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3623)

将原始收藏分成一对清单,其中* 第一批* 清单载有 `predicate` 得出 `true` 的元素,而* 第二清单载有 `predicate` 得出 `false` 的元素。

@sample 样本 采集 可行 操作 部门

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    data class Person(val name: String, val age: Int) {
        override fun toString(): String {
            return "$name - $age"
        }
    }

    val list = listOf(Person("Tom", 18), Person("Andy", 32), Person("Sarah", 22))
    val result = list.partition { it.age < 30 }
    println(result)
}
```

```text title="输出"
([Tom - 18, Sarah - 22], [Andy - 32])
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/iterables.kt#L75)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
