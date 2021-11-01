using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LR_4
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
        void GetNorm()
        {

        }
    }
}
