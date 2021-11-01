using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LR_2
{
    class Array_vector
    {
        private double[] mas;
        public Array_vector(int n)
        {
            mas = new double[n];
        }
        public Array_vector()
        {
            mas = new double[5];
        }
        public double this[int index]
        {
            get
            {
                if ((0 < index) && (index <= mas.Length))
                {
                    return mas[index - 1];
                }
                else
                {
                    Console.WriteLine("Индекс выходит за пределы массива");
                    return 0;
                }
            }
            set
            {
                if ((0 < index) && (index <= mas.Length))
                {
                    mas[index - 1] = value;
                }
                else
                {
                    Console.WriteLine("Индекс выходит за пределы массива");
                }
            }
        }
        public void GetNorm()
        {
            double sum = 0;
            for (int i = 0; i < mas.Length; i++)
            {
                sum = sum + mas[i] * mas[i];
            }
            Console.WriteLine($"Модуль вектора равен {Math.Sqrt(sum)}");
        }
        public int Lenght
        {
            get
            {
                return mas.Length;
            }
        }
        public void inf()
        {
            for (int i = 0; i < Lenght; i++)
            {
                Console.Write(mas[i] + "  ");

            }
            Console.WriteLine();
        }
    }
}
