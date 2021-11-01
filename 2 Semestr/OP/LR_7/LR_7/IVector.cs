using System;
using System.Collections.Generic;
using System.Text;

namespace LR_7
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
        public int CompareTo(object o);

        double GetNorm();

        object Clone();
        
    }
}
