# Preconditions.kt

参数检查、状态检查和不可达分支处理。本文覆盖 **kotlin-stdlib 2.4.21** 中此文件的全部 **5 组函数、9 个重载**。

| API | 用途 | 失败时异常 | 返回值 |
| --- | --- | --- | --- |
| [`require`](../api/kotlin/require--c4d0cf24.md) | 检查参数条件 | `IllegalArgumentException` | `Unit` |
| [`requireNotNull`](../api/kotlin/requirenotnull--506b0c8f.md) | 检查参数非空 | `IllegalArgumentException` | `T` |
| [`check`](../api/kotlin/check--20f65c28.md) | 检查对象或程序状态 | `IllegalStateException` | `Unit` |
| [`checkNotNull`](../api/kotlin/checknotnull--25a38b02.md) | 检查表示状态的值非空 | `IllegalStateException` | `T` |
| [`error`](../api/kotlin/error--ca00fccf.md) | 立即抛出状态异常 | `IllegalStateException` | `Nothing` |

## 默认消息

| API | 消息 |
| --- | --- |
| `require` | `Failed requirement.` |
| `check` | `Check failed.` |
| `requireNotNull` / `checkNotNull` | `Required value was null.` |

## 使用时注意

- 参数不合法使用 `require` / `requireNotNull`；状态不合法使用 `check` / `checkNotNull`。
- 带 `lazyMessage` 的重载只在失败时计算消息，可避免在成功路径执行字符串拼接等工作。
- 非空检查的契约支持符合条件的变量进行智能转换。
- `error` 的返回类型是 `Nothing`，适合放在 `when` 的失败分支或 Elvis 表达式中。
- 上表各 API 的独立页面都提供不依赖测试库的完整程序，直接打印正常结果与异常信息，输出已用 2.4.21 校验。

[Preconditions.kt · v2.4.21](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Preconditions.kt)
