# 12-Week Aggressive Engineering Acceleration Plan (Windows-First, Two-Project Track)

## Summary
This plan is optimized for long-term elite engineering capability, not short-term GPA.  
It uses a `6+1` cycle (6 high-output days, Sunday full recovery), `Windows-first` systems work, `balanced` algorithm training (contest + interview style), and `two focused low-level projects` that force memory, performance, and systems thinking.

Core outcomes by Week 12:
1. C++ moves from basic to strong intermediate/early advanced (RAII, STL depth, memory, concurrency, profiling).
2. You can design and implement non-trivial systems with correctness + performance constraints.
3. You ship two portfolio projects with benchmarks, tests, and technical writeups.
4. You build a repeatable growth system you can run again for the next 3-6 months.

## 1) Weekly Training Schedule (With Intensity Distribution)

### Weekly rhythm
- Work days: Monday-Saturday, `6h/day` outside lectures (`36h/week`).
- Recovery day: Sunday (no coding; optional 30-45 min weekly review only).
- Intensity split: `24h high-intensity` (new implementation/problem-solving) + `12h medium-intensity` (reading, debugging, review).

### Daily block template
| Block | Duration | Intensity | Purpose |
|---|---:|---|---|
| A | 2h | High | Hard implementation (C++ internals / project core) |
| B | 2h | High | Algorithms or systems build |
| C | 1h | Medium | Deep reading + notes (DB/network/perf internals) |
| D | 1h | Medium | Debugging/profiling/retrieval review |

### Day-by-day focus map
| Day | Block A | Block B | Block C | Block D |
|---|---|---|---|---|
| Monday | C++ mastery | DS implementation | DB course reinforcement | Spaced recall + bug log |
| Tuesday | Algorithms timed set | Project sprint | Networking fundamentals | Solution review |
| Wednesday | Project deep build | Project deep build | DB internals lab | Performance notes |
| Thursday | Memory/performance | Networking coding lab | DLD linkage concepts | Refactor + tests |
| Friday | Algorithms mixed set | Project integration | Datacom reinforcement | Benchmark run |
| Saturday | Virtual contest (2h) | Weekly project milestone | Profiling session | Weekly retrospective |

### Lecture-anchor rule
- On heavy lecture days (Mon/Tue/Fri): do Blocks A+B before first lecture, Block C between lecture windows, Block D after final lecture.
- On Wednesday/Saturday: run A+B in prime cognitive hours (morning), C+D later.

### Phase intensity distribution across 12 weeks
| Phase | Weeks | C++/Systems Core | Algorithms | DB Internals | Networking/Perf | Projects |
|---|---|---:|---:|---:|---:|---:|
| Foundation | 1-4 | 14h/wk | 8h/wk | 6h/wk | 4h/wk | 4h/wk |
| Build | 5-8 | 10h/wk | 7h/wk | 7h/wk | 5h/wk | 7h/wk |
| Integration | 9-12 | 7h/wk | 6h/wk | 4h/wk | 5h/wk | 14h/wk |

## 2) Cognitive Load Management Strategy (12-Week Sustainment)

### Load architecture
| Week | Target Load | Intent |
|---|---:|---|
| 1 | 32h | Ramp and baseline |
| 2 | 36h | Full load |
| 3 | 36h | Full load |
| 4 | 26h | Deload + consolidation |
| 5 | 32h | Exam-adjusted build |
| 6 | 30h | Exam-adjusted build |
| 7 | 36h | Peak build |
| 8 | 26h | Deload + cleanup |
| 9 | 36h | Peak integration |
| 10 | 36h | Peak integration |
| 11 | 36h | Peak integration |
| 12 | 30h | Benchmark + packaging + reflection |

### Non-negotiable sustainment rules
1. Sleep: 7.5-8.5h nightly; two nights below 6.5h triggers automatic next-day intensity reduction.
2. Active recovery: 30-45 min walk/strength daily.
3. No-context-switch protocol: one objective per block, no multitasking, no passive tutorial bingeing.
4. Weekly review on Sunday: score metrics, diagnose bottlenecks, adjust next week.
5. Autoregulation trigger: if 2 consecutive days show poor output (less than 70% planned completion), cut next 48h high-intensity volume by 40%.

## 3) Progressive C++ Mastery Roadmap (Week-by-Week Ramp)

| Week | C++ Focus | Mandatory Output | Gate Test |
|---|---|---|---|
| 1 | Toolchain, RAII, value semantics | CMake project + tests + RAII exercises | 90% pass on 40 unit tests |
| 2 | OOP done correctly, Rule of 0/5 | `UniquePtr`-like type + polymorphism exercise | No leaks under sanitizer |
| 3 | STL deep use (containers/iterators/algorithms) | Same task solved via STL + complexity notes | Explain complexity tradeoffs clearly |
| 4 | Templates + generic programming | `RingBuffer<T>` with iterator support | Works for 3 value types |
| 5 | Memory layout, alignment, allocators | Pool allocator + benchmark vs `new/delete` | Measurable allocation improvement |
| 6 | Hash table internals | Open-addressing hash map from scratch | Randomized correctness tests pass |
| 7 | Trees + invariants | B+tree node/page model implementation | Invariant checks pass under fuzz inputs |
| 8 | Concurrency basics | Thread pool + producer/consumer queue | Data-race free under stress tests |
| 9 | Socket programming in C++ | Winsock client/server baseline | Handles concurrent clients reliably |
| 10 | Profiling + optimization workflow | Baseline/optimized benchmark report | >=30% improvement on hotspot |
| 11 | Design patterns in modern C++ | Refactor project modules (strategy/state/pimpl where needed) | Coupling reduced, tests still green |
| 12 | Hardening | Sanitizer-clean build + final docs | Release candidate tagged |

## 4) Deep-Dive Recommendations

### Database internals
1. Query planning first: use `EXPLAIN` weekly to connect SQL to execution plans.
2. Index internals second: prioritize B-tree and hash behavior before exotic indexes.
3. Concurrency and correctness: MVCC + transaction isolation anomalies.
4. Recovery mechanics: WAL/rollback journal and crash-recovery invariants.
5. File/page layout: study SQLite page format and map to your storage-engine project.

Inference from current PostgreSQL docs: start with B-tree, planner literacy, and transaction semantics before advanced index families.

### Networking fundamentals
1. TCP fundamentals from RFC 9293: states, retransmission, flow/congestion basics.
2. HTTP semantics from RFC 9110 for protocol correctness.
3. Hands-on path: blocking server -> non-blocking server -> load testing -> backpressure/timeouts.
4. Windows-first implementation using Winsock APIs; keep protocol binary and explicit.

### Memory and performance engineering
1. Measurement discipline: benchmark before any optimization.
2. Tool chain: Google Benchmark + Visual Studio Profiler/WPR-WPA + AddressSanitizer.
3. CPU-aware coding: cache locality, allocation frequency, branch behavior, false sharing.
4. Optimization loop: measure -> hypothesis -> change -> validate -> document.

## 5) ML Decision
**Decision: Delayed completely for this 12-week cycle.**

Justification:
1. Your bottleneck is systems depth, not model-building exposure.
2. ML now would fragment scarce high-focus cycles and slow compounding in C++/systems.
3. Strong systems fundamentals make future ML engineering work far stronger (inference performance, infra, reliability).

## 6) Project Roadmap (Forcing Low-Level Thinking)

### Project 1 (Weeks 3-8): `PageStore` Embedded Storage Engine
Scope:
1. Fixed-size page format + slotted page.
2. B+tree index over key-value records.
3. Write-ahead log + recovery on restart.
4. Minimal transaction API (`begin/commit/rollback`, single-writer, multi-reader).
5. CLI and benchmark harness.

Definition of done:
1. 100 randomized operation-sequence tests pass.
2. Crash-recovery test loop (forced process kill) restores consistency.
3. Benchmark report includes throughput and p95 latency.

### Project 2 (Weeks 8-12): `WirePulse` High-Concurrency Server + Load Generator
Scope:
1. Custom binary protocol parser/serializer.
2. Multi-client server (Winsock), connection lifecycle management.
3. Thread pool + bounded queue + backpressure.
4. Timeouts/retries/error handling + metrics logging.
5. Companion load generator for reproducible benchmarking.

Definition of done:
1. Stable 60-minute soak test without crashes/leaks.
2. Handles malformed packet corpus safely.
3. Optimized version shows >=2x throughput or >=35% latency reduction vs baseline.

## 7) Objective Performance Metrics (Real Growth, Not Vanity)

| Metric | Week 1 Baseline | Week 12 Target |
|---|---|---|
| Timed C++ implementation | Implement tested DS in 150 min | Same quality in 75-90 min |
| Algorithm throughput | 4 solved/week (mixed) | 8 solved/week with written postmortems |
| Contest performance | 0-1 virtual contests/week | 2 virtual contests/week, stable solves under time pressure |
| Memory safety | Frequent hidden issues | 0 sanitizer findings on release branch |
| Project reliability | Ad-hoc manual checks | Deterministic test suites + soak/crash tests |
| Performance engineering | Qualitative “feels faster” | Quantified benchmark deltas with reports |
| Abstraction ability | Code-first, little design | Weekly design notes with explicit tradeoff decisions |

## 8) Common Failure Patterns (High-Discipline Students) and Controls
1. Overloading every day at max intensity; control with scheduled deload weeks.
2. Mistaking time spent for skill gain; control with hard output gates each week.
3. Tutorial dependence; control with build-first/read-second rule.
4. Ignoring debugging depth; control with mandatory bug journal and root-cause writeups.
5. Premature optimization; control with benchmark-before-change policy.
6. Project bloat; control with strict “definition of done” and frozen scope after Week 6.
7. No recovery discipline; control with Sunday off and sleep triggers.
8. Metric gaming; control with mixed metrics (speed + correctness + explanation quality).

## Important Interfaces / APIs / Types

### Project interfaces to implement
1. `PageStore` API:
   - `put(key, value) -> Status`
   - `get(key) -> optional<value>`
   - `del(key) -> Status`
   - `begin_txn() -> TxnId`
   - `commit(txn_id) -> Status`
   - `rollback(txn_id) -> Status`
2. `WirePulse` protocol types:
   - `Request { id:uint32, op:uint16, len:uint32, payload:bytes }`
   - `Response { id:uint32, status:uint16, len:uint32, payload:bytes }`

### Training system interfaces
1. Daily log schema: `planned_blocks`, `completed_blocks`, `failures`, `next_action`.
2. Weekly scorecard schema: `implementation_speed`, `algo_results`, `perf_delta`, `reliability`, `notes`.

## Test Cases and Scenarios

### Project 1 tests
1. Randomized put/get/delete with reference-model comparison.
2. Crash during write then restart recovery.
3. Transaction rollback correctness under concurrent readers.
4. Corrupted log/page header handling.

### Project 2 tests
1. Concurrent client stress test (ramp load + soak).
2. Slow-consumer and backpressure behavior.
3. Malformed/partial packet parser safety.
4. Timeout and retry behavior under packet loss simulation.

### Growth process tests
1. Weekly timed implementation drill.
2. Weekly virtual contest.
3. End-of-phase checkpoint demos (Weeks 4, 8, 12).

## Assumptions and Defaults Chosen
1. You can sustain 6h/day outside lectures for 6 days/week.
2. Sunday is a full recovery day.
3. Moderate exam pressure around Weeks 5-6.
4. Windows-first development environment.
5. Two focused systems projects (not one flagship).
6. Balanced algorithm style (contest + interview).
7. ML postponed for this cycle.

## Primary References (Current, Technical Sources)
1. C++ Core Guidelines: https://github.com/isocpp/CppCoreGuidelines  
2. C++ reference: https://en.cppreference.com/w/cpp  
3. PostgreSQL Index Types (v18 current docs): https://www.postgresql.org/docs/current/indexes-types.html  
4. PostgreSQL `EXPLAIN`: https://www.postgresql.org/docs/current/using-explain.html  
5. PostgreSQL MVCC intro: https://www.postgresql.org/docs/current/mvcc-intro.html  
6. PostgreSQL Transaction Isolation: https://www.postgresql.org/docs/current/transaction-iso.html  
7. SQLite file format and WAL internals: https://www.sqlite.org/fileformat.html  
8. TCP specification (RFC 9293): https://www.rfc-editor.org/rfc/rfc9293  
9. HTTP semantics (RFC 9110): https://www.rfc-editor.org/rfc/rfc9110  
10. Winsock overview: https://learn.microsoft.com/en-us/windows/win32/winsock/windows-sockets-start-page-2  
11. Windows Performance Toolkit (WPR/WPA): https://learn.microsoft.com/en-us/windows-hardware/test/wpt/  
12. MSVC AddressSanitizer example docs: https://learn.microsoft.com/en-us/cpp/sanitizers/error-heap-buffer-overflow?view=msvc-170  
13. Codeforces EDU courses: https://codeforces.com/edu/courses  
14. CMU 15-445/645 DB Systems (Spring 2026): https://15445.courses.cs.cmu.edu/
