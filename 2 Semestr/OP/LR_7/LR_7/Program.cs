using System;

namespace LR_7
{
    class Program
    {
        delegate void Osn();
        delegate void Menu();
        static void Main(string[] args)
        {
            string trac = "";
            Osn menu = null;
            bool key1 = true;
            while (key1 == true)
            {
                Console.WriteLine("=================================================================================================");
                Console.WriteLine("Выполнил ученик гр 6115 Кочетков А.В.");
                Console.WriteLine("=================================================================================================");
                Console.WriteLine("Формируем траекторию работы с программой");
                Console.WriteLine("Текущая траектория  " + trac);
                Console.WriteLine("=================================================================================================");
                Console.WriteLine("Для добавления в траекторию реализции класса ArrayVector         нажмите 1");
                Console.WriteLine("Для добавления в траекторию реализции класса LinkedListVector    нажмите 2");
                Console.WriteLine("Для добавления в траекторию реализции класса Vectors             нажмите 3");
                Console.WriteLine("Для добавления в траекторию проверки стандартных интерфейсов     нажмите 4");
                Console.WriteLine("Для окончания формирования траектории                            нажмите 5");
                Console.WriteLine("=================================================================================================");
                string case1 = Console.ReadLine();
                switch (case1)
                {
                    case "1":
                        menu += Menu_Array_Vector;
                        trac += case1;
                        break;
                    case "2":
                        menu += Menu_LinkedListVector;
                        trac += case1;
                        break;
                    case "3":
                        menu += Menu_Vectors;
                        trac += case1;
                        break;
                    case "4":
                        menu += Menu_Interface;
                        trac += case1;
                        break;
                    case "5":
                        key1 = false;
                        break;
                    default:
                        Console.WriteLine("Введеной функции нет повторите");
                        Console.ReadKey();

                        break;
                }
                Console.Clear();
            }
            menu();
            Console.WriteLine("Траектория пройдена");
            Console.ReadKey();
        }
        private static void Menu_Array_Vector()
        {
            Console.Clear();
            Console.WriteLine("Работа с Array_Vector");
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
                Console.WriteLine("Для перехода на следущий шаг траектории            нажмите 4 ");
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
        }
        private static void Menu_LinkedListVector()
        {
            Console.Clear();
            Console.WriteLine("Работа с LinkedListVector");
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
                Console.WriteLine("Для перехода на следущий шаг траектории            нажмите 4 ");
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
        }
        private static void Menu_Vectors()
        {
            Console.Clear();
            Console.WriteLine("Работа с Vectors");
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
                Console.WriteLine("Для перехода на следущий шаг траектории     нажмите 7 ");
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
        }
        private static void Menu_Interface()
        {

            Console.Clear();
            Console.WriteLine("Работа со стандартными интерфейсами");
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
            int minL = Vmin.Lenght;
            int maxL = Vmax.Lenght;
            int minK = 0;
            int maxK = 0;
            for (int i = 1; i < Math.Abs(l); i++)
            {
                if (Vmax.CompareTo(vekkor[i]) < 0)
                {
                    Vmax = vekkor[i];
                    maxL = Vmax.Lenght;
                }
                if (Vmin.CompareTo(vekkor[i]) > 0)
                {
                    Vmin = vekkor[i];
                    minL = Vmin.Lenght;
                }
            }
            for (int i = 0; i < Math.Abs(l); i++)
            {
                if (Vmax.CompareTo(vekkor[i]) == 0)
                {
                    maxK++;
                }
                if (Vmin.CompareTo(vekkor[i]) == 0)
                {
                    minK++;
                }
            }
            IVector[] maxs = new IVector[maxK];
            IVector[] mins = new IVector[minK];
            int i1 = 0;
            int i2 = 0;
            for (int i = 0; i < Math.Abs(l); i++)
            {
                if (Vmax.CompareTo(vekkor[i]) == 0)
                {
                    maxs[i1] = vekkor[i];
                    i1++;
                }
                if (Vmin.CompareTo(vekkor[i]) == 0)
                {
                    mins[i2] = vekkor[i];
                    i2++;
                }
            }
            for (int i = 0; i < maxs.Length; i++)
            {
                Console.WriteLine("Вектор наибольшей длины №{0}  " + maxs[i], (i + 1));
            }
            Console.WriteLine("================================================================================");
            for (int i = 0; i < mins.Length; i++)
            {
                Console.WriteLine("Вектор наименьшей длины №{0}  " + mins[i], (i + 1));
            }
            Console.WriteLine("================================================================================");

            Array.Sort(vekkor, new DOP_05());
            Console.WriteLine("После сортировки");
            for (int i = 0; i < Math.Abs(l); i++)
            {
                Console.WriteLine("Вектор № " + (i + 1) + "  " + vekkor[i]);
            }
            Console.WriteLine("================================================================================");
            Console.WriteLine("Для клонирования был выбран вектор  " + Vmax);
            IVector clon = (IVector)Vmax.Clone();
            Console.WriteLine("Оригинал   " + Vmax);
            Console.WriteLine("Клон       " + clon);
            if (Vmax.Equals(clon))
            {
                Console.WriteLine("Вектора равны проверено методом Equals");
            }
            else
            {
                Console.WriteLine("Вектора не равны");
            }
            Console.ReadKey();
            Console.Clear();
        }
    }
}