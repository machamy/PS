
using System;

public static class SeasonsOfMemories
{
    const int YEAR = 2015;
    const int MONTH = 1;
    const int DAY = 16;


    public static void Main()
    {
        string[] input = Console.ReadLine().Split();

        int year = int.Parse(input[0]);
        int month = int.Parse(input[1]);
        int day = int.Parse(input[2]);

        int ans = 1;

        ans += (year - 2015) * 4;
        switch (month)
        {
            case 1:
            case 2:
                ans += 0;
                break;
            case 3:
            case 4:
            case 5:
                ans += 1;
                break;
            case 6:
            case 7:
            case 8:
                ans += 2;
                break;
            case 9:
            case 10:
            case 11:
                ans += 3;
                break;
            case 12:
                ans += 4;
                break;
        }

        Console.WriteLine(ans);
    }
}