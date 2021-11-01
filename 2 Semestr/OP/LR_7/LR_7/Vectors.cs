﻿using System;
using System.Collections.Generic;
using System.Text;

namespace LR_7
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

    }
}
