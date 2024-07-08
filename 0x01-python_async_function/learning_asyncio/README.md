# Async - Python
## REFERENCE

- https://realpython.com/async-io-python/

### Parallelism: 
Consists of performing multiple operation at the same time. **Multiprocessing** is a means to effect **Parallelism**, and it entails spreading task over a computer's central processing units (CPU's, or cores). Multiprocessing is well suited for CPU-bound tasks; tightly bound `for loops` and mathematical computations usually fall into this category.

### Concurrency:
This is slightly broader term than parallelism. It suggests that multiple tasks have the ability to run in an overlapping manner.

### Threading:
This involves concurrent execution model whereby multiple threads take turns executing tasks. One process can contain multiple threads.

Concurrency encompasses both multiprocessing (ideal for CPU-bound tasks) and threading (suited for IO-bound tasks). Multiprocessing is a form of parallelism, with parallelism being a specific type (subset) of concurrency.

So what does **asynchronous** mean:

- Asynchronous process creates a rountine which enables a task to be paused while **waiting** on their ultimate result, while waiting other tasks can be ran in the meantime.
- **Asynchronous code**, through the mechanism above, facilitates concurrent execution. Asynchronous code gives the impression of concurrency.

Here is an example for the reference article that better explains the concept.

> Chess master Judit Polgár hosts a chess exhibition in which she plays multiple amateur players. She has two ways of conducting the exhibition: synchronously and asynchronously.

Assumptions:

24 opponents
Judit makes each chess move in 5 seconds
Opponents each take 55 seconds to make a move
Games average 30 pair-moves (60 moves total)
Synchronous version: Judit plays one game at a time, never two at the same time, until the game is complete. Each game takes (55 + 5) * 30 == 1800 seconds, or 30 minutes. The entire exhibition takes 24 * 30 == 720 minutes, or 12 hours.

Asynchronous version: Judit moves from table to table, making one move at each table. She leaves the table and lets the opponent make their next move during the wait time. One move on all 24 games takes Judit 24 * 5 == 120 seconds, or 2 minutes. The entire exhibition is now cut down to 120 * 30 == 3600 seconds, or just 1 hour.

