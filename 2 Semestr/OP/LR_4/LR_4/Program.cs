using System;

namespace LR_4
{
    class Program
    {
        static void Main(string[] args)
        {
            bool key1 = true;
            while (key1 == true)
            {
                Console.WriteLine("=================================================================================================");
                Console.WriteLine("Выполнил ученик гр 6115 Кочетков А.В.");
                Console.WriteLine("=================================================================================================");
                Console.WriteLine("Для проверки реализции класса ArrayVector         нажмите 1");
                Console.WriteLine("Для проверки реализции класса LinkedListVector    нажмите 2");
                Console.WriteLine("Для проверки реализции класса Vectors             нажмите 3");
                Console.WriteLine("Для выхода из программы                           нажмите 4");
                Console.WriteLine("=================================================================================================");
                string case1 = Console.ReadLine();
                switch (case1)
                {
                    case "1":
                        Console.Clear();
                        Console.Write("Введите размерность  вектора = ");
                        int n1 = Convert.ToInt32(Console.ReadLine());
                        Array_vector vek1 = new Array_vector(n1);
                        Console.Clear();
                        bool key2 = true;
                        while (key2 == true)
                        {
                            Console.WriteLine("=================================================================================================");
                            Console.Write("Вектор     "); Console.WriteLine(vek1);
                            Console.WriteLine("=================================================================================================");
                            Console.WriteLine("Для получения модуля  вектора                      нажмите 1 ");
                            Console.WriteLine("Для изменения значений  вектора                    нажмите 2 ");
                            Console.WriteLine("Свойство для чтения количества координат вектора   нажмите 3 ");
                            Console.WriteLine("Для выхода в верхнее меню                          нажмите 4 ");
                            Console.WriteLine("=================================================================================================");
                            string case2 = Console.ReadLine();
                            switch (case2)
                            {
                                case "1":
                                    vek1.GetNorm();
                                    break;
                                case "2":
                                    Console.WriteLine("Введите номер изменяемого элемента");
                                    int ns1 = Convert.ToInt32(Console.ReadLine());
                                    Console.WriteLine("Введите значение на которое необходимо заменить");
                                    double zs1 = Convert.ToDouble(Console.ReadLine());
                                    vek1[ns1 - 1] = zs1;
                                    break;
                                case "3":
                                    Console.WriteLine("Количество координат вектора равно " + vek1.Lenght);
                                    break;
                                case "4":
                                    key2 = false;
                                    break;
                                default:
                                    Console.WriteLine("Введеной функции нет повторите");
                                    break;

                            }
                            Console.ReadKey();
                            Console.Clear();
                        }
                        break;
                    case "2":
                        Console.Clear();
                        Console.Write("Введите размерность списка = ");
                        int n2 = Convert.ToInt32(Console.ReadLine());
                        LinkedListVector list1 = new LinkedListVector(n2);
                        Console.Clear();
                        bool key3 = true;
                        while (key3 == true)
                        {
                            Console.WriteLine("=================================================================================================");
                            Console.Write("Список     "); Console.WriteLine(list1);
                            Console.WriteLine("=================================================================================================");
                            Console.WriteLine("Для получения модуля  списка                       нажмите 1 ");
                            Console.WriteLine("Для изменения значений  списка                     нажмите 2 ");
                            Console.WriteLine("Свойство для чтения количества координат вектора   нажмите 3 ");
                            Console.WriteLine("Для выхода в верхнее меню                          нажмите 4 ");
                            Console.WriteLine("=================================================================================================");
                            string case3 = Console.ReadLine();
                            switch (case3)
                            {
                                case "1":
                                    list1.GetNorm();
                                    break;
                                case "2":
                                    Console.WriteLine("Введите номер изменяемого элемента");
                                    int ns1 = Convert.ToInt32(Console.ReadLine());
                                    Console.WriteLine("Введите значение на которое необходимо заменить");
                                    double zs1 = Convert.ToDouble(Console.ReadLine());
                                    list1[ns1 - 1] = zs1;
                                    break;
                                case "3":
                                    Console.WriteLine("Количество координат вектора равно " + list1.Lenght);
                                    break;
                                case "4":
                                    key3 = false;
                                    break;
                                default:
                                    Console.WriteLine("Введеной функции нет повторите");
                                    Console.ReadKey();
                                    Console.Clear();
                                    break;
                            }
                            Console.ReadKey();
                            Console.Clear();
                        }
                        break;
                    case "3":
                        Console.Clear();
                        Console.Write("Введите размерность 1-ого вектора = ");
                        int n3 = Convert.ToInt32(Console.ReadLine());
                        Array_vector vek3 = new Array_vector(n3);
                        Console.Write("Введите размерность 2-ого вектора = ");
                        int n4 = Convert.ToInt32(Console.ReadLine());
                        Array_vector vek4 = new Array_vector(n4);
                        Console.Clear();
                        bool key4 = true;
                        while (key4 == true)
                        {
                            Console.WriteLine("================================================================================");
                            Console.Write("Вектор №1    "); Console.WriteLine(vek3);
                            Console.WriteLine("================================================================================");
                            Console.Write("Вектор №2    "); Console.WriteLine(vek4);
                            Console.WriteLine("================================================================================");
                            Console.WriteLine("Для сложения двух векторов                  нажмите 1 ");
                            Console.WriteLine("Для скалярного произведения двух векторов   нажмите 2 ");
                            Console.WriteLine("Для изменения значений  1 ого вектора       нажмите 3 ");
                            Console.WriteLine("Для изменения значений  2 ого вектора       нажмите 4 ");
                            Console.WriteLine("Для получения модуля 1-ого вектора          нажмите 5");
                            Console.WriteLine("Для получения модуля 2-ого вектора          нажмите 6");
                            Console.WriteLine("Для выхода в верхнее меню                   нажмите 7");
                            Console.WriteLine("================================================================================");
                            string case4 = Console.ReadLine();
                            Console.WriteLine("================================================================================");
                            switch (case4)
                            {
                                case "1":
                                    IVector q1 = Vectors.Sum(vek3, vek4);
                                    Console.Write("Получившийся вектор   ");
                                    Console.WriteLine(q1);
                                    break;
                                case "2":
                                    double q2 = Vectors.Scalar(vek3, vek4);
                                    Console.Write("Скалярное произведение = " + q2);
                                    break;
                                case "3":
                                    Console.WriteLine("Введите номер изменяемого элемента");
                                    int ns1 = Convert.ToInt32(Console.ReadLine());
                                    Console.WriteLine("Введите значение на которое необходимо заменить");
                                    double zs1 = Convert.ToDouble(Console.ReadLine());
                                    vek3[ns1 - 1] = zs1;
                                    break;
                                case "4":
                                    Console.WriteLine("Введите номер изменяемого элемента");
                                    int ns2 = Convert.ToInt32(Console.ReadLine());
                                    Console.WriteLine("Введите значение на которое необходимо заменить");
                                    double zs2 = Convert.ToDouble(Console.ReadLine());
                                    vek4[ns2 - 1] = zs2;
                                    break;
                                case "5":
                                    Console.WriteLine($"Модуль первого вектора равен {Vectors.GetNorm(vek3)}");
                                    break;
                                case "6":
                                    Console.WriteLine($"Модуль второго вектора равен {Vectors.GetNorm(vek4)}");
                                    break;
                                case "7":
                                    key4 = false;
                                    break;
                                default:
                                    Console.WriteLine("Введеной функции нет повторите");
                                    break;
                            }
                            Console.ReadKey();
                            Console.Clear();
                        }
                        break;
                    case "4":
                        key1 = false;
                        break;
                    default:
                        Console.WriteLine("Введеной функции нет повторите");
                        Console.ReadKey();
                        Console.Clear();
                        break;
                }
            }
        }
    }
}
