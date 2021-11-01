using System;
using System.Collections.Generic;
using System.Text;
using System.Net.Sockets;
using System.IO;

namespace LR_6
{
    class Vectors
    {
        public static IVector Sum( IVector a1, IVector a2)
        {
            if (a1.Lenght == a2.Lenght)
            {
                Array_vector a3 = new Array_vector(a1.Lenght);
                for (int i = 0; i < a1.Lenght; i++)
                {
                    a3[i] = a2[i] + a1[i];

                }
                return a3;
            }
            else
            {
                Console.WriteLine("действие невозможно выполнить из-за разности длин");
                Array_vector a3 = new Array_vector(1);
                return a3;
            }
        }
        public static double Scalar(IVector a1, IVector a2)
        {
            if (a1.Lenght == a2.Lenght)
            {
                double sum = 0;
                for (int i = 0; i < a1.Lenght; i++)
                {
                    sum += a1[i ] * a2[i];
                }
                double sum2 = 0;
                double sum3 = 0;
                for (int i = 0; i < a1.Lenght; i++)
                {
                    sum2 = sum2 + a1[i ] * a1[i ];
                    sum3 = sum3 + a1[i] * a1[i];
                }
                return (Math.Abs(sum) / (Math.Sqrt(sum2) * Math.Sqrt(sum3)));
            }
            else
            {
                Console.WriteLine("действие невозможно выполнить");
                return 0;
            }

        }
        public static double GetNorm(IVector a1)
        {
            double sum = 0;
            for (int i = 0; i < a1.Lenght; i++)
            {
                sum = sum + a1[i ] * a1[i];
            }
            return Math.Sqrt(sum);
        }
        public static IVector Fmin(IVector[] mas)
        {
            IVector min=mas[0];
            for(int i = 0; i < mas.Length; i++)
            {
                mas[0].GetNorm().CompareTo(mas[1].GetNorm());
            }
            return min;
        }
        public static void OutputVector(IVector v, Stream output)
        {
            output.WriteByte(Convert.ToByte(v.Lenght + 48));
            for (int i = 0; i < v.Lenght; i++)
            {
                output.WriteByte(Convert.ToByte(v[i] + 48));
            }
        }
        public static IVector InputVector(Stream input)
        {
            int n =(input.ReadByte()-48);
            IVector h = new Array_vector(n);
            for (int i = 0; i < n; i++)
            {
                h[i] = (input.ReadByte()-48);
            }
            return h;            
        }
        public static void WriteVector(IVector v, TextWriter output)
        {
            output.WriteLine(v);
        }
        public static IVector ReadVector(TextReader input)
        {
            
            string str = input.ReadLine();
            string[] subs = str.Split(" ");
            IVector ar = new Array_vector(Convert.ToInt32(subs[0]));
            for(int i = 0; i < ar.Lenght; i++)
            {
                ar[i] = Convert.ToDouble(subs[i + 1]);
            }
            return ar;
        }        
    }
}
