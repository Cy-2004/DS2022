# Scripting with Python and Bash

This module covers Bash and Python scripting. In the lab you will be using the [uv](https://docs.astral.sh/uv/) package manager for isolated Python environments; the tutorial below prepares you for that.

## Setup

For the Python examples in this module (and for [Lab 03](https://github.com/ksiller/lab-03-scripting)), you need **Python 3** and **[uv](https://docs.astral.sh/uv/)** on your computer.

**Confirm that both are installed.** Open a terminal (on Windows, use a WSL bash terminal, not PowerShell):

```bash
which python3
python3 -V
```

The path should look like `/usr/bin/python3` (or similar). Prefer **Python 3.11 or newer**.

```bash
uv --version
```

If `uv --version` fails, install `uv` from the official docs: [Installing uv](https://docs.astral.sh/uv/getting-started/installation/). On macOS or Linux you can run:

```bash
curl -LsSf https://astral.sh/uv/install.sh -o uv-installer.sh
sh uv-installer.sh
```

After installing, close and reopen the terminal (or run `source ~/.bashrc` / `source ~/.zshrc`), then confirm with `uv --version` again.

Work in `~/ds2022-fall-26` for the hands-on steps below. Do **not** nest a new Git repository inside this course repository unless you are intentionally creating a separate practice folder outside it.

## Managing Python environments with `uv`

### Why isolate environments?

Different projects often need different versions of the same package (library). Historically, the `pip install` command has been widely used to install Python packages. The problem is that one global `pip install` cannot satisfy every project at once.

Here is a realistic clash between **two packages that do not depend on each other**, but that both require the shared library `protobuf` with **non-overlapping** version ranges:

- **`dbt-core`** — runs analytics transformations (dbt models) against a data warehouse.
- **`google-cloud-pubsub`** — publish and subscribe to messages on Google Cloud Pub/Sub.

**Try this conflict** (it should fail — that is the point):

```bash
python3 -m pip install dbt-core==1.7.14 google-cloud-pubsub==2.40.0
```

You should see a resolver error similar to:

```text
ERROR: Cannot install dbt-core==1.7.14 and google-cloud-pubsub==2.40.0 because these package versions have conflicting dependencies.

The conflict is caused by:
    dbt-core 1.7.14 depends on protobuf<5 and >=4.0.0
    google-cloud-pubsub 2.40.0 depends on protobuf<8.0.0 and >=6.33.5
```

Neither package lists the other as a dependency. Both need `protobuf`, but one requires version 4.x and the other requires 6.x — no single version can satisfy both. The clean solution is **separate environments**: one project gets `dbt-core`, another gets `google-cloud-pubsub`. `uv` creates and manages those environments for you.

### Core ideas

| Piece | Role |
| --- | --- |
| `.venv/` | Local virtual environment (installed packages live here). **Do not commit it.** |
| `pyproject.toml` | Declares your project and its dependencies (what you want). |
| `uv.lock` | Pins the exact versions `uv` resolved (what you got). Makes installs reproducible. |
| `.python-version` | Records which Python version this project expects. |

Typical workflow: 
1. edit dependencies with `uv add` / `uv rm`. 
2. That triggers `uv` to update `pyproject.toml` and `uv.lock`
3. execute `uv sync` to (re)create or update `.venv` 
4. run code with `uv run`.

### Hands-on: a tiny `uv` project

Create a practice folder:

```bash
mkdir -p ~/ds2022-fall-26/uv-practice
cd ~/ds2022-fall-26/uv-practice
```

#### 1. `uv init`

```bash
uv init --name hello-uv --description "Practice project for uv"
```

Inspect what appeared:

```bash
ls -la
cat pyproject.toml
cat .python-version
```

You should see `pyproject.toml`, `.python-version`, and usually a small starter layout. Open the `pyproject.toml` file and notice that the `dependencies` entry starts empty.

#### 2. `uv add`

Let's add a package.
```bash
uv add requests
```

Check:

- `pyproject.toml` — `requests` is listed under dependencies
- `uv.lock` — exact version (and transitive deps) are pinned
- `.venv/` — packages were installed into an isolated environment

```bash
ls .venv
grep -A2 dependencies pyproject.toml # or open pyproject.toml file in editor
```

#### 3. `uv run`

Run Python **through** the project environment (no need to `source .venv/bin/activate` first):

```bash
uv run python -c "import requests; print(requests.__version__)"
```

Or start an interactive shell in that environment:

```bash
uv run python
```

#### 4. `uv rm`

```bash
uv rm requests
uv run python -c "import requests"
```

The last command should fail: `requests` is gone from the project env. `pyproject.toml` and `uv.lock` were updated for you.

Add it back for the next steps:

```bash
uv add requests
```

#### 5. `uv sync`

`uv sync` installs whatever `pyproject.toml` + `uv.lock` describe into `.venv`. Use it when you clone a project that already has those files, or after pulling lockfile changes:

```bash
uv sync
```

On a fresh machine (or HPC), you typically clone the repo, then `uv sync` or `uv run ...` (which can sync as needed) — you do **not** copy `.venv` between computers.

#### 6. Relationship: `pyproject.toml` and `uv.lock`

- **`pyproject.toml`** — human-oriented declaration (`requests` without spelling every sub-dependency).
- **`uv.lock`** — machine-oriented snapshot of the full resolved tree.

Both belong in Git. Together they let someone else recreate the same environment with `uv sync`.

### Using a `requirements.txt` with `uv`

If you already have a classic requirements file:

```bash
echo "requests>=2.31.0" > requirements.txt
uv add -r requirements.txt
```

That imports those packages into the `uv` project (`pyproject.toml` / `uv.lock`). You can still keep `requirements.txt` for documentation, but the source of truth for a `uv` project is `pyproject.toml` + `uv.lock`.

To export a lock-compatible requirements-style list for tools that only understand that format:

```bash
uv export --no-dev -o requirements-locked.txt
```

(Optional; Lab 03 focuses on `pyproject.toml` / `uv.lock`.)

### Advanced: one-off packages with `uv run --with`

Sometimes you want a tool for a single command without adding it to the project:

```bash
uv run --with rich python -c "from rich import print; print('[bold green]hello[/]')"
```

`rich` is available for that run; it is **not** added to `pyproject.toml` unless you later `uv add rich`. Handy for quick experiments; prefer `uv add` for real project dependencies.

### Version control

**Commit:**

- `pyproject.toml`
- `uv.lock`
- `.python-version`
- `.gitignore` (include `.venv/`)

**Do not commit:**

- `.venv/` (recreate with `uv sync` / `uv run`)

**Do not hand-edit:**

- `uv.lock` (let `uv add`, `uv rm`, and `uv sync` maintain it)
- Prefer changing dependencies with `uv add` / `uv rm` instead of hand-editing `pyproject.toml` dependency lists (avoids lockfile drift)

Quick `.gitignore` line:

```bash
echo ".venv/" >> .gitignore
```

## Scripting Best Practices

All scripts should adhere to [coding best practices](../../best-practices.md). Specifically, they should be written in a way that takes into account several factors:

1. Use the shebang / make the script executable
2. Error out gracefully --> set -e / error codes --> || exit 1;
3. Use input parameters
4. Conditional logic
5. Environment / full paths / env variables
6. Logging
7. Use comments

## bash

### shebang
A well-formatted `bash` script begins with a "shebang" line:
```
#!/bin/bash
```
that points to the full path of the `bash` shell. This may differ from one environment
to the next.

To make any bit of code executable, use `chmod 755` against it.

### Use full paths

Any binary executables used in a shell script should be invoked using their full
paths. This is to avoid any ambiguity and preempt any errors of a shell not being
able to find the command.

For example, when invoking the `aws` command-line in a script you would normally call
```
/usr/local/bin/aws
```
To determine the full path of an executable in a given system, use the `which` command:
```
which aws
```

### Graceful Errors

Near the top of most `bash` scripts, put:

```bash
set -euo pipefail
```

- `-e` — stop the script as soon as any command fails. Continuing past an error can produce bad results or unintended side effects.
- `-u` — stop if the script uses a variable that was never set (typos and missing arguments show up immediately).
- `-o pipefail` — a pipeline fails if **any** command in it fails. Without this, only the last command's exit status counts, so an early failure can be hidden.

See `strict-mode.sh` for a short example. Try:

```bash
chmod 755 strict-mode.sh
./strict-mode.sh /etc/hosts
./strict-mode.sh no-such-file.txt
```

Another option is a conditional so that when a specific line fails, the script `exit`s with a non-zero code. That can be useful when debugging.

### Sleep

If you need a deliberate pause in the middle of a script, simply `sleep 5` for a 5-second
pause, etc. This may be especially useful in the midst of `try` logic.

### Input parameters

Remember that `$0`, `$1`, `$2`, etc. are reserved parameters `bash` understands as positional
arguments when invoking from the command-line:

- `$0` is the invoking script itself
- `$1` is the first parameter after the script name
- `$2` is the second parameter ...
- . . .

`positional-args.sh`
```
#!/bin/bash

echo "$0 <-- invoking script"
echo "$1 <-- first parameter"
echo "$2 <-- second parameter"
```
returns the following output:

```
$ ./positional-args.sh bananas blueberries

./positional-args.sh <-- invoking script
bananas <-- first parameter
blueberries <-- second parameter
```


### If/Else conditional logic

Start your `if` with a comparison, end with `fi`.

```bash
if [[ $VAR -gt 10 ]]
then
  echo "That number is greater than 10."
else
  echo "Your number is pretty small!"
  exit 0;
fi
```

### Loops

Start with for, define a do loop, end with done

```bash
names=("alice" "bob" "carol")
for name in "${names[@]}"; do
    echo "Name: $name"
done
```

### Environment

`env` gives you all environment variables for your session. This may vary
for an unattended script (without you around).

Add environment variables in `bash`:
```
export VARIABLE=value-of-variable
```

Use full paths to your binaries to avoid your unattended script being unable
to locate a binary. Just because you can run it by hand does not mean it can
run without you around.

### Storing a command's output in a variable

```bash
# general format
VAR=$(command_to_execute)
```

Example
```bash
TODAY=$(date)
echo $TODAY
```
Executes the date command and stores its output in a variable TODAY. Then echo the content of $TODAY to the terminal.

You are not restricted to a single command. You can also insert a pipeline of commands inside $( ).

### Logging

A simple-yet-valuable step in your scripting is to log. You can log every action
taken by the script, or limit logging to successes or failures.

A common format for logging might be a snippet like this:

```
# First establish the datetime:
NOW=$(date +"%m-%d-%Y-%H:%M:%SEDT")
echo $DATE " OK - Successfully processed " $FILENAME >> /var/log/output.log
```
The result would be a single file building with each row as it is logged.
Note the `>>` to append to a file instead of overwriting it!

### Comment

One of the most useful habits you can develop as a programmer is adding comments
to your code. This explains each chunk of code but might also justify why a particular
choice has been made. This will be invaluable to you, when you come back to the code
two years later, or when your code is shared with others.

Comments start with a `#`; all characters following the `#` on that line are ignored. Here's an example demonstrating good commenting practice:
```bash
#!/bin/bash
# This script greets a user by name
# Usage: ./greet.sh <name>

# Exit immediately if any command fails
set -e

# Check if a name was provided as an argument
if [ $# -eq 0 ]; then
    echo "Error: Please provide a name"
    exit 1
fi

# Store the first argument in a variable
NAME=$1

# Display a personalized greeting
echo "Hello, $NAME! Welcome to bash scripting."
```

## Python3

Scripting in `python` is fairly similar, but it has many a lot more functionality in 
terms of libraries, classes, functions, etc. A few things to note:

- Unlike `bash` it is not as easy to pass `$1`, `$2` parameters in the command-line.
[Refer to this](https://stackabuse.com/command-line-arguments-in-python/) for a basic tutorial.
- Python can invoke shell scripts in other languages.
- Python has many better options for conditional logic, error handling, and logging.
- Whereas `bash` and other low-level tools (`grep`, `sed`, `awk`, `tr`, `perl`, etc.) can parse 
plain-text "flat" files fairly efficiently, Python can ingest a data file and load it 
into memory for much more complex transformations. A library like `pandas` can use 
dataframes like a staging database for you to query, scan, count, etc. [Here's a great
tutorial](https://www.kaggle.com/sohier/tutorial-accessing-data-with-pandas) on Kaggle.

>**Note:** Review [coding best practices](../../best-practices.md).

## Resources

[[Watch] Bash Scripting Tutorial](https://www.youtube.com/watch?v=tK9Oc6AEnR4)
[Linux Config: Bash Scripting Tutorial](https://linuxconfig.org/bash-scripting-tutorial)