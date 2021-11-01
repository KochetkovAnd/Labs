using System;
using System.Collections.Generic;
using System.Text;

namespace LR_6
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
        void zap()
        {

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
