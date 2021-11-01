using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LR_1
{
    class Vectors
    {
        public static Array_vector Sum(Array_vector a1, Array_vector a2)
        {
            if (a1.n == a2.n)
            {
                Array_vector a3 = new Array_vector(a1.n);
                a3.n = a1.n;
                for (int i = 0; i < a1.n; i++)
                {
                    a3.mas[i] = a1.mas[i] + a2.mas[i];
                }
                return a3;
            }
            else
            {
                Console.WriteLine("действие невозможно выполнить");
                Array_vector a3 = new Array_vector(1);
                return a3;
            }

        }
        public static double Scalar(Array_vector a1, Array_vector a2)
        {
            if (a1.n == a2.n)
            {
                double sum = 0;
                for (int i = 0; i < a1.n; i++)
                {
                    sum += a1.mas[i] * a2.mas[i];
                }
                double sum2 = 0;
                double sum3 = 0;
                for (int i = 0; i < a1.n; i++)
                {
                    sum2 = sum2 + a1.mas[i] * a1.mas[i];
                    sum3 = sum3 + a1.mas[i] * a1.mas[i];
                }
                return Math.Abs(sum) / (Math.Sqrt(sum2) * Math.Sqrt(sum3));
            }
            else
            {
                Console.WriteLine("действие невозможно выполнить");
                return 0;
            }

        }
        public static Array_vector NumberMul(Array_vector a1, double d)
        {
            Array_vector a2 = a1;
            for (int i = 0; i < a1.n; i++)
            {
                a2.mas[i] *= d;
            }
            return a2;
        }
        public static double GetNorm(Array_vector a1)
        {
            double sum = 0;
            for (int i = 0; i < a1.n; i++)
            {
                sum = sum + a1.mas[i] * a1.mas[i];
            }
            return Math.Sqrt(sum);
        }

    }
}
