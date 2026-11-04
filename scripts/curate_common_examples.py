"""Compile and capture the hand-written examples that need API-specific contexts."""

from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
from textwrap import dedent

from collect_api import ROOT
from verify_examples import output_can_vary

HEADER = '''@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)
'''
PROGRAMS = []


def add(package, names, code, imports="", **metadata):
    PROGRAMS.append({"keys":[package+"/"+name for name in names.split()],
                     "code":HEADER+"\n"+imports+"\n"+dedent(code).strip()+"\n", **metadata})


def catalog():
    add("kotlin.collections", "flatMapIndexedTo flatMapTo mapIndexedNotNullTo mapIndexedTo mapKeysTo mapNotNullTo mapTo mapValues mapValuesTo", '''
        fun main() {
            println(listOf(1, 2).flatMapTo(mutableListOf<Int>()) { listOf(it, -it) })
            println(listOf(1, 2).flatMapIndexedTo(mutableListOf<Int>()) { index, value -> listOf(index, value) })
            println(listOf(1, 2).mapTo(mutableListOf<String>()) { "v$it" })
            println(listOf(1, 2).mapIndexedTo(mutableListOf<String>()) { index, value -> "$index:$value" })
            println(listOf(1, 2).mapNotNullTo(mutableListOf<Int>()) { it.takeIf { n -> n > 1 } })
            println(listOf(1, 2).mapIndexedNotNullTo(mutableListOf<Int>()) { index, value -> value.takeIf { index > 0 } })
            val values = linkedMapOf("a" to 1, "b" to 2)
            println(values.mapKeysTo(linkedMapOf<String, Int>()) { it.key.uppercase() })
            println(values.mapValues { it.value * 10 })
            println(values.mapValuesTo(linkedMapOf<String, Int>()) { it.value * 10 })
        }
    ''')
    add("kotlin.collections", "MutableListIterator.remove", '''
        fun main() {
            val values = mutableListOf(1, 2, 3)
            val iterator = values.listIterator()
            println(iterator.next())
            iterator.remove()
            println(values)
        }
    ''')
    add("kotlin.collections", "ArrayDeque.removeRange", '''
        fun main() {
            val deque = ArrayDeque(listOf(1, 2, 3, 4))
            // removeRange is a protected implementation hook; use the public subList view.
            deque.subList(1, 3).clear()
            println(deque)
        }
    ''', note_zh="`removeRange` 是受保护的实现钩子，不能直接调用。本例通过公开的 `subList().clear()` 删除区间。", note_en="`removeRange` is a protected implementation hook. Use the public `subList().clear()` operation to remove a range.")
    for scalar, values in {"Boolean":"true, false", "Byte":"1.toByte(), 2.toByte()", "Char":"'a', 'b'", "Double":"1.0, 2.0", "Float":"1f, 2f", "Short":"1.toShort(), 2.toShort()", "UShort":"1.toUShort(), 2.toUShort()"}.items():
        add("kotlin.collections", "to"+scalar+"Array", f'''fun main() {{ println(listOf({values}).to{scalar}Array().contentToString()) }}''')
    add("kotlin.sequences", "SequenceScope flatMapIndexedTo flatMapTo ifEmpty mapIndexedNotNullTo mapIndexedTo mapNotNullTo mapTo sumByDouble", '''
        fun main() {
            val values = sequence<Int> { yield(1); yieldAll(listOf(2, 3)) }
            println(values.toList())
            println(values.flatMapTo(mutableListOf<Int>()) { sequenceOf(it, -it) })
            println(values.flatMapIndexedTo(mutableListOf<Int>()) { index, value -> sequenceOf(index, value) })
            println(values.mapTo(mutableListOf<String>()) { "v$it" })
            println(values.mapIndexedTo(mutableListOf<String>()) { index, value -> "$index:$value" })
            println(values.mapNotNullTo(mutableListOf<Int>()) { it.takeIf { n -> n > 1 } })
            println(values.mapIndexedNotNullTo(mutableListOf<Int>()) { index, value -> value.takeIf { index > 0 } })
            println(emptySequence<Int>().ifEmpty { sequenceOf(42) }.toList())
            println(values.sumByDouble { it.toDouble() })
        }
    ''', imports="import kotlin.sequences.*", note_zh="`sumByDouble` 已弃用，新代码使用 `sumOf`。", note_en="`sumByDouble` is deprecated; use `sumOf` in new code.")
    add("kotlin.text", "findAnyOf findLastAnyOf flatMapIndexedTo flatMapTo foldIndexed foldRight foldRightIndexed forEachIndexed mapIndexedNotNullTo mapIndexedTo mapNotNullTo mapTo onEach onEachIndexed single sumByDouble toCollection", '''
        fun main() {
            val text = "abc"
            println(text.findAnyOf(listOf("b", "c")))
            println(text.findLastAnyOf(listOf("b", "c")))
            println(text.flatMapTo(mutableListOf<Char>()) { listOf(it, it) })
            println(text.flatMapIndexedTo(mutableListOf<String>()) { index, char -> listOf("$index:$char") })
            println(text.foldIndexed("") { index, acc, char -> "$acc$index$char" })
            println(text.foldRight("") { char, acc -> "$acc$char" })
            println(text.foldRightIndexed("") { index, char, acc -> "$acc$index$char" })
            text.forEachIndexed { index, char -> println("$index:$char") }
            println(text.mapTo(mutableListOf<String>()) { it.uppercase() })
            println(text.mapIndexedTo(mutableListOf<String>()) { index, char -> "$index:$char" })
            println(text.mapNotNullTo(mutableListOf<Char>()) { it.takeIf { c -> c != 'b' } })
            println(text.mapIndexedNotNullTo(mutableListOf<Char>()) { index, char -> char.takeIf { index > 0 } })
            println(text.onEach { print(it.uppercase()) })
            println(text.onEachIndexed { index, char -> print("$index$char ") })
            println(text.single { it == 'b' })
            println(text.sumByDouble { it.code.toDouble() })
            println(text.toCollection(linkedSetOf<Char>()))
        }
    ''')
    add("kotlin.text", "Appendable", '''
        fun appendGreeting(destination: Appendable) { destination.append("Hello").append('!') }
        fun main() { val text = StringBuilder(); appendGreeting(text); println(text) }
    ''')
    add("kotlin.text", "MatchNamedGroupCollection MatchNamedGroupCollection.get", '''
        fun main() {
            val match = Regex("(?<word>[a-z]+)-(?<number>[0-9]+)").matchEntire("item-42")!!
            println(match.groups["word"]?.value)
            println(match.groups["number"]?.value)
        }
    ''')
    add("kotlin.text", "MatchResult.Destructured MatchResult.Destructured.match MatchResult.Destructured.toList " + " ".join("MatchResult.Destructured.component"+str(i) for i in range(1,11)), '''
        fun main() {
            val match = Regex("(a)(b)(c)(d)(e)(f)(g)(h)(i)(j)").matchEntire("abcdefghij")!!
            val groups = match.destructured
            val (a, b, c, d, e, f, g, h, i, j) = groups
            println(listOf(a, b, c, d, e, f, g, h, i, j))
            println(groups.toList())
            println(groups.match.value)
        }
    ''')
    add("kotlin.text", "HexFormat.BytesHexFormat HexFormat.BytesHexFormat.Builder HexFormat.BytesHexFormat.toString HexFormat.NumberHexFormat.toString HexFormat.bytes HexFormat.number HexFormat.toString", '''
        fun main() {
            val format = HexFormat {
                bytes { byteSeparator = ":"; upperCase = true }
                number { prefix = "0x"; removeLeadingZeros = true }
            }
            println(byteArrayOf(10, 15).toHexString(format))
            println(255.toHexString(format))
            println(format.bytes.toString())
            println(format.number.toString())
            println(format.toString())
        }
    ''')
    add("kotlin.text", "toLowerCase toUpperCase", '''
        fun main() {
            println("KOTLIN".toLowerCase())
            println("kotlin".toUpperCase())
            println("KOTLIN".lowercase())
            println("kotlin".uppercase())
        }
    ''', note_zh="旧大小写转换 API 已弃用；新代码使用 `lowercase` / `uppercase`。", note_en="The legacy case conversion APIs are deprecated. Use `lowercase` / `uppercase` in new code.")
    add("kotlin.properties", "ObservableProperty ObservableProperty.afterChange ObservableProperty.beforeChange ObservableProperty.constructor ObservableProperty.getValue ObservableProperty.setValue ObservableProperty.toString", '''
        import kotlin.properties.ObservableProperty
        import kotlin.reflect.KProperty
        class NonNegative(initial: Int) : ObservableProperty<Int>(initial) {
            override fun beforeChange(property: KProperty<*>, oldValue: Int, newValue: Int): Boolean = newValue >= 0
            override fun afterChange(property: KProperty<*>, oldValue: Int, newValue: Int) {
                println("${property.name}: $oldValue -> $newValue")
            }
        }
        fun main() {
            val delegate = NonNegative(1)
            var count by delegate
            println(count)
            count = 2
            count = -1
            println(count)
            println(delegate.toString())
        }
    ''')
    add("kotlin.properties", "PropertyDelegateProvider PropertyDelegateProvider.provideDelegate", '''
        import kotlin.properties.PropertyDelegateProvider
        import kotlin.properties.ReadOnlyProperty
        fun main() {
            val provider = PropertyDelegateProvider<Any?, ReadOnlyProperty<Any?, String>> { _, property ->
                println("provide: ${property.name}")
                ReadOnlyProperty { _, _ -> "ready" }
            }
            val status by provider
            println(status)
        }
    ''')
    add("kotlin.ranges", "ClosedFloatingPointRange ClosedFloatingPointRange.lessThanOrEquals", '''
        fun main() {
            val range: ClosedFloatingPointRange<Double> = 1.0..3.0
            println(2.0 in range)
            println(range.lessThanOrEquals(1.0, 3.0))
            println(range.lessThanOrEquals(Double.NaN, 3.0))
        }
    ''')
    add("kotlin.reflect", "KProperty1.get KMutableProperty1.set", '''
        import kotlin.reflect.KMutableProperty1
        class Counter(var count: Int)
        fun main() {
            val property: KMutableProperty1<Counter, Int> = Counter::count
            val counter = Counter(1)
            println(property.get(counter))
            property.set(counter, 42)
            println(counter.count)
        }
    ''')
    add("kotlin.reflect", "KProperty2 KProperty2.get KMutableProperty2 KMutableProperty2.set", '''
        import kotlin.reflect.KMutableProperty2
        import kotlin.reflect.full.memberExtensionProperties
        class Labels(var prefix: String) {
            var Int.label: String
                get() = "$prefix$this"
                set(value) { prefix = value }
        }
        fun main() {
            @Suppress("UNCHECKED_CAST")
            val property = Labels::class.memberExtensionProperties.single() as KMutableProperty2<Labels, Int, String>
            val labels = Labels("item-")
            println(property.get(labels, 7))
            property.set(labels, 7, "new-")
            println(property.get(labels, 7))
        }
    ''', dependencies=["kotlin-reflect:2.4.21"])
    for typ in ("Long", "Double"):
        add("kotlin.time", " ".join("Abstract"+typ+"TimeSource"+suffix for suffix in ("", ".constructor", ".read", ".unit")), f'''
            import kotlin.time.*
            class ManualClock : Abstract{typ}TimeSource(DurationUnit.MILLISECONDS) {{
                var reading = {"0L" if typ=="Long" else "0.0"}
                override fun read(): {typ} = reading
                fun unitName(): String = unit.name
            }}
            fun main() {{
                val clock = ManualClock()
                val mark = clock.markNow()
                clock.reading = {"25L" if typ=="Long" else "25.0"}
                println(clock.unitName())
                println(mark.elapsedNow())
            }}
        ''')
    add("kotlin.time", "Clock Instant.Companion.now TimeSource TimeSource.Monotonic.ValueTimeMark TimeSource.WithComparableMarks TestTimeSource.read", '''
        import kotlin.time.*
        import kotlin.time.Duration.Companion.milliseconds
        fun main() {
            val clock: Clock = object : Clock { override fun now(): Instant = Instant.fromEpochMilliseconds(0) }
            println(clock.now())
            val source: TimeSource.WithComparableMarks = TestTimeSource()
            val mark = source.markNow()
            (source as TestTimeSource) += 25.milliseconds
            println(mark.elapsedNow())
            val monotonic: TimeSource = TimeSource.Monotonic
            val valueMark: TimeSource.Monotonic.ValueTimeMark = TimeSource.Monotonic.markNow()
            println(valueMark.hasPassedNow())
            println(monotonic.markNow().hasPassedNow())
            try { println(Instant.now()) } catch (error: NotImplementedError) { println("Instant.now: ${error.message}") }
        }
    ''', note_zh="`TestTimeSource.read` 是由时间标记间接使用的受保护钩子。`Instant.now()` 已弃用，2.4.21 中的实现会抛出 `NotImplementedError`；本例捕获该异常，新代码使用 `Clock.System.now()`。", note_en="`TestTimeSource.read` is a protected time-mark hook. Deprecated `Instant.now()` throws `NotImplementedError` in 2.4.21; this example catches it. Use `Clock.System.now()` in new code.")
    add("kotlin", "Annotation", '''
        annotation class Label(val value: String)
        fun main() { val label: Annotation = Label("example"); println(label.annotationClass.simpleName) }
    ''')
    add("kotlin", "Nothing", '''
        fun fail(message: String): Nothing = throw IllegalStateException(message)
        fun main() {
            try { fail("missing value") } catch (error: IllegalStateException) { println(error.message) }
            val value: String? = null
            println(value ?: "fallback")
        }
    ''')
    add("kotlin", "arrayOfNulls enumValues", '''
        enum class State { READY, DONE }
        fun main() {
            println(arrayOfNulls<String>(3).contentToString())
            println(enumValues<State>().contentToString())
        }
    ''')
    add("kotlin", "isInitialized", '''
        lateinit var title: String
        fun main() { println(::title.isInitialized); title = "Kotlin"; println(::title.isInitialized) }
    ''')
    add("kotlin", "takeUnless", '''
        fun main() { println(42.takeUnless { it < 0 }); println((-1).takeUnless { it < 0 }) }
    ''')
    for typ in ("UByte", "UShort", "UInt", "ULong"):
        factory=typ.lower()+"ArrayOf"
        add("kotlin", typ+"Array.containsAll", f'''fun main() {{ println({factory}(1u, 2u, 3u).containsAll(listOf(1u, 3u))); println({factory}(1u, 2u).containsAll(listOf(3u))) }}'''.replace("listOf(1u, 3u)",f"listOf(1u.to{typ}(), 3u.to{typ}())").replace("listOf(3u)",f"listOf(3u.to{typ}())"))
    for typ,literal in {"Byte":"65.toByte()", "Short":"65.toShort()", "Long":"65L", "Float":"65.5f", "Double":"65.5"}.items():
        names=typ+".toChar"+(" "+typ+".toByte "+typ+".toShort" if typ in {"Float","Double"} else "")
        add("kotlin", names, f'''fun main() {{ val value = {literal}; println(value.toChar()); {"println(value.toByte()); println(value.toShort());" if typ in {"Float","Double"} else ""} println(value.toInt().toChar()) }}''', note_zh="旧的直接转换已弃用。示例为兼容旧代码演示而抑制错误；新代码先显式转为 `Int`。", note_en="These direct conversions are deprecated. This compatibility example suppresses deprecation errors; explicitly convert to `Int` first in new code.")
    add("kotlin", "DeepRecursiveScope DeepRecursiveScope.invoke", '''
        fun main() {
            val sum = DeepRecursiveFunction<Int, Int> { n -> if (n == 0) 0 else n + callRecursive(n - 1) }
            println(sum(100))
            lateinit var invalid: DeepRecursiveFunction<Int, Int>
            invalid = DeepRecursiveFunction { n -> invalid(n) }
            try { invalid(1) } catch (error: UnsupportedOperationException) { println(error.message) }
        }
    ''', note_zh="作用域内部应使用 `callRecursive`；直接调用 `invoke` 已禁止，本例同时展示被抑制后的异常，便于迁移旧代码。", note_en="Use `callRecursive` inside the scope. Direct `invoke` is forbidden; the suppressed legacy call demonstrates its exception for migration.")
    add("kotlin.coroutines", "AbstractCoroutineContextElement AbstractCoroutineContextElement.constructor CoroutineContext.Element CoroutineContext.Key CoroutineContext.Element.fold CoroutineContext.Element.get CoroutineContext.Element.minusKey EmptyCoroutineContext.get EmptyCoroutineContext.minusKey", '''
        import kotlin.coroutines.*
        class RequestId(val value: String) : AbstractCoroutineContextElement(Key) {
            companion object Key : CoroutineContext.Key<RequestId>
        }
        fun main() {
            val element: CoroutineContext.Element = RequestId("request-42")
            println(element[RequestId]?.value)
            println(element.fold(0) { count, _ -> count + 1 })
            println(element.minusKey(RequestId) === EmptyCoroutineContext)
            println(EmptyCoroutineContext[RequestId])
            println(EmptyCoroutineContext.minusKey(RequestId) === EmptyCoroutineContext)
        }
    ''')
    add("kotlin.coroutines", "AbstractCoroutineContextKey AbstractCoroutineContextKey.constructor", '''
        import kotlin.coroutines.*
        open class BaseElement : CoroutineContext.Element {
            companion object Key : CoroutineContext.Key<BaseElement>
            override val key: CoroutineContext.Key<*> get() = Key
            override fun <E : CoroutineContext.Element> get(key: CoroutineContext.Key<E>): E? = getPolymorphicElement(key)
            override fun minusKey(key: CoroutineContext.Key<*>): CoroutineContext = minusPolymorphicKey(key)
        }
        class DerivedElement : BaseElement() {
            companion object Key : AbstractCoroutineContextKey<BaseElement, DerivedElement>(BaseElement, { it as? DerivedElement })
        }
        fun main() {
            val context: CoroutineContext = DerivedElement()
            println(context[BaseElement] != null)
            println(context[DerivedElement] != null)
        }
    ''', note_zh="此多态键 API 在 2.4 中已弃用。新代码建议按基础键获取元素后显式转换类型。", note_en="Polymorphic context keys are deprecated since 2.4. Retrieve by the base key and cast explicitly in new code.")
    add("kotlin.coroutines", "Continuation Continuation.context Continuation.resumeWith resume resumeWithException", '''
        import kotlin.coroutines.*
        fun main() {
            val completion = object : Continuation<Int> {
                override val context: CoroutineContext = EmptyCoroutineContext
                override fun resumeWith(result: Result<Int>) {
                    println(result.fold({ "value=$it" }, { "error=${it.message}" }))
                }
            }
            println(completion.context === EmptyCoroutineContext)
            completion.resumeWith(Result.success(1))
            completion.resume(42)
            completion.resumeWithException(IllegalStateException("failed"))
        }
    ''', note_zh="这里使用普通回调对象分别展示三个入口。由协程创建的一次性 continuation 只能恢复一次，不能按此例连续恢复同一真实挂起点。", note_en="This plain callback object demonstrates three entry points. A one-shot continuation produced by a coroutine must be resumed only once.")
    add("kotlin.coroutines", "createCoroutine startCoroutine suspendCoroutine coroutineContext", '''
        import kotlin.coroutines.*
        class RequestId(val value: String) : AbstractCoroutineContextElement(Key) {
            companion object Key : CoroutineContext.Key<RequestId>
        }
        fun main() {
            val completion = object : Continuation<Int> {
                override val context: CoroutineContext = RequestId("request-42")
                override fun resumeWith(result: Result<Int>) { println("result=${result.getOrThrow()}") }
            }
            val work: suspend () -> Int = {
                println(coroutineContext[RequestId]?.value)
                suspendCoroutine { continuation -> continuation.resume(42) }
            }
            val created = work.createCoroutine(completion)
            println("created")
            created.resume(Unit)
            work.startCoroutine(completion)
        }
    ''')
    add("kotlin", "suspend", '''
        import kotlin.coroutines.*
        fun main() {
            val work = suspend { 42 }
            work.startCoroutine(object : Continuation<Int> {
                override val context = EmptyCoroutineContext
                override fun resumeWith(result: Result<Int>) { println(result.getOrThrow()) }
            })
        }
    ''')
    add("kotlin.coroutines", "ContinuationInterceptor ContinuationInterceptor.get ContinuationInterceptor.interceptContinuation ContinuationInterceptor.minusKey ContinuationInterceptor.releaseInterceptedContinuation", '''
        import kotlin.coroutines.*
        class LoggingInterceptor : AbstractCoroutineContextElement(ContinuationInterceptor), ContinuationInterceptor {
            override fun <T> interceptContinuation(continuation: Continuation<T>): Continuation<T> =
                object : Continuation<T> {
                    override val context = continuation.context
                    override fun resumeWith(result: Result<T>) { println("intercept"); continuation.resumeWith(result) }
                }
            override fun releaseInterceptedContinuation(continuation: Continuation<*>) { println("released") }
        }
        fun main() {
            val interceptor = LoggingInterceptor()
            println(interceptor[ContinuationInterceptor] === interceptor)
            println(interceptor.minusKey(ContinuationInterceptor) === EmptyCoroutineContext)
            val work: suspend () -> Int = { 42 }
            work.startCoroutine(object : Continuation<Int> {
                override val context: CoroutineContext = interceptor
                override fun resumeWith(result: Result<Int>) { println(result.getOrThrow()) }
            })
        }
    ''')
    add("kotlin.coroutines.intrinsics", "createCoroutineUnintercepted intercepted startCoroutineUninterceptedOrReturn suspendCoroutineUninterceptedOrReturn", '''
        import kotlin.coroutines.*
        import kotlin.coroutines.intrinsics.*
        fun main() {
            val completion = object : Continuation<Int> {
                override val context: CoroutineContext = EmptyCoroutineContext
                override fun resumeWith(result: Result<Int>) { println("completed=${result.getOrThrow()}") }
            }
            val work: suspend () -> Int = { suspendCoroutineUninterceptedOrReturn<Int> { 42 } }
            val created = work.createCoroutineUnintercepted(completion)
            println(created.intercepted() === created)
            created.resume(Unit)
            val immediate = work.startCoroutineUninterceptedOrReturn(completion)
            println("immediate=$immediate")
            println(immediate === COROUTINE_SUSPENDED)
        }
    ''', note_zh="这是协程实现者使用的底层 API。同步返回值时不会再调用 completion；真正挂起时必须返回 `COROUTINE_SUSPENDED` 并确保只恢复一次。", note_en="These are coroutine implementation primitives. A synchronous result does not invoke completion. A suspended operation must return `COROUTINE_SUSPENDED` and resume exactly once.")
    add("kotlin.coroutines.debug", "StackTraceRecoverable StackTraceRecoverable.copyForStackTraceRecovery", '''
        import kotlin.coroutines.debug.StackTraceRecoverable
        class TaskFailure(message: String, cause: Throwable? = null) : Exception(message, cause), StackTraceRecoverable<TaskFailure> {
            override fun copyForStackTraceRecovery(): TaskFailure = TaskFailure(message ?: "", this)
        }
        fun main() {
            val original = TaskFailure("task failed")
            val copy = original.copyForStackTraceRecovery()
            println(copy.message)
            println(copy.cause === original)
        }
    ''')
    add("kotlin.io", "readln", '''fun main() { val name = readln(); println("Hello, $name!") }''', stdin="Kotlin\n")
    add("kotlin.contracts", "CallsInPlace ConditionalEffect ContractBuilder ContractBuilder.callsInPlace ContractBuilder.returns ContractBuilder.returnsNotNull Effect Returns ReturnsNotNull SimpleEffect SimpleEffect.implies contract InvocationKind InvocationKind.EXACTLY_ONCE", '''
        import kotlin.contracts.*
        fun isText(value: Any?): Boolean {
            contract { returns(true) implies (value is String) }
            return value is String
        }
        fun requireText(value: Any?) {
            contract { returns() implies (value is String) }
            require(value is String)
        }
        fun textOrNull(value: Any?): String? {
            contract { returnsNotNull() implies (value is String) }
            return value as? String
        }
        inline fun once(block: () -> Unit) {
            contract { callsInPlace(block, InvocationKind.EXACTLY_ONCE) }
            block()
        }
        fun main() {
            val value: Any? = "Kotlin"
            if (isText(value)) println(value.length)
            requireText(value)
            println(value.length)
            val result = textOrNull(value)
            println(result)
            val initialized: Int
            once { initialized = 42 }
            println(initialized)
        }
    ''', note_zh="契约效果类型由 `contract` DSL 构造，不能作为普通对象手动创建。编译器使用这些声明进行智能转换和初始化分析；它们不会自动检查函数体是否兑现承诺。", note_en="Effect interfaces are produced by the contract DSL, not instantiated as ordinary objects. Contracts guide smart casts and initialization analysis; they do not enforce the function's promises at runtime.")
    for kind,loop in {"AT_MOST_ONCE":"if (enabled) block()", "AT_LEAST_ONCE":"block(); if (enabled) block()", "UNKNOWN":"repeat(if (enabled) 3 else 0) { block() }"}.items():
        add("kotlin.contracts", "InvocationKind."+kind, f'''
            import kotlin.contracts.*
            inline fun invokeBlock(enabled: Boolean, block: () -> Unit) {{
                contract {{ callsInPlace(block, InvocationKind.{kind}) }}
                {loop}
            }}
            fun main() {{ var count = 0; invokeBlock(true) {{ count++ }}; println(count) }}
        ''')
    add("kotlin.contracts", "ContractBuilder.holdsIn HoldsIn", '''
        import kotlin.contracts.*
        inline fun whenEnabled(enabled: Boolean, block: () -> Unit) {
            contract { enabled holdsIn block; callsInPlace(block, InvocationKind.AT_MOST_ONCE) }
            if (enabled) block()
        }
        fun main() { val enabled = true; whenEnabled(enabled) { println("enabled=$enabled") } }
    ''', compiler_options=["-Xallow-holdsin-contract"])
    add("kotlin.contracts", "ContractBuilder.implies", '''
        import kotlin.contracts.*
        fun textOrNull(value: Any?): String? {
            contract { (value is String) implies returnsNotNull() }
            return value as? String
        }
        fun main() { println(textOrNull("Kotlin")); println(textOrNull(42)) }
    ''', compiler_options=["-Xallow-condition-implies-returns-contracts"])
    add("kotlin.contracts", "ContractBuilder.returnsResultOf", '''
        import kotlin.contracts.*
        inline fun <T> evaluate(block: () -> T): T {
            contract { callsInPlace(block, InvocationKind.EXACTLY_ONCE); returnsResultOf(block) }
            return block()
        }
        fun main() { println(evaluate { 42 }) }
    ''', compiler_options=["-Xallow-returns-result-of", "-Xreturn-value-checker=check"])
    add("kotlin", "OptIn OptIn.constructor OptIn.markerClass RequiresOptIn.Level", '''
        @RequiresOptIn(level = RequiresOptIn.Level.WARNING)
        annotation class Preview
        @Preview fun previewValue(): Int = 42
        @OptIn(Preview::class)
        fun main() { println(previewValue()) }
    ''')
    add("kotlin", "SubclassOptInRequired SubclassOptInRequired.constructor SubclassOptInRequired.markerClass", '''
        @RequiresOptIn annotation class ExtensionApi
        @SubclassOptInRequired(ExtensionApi::class)
        open class Service { fun value(): Int = 42 }
        @OptIn(ExtensionApi::class)
        class CustomService : Service()
        fun main() { println(Service().value()); println(CustomService().value()) }
    ''')
    add("kotlin", "BuilderInference", '''
        fun <T> collect(@BuilderInference block: MutableList<T>.() -> Unit): List<T> = mutableListOf<T>().apply(block)
        fun main() { val values = collect { add("Kotlin"); add("stdlib") }; println(values) }
    ''', note_zh="这是兼容旧代码的注解示例。现代 Kotlin 在需要时会自动启用构建器类型推断，该注解已弃用。", note_en="This is a compatibility example. Modern Kotlin enables builder inference automatically when needed; the annotation is deprecated.")
    add("kotlin", "OverloadResolutionByLambdaReturnType", '''
        @OverloadResolutionByLambdaReturnType
        fun choose(block: () -> Int, marker: Int = 0): String = "Int: ${block()}"
        @OverloadResolutionByLambdaReturnType
        fun choose(block: () -> String, marker: String = ""): String = "String: ${block()}"
        fun main() { println(choose({ 42 })); println(choose({ "Kotlin" })) }
    ''')
    add("kotlin", "IntroducedAt IntroducedAt.constructor IntroducedAt.version", '''
        fun greeting(name: String, @IntroducedAt("1.1") punctuation: String = "!"): String = "Hello, $name$punctuation"
        fun main() { println(greeting("Kotlin")); println(greeting("Kotlin", "?")) }
    ''', note_zh="版本号表示库自己的发布版本，并非 Kotlin 版本。注解参数必须带默认值，编译器生成旧签名以维持二进制兼容。", note_en="The version belongs to the library being published, not Kotlin itself. Annotated parameters need defaults; the compiler emits old signatures for binary compatibility.")
    add("kotlin", "OptionalExpectation", '''
        fun main() { println(taggedValue()) }
    ''', files={"common.kt":'''@file:OptIn(kotlin.ExperimentalMultiplatform::class)
@OptionalExpectation
expect annotation class OptionalTrace()
@OptionalTrace
fun taggedValue(): String = "common annotation, no actual required"
'''}, compiler_options=["-Xmulti-platform", "-Xcommon-sources={common.kt}"], note_zh="这是一个最小多平台编译示例。`common.kt` 属于 common 源集；注解没有 actual 实现时会被擦除，通用函数仍可正常使用。", note_en="This minimal multiplatform compilation puts `common.kt` in the common source set. The optional annotation is erased without an actual implementation; the common function still works.")
    add("kotlin.experimental", "ExpectRefinement", '''
        actual class Device {
            actual fun name(): String = "device"
            actual fun feature(): String = "refined"
        }
        fun main() { val device = Device(); println(device.name()); println(device.feature()) }
    ''', files={"common.kt":'''expect class Device { fun name(): String }
''', "shared.kt":'''@file:OptIn(kotlin.ExperimentalMultiplatform::class)
import kotlin.experimental.ExpectRefinement
@ExpectRefinement
expect class Device { fun name(): String; fun feature(): String }
'''}, compiler_options=["-Xmulti-platform", "-XXLanguage:+ExpectRefinement", "-Xfragments=common,shared,jvm", "-Xfragment-refines=shared:common", "-Xfragment-refines=jvm:shared", "-Xfragment-sources=common:{common.kt}", "-Xfragment-sources=shared:{shared.kt}", "-Xfragment-sources=jvm:{main}"], note_zh="这是实验性的 expect 声明细化示例：common → shared → JVM。shared 重复原成员并新增成员，最终由 actual 类实现；它属于 Common 多平台声明机制。", note_en="This experimental expect-refinement example follows common → shared → JVM. The intermediate expect repeats existing members and adds a member, with a final actual implementation.")


def run():
    catalog()
    api_keys={g["key"] for g in json.loads((ROOT/"data/api.json").read_text())["groups"]}
    work=ROOT/".tools/curated"
    work.mkdir(exist_ok=True)
    lib=ROOT/".tools/maven-kotlinc/lib/kotlin-stdlib.jar"
    reflect=ROOT/".tools/kotlin-reflect-2.4.21.jar"
    cp=str(lib)+":"+str(reflect)
    destination=ROOT/"data/manual-examples.json"
    verified=json.loads(destination.read_text())
    text_path=ROOT/"data/manual-api-text.json"
    explanations=json.loads(text_path.read_text())
    failures={}
    def execute(entry):
        previous=next((verified[key] for key in entry["keys"] if key in verified),None)
        if previous and all(previous.get(key)==entry.get(key) for key in ("code","stdin","compiler_options","files")) and previous.get("dependencies",[])==entry.get("dependencies",[]):
            return entry,previous,None
        ident="c"+hashlib.sha256(entry["code"].encode()).hexdigest()[:12]
        folder=work/ident; folder.mkdir(exist_ok=True)
        source=folder/"Example.kt"; source.write_text(entry["code"])
        paths={"main":str(source)}
        extras=[]
        for filename,code in entry.get("files",{}).items():
            path=folder/filename; path.write_text(code); paths[filename]=str(path); extras.append(str(path))
        flags=entry.get("compiler_options",[])[:]
        for name,path in paths.items():
            flags=[flag.replace("{"+name+"}",path) for flag in flags]
        compiled=subprocess.run([str(ROOT/".tools/maven-kotlinc/bin/kotlinc"),"-nowarn","-no-stdlib","-no-reflect","-classpath",cp,"-d",str(folder/"classes"),*flags,str(source),*extras],capture_output=True,text=True,timeout=120)
        if compiled.returncode:return entry,None,(compiled.stdout+compiled.stderr)[-2400:]
        with tempfile.TemporaryDirectory(prefix="stdlib-curated-") as cwd:
            command=["java","-cp",str(folder/"classes")+":"+cp,"ExampleKt"]
            a=subprocess.run(command,cwd=cwd,input=entry.get("stdin",""),capture_output=True,text=True,timeout=10)
            b=subprocess.run(command,cwd=cwd,input=entry.get("stdin",""),capture_output=True,text=True,timeout=10)
        if a.returncode or b.returncode:return entry,None,(a.stderr+b.stderr)[-2000:]
        return entry,{"code":entry["code"],"output":a.stdout,"deterministic":a.stdout==b.stdout and not output_can_vary(entry["code"],a.stdout),"platform":"JVM","verified_version":"2.4.21","dependencies":entry.get("dependencies",[]),**{key:entry[key] for key in ("stdin","compiler_options","files") if key in entry}},None
    with ThreadPoolExecutor(max_workers=4) as pool:
        for entry,result,error in pool.map(execute,PROGRAMS):
            if error:
                failures[entry["keys"][0]]=error
            else:
                for key in entry["keys"]:
                    if key not in api_keys:continue
                    verified[key]=result
                    if entry.get("note_zh"):
                        explanations[key]={"zh":entry["note_zh"],"en":entry["note_en"]}
    destination.write_text(json.dumps(verified,ensure_ascii=False,indent=2)+"\n")
    text_path.write_text(json.dumps(explanations,ensure_ascii=False,indent=2)+"\n")
    (work/"failures.json").write_text(json.dumps(failures,ensure_ascii=False,indent=2)+"\n")
    print(f"Curated programs: {len(PROGRAMS)-len(failures)}/{len(PROGRAMS)} passed; {len(verified)} API mappings recorded.")
    for key,error in failures.items():print(key+": "+error[:1200])


if __name__=="__main__":
    run()
