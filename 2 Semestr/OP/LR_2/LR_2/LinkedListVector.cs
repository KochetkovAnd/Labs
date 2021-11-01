using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LR_2
{
    class LinkedListVector
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
            for (int i = 0; i < n; i++)
            {
                Add(0);
            }
        }
        public double this[int index]
        {
            get
            {
                Node cur = head;
                int v = 1;
                while ((cur != null) && (v != index))
                {
                    cur = cur.next;
                    v++;
                }
                if (cur == null)
                {
                    Console.WriteLine("Индекс выходит за пределы массива");
                    return 0;
                }
                else
                {
                    return cur.data;
                }
            }
            set
            {
                Node cur = head;
                int v = 1;
                while ((cur != null) && (v != index))
                {
                    cur = cur.next;
                    v++;
                }
                if (cur == null)
                {
                    Console.WriteLine("Индекс выходит за пределы массива");
                }
                else
                {
                    cur.data = value;
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
        public void inf()
        {
            Node cur = head;
            while (cur != null)
            {
                Console.Write(cur.data + "  ");
                cur = cur.next;
            }

            Console.WriteLine();
        }

    }
}
