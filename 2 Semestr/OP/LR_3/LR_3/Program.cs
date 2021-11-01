using System;

namespace LR_3
{
    enum Vacancies
    {
        Manager = 1,
        Boss,
        Clerk,
        Salesman,
    }
    class Program
    {
        static void Main(string[] args)
        {
            bool bosses = true;
            Console.WriteLine("==========================================================================================================");
            Console.WriteLine("Введите количество сотрудников");
            Console.WriteLine("==========================================================================================================");
            int n = Convert.ToInt32(Console.ReadLine());
            Employee[] sot = new Employee[n];
            for (int i = 0; i < n; i++)
            {
                Console.Clear();
                Console.WriteLine("==========================================================================================================");
                Employee f = new Employee();
                Console.WriteLine($"Сотрутник номер {i + 1}");
                Console.WriteLine("==========================================================================================================");
                Console.WriteLine("Введите Имя сотрурника");
                string name = Console.ReadLine();
                Console.WriteLine("==========================================================================================================");
                f.name = name;
                bool key = true;
                while (key == true)
                {
                    Console.WriteLine("Выберите проффесию сотрудника 1-Менеджер 2-Босс, 3-Офисный работник, 4-Продавец");
                    string menu = Console.ReadLine();
                    Console.WriteLine("==========================================================================================================");
                    switch (menu)
                    {
                        case "1":
                            f.vacancy = Vacancies.Manager;
                            key = false;
                            break;
                        case "2":
                            if (bosses)
                            {
                                f.vacancy = Vacancies.Boss;
                                key = false;
                                bosses = false;
                            }
                            else
                            {
                                Console.WriteLine("Не может быть более одного босса,повторите выбор");
                            }
                            break;
                        case "3":
                            f.vacancy = Vacancies.Clerk;
                            key = false;
                            break;
                        case "4":
                            f.vacancy = Vacancies.Salesman;
                            key = false;
                            break;
                        default:
                            Console.WriteLine("Профессия отсутствует, повторите выбор");
                            break;
                    }
                }
                Console.WriteLine("Введите зарплату сотрудника");
                int salary = Convert.ToInt32(Console.ReadLine());
                Console.WriteLine("==========================================================================================================");
                f.salary = salary;
                Console.WriteLine("Введите дату приема на работу");

                bool keyf = true;
                while (keyf == true)
                {
                    Console.WriteLine("День");
                    int day = Convert.ToInt32(Console.ReadLine());
                    if ((day > 0) && (day < 32))
                    {
                        f.hiredate[0] = day;
                        keyf = false;
                    }
                    else
                    {
                        Console.WriteLine("Дата не существует, повторите");
                    }
                }
                keyf = true;
                while (keyf == true)
                {
                    Console.WriteLine("Месяц");
                    int month = Convert.ToInt32(Console.ReadLine());
                    if ((month > 0) && (month < 13))
                    {
                        f.hiredate[1] = month;
                        keyf = false;
                    }
                    else
                    {
                        Console.WriteLine("Дата не существует, повторите");
                    }
                }
                keyf = true;
                while (keyf == true)
                {
                    Console.WriteLine("Год");
                    int year = Convert.ToInt32(Console.ReadLine());
                    if ((year > 0) && (year < 10000))
                    {
                        f.hiredate[2] = year;
                        keyf = false;
                    }
                    else
                    {
                        Console.WriteLine("Дата не существует, повторите");
                    }
                }
                sot[i] = f;
            }
            bool key2 = true;
            while (key2 == true)
            {
                Console.Clear();
                Console.WriteLine("==========================================================================================================");
                Console.WriteLine("            Имя      Должность      Зартплата     Дата приема на работу");
                Console.WriteLine("==========================================================================================================");
                for (int i = 0; i < n; i++)
                {
                    sot[i].inf();
                }
                Console.WriteLine("==========================================================================================================");
                Console.WriteLine("Для вывода информации о людях, заданной должности                                      | нажмите 1 ");
                Console.WriteLine("Для вывод менеджеров с зарплатой больше средней зарплаты клерков                       | нажмите 2 ");
                Console.WriteLine("Для вывода сотрудников принятых на работу раньше босса                                 | нажмите 3 ");
                Console.WriteLine("Для выхода из программы                                                                | нажмите 4 ");
                Console.WriteLine("==========================================================================================================");
                string menu = Console.ReadLine();
                switch (menu)
                {
                    case "1":
                        Console.WriteLine("==========================================================================================================");
                        Console.WriteLine("Выберите проффесию сотрудника 1-Менеджер 2-Босс, 3-Офисный работник, 4-Продавец");
                        int hr = Convert.ToInt32(Console.ReadLine());
                        Console.WriteLine("==========================================================================================================");
                        if ((hr > 0) && (hr < 5))
                        {
                            for (int i = 0; i < n; i++)
                            {
                                Vacancies op = sot[i].vacancy;
                                if (((int)op) == hr)
                                {
                                    sot[i].inf();
                                }
                            }
                        }
                        else
                        {
                            Console.WriteLine("Такой проффесии нет");
                        }
                        Console.WriteLine("==========================================================================================================");
                        Console.ReadKey();
                        break;
                    case "2":
                        int k = 0;
                        int s = 0;
                        for (int i = 0; i < n; i++)
                        {
                            if (((int)sot[i].vacancy) == 3)
                            {
                                k++;
                                s += sot[i].salary;
                            }
                        }
                        if (k > 0)
                        {
                            double average = s / k;
                            int b = 0;
                            for (int i = 0; i < n; i++)
                            {
                                if ((((int)sot[i].vacancy) == 1) && (sot[i].salary > average))
                                {
                                    b++;
                                }
                            }
                            Employee[] vrsot = new Employee[b];
                            int j = 0;
                            for (int i = 0; i < n; i++)
                            {
                                if ((((int)sot[i].vacancy) == 1) && (sot[i].salary > average))
                                {

                                    vrsot[j] = sot[i];
                                    j++;
                                }

                            }
                            vrsot = Employee.alfsort(vrsot);
                            Console.WriteLine("==========================================================================================================");
                            for (int i = 0; i < b; i++)
                            {
                                vrsot[i].inf();
                            }
                            Console.WriteLine("==========================================================================================================");
                        }
                        else
                        {
                            Console.WriteLine("В компании нет клерков");
                        }
                        Console.ReadKey();
                        break;
                    case "3":
                        int g = -1;
                        for (int i = 0; i < n; i++)
                        {
                            if (((int)sot[i].vacancy) == 2)
                            {
                                g = i;
                            }
                        }
                        if (g != -1)
                        {
                            int h = 0;
                            for (int i = 0; i < n; i++)
                            {
                                if (Employee.hirecheck(sot[g].hiredate, sot[i].hiredate))
                                {
                                    h++;
                                }
                            }
                            Employee[] vssot = new Employee[h];
                            int q = 0;
                            for (int i = 0; i < n; i++)
                            {
                                if (Employee.hirecheck(sot[g].hiredate, sot[i].hiredate))
                                {

                                    vssot[q] = sot[i];
                                    q++;
                                }
                            }
                            vssot = Employee.alfsort(vssot);
                            Console.WriteLine("==========================================================================================================");
                            for (int i = 0; i < h; i++)
                            {
                                vssot[i].inf();
                            }
                            Console.WriteLine("==========================================================================================================");
                        }
                        else
                        {
                            Console.WriteLine("В вашей компании нет босса");
                        }
                        Console.ReadKey();
                        break;
                    case "4":
                        key2 = false;
                        break;
                    default:
                        Console.WriteLine("Введенной функции не повторите");
                        break;


                }
            }
        }
    }
}