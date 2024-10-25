<h1 align="center">The Iterator pattern</h1>

## Identify the Iterator Pattern in C#

- **`IEnumerable`**: This interface provides a method `GetEnumerator()`, which returns an enumerator that iterates through a collection.
- **`IEnumerator`**: This interface has methods `MoveNext()`, `Reset()`, and a property `Current` to access elements one by one.

## Identify Which Types in C# are Iterable

- **Arrays**
- **Lists**
- **Dictionaries**
- **Sets**
- **Queues** and **Stacks**

## Implement a Small Code Example to Iterate Through an Aggregate Object

```csharp
using System;
using System.Collections;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        List<string> fruits = new List<string>() { "Apple", "Banana", "Cherry", "Date" };

        foreach (var fruit in fruits)
        {
            Console.WriteLine(fruit);
        }

        IEnumerable<string> enumerableFruits = fruits;
        IEnumerator<string> enumerator = enumerableFruits.GetEnumerator();

        Console.WriteLine("Using IEnumerator:");
        while (enumerator.MoveNext())
        {
            Console.WriteLine(enumerator.Current);
        }
    }
}
```
