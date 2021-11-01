using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LR_4
{
    class LinkedListVector : IVector
    {
        public class Node
        {
            public double data;
            public Node next;
            public Node(double data)
            {
                this.data = data;
                next = null;
            }

        }
        public Node head;
        public LinkedListVector()
        {
            for (int i = 0; i < 5; i++)
            {
                Add(0);
            }
        }
        public LinkedListVector(int n)
        {
            if (n >= 0)
            {
                for (int i = 0; i < n; i++)
                {
                    Add(0);
                }
            }
            else
            {
                Console.WriteLine("Длина вектора не может быть отрицательной, задан вектор с длинной равной модулю введеного числа");
                Console.ReadKey();
                for (int i = 0; i < -n; i++)
                {
                    Add(0);
                }
            }
        }
        public double this[int index]
        {
            get
            {
                if (index >= 0)
                {
                    try
                    {
                        Node cur = head;
                        for (int i = 0; i < index; i++)
                        {
                            cur = cur.next;
                        }
                        return cur.data;
                    }
                    catch (NullReferenceException)
                    {
                        Console.WriteLine("Индекс выходит за пределы массива");
                        return 0;
                    }
                }
                else
                {
                    Console.WriteLine("Индекс выходит за пределы массива");
                    return 0;
                }
            }
            set
            {
                if (index >= 0)
                {
                    try
                    {
                        Node cur = head;
                        for (int i = 0; i < index; i++)
                        {
                            cur = cur.next;
                        }
                        cur.data = value;
                    }
                    catch (NullReferenceException)
                    {
                        Console.WriteLine("Индекс выходит за пределы массива");
                    }
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
            Node cur = head;
            while (cur != null)
            {
                sum += cur.data * cur.data;
                cur = cur.next;
            }
            Console.WriteLine($"Модуль вектора равен {Math.Sqrt(sum)}");
        }
        public int Lenght
        {
            get
            {
                int i = 0;
                Node cur = head;
                while (cur != null)
                {
                    i++;
                    cur = cur.next;
                }
                return i;
            }
        }

        public void Add(double data)
        {
            Node nd = new Node(data);
            if (head == null)
            {
                head = nd;
            }
            else
            {
                Node cur = head;
                while (cur.next != null)
                {
                    cur = cur.next;
                }
                cur.next = nd;
            }

        }
        public override string ToString()
        {
            Node cur = head;
            string str = new string("");
            str += Convert.ToString(this.Lenght);
            str += " || ";
            while (cur != null)
            {
                str += cur.data;
                str += " ";
                cur = cur.next;
            }
            return str;
        }
    }
}
