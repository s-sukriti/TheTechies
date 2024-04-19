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

        while (true)
        {
            for (int i = 0; i < lanes.Length; i++)
            {
                string currentLane = lanes[i];
                if (i == greenIndex)
                {
                    signals[currentLane] = "green";
                }
                else
                {
                    signals[currentLane] = "red";
                }
            }

            foreach (var lane in lanes)
            {
                Console.WriteLine($"{lane} : {signals[lane]}");
            }

            Thread.Sleep(30000); // 30 seconds delay

            greenIndex = (greenIndex + 1) % lanes.Length; // move to the next lane for green light
        }
    }

    static void EmergencyTraffic()
    {
        // logic for emergency vehicle situation for later
    }
}
