# 🐍 Python Study

A structured, self-paced Python curriculum built from the **[Net Ninja Python Playlist](https://www.youtube.com/playlist?list=PL4cUxeGkcC9idu6GZ8EU_5B6WpKTdYZbK)** and **[Python Crash Course (3rd Edition)](https://nostarch.com/python-crash-course-3rd-edition)** by Eric Matthes — from absolute beginner (`print("Hello, World!")`) to API design.

## Repo Structure

```text
python-study/
├── CURRICULUM/          29 numbered modules, 01_hello_python → 23_virtual_envs_in_practice
│   └── README.md        module index
├── quests/              13 practice quests in 5 tiers:
│   ├── 01_absolute_beginner/   q01–q05
│   ├── 02_beginner/            q06–q07
│   ├── 03_intermediate/        q08–q09
│   ├── 04_advanced/            q10–q11
│   └── 05_challenges/          q12–q13
├── DOCKER/              Docker learning path, basics → expert (7 levels)
├── DSA/                 data structures & algorithms track
├── OOP/                 object-oriented programming track
├── TYPE-CONVERSION/     conversion notes + practice
├── RESOURCES/           cheatsheets, book notes, links, common mistakes
├── answers/             worked exercise answers
├── python-quest/        additional question/answer sets
├── tryout/  random/     scratch experiments
```

## Quest Format

Every quest folder follows the same contract:

1. `instructions.md` — description, expected output, constraints, hints, and a collapsible solution.
2. `solution.py` — runnable reference implementation.

Work the quest from `instructions.md` first; only open the collapsible solution when stuck.

## How to Use This Repo

1. Start at `CURRICULUM/README.md` and work the numbered modules in order.
2. After each tier of modules, attempt the matching quest tier in `quests/`.
3. Track the DSA and OOP tracks in parallel once you're comfortable with basics.
4. Use `RESOURCES/python_cheatsheet.md` and `common_mistakes.md` for quick reference.

## Sources

1. [Net Ninja Python Playlist](https://www.youtube.com/playlist?list=PL4cUxeGkcC9idu6GZ8EU_5B6WpKTdYZbK) — basics, data types, control flow, functions, file I/O, modules.
2. [Python Crash Course 3e](https://nostarch.com/python-crash-course-3rd-edition) by Eric Matthes — variables, lists, dicts, classes, testing, files, projects.
3. [Official PCC Source Code](https://github.com/ehmatnes/pcc_3e) — free companion code for every chapter.
