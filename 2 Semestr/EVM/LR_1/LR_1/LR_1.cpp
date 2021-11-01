#include <iostream>
#include <stdio.h>
#include <conio.h>
#include <locale.h>
#include <math.h>
int calc(int a, int d) {
	int result = 0;
	__asm
	{
		xor eax, eax//обнуление eax
		xor ebx, ebx//обнуление ebx
		//(24-d/4)(a*a+1)
		mov eax, a

		imul eax//a*a
		add eax, 1//a*a+1
		push eax
		mov eax, d//d
		mov ebx, 4
		idiv ebx//d/4
		mov ebx, eax
		mov eax, 24
		sub eax, ebx//24-d/4
		pop ebx
		cdq;
		idiv ebx//(24-d/4)/a*a+1
			mov result, eax
	}
	return result;
}

int main()
{
	setlocale(LC_ALL, "Russian");
	std::cout << "Ассемблер. Лабораторная работа № 1" << std::endl;
	std::cout << "Арифметические и логические команды" << std::endl;
	std::cout << "Выполнил Кочетков Андрей Владимирович, группа 6115" << std::endl;
	std::cout << "Вариант 7" << std::endl;
	std::cout << "В задание необходимо реализовать функцию вычисления целочисленного " << std::endl;
	std::cout << "выражения (24 – d/4)/(a*a + 1) на встроенном ассемблере MASM " << std::endl;
	std::cout << "MASM в среде Microsoft Visual Studio на языке C++ " << std::endl;

	int a, d;
	std::cout << "a = ";
	std::cin >> a;
	std::cout << "d = ";
	std::cin >> d;

	int res1 = calc(a, d);
	int res2 = (24 - d / 4) / (a * a + 1);
	std::cout << "Результат в Assembler = " << res1 << std::endl;
	std::cout << "Результат в С++ = " << res2 << std::endl;
	system("Pause");
	return 0;
}