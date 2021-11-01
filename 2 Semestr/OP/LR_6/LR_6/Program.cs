using System;
using System.Net.Sockets;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;

namespace LR_6
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
                Console.WriteLine("Для проверки стандартных интерфейсов              нажмите 4");
                Console.WriteLine("Для проверки пококовых ввода и вывода             нажмите 5");
                Console.WriteLine("Для проверки сериализации                         нажмите 6");
                Console.WriteLine("Для выхода из программы                           нажмите 7");
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
                                    Console.WriteLine("Модуль вектора равен " + vek1.GetNorm());
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
                                    Console.WriteLine("Модуль вектора равен " + list1.GetNorm());
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
                        Console.Clear();
                        IVector[] vekkor;
                        Console.WriteLine("Введите количество векторов в массиве");
                        int l = Convert.ToInt32(Console.ReadLine());
                        try
                        {
                            vekkor = new IVector[l];
                        }
                        catch (OverflowException)
                        {
                            Console.WriteLine("Длина вектора не может быть отрицательной, задан вектор с длинной равной модулю введеного числа");
                            vekkor = new IVector[-l];
                            Console.ReadKey();
                        }
                        for (int i = 0; i < Math.Abs(l); i++)
                        {
                            bool key5 = true;
                            Console.WriteLine("Введите количеcтво координат вектора №{0}", i + 1);
                            int w = Convert.ToInt32(Console.ReadLine());
                            while (key5)
                            {
                                Console.WriteLine("Выберите тип вектора  Массив-1     Список-2");
                                string nemu = Console.ReadLine();
                                switch (nemu)
                                {
                                    case "1":
                                        Array_vector arrr = new Array_vector(w);
                                        arrr.zap();
                                        vekkor[i] = arrr;
                                        key5 = false;
                                        break;
                                    case "2":
                                        LinkedListVector arrr2 = new LinkedListVector(w);
                                        arrr2.zap();
                                        vekkor[i] = arrr2;
                                        key5 = false;
                                        break;
                                    default:
                                        Console.WriteLine("Выбраного действия нет повторите");
                                        break;
                                }
                            }
                        }
                        Console.Clear();
                        Console.WriteLine("================================================================================");
                        for (int i = 0; i < Math.Abs(l); i++)
                        {
                            Console.WriteLine("Вектор № " + (i + 1) + "  " + vekkor[i]);
                        }
                        Console.WriteLine("================================================================================");
                        IVector Vmin = vekkor[0];
                        IVector Vmax = vekkor[0];
                        for (int i = 1; i < Math.Abs(l); i++)
                        {
                            if (Vmax.CompareTo(vekkor[i]) < 0)
                            {
                                Vmax = vekkor[i];
                            }
                            if (Vmin.CompareTo(vekkor[i]) > 0)
                            {
                                Vmin = vekkor[i];
                            }
                        }
                        Console.WriteLine("Вектор наибольшей длины  " + Vmax);
                        Console.WriteLine("Вектор наименьшей длины  " + Vmin);
                        Console.WriteLine("================================================================================");

                        Array.Sort(vekkor, new DOP_05());
                        Console.WriteLine("После сортировки");
                        for (int i = 0; i < Math.Abs(l); i++)
                        {
                            Console.WriteLine("Вектор № " + (i + 1) + "  " + vekkor[i]);
                        }
                        Console.WriteLine("================================================================================");
                        Console.WriteLine("Для клонирования был выбран вектор  " + Vmax);
                        Console.WriteLine("Затем первая координата была заменена на 0");
                        IVector clon = (IVector)Vmax.Clone();
                        clon[0] = 0;
                        Console.WriteLine("Оригинал   " + Vmax);
                        Console.WriteLine("Клон       " + clon);
                        Console.ReadKey();
                        Console.Clear();
                        break;
                    case "5":
                        using (Stream fstream = new FileStream("byte_stream", FileMode.Create))
                        {
                            Console.WriteLine("================================================================================");
                            Console.WriteLine("Работа с байтовым потоком");
                            Console.WriteLine("================================================================================");
                            Console.WriteLine("Введите вектор помещаемый в поток");
                            Console.WriteLine("Введите количеcтво координат вектора");
                            int w = Convert.ToInt32(Console.ReadLine());
                            IVector pot1 = new Array_vector(w);
                            pot1.zap();
                            Console.Clear();
                            Console.WriteLine("================================================================================");
                            Console.WriteLine("Введенный вектор " + pot1);
                            Vectors.OutputVector(pot1, fstream);
                            fstream.Seek(0, SeekOrigin.Begin);
                            IVector pot2 = Vectors.InputVector(fstream);
                            Console.WriteLine("Полученный вектор " + pot2);
                            Console.WriteLine("================================================================================");

                        }

                        using (TextWriter wd = new StreamWriter("sim_stream.txt", false, System.Text.Encoding.Default))
                        {
                            Console.WriteLine("================================================================================");
                            Console.WriteLine("Работа с символьным  потоком");
                            Console.WriteLine("================================================================================");
                            Console.WriteLine("Введите вектор помещаемый в поток");
                            Console.WriteLine("Введите количеcтво координат вектора");
                            int w2 = Convert.ToInt32(Console.ReadLine());
                            IVector pot1 = new Array_vector(w2);
                            pot1.zap();
                            Console.Clear();
                            Console.WriteLine("================================================================================");
                            Console.WriteLine("Введенный вектор " + pot1);
                            Vectors.WriteVector(pot1, wd);
                        }
                        using (TextReader rd = new StreamReader("sim_stream.txt"))
                        {
                            IVector pot2 = Vectors.ReadVector(rd);
                            Console.WriteLine("Полученный вектор " + pot2);
                            Console.WriteLine("================================================================================");
                        }
                        Console.ReadKey();
                        Console.Clear();
                        break;
                    case "6":
                        Console.Clear();
                        Console.WriteLine("================================================================================");
                        Console.WriteLine("Проверка сериализации для Array_vector");
                        Console.WriteLine("================================================================================");
                        Console.WriteLine("Введите длину сериализуемого вектора");
                        int nw = Convert.ToInt32(Console.ReadLine());
                        Array_vector ars = new Array_vector(nw);
                        Array_vector newVector;
                        ars.zap();
                        BinaryFormatter formatter = new BinaryFormatter();
                        using (FileStream fs = new FileStream("Array_Vector.dat", FileMode.OpenOrCreate))
                        {
                            formatter.Serialize(fs, ars);
                            fs.Seek(0, SeekOrigin.Begin);
                            newVector = (Array_vector)formatter.Deserialize(fs);
                        }
                        Console.WriteLine("================================================================================");
                        Console.WriteLine("Введеный вектор            " + ars);
                        Console.WriteLine("Вектор после сериализации  " + newVector);
                        if (ars.Equals(newVector))
                        {
                            Console.WriteLine("Вектора равны");
                        }
                        else
                        {
                            Console.WriteLine("Вектора не равны");
                        }
                        Console.WriteLine("================================================================================");
                        Console.ReadKey();
                        Console.Clear();


                        Console.WriteLine("================================================================================");
                        Console.WriteLine("Проверка сериализации для LinkedListVector");
                        Console.WriteLine("================================================================================");
                        Console.WriteLine("Введите длину сериализуемого вектора");
                        int nw2 = Convert.ToInt32(Console.ReadLine());
                        LinkedListVector ars2 = new LinkedListVector(nw2);
                        LinkedListVector newListVector;
                        ars2.zap();
                        BinaryFormatter formatter2 = new BinaryFormatter();
                        using (FileStream fs2 = new FileStream("LinkedListVector.dat", FileMode.OpenOrCreate))
                        {
                            formatter2.Serialize(fs2, ars2);
                            fs2.Seek(0, SeekOrigin.Begin);
                            newListVector = (LinkedListVector)formatter2.Deserialize(fs2);
                        }
                        Console.WriteLine("================================================================================");
                        Console.WriteLine("Введеный вектор            " + ars2);
                        Console.WriteLine("Вектор после сериализации  " + newListVector);
                        if (ars2.Equals(newListVector))
                        {
                            Console.WriteLine("Вектора равны");
                        }
                        else
                        {
                            Console.WriteLine("Вектора не равны");
                        }
                        Console.WriteLine("================================================================================");
                        Console.ReadKey();
                        Console.Clear();
                        break;
                    case "7":
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
