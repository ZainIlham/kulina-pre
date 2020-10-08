## Basic Concept
1. Coding
    - Code Smell

    Alternative classes with different interfaces usually happens in a large projects. The problem is that there are two or more classes perform identical functions but have different method names. The programmer who created one of these classes probably didn't know that a functionally equivalent class already existed. To make sure that this problem doesn't occur, the programmer need to put the interface of classes in terms of a common denominator such as rename the methods to make them identical in all alternative classes.

    - Dependency Injection

    When class A uses some functionality of class B, then its said that class A has a dependency of class B. Dependency injection is used to make dependency changes in a class easier. We do not need to make a whole new class if there are any changes to a dependency. There are three types of dependecy injection such as constructor injection, setter injection, and interface injection. Dependency injection helps to enable loose coupling and extending the application becomes easier.

2. Rest API
    - POST

    Do use POST whenever something need to be changed. Post is used for writing data and submits data to the identified resource like databases. 

    - GET

    Do use GET whenever something need to be show, without changing it. Don't ever use GET to alter state. GET can be used for things like calculations.

    In conclusion, GET is used to retrieve remote data, and POST is used to insert/update remote data.
