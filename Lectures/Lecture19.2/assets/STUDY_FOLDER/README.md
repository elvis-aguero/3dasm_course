# The supercompressible study folder

What an agentic run is given, and what it writes. Five files.

| file | what it is |
|---|---|
| `PROBLEM_STATEMENT.md` | The real brief the campaign ran under, 666 lines. The only required input. |
| `PROBLEM_STATEMENT_SUMMARIZED.md` | The same brief in one page. **Read this one first.** |
| `config.yaml` | 26 lines: which model runs which node, the wall-clock budget, where the evaluator lives. |
| `data_generator.py` | The f3dasm evaluator, **written by the agent during the run**. Trimmed from 3,966 lines. |
| `oracle_circular.py` | The reference oracle for Bessa's circular family: one call, two Abaqus stages. Trimmed from 353. |

The two `.py` files are real code with marked elisions, not rewrites, so the shape and the
comments are the authors' own.

Provenance: `bessagroup/f3dasm-agentic-benchmarks`, `supercompressible-material/`.
