using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LR_3
{
    class Employee
    {
        public string name = "";
        public Vacancies vacancy = Vacancies.Manager;
        public int salary = 0;
        public int[] hiredate = new int[3] { 0, 0, 0 };
        public Employee()
        {
            name = "";
            vacancy = Vacancies.Manager;
            salary = 0;
            hiredate[0] = 0;
            hiredate[1] = 0;
            hiredate[2] = 0;
        }
        public void inf()
        {
            Console.WriteLine($"{name,15}{vacancy,15}{salary,15}{hiredate[0],10:00}.{hiredate[1],2:00}.{hiredate[2],4:0000}");
        }
        public static Employee[] alfsort(Employee[] sot)
        {
            int n = sot.Length;
            string[] names = new string[n];
            for (int i = 0; i < n; i++)
            {
                names[i] = sot[i].name;
            }
            Array.Sort(names);
            for (int i = 0; i < n - 1; i++)
            {
                int j = i;
                while (names[i] != sot[j].name)
                {
                    j++;
                }
                Employee d;
                d = sot[i];
                sot[i] = sot[j];
                sot[j] = d;
            }
            return sot;
        }
        public static bool hirecheck(int[] bs, int[] em)
        {
            if (bs[2] > em[2])
            {
                return true;
            }
            else
            {
                if (bs[2] < em[2])
                {
                    return false;
                }
                else
                {
                    if (bs[1] > em[1])
                    {
                        return true;
                    }
                    else
                    {
                        if (bs[1] < em[1])
                        {
                            return false;
                        }
                        else
                        {
                            if (bs[0] > em[0])
                            {
                                return true;
                            }
                            else
                            {
                                return false;
                            }
                        }
                    }
                }
            }
        }
    }
}
