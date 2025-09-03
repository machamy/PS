using System;



public class Program
{
    public static void Main(string[] args)
    {
        int n = int.Parse(Console.ReadLine());
        Tuple<int, int>[] arr = new Tuple<int, int>[n];


        for (int i = 0; i < n; i++)
        {
            string[] inputs = Console.ReadLine().Split();
            int d = int.Parse(inputs[0]);
            int t = int.Parse(inputs[1]);
            arr[i] = new Tuple<int, int>(d, t);
        }
        /*
        arr = d,t
        t에 대하여 내림차순 정렬
        d에 대하여 오름차순 정렬

        뒤 날짜부터 채워 넣기
        */
        int current = 1_000_000_001;
        Array.Sort(arr, (a, b) =>
        {
            if (b.Item2 == a.Item2)
                return a.Item1.CompareTo(b.Item1);
            return b.Item2.CompareTo(a.Item2);
        });
        for (int i = 0; i < n; i++)
        {
            int d = arr[i].Item1;
            int t = arr[i].Item2;
            current = Math.Min(current, t) - d;
        }

        Console.WriteLine(current);
    }
}