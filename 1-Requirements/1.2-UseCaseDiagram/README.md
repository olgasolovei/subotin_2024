@startuml
left to right direction

actor "Метеорологічна служба" as Meteorology
actor "Керівник безпеки" as SafetyManager
actor "Оператор крана" as Operator
actor "Працівники майданчика" as Workers

usecase "Моніторинг погодних умов" as MonitorWeather
usecase "Передати попередження" as SendAlert
usecase "Отримати попередження про погіршення погоди" as WeatherAlert
usecase "Припинити роботу та зафіксувати кран" as StopWork
usecase "Інформувати керівника безпеки" as InformSafetyManager
usecase "Евакуюватися з майданчика" as Evacuate
usecase "Очікувати інструкцій" as AwaitInstructions
usecase "Координувати дії під час небезпеки" as CoordinateActions

Meteorology --> MonitorWeather
Meteorology --> SendAlert
SendAlert --> WeatherAlert 

WeatherAlert --> Operator 
WeatherAlert --> Workers 
WeatherAlert --> SafetyManager

Operator --> StopWork
Operator --> InformSafetyManager
InformSafetyManager --> SafetyManager

Workers --> Evacuate
Workers --> AwaitInstructions

SafetyManager --> CoordinateActions

@enduml

