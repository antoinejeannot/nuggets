<p align="center">
  <img src="https://raw.githubusercontent.com/antoinejeannot/nuggets/main/.github/resources/logo.svg" alt="Nuggets" width="80" height="80">
</p>

Reference: [The Clean Code Talks - Global State and Singletons](https://www.youtube.com/watch?v=-FRm3VPhseI)

## Global State in Programming

Using global variables can create hard-to-detect bugs and make the system behavior unpredictable.
Changes in one part of the system can unintentionally affect other
parts, leading to a codebase that's challenging to debug and maintain.

```python
global_count = 0

def increment_global_count():
    global global_count
    global_count += 1

def get_global_count():
    return global_count

print(get_global_count())  # Output: 0
increment_global_count()
print(get_global_count())  # Output: 1
# skip tests
```

#### More details

- **Unpredictable Behavior:** Global state, often introduced
  through global variables or shared data, leads to
  unpredictability as changes in one part of the code can
  unintentionally affect other parts, causing unexpected behavior.

- **Challenging Debugging:** Debugging becomes difficult when
  global state is prevalent because tracing the origin of bugs and
  errors related to shared data can be complex and time-consuming.

- **Testing Complications:** The presence of global state
  complicates testing since it can be challenging to isolate and
  test individual components or functions that rely on shared data
  that is difficult to control during testing.

- **Scalability Limitations:** Global state can hinder the
  scalability of a software system, especially in multi-core or
  distributed environments, where managing shared data across
  threads or processes becomes problematic.

- **Collaboration Challenges:** Collaboration among developers
  can be hampered when global state is used extensively, as
  multiple team members may inadvertently impact shared data,
  leading to conflicts and coordination difficulties.

---

## singleton vs Singleton Pattern

### singleton (lowercase s)

Refers to the practice of using a single
instance of a class throughout the application. It's a pattern where
the class itself doesn't restrict instantiation, but the application
does so by convention.

```python
class DatabaseConnection:
    pass

database_connection = DatabaseConnection()
```

#### More details

- **Flexibility:** This approach offers flexibility in
  managing and using the single instance, allowing developers to
  choose how they enforce the singleton behavior within the
  application.

### Singleton (uppercase S)
This design pattern ensures that a class has only one instance and provides a global point of access to that instance. It's enforced by making the constructor private and controlling the instance creation within the class.

```python
class SingletonDatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
connection = SingletonDatabaseConnection()
```

#### More details

- **Global State**: The Singleton pattern introduces global
  state, potentially leading to tight coupling and reduced
  modularity in the codebase.

- **Testing Challenges**: Testing Singleton classes can be
  complex due to difficulties in substituting the Singleton
  instance for testing purposes.

- **Hidden Dependencies**: The pattern can hide class
  dependencies, making them harder to identify and manage
  explicitly.

- **Thread Safety Concerns**: Ensuring thread safety in
  Singleton instances can add complexity and affect performance in
  multi-threaded environments.

- **Resource Management**: Singleton instances can outlive
  their usefulness for resources with limited lifespans, requiring
  explicit management.

- **Global State Maintenance**: Managing global state through a
  Singleton can lead to complexity in understanding and debugging
  state changes.

---

## Deceptive APIs

These are APIs that conceal their dependencies,
making the system more complex and the code harder to test. They often
lead to unexpected behavior as the dependencies are not clear from the
interface.

```python
class PaymentProcessor:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def process(self, amount):
        print(f"Processing payment of {amount}")

class CreditCard:
    def charge(self, amount):
        processor = PaymentProcessor()
        processor.process(amount)

card = CreditCard()
card.charge(100)
```

#### More details

- **Hidden Dependencies:** Explores how deceptive APIs obscure their dependencies, making it difficult for developers to understand and test the system.

- **Testing and Maintainability Issues**: The concealment of dependencies within APIs leads to challenges in creating effective unit tests and maintaining the code, as the true dependencies of a component are not clear.

---

## Dependency Injection

This approach involves supplying objects
with their dependencies from the outside rather than hardcoding them
within the object. It leads to more testable, maintainable, and
modular code.

```python
class DatabaseConnection:
    pass

class UserRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

db = DatabaseConnection()
user_repo = UserRepository(db)
```

#### More details

- **External Dependency Supply**: objects receive their
  required dependencies from external sources, typically through
  constructor parameters or setter methods, rather than hardcoding
  those dependencies within the object itself.

- **Enhanced Testability**: DI facilitates improved testability
  because it allows for the injection of mock or test dependencies
  during testing, enabling isolated and controlled testing of
  individual components.

- **Enhanced Maintainability**: by decoupling an object from
  its dependencies and making those dependencies explicit, DI
  leads to more maintainable code, as changes to dependencies can
  be managed externally without modifying the object itself.

- **Modular Code**: DI encourages modularity by separating
  concerns, making it easier to swap out or update dependencies
  independently without affecting the overall functionality of the
  object or application.
