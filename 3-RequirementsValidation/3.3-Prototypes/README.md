@startuml
skinparam backgroundColor #f0f0f0
skinparam handwritten false
skinparam rectangle {
    BackgroundColor #d9eaf7
    BorderColor #4a90e2
}

title Горизонтальний прототип системи моніторингу ризиків

package "Збір даних" {
    rectangle "Система моніторингу" as Monitoring
    rectangle "Збір даних про погодні умови" as WeatherData
    rectangle "Оновлення даних щосекунди" as DataUpdate
    rectangle "Сповіщення про небезпечні умови" as Alert

    Monitoring --> WeatherData
    WeatherData --> DataUpdate
    DataUpdate --> Alert
}

package "Аналіз ризиків" {
    rectangle "Аналіз ризиків" as RiskAnalysis
    rectangle "Визначення небезпеки перекидання" as RiskAssessment
    rectangle "Сповіщення працівників" as UserNotification

    RiskAnalysis --> RiskAssessment
    RiskAssessment --> UserNotification
}

package "Історія подій" {
    rectangle "Історія подій" as EventHistory
    rectangle "Зберігання даних" as DataStorage

    EventHistory --> DataStorage
}

note right of WeatherData
    Система збирає дані про погодні умови в реальному часі
end note

note right of Alert
    Система сповіщає про небезпечні умови для працівників
end note

note right of RiskAnalysis
    Система аналізує ризики перекидання крана
end note

note right of DataStorage
    Система зберігає всі події для подальшого аналізу
end note

@enduml

