using System;
using System.Collections.Generic;
using System.Threading;

class TrafficSimulation
{
    static void Main(string[] args)
    {
        RegularTraffic();
    }

    static void RegularTraffic()
    {
        string[] lanes = { "l1", "l2", "l3", "l4" };
        var signals = new Dictionary<string, string>
        {
            { "l1", "red" },
            { "l2", "red" },
            { "l3", "red" },
            { "l4", "red" }
        };

        int greenIndex = 0;

        // initialize list to hold cars
        List<Car> cars = new List<Car>();

        while (true) // this will create an infinite loop until stopped
        {
            // updating traffic light state
            UpdateTrafficLight(signals, greenIndex);

            // move cars and handle intersection logic
            MoveCars(cars, signals, lanes, greenIndex);

            // print traffic state
            PrintTrafficState(signals, cars);

            Thread.Sleep(1000); // delay for simulation speed
        }
    }

    static void UpdateTrafficLight(Dictionary<string, string> signals, int greenIndex)
    {
        foreach (var lane in signals.Keys)
        {
            signals[lane] = "red"; // set all lights to red initially
        }
        signals["l" + (greenIndex + 1)] = "green"; // set the light in the current green lane to green
    }

    static void MoveCars(List<Car> cars, Dictionary<string, string> signals, string[] lanes, int greenIndex)
    {
        foreach (var car in cars)
        {
            if (car.CurrentLane != $"l{greenIndex + 1}" || signals[car.CurrentLane] == "red" || car.DistanceFromLight < 0)
            {
                // car needs to stop or can't move to intersection yet
                car.Stop();
            }
            else
            {
                // car can move forward or switch lanes at the intersection
                car.MoveForward();
                if (car.DistanceFromLight == 0 && signals[car.CurrentLane] != "red")
                {
                    // car reached intersection and the light is not red, allow it to switch lanes
                    car.SwitchLane(lanes, greenIndex);
                }
            }
        }
    }

    static void PrintTrafficState(Dictionary<string, string> signals, List<Car> cars)
    {
        Console.WriteLine("Traffic State:");
        foreach (var kvp in signals)
        {
            string lane = kvp.Key;
            string signal = kvp.Value;

            Console.WriteLine($"Lane {lane} - Signal: {signal}");
        }
        Console.WriteLine();

        Console.WriteLine("Cars:");
        foreach (var car in cars)
        {
            Console.WriteLine($"Car - Lane: {car.CurrentLane}, Distance from Light: {car.DistanceFromLight}");
        }
        Console.WriteLine();
    }
}

class Car
{
    public string CurrentLane { get; set; }
    public int DistanceFromLight { get; set; }

    public Car(string lane)
    {
        CurrentLane = lane;
        DistanceFromLight = 10; // Initial distance from traffic light
    }

    public void MoveForward()
    {
        DistanceFromLight--;
    }

    public void Stop()
    {
        // Car stops, no movement
    }

    public void SwitchLane(string[] lanes, int greenIndex)
    {
        Random rand = new Random();
        int randomLaneIndex = rand.Next(0, lanes.Length);
        while (lanes[randomLaneIndex] == CurrentLane || randomLaneIndex == greenIndex)
        {
            // Choose a random lane other than the current lane and the green lane
            randomLaneIndex = rand.Next(0, lanes.Length);
        }
        CurrentLane = lanes[randomLaneIndex];
    }
}
