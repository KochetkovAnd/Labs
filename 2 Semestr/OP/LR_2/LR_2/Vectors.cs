using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LR_2
{
    class Vectors
    {
        public static Array_vector Sum(Array_vector a1, Array_vector a2)
        {
            if (a1.Lenght == a2.Lenght)
            {
                Array_vector a3 = new Array_vector(a1.Lenght);
                for (int i = 0; i < a1.Lenght; i++)
                {
                    a3[i + 1] = a2[i + 1] + a1[i + 1];

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
        public static double Scalar(Array_vector a1, Array_vector a2)
        {
            if (a1.Lenght == a2.Lenght)
            {
                double sum = 0;
                for (int i = 0; i < a1.Lenght; i++)
                {
                    sum += a1[i + 1] * a2[i + 1];
                }
                double sum2 = 0;
                double sum3 = 0;
                for (int i = 0; i < a1.Lenght; i++)
                {
                    sum2 = sum2 + a1[i + 1] * a1[i + 1];
                    sum3 = sum3 + a1[i + 1] * a1[i + 1];
                }
                return (Math.Abs(sum) / (Math.Sqrt(sum2) * Math.Sqrt(sum3)));
            }
            else
            {
                Console.WriteLine("действие невозможно выполнить");
                return 0;
            }

        }
        public static double GetNorm(Array_vector a1)
        {
            double sum = 0;
            for (int i = 0; i < a1.Lenght; i++)
            {
                sum = sum + a1[i + 1] * a1[i + 1];
            }
            return Math.Sqrt(sum);
        }
    }
}
