@startuml
class Context {
    - state: State
    + setState(s: State)
    + request()
    + transitionTo(s: State)
}

interface State {
    + handle()
    + nextState() : State
}

class ConcreteStateA {
    + handle()
    + nextState() : State
}

class ConcreteStateB {
    + handle()
    + nextState() : State
}

class ConcreteStateC {
    + handle()
    + nextState() : State
}

Context --> State : uses
State <|-- ConcreteStateA
State <|-- ConcreteStateB
State <|-- ConcreteStateC

ConcreteStateA --> ConcreteStateB : transitions to
ConcreteStateB --> ConcreteStateC : transitions to
ConcreteStateC --> ConcreteStateA : transitions to

@enduml

