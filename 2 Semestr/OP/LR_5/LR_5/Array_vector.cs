using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LR_5
{
    class Array_vector : IVector, IComparable, ICloneable
    {
        private double[] mas;
        public Array_vector(int n)
        {
            try
            {
                mas = new double[n];
            }
            catch (OverflowException)
            {
                Console.WriteLine("Длина вектора не может быть отрицательной, задан вектор с длинной равной модулю введеного числа");
                mas = new double[-n];
                Console.ReadKey();
            }
        }
        public Array_vector()
        {
            mas = new double[5];
        }
        public double this[int index]
        {
            get
            {
                try
                {
                    return mas[index];
                }
                catch (IndexOutOfRangeException)
                {
                    Console.WriteLine("Индекс выходит за пределы массива");
                    return 0;
                }
            }
            set
            {
                try
                {
                    mas[index] = value;
                }
                catch (IndexOutOfRangeException)
                {
                    Console.WriteLine("Индекс выходит за пределы массива");
                }
            }
        }
        public int Lenght
        {
            get
            {
                return mas.Length;
            }
        }
        public void zap()
        {
            Console.WriteLine("Введите значение элементов");
            for (int i = 0; i < Lenght; i++)
            {

                mas[i] = Convert.ToDouble(Console.ReadLine());
            }
        }
        public double GetNorm()
        {
            double sum = 0;
            for (int i = 0; i < mas.Length; i++)
            {
                sum = sum + mas[i] * mas[i];
            }
            return Math.Sqrt(sum);
        }

        public int CompareTo(object obj)
        {
            IVector tot = obj as IVector;
            return this.Lenght.CompareTo(tot.Lenght);
        }
        public object Clone()
        {
            Array_vector ret = new Array_vector(Lenght);
            for (int i = 0; i < Lenght; i++)
            {
                ret[i] = this[i];
            }
            return ret;
        }
        public override string ToString()
        {
            string str = new string("");
            str += Convert.ToString(this.Lenght);
            str += " || ";
            for (int i = 0; i < Lenght; i++)
            {
                str += mas[i];
                str += " ";
            }
            return str;
        }
        public override bool Equals(object obj)
        {
            Array_vector tot = (Array_vector)obj;
            if (tot.Lenght == this.Lenght)
            {
                bool key = true;
                for (int i = 0; i < Lenght; i++)
                {
                    if (this[i] != tot[i])
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
                return true;
            }
        }
        public override int GetHashCode()
        {
            return base.GetHashCode();
        }
    }
}
