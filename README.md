# hello_agent

学习型工作区，分离日常测试代码与正式项目代码。

## 目录结构

```text
hello_agent/
├─ demo_test/                # 平时测试/练习代码
│  ├─ python_basics/         # Python 基础语法、标准库练习
│  ├─ framework_sandbox/     # 第三方库/框架试验
│  └─ tmp_playground/        # 临时实验代码
├─ projects/                 # 正式项目代码（可多个）
│  ├─ project_01/
│  ├─ project_02/
│  └─ shared_lib/
├─ .vscode/
│  ├─ settings.json
│  ├─ extensions.json
│  └─ launch.json
├─ .gitignore
└─ README.md
```

## Python 环境

默认开发环境：`conda` 下的 `agent_base`。

首次使用建议：

```powershell
conda activate agent_base
python --version
```

> 如果你的 Conda 安装路径不是默认路径，请在 `.vscode/settings.json` 中调整 `python.defaultInterpreterPath`。

## 使用建议

- 把零散学习/验证代码放到 `demo_test/`。
- 把可长期维护的业务代码放到 `projects/`。
- 每个新项目建议在 `projects/` 下单独建目录，并放自己的 `README.md` 与依赖文件。
"# hello_agent" 
