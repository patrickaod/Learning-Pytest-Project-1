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

The original FreeCodeCamp Blackjack project is a simple terminal-based game intended to teach Python fundamentals through a practical example. While effective for beginners, the implementation introduces several architectural limitations from a software engineering perspective.

The application is tightly coupled to the terminal, with core logic directly dependent on `input()` and `print()` calls. Although this simplifies the learning experience, it prevents the game logic from being reused independently of the CLI and limits extensibility for alternative interfaces such as web or mobile applications.

A key issue is the lack of separation between business logic and presentation. Game rules, control flow, and user interaction are handled within the same execution path, creating strong coupling between components. As the project grows, this increases maintenance complexity and raises the risk of unintended side effects when modifying behaviour.

The design also blurs class responsibilities. The `Game` class manages orchestration, rule evaluation, and user interaction, while the Hand class combines state management with display formatting. This violates the Single Responsibility Principle and reduces the modularity of the system.

Because runtime I/O is embedded directly into core methods, automated testing becomes more difficult. Logic cannot be tested cleanly in isolation, often requiring output-capturing workarounds or manual verification instead of straightforward unit tests.

Finally, the game loop follows a monolithic structure in which most behaviour is concentrated in a single procedural flow. While suitable for demonstrating foundational programming concepts, this approach becomes harder to extend, debug, and refactor compared to a layered or modular architecture with clearly separated responsibilities.

Overall, the project succeeds as an educational introduction to Python, but it does not reflect the design principles typically associated with production-grade software systems.

### Refactored Architecture (Before → After)
The project has been progressively refactored from a tightly coupled tutorial implementation into a modular, testable, object-oriented system. The goal of this transformation was to align the codebase more closely with real-world software engineering practices.

**Key Refactor Changes From Phases 1-3**

* Separated game logic from input/output (removed logic tied to `print()` and `input()`)
* Refactored functions to return values instead of producing direct side effects
* Clarified class responsibilities:

  * `Hand` handles card state and scoring only
  * `Deck` handles card creation and dealing
  * `Game` handles game flow orchestration only
* Removed mixed responsibilities within single methods (improved Single Responsibility Principle adherence)
* Reduced side effects in core methods to improve testability
* Introduced modular game phases (deal → player turn → dealer turn → result evaluation)
* Replaced monolithic game loop structure with clearer staged flow
* Introduced automated testing using Pytest for core components
* Enabled unit testing by isolating business logic from terminal I/O
* Improved overall code readability, maintainability, and extensibility

The project has now been significantly refactored from its original tutorial-based structure into a more modular and testable application. Core game logic has been separated from input and output, responsibilities have been clarified across the main classes, and the overall game flow has been broken into clearer stages. This has addressed many of the original issues around tight coupling, side effects in core methods, and a lack of separation of concerns.

As a result, the codebase is now much closer to a production-style structure, with improved maintainability, readability, and automated test coverage. The remaining gaps mainly relate to further isolating the game loop from terminal interaction and continuing to refine the architecture for potential expansion into other interfaces such as a web or API-based front end.
