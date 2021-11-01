using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LR_1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Введите размерность 1-ого вектора = ");
            int n1 = Convert.ToInt32(Console.ReadLine());
            Array_vector vek1 = new Array_vector(n1);
            Console.Write("Введите размерность 2-ого вектора = ");
            int n2 = Convert.ToInt32(Console.ReadLine());
            Array_vector vek2 = new Array_vector(n2);
            Console.Clear();
            bool key = true;
            while (key == true)
            {
                Console.WriteLine("================================================================================");
                Console.Write("Вектор №1    "); vek1.inf();
                Console.WriteLine("================================================================================");
                Console.Write("Вектор №2    "); vek2.inf();
                Console.WriteLine("================================================================================");
                Console.WriteLine("Для сложения двух векторов нажмите (1) ");
                Console.WriteLine("Для скалярного произведения двух векторов нажмите (2) ");
                Console.WriteLine("Для умножения 1-ого вектора на число нажмите (3)  ");
                Console.WriteLine("Для умножения 1-ого вектора на число нажмите (4)  ");
                Console.WriteLine("Для получения модуля 1-ого вектора нажмите (5) ");
                Console.WriteLine("Для получения модуля 2-ого вектора нажмите (6)  ");
                Console.WriteLine("Для изменения значений 1-ого вектора нажмите (7) ");
                Console.WriteLine("Для изменения значений 2-ого вектора нажмите (8) ");
                Console.WriteLine("Для выхода нажмите любую другую кнопку ");
                Console.WriteLine("================================================================================");
                string menu = Console.ReadLine();
                Console.WriteLine("================================================================================");
                switch (menu)
                {
                    case "1":
                        Array_vector q1 = Vectors.Sum(vek1, vek2);
                        Console.Write("Получившийся вектор   ");
                        q1.inf();
                        break;
                    case "2":
                        double q2 = Vectors.Scalar(vek1, vek2);
                        Console.Write("Скалярное произведение = " + q2);
                        break;
                    case "3":
                        Console.WriteLine("Введите число на которое надо умножить вектор");
                        double qq3 = Convert.ToDouble(Console.ReadLine());
                        Array_vector q3 = Vectors.NumberMul(vek1, qq3);
                        Console.Write("Получившийся вектор   ");
                        q3.inf();
                        break;
                    case "4":
                        Console.WriteLine("Введите число на которое надо умножить вектор");
                        double qq4 = Convert.ToDouble(Console.ReadLine());
                        Array_vector q4 = Vectors.NumberMul(vek2, qq4);
                        Console.Write("Получившийся вектор   ");
                        q4.inf();
                        break;
                    case "5":
                        Console.WriteLine($"Модуль первого вектора равен {Vectors.GetNorm(vek1)}");
                        break;
                    case "6":
                        Console.WriteLine($"Модуль первого вектора равен {Vectors.GetNorm(vek2)}");
                        break;
                    case "7":
                        Console.WriteLine("Введите номер изменяемого элемента ");
                        int w = Convert.ToInt32(Console.ReadLine());
                        Console.WriteLine("Введите значения на которое необходимо заменить ");
                        double w2 = Convert.ToDouble(Console.ReadLine());
                        vek1.SetElement(w, w2);
                        break;
                    case "8":
                        Console.WriteLine("Введите номер изменяемого элемента ");
                        int l = Convert.ToInt32(Console.ReadLine());
                        Console.WriteLine("Введите значения на которое необходимо заменить ");
                        double l2 = Convert.ToDouble(Console.ReadLine());
                        vek2.SetElement(l, l2);
                        break;
                    default:
                        key = false;
                        break;
                }
                Console.ReadKey();
                Console.Clear();
            }

        }
    }
}