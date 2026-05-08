# Zero to Hero - FreeCodeCamp Tutorial to Full Deployment
This project begins with the [FreeCodeCamp Python Tutorial for Beginners](https://www.youtube.com/watch?v=eWRfhZUzrAc) and evolves it from a single‑file “god function” into a fully modular, object‑oriented, production‑ready application.

My goal is to use this simple starting point as a springboard to explore real‑world full‑stack concepts — including Docker, AWS / Azure deployment, Pytest, and a React front end.

This repository documents my journey from fundamentals to full deployment, capturing what I learn as I refactor, test, containerise, and eventually deploy the application to the cloud.

## Description
This project takes the original FreeCodeCamp Python tutorial and transforms it into a fully modular, object‑oriented application while placing a strong emphasis on unit testing at every stage of development.

As the application evolves, I will introduce pytest to validate each component — from basic functions to API routes, containerised services, and eventually cloud‑deployed infrastructure. Testing is not an afterthought here; it is the core practice guiding architecture, refactoring, and deployment decisions.

The goal is to build a complete end‑to‑end project while developing strong habits around maintainability, testability, and continuous integration.

### Objectives

  - Refactor the original tutorial code into a modular, object‑oriented structure

  - Introduce automated testing with Pytest

  - Containerize the application using Docker

  - Deploy to AWS or Azure

  - Build a simple React front end

  - Document the entire learning process

## Project Overview (Original Codebase)

The original FreeCodeCamp Blackjack project is a simple terminal-based game designed to teach Python fundamentals through a working example. While effective for beginners, the initial implementation introduces several architectural limitations from a software engineering perspective.

The game is tightly coupled to the terminal, with core logic directly dependent on 'input()' and 'print()' statements. This makes the system easy to follow in a learning context, but prevents reuse of the logic outside a CLI environment and limits extensibility for web or mobile applications.

Because business logic and presentation are combined, the codebase becomes difficult to scale. Any attempt to extend functionality risks introducing tightly coupled dependencies, often leading to “spaghetti code” structures where changes in one area unintentionally affect others. This also makes automated testing more difficult, as core behaviour is not isolated from runtime I/O.

The original design also lacks clear separation of responsibilities between classes:

The 'Game' class handles control flow, user interaction, and rule evaluation
The 'Hand' class manages card state, scoring, and display formatting

This violates the Single Responsibility Principle, making the system harder to maintain, test, and modify safely.

Additionally, heavy reliance on print-based output introduces side effects into core methods. While this is common in beginner projects, it reduces testability and forces reliance on workarounds such as 'capsys' or manual testing rather than pure unit tests.

Finally, the monolithic structure of the game loop concentrates all logic into a single execution flow. This makes the system harder to extend, debug, and refactor compared to a modular or layered architecture where responsibilities are clearly separated.

While this approach is appropriate for learning core programming concepts, it does not reflect production-grade software design practices.
