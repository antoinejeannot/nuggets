<p align="center">
  <img src="https://raw.githubusercontent.com/antoinejeannot/nuggets/main/.github/resources/logo.svg" alt="Nuggets" width="80" height="80">
</p>

Reference: [The Clean Code Talks - Don't Look For Things!](https://www.youtube.com/watch?v=RlfLCWKxHJ0)


## Testing Challenges

Complex constructors with direct
instantiation of objects or reliance on static initialization and
singletons make testing difficult.

```python
class Document:
    def __init__(self):
        self.html_client = HTMLClient()  # Direct instantiation

    def load_content(self, url):
        return self.html_client.fetch(url)

# Testing this requires setting up the HTMLClient and its dependencies
```

#### More details

- **Instantiation Complexity:** When constructors instantiate
  dependencies internally, it becomes challenging to isolate the
  class for unit testing. The dependencies create a tightly
  coupled system, leading to a need for extensive setup in test
  environments.

- **Singletons and Static States:** Use of singletons and
  static states further complicates testing as they introduce
  global states, making tests dependent on the order of
  execution and shared states.

- **Tightly Coupled Dependencies**: To test
  Document.load_content, we need to ensure that HTMLClient is
  properly initialized, which may involve setting up network
  connections or other configurations.

- **Uncontrolled External Interactions**: If HTMLClient makes
  actual network calls or interacts with external systems,
  testing Document could become unpredictable and reliant on
  external factors.

- **Inflexibility in Testing Scenarios**: Creating mock
  scenarios or testing specific edge cases becomes difficult, as
  HTMLClient's behavior is hardcoded within Document.

- **Increased Complexity in Test Setup**: The test setup must
  account for HTMLClient's initialization and behavior, leading
  to more complex and less focused tests for the Document class.

---

## Dependency Injection vs Direct Instantiation

Dependency injection enhances testability by allowing flexible substitution of dependencies.

```python
class HTMLClient:
    def fetch(self, url): # Complex logic to fetch data from a URL
        return f"Fetched content from {url}"

class Document:
    def __init__(self, html_client):
        self.html_client = html_client # Dependency injected

    def load_content(self, url):
        return self.html_client.fetch(url)

# With dependency injection, testing becomes easier
# Mock or substitute HTMLClient can be injected for testing purposes
```

#### More details

- **Service Locators:** While service locators can centralize
  object creation, they obscure a class's true dependencies,
  making the system more complex and harder to test.

- **Flexibility in Testing:** Dependency injection allows for
  the substitution of real dependencies with mock objects during
  testing. This flexibility makes it possible to test the
  behavior of the _Document_ class in isolation without relying
  on the actual implementation of _HTMLClient_.

- **Isolation of Components:** By injecting dependencies,
  each component can be tested independently. This isolation is
  crucial for unit testing, where the focus is on testing each
  part of the code in isolation from others.

- **Example of Mocking in Tests:** In a test scenario,
  _HTMLClient_ can be mocked to return a predefined response,
  enabling the tester to verify how _Document_ handles this
  response without having to deal with the complexities of the
  actual _HTMLClient_.

```python
class MockHTMLClient:
    def fetch(self, url):
        return "Mocked content"

# Create a mock HTMLClient for testing & inject mock_client into Document for testing
mock_client = MockHTMLClient()
test_document = Document(mock_client)
assert test_document.load_content("http://test.com") == "Mocked content"
```

- **Reduced Complexity:** Dependency injection reduces the
  complexity of setting up tests, as it eliminates the need to
  replicate the exact environment in which the dependencies
  operate, such as network configurations for _HTMLClient_.

---

## Exact Dependencies in Constructors

Constructors should explicitly ask for their dependencies, promoting clear and maintainable code.

```python
class Document:
    def content(self):
        return "Document content"

class Printer:
    def __init__(self, document):
        self.document = document  # Direct dependency

    def print(self):
        return f"Printing: {self.document.content()}"

# Clear and testable, as the dependency on Document is explicit
```

#### More details

- **Clarity and Maintainability:** Explicit dependencies in
  constructors make the code clearer by directly stating what
  objects are required for a class to function. This clarity
  leads to code that is easier to understand, maintain, and
  modify.

- **Simplified Testing:** When dependencies are explicit, it
  becomes easier to perform unit testing. Testers can provide
  specific implementations or mock objects for these
  dependencies, focusing on the behavior of the class being
  tested.

```python
class MockDocument:
    def content(self):
        return "Mock content"

# Inject a MockDocument into Printer for testing
mock_document = MockDocument()
printer = Printer(mock_document)
assert printer.print() == "Printing: Mock content"
```

- **Reduced Hidden Complexity:** Constructors that explicitly
  ask for dependencies avoid the hidden complexity that comes
  with object creation inside the class. This approach promotes
  a separation of concerns, where object creation and object
  logic are decoupled.

- **Enhanced Modularity:** Explicitly asking for dependencies
  makes classes more modular and reusable, as they don't make
  assumptions about how their dependencies are created or
  managed.

---

## Law of Demeter

Following this law reduces coupling by limiting an object's interactions to its immediate dependencies.

```python
# In practice:
class Door:
    def open(self):
        return "Door opened"

class House:
    def __init__(self, door):
        self.door = door # Interact only with the door

    def open_front_door(self):
        return self.door.open()
# The House class does not need to know about the details behind the Door class
```

#### More details

- **Reduced Coupling:** The Law of Demeter leads to reduced
  coupling in software designs. It encourages classes to
  interact only with immediate dependencies, rather than
  navigating through a chain of dependencies. This results in a
  looser coupling between components, enhancing modularity.

- **Enhanced Maintainability:** Adhering to this law makes
  classes less dependent on the internal structures or behaviors
  of their dependencies, leading to more maintainable code.
  Changes in one class are less likely to require changes in
  classes that depend on it.

```python
class Door:
    def __init__(self):
        self.lock_status = "Locked"

    def unlock(self):
        self.lock_status = "Unlocked"

    def open(self):
        if self.lock_status == "Unlocked":
            return "Door opened"
        return "Door is locked"

class House:
    def __init__(self, door):
        self.door = door

    def open_front_door(self):
        return self.door.open()

# Later, if changes are made to Door's internal structure
# House class remains unaffected as long as the 'open' method's interface is stable.
```

- **Simplified Testing:** Testing becomes simpler as each
  class needs to account only for its direct dependencies. This
  isolation aids in creating focused unit tests.

```python
class MockDoor:
    def open(self):
        return "Mock door opened"

# Testing House with a MockDoor
mock_door = MockDoor()
house = House(mock_door)
assert house.open_front_door() == "Mock door opened"
```

- **Clearer Interface Design:** By following the Law of
  Demeter, the interfaces between classes become clearer. Each
  class defines a clear and concise API for its collaborators,
  reducing the risk of unintended interactions.
