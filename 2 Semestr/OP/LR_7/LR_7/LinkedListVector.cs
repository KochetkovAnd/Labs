﻿using System;
using System.Collections.Generic;
using System.Text;

namespace LR_7
{
    class LinkedListVector:IVector,IComparable,ICloneable
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
        public double GetNorm()
        {
            double sum = 0;
            Node cur = head;
            while (cur != null)
            {
                sum += cur.data * cur.data;
                cur = cur.next;
            }
            return Math.Sqrt(sum);
        }
        public void zap()
        {
            Console.WriteLine("Введите значение элементов");
            Node cur = head;
            while (cur != null)
            {                
                double datta = Convert.ToDouble(Console.ReadLine());                
                cur.data = datta;
                cur = cur.next;
            }
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
        public int CompareTo(object obj)
        {
            IVector tot = obj as IVector;
            return this.Lenght.CompareTo(tot.Lenght);
        }
        public object Clone()
        {
            LinkedListVector ret = new LinkedListVector(Lenght);
            Node curthis = this.head;
            Node curret=ret.head;
            while (curthis != null)
            {
                curret.data = curthis.data;
                curthis = curthis.next;
                curret = curret.next;
            }
            return ret;
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
        public override bool Equals(object obj)
        {
            LinkedListVector tot = (LinkedListVector)obj;
            if (this.Lenght == tot.Lenght)
            {
                Node cur1 = this.head;
                Node cur2 = tot.head;
                bool key = true;
                for (int i = 0; i < Lenght; i++)
                {
                    if (cur1.data!=cur2.data)
                    {
                        key = false;
                    }

                }
                if (key)
                {
                    return true;
                }
                else
                {
                    return false;
                }
            }
            else
            {
                return false;
            }
            
        }
        public override int GetHashCode()
        {
            return base.GetHashCode();
        }

    }
}