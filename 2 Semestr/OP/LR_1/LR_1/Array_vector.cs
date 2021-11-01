using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LR_1
{
    class Array_vector
    {
        public int n;
        public double[] mas;
        public Array_vector(int n)
        {
            this.n = n;
            mas = new double[n];
        }
        public Array_vector()
        {
            n = 5;
            mas = new double[5];
        }
        public void SetElement(int m, double c)
        {
            mas[m - 1] = c;
        }
        public void GetElement(int m)
        {
            Console.WriteLine($"Элемент массива номер {m} равен {mas[m]} ");
        }
        public void GetNorm()
        {
            double sum = 0;
            for (int i = 0; i < n; i++)
            {
                sum = sum + mas[i] * mas[i];
            }
            Console.WriteLine($"Модуль вектора равен {Math.Sqrt(sum)}");
        }
        public void inf()
        {
            for (int i = 0; i < n; i++)
            {
                Console.Write(mas[i] + "  ");

            }
            Console.WriteLine();
        }
        public void vvod()
        {
            for (int i = 0; i < n; i++)
            {


            }
        }
        public void SumPositivesFromChetIndex()
        {
            double sum = 0;
            for (int i = 1; i < n; i = i + 2)
            {
                if (mas[i] > 0)
                {
                    sum += mas[i];
                }
            }
            Console.WriteLine($"сумма всех положительных элементов массива с четными номерами = {sum}");
        }
        public void SumLessFromNechetIndex()
        {
            double sum = 0;
            for (int i = 0; i < n; i++)
            {
                sum += Math.Abs(mas[i]);
            }
            double avr = sum / n;
            sum = 0;
            for (int i = 0; i < n; i = i + 2)
            {
                if (mas[i] < avr)
                {
                    sum += mas[i];
                }
            }
            Console.WriteLine($"сумма элементов массива, которые имеют нечетные номера и  одновременно меньше среднего значения всех модулей элементов массива  {sum}");
        }
        public void MulChet()
        {
            double sum = 0;
            for (int i = 1; i < n; i = i + 2)
            {
                if (mas[i] > 0)
                {
                    sum *= mas[i];
                }
            }
            Console.WriteLine($"Метод подсчета произведения всех четных положительных элементов = {sum}");
        }
        public void MulNechet()
        {
            double sum = 0;
            for (int i = 0; i < n; i = i + 2)
            {
                if ((mas[i] % 3) != 0)
                {
                    sum *= mas[i];
                }
            }
            Console.WriteLine($"Метод подсчета произведения всех нечетных элементов, не делящихся на три = {sum}");
        }
        public void SortUp()
        {
            for (int i = 0; i < n - 1; i++)
            {
                for (int j = i + 1; j < n; j++)
                {
                    if (mas[i] > mas[j])
                    {
                        double c = mas[i];
                        mas[i] = mas[j];
                        mas[j] = c;
                    }
                }
            }
        }
        public void SortDown()
        {
            for (int i = 0; i < n - 1; i++)
            {
                for (int j = i + 1; j < n; j++)
                {
                    if (mas[i] < mas[j])
                    {
                        double c = mas[i];
                        mas[i] = mas[j];
                        mas[j] = c;
                    }
                }
            }
        }
    }
}
