using System;
using System.Collections.Generic;
using System.Text;

namespace LR_6
{
    class DOP_05:IComparer<IVector>
    {
        public int Compare(IVector a1, IVector a2)
        {
            return Math.Sign(a1.GetNorm() - a2.GetNorm());
        }
    }
}
