@startuml
actor "Оператор крану" as CraneOperator
actor "Працівник майданчику" as SiteWorker
actor "Метеорологічна служба" as WeatherService

usecase "Виявлення ризиків через несприятливі погодні умови" as RiskDetection
usecase "Альтернативний план дій при несприятливих погодних умовах" as AltActionPlan
usecase "Моніторинг погодних умов для безпеки на майданчику" as WeatherMonitoring
usecase "Альтернативний моніторинг погодних умов" as AltMonitoring

CraneOperator -- RiskDetection
CraneOperator -- AltActionPlan
SiteWorker -- RiskDetection
SiteWorker -- AltActionPlan
WeatherService -- WeatherMonitoring
WeatherService -- AltMonitoring
@enduml

