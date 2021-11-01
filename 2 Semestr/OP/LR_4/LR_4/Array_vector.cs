using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LR_4
{
    class Array_vector : IVector
    {
        private double[] mas;
        public Array_vector(int n)
        {
            try
            {
                mas = new double[n];
            }
            catch (OverflowException)
            {
                Console.WriteLine("Длина вектора не может быть отрицательной, задан вектор с длинной равной модулю введеного числа");
                mas = new double[-n];
                Console.ReadKey();
            }
        }
        public Array_vector()
        {
            mas = new double[5];
        }
        public double this[int index]
        {
            get
            {
                try
                {
                    return mas[index];
                }
                catch (IndexOutOfRangeException)
                {
                    Console.WriteLine("Индекс выходит за пределы массива");
                    return 0;
                }
            }
            set
            {
                try
                {
                    mas[index] = value;
                }
                catch (IndexOutOfRangeException)
                {
                    Console.WriteLine("Индекс выходит за пределы массива");
                }
            }
        }
        public int Lenght
        {
            get
            {
                return mas.Length;
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
        public override string ToString()
        {
            string str = new string("");
            str += Convert.ToString(this.Lenght);
            str += " || ";
            for (int i = 0; i < Lenght; i++)
            {
                str += mas[i];
                str += " ";
            }
            return str;
        }
    }
}
