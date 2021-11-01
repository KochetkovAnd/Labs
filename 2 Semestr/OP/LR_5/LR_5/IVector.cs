using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LR_5
{
    interface IVector
    {
        public double this[int index]
        {
            get;
            set;
        }
        public int Lenght
        {
            get;
        }
        public int CompareTo(object o)
        {
            return 0;
        }
        double GetNorm()
        {
            return 0;
        }
        object Clone()
        {
            return 0;
        }
    }
}
