Password-Strength Analyzer (CYB333 Final Project)

Command-line utility that scores a password from A (strongest) → D (weakest) using length, character-set variety, and simple entropy heuristics.
Built to demonstrate secure coding & security‑automation practices: packaging, unit tests with 100 % coverage, CLI entry‑point, and GitHub CI readiness.

1 · Quick start
    git clone https://github.com/Test-Monk3y/CYB333-Automation.git
    cd CYB333-Automation
    conda activate cyb333
    pip install -e .
    psa "Tr!ckyP@55!"

2 · Usage examples
    psa "S3cur3P@55!"          -> A
    type pwlist.txt | psa      -> grades each line
    from psa.strength import grade
    print(grade("hunter2"))    -> D

3 · How it works ✔︎
    Factor                         Points
    Base length (≥ 8)              +1
    Mixed upper/lower              +1
    Digits present                 +1
    Symbols (!@#$%…)               +1
    Entropy ≥ 50 bits              +1

    Total  Grade
      0‑1    D
        2    C
        3    B
      4‑5    A

4 · Project structure
    psa/               package code
      ├─ strength.py   scoring function
      └─ cli.py        argparse wrapper
    tests/             pytest suite
    htmlcov/           coverage HTML report
    dist/              wheel + sdist
    README‑midterm.md  archived Week‑6 readme

5 · Development & CI
    pip install -r requirements-dev.txt
    pytest -v
    coverage run -m pytest && coverage html
    python -m build --sdist --wheel
    git tag v0.0.0 && git push origin v0.0.0

6 · AI assistance
    OpenAI o3 used for scaffolding, heuristic refinement, and packaging fixes; all code reviewed and security‑checked.

License: MIT
